# Hosting static Web sites

We want to host a static Web site with content from a S3 bucket.

In particular, we want the following:

1. host a root domain (e.g. example.com)
2. use S3 to host the Web site static content
2. use Route 53 to manage DNS
3. have a custom SSL certificate for access via HTTPS
4. have HTTP requests automatically redirected to HTTPS

Here are a couple of caveats doing so:

1. For a Web site that should be reachable under `example.com`, the bucket with the content MUST be named `example.com`. See [here](http://serverfault.com/a/584714/117074).

2. The wildcard certificates issued by Amazon for S3 buckets will NOT work when the bucket name contains periods. See [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html): "When using virtual hosted–style buckets with SSL, the SSL wild card certificate only matches buckets that do not contain periods.". See also [this boto bug](https://github.com/boto/boto/issues/2836).

3. Using Cloudfront, it is possible to use custom certificates with static Websites (see [here](https://aws.amazon.com/de/blogs/aws/custom-ssl-domain-names-root-domain-hosting-for-amazon-cloudfront/) and [here](http://aws.amazon.com/de/cloudfront/custom-ssl-domains/) and [here](https://bryce.fisher-fleig.org/blog/setting-up-ssl-on-aws-cloudfront-and-s3/)). This will cost 600 US-$ per month and Web site.

Yeah, bummer.

However, since of March 2014, Amazon [supports TLS SNI](http://aws.amazon.com/de/about-aws/whats-new/2014/03/05/amazon-cloudront-announces-sni-custom-ssl/)!!

This should finally make it possible to satisfy all our requirements from above.

There are two minor or, more precise, inevitable issues left:

1. We will need to upload certificates *and* private keys to Amazon Cloudfront. Means: Amazon will be able to impersonate our sites.
2. TLS SNI is supported only on decently modern browsers (e.g. IE on XP is *not* supported)

> Browsers that support TLS SNI include Chrome version 6 and later (running on Windows XP and later or OS X 10.5.7 and later), Safari version 3 and later (running on Windows Vista and later or Mac OS X 10.5.6. and later), Firefox 2.0 and later, and Internet Explorer 7 and later (running on Windows Vista and later).

Regarding 2): total traffic last month to http://autobahn.ws for IE on *any* Windows version was <2%.

Regarding 1): yes, we need to trust Amazon here. But we will be using our own servers (with private keys) for any *dynamic* content (namely, any WebSocket, WAMP or REST or HTTP/POST stuff). So we are talking only about static content. Yes, this includes JS, which is an attack vector.

## Configuration

The following was tested to host this bucket

* [web-tabulator-io](https://web-tabulator-io.s3-eu-west-1.amazonaws.com/)

as a root domain on Cloudfront

* [tabulator-io](https://tabulator.io)

Open issues:

* How to trigger updates when stuff is cached in Cloudfront?
* Does Cloudfront honor headers like SVG content type or GZ content encodings?

The bucket

* must NOT contain periods (this is definitely required)
* must NOT be configured as a "S3 Website" (I think this is required)
* must be PUBLIC (I'm not sure if this is required for Cloudfront to access the bucket as a source) 

The steps are:

1. Create a server key and certificate
2. Upload the key and certificate to AWS IAM
3. Create a S3 bucket
4. Create a Cloudfront Web distribution with the bucket as source
5. Configure Route 53

Here are some resources:

* https://timnash.co.uk/building-cdn-ssl-cloudfront-certificates/
* http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html
* http://aws.amazon.com/cloudfront/custom-ssl-domains/
* http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS/

### Upload key/certificate to AWS IAM

You will need to remove any passphrase from your SSL private key:

```
openssl rsa -in example_com_key.pem -out example_com_key_no_passphrase.pem
```

We will now need to upload the key and certifiate to AWS IAM (see [Managing Server Certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingServerCerts.html).

It seems, this must be done from CLI (not possible via AWS IAM Web console). We'll be using the [AWS CLI](https://aws.amazon.com/cli/?nc2=h_ls).

Install:

```console
$ pip install awscli
```

Configure:

```console
$ aws configure
AWS Access Key ID [None]: XXXXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [None]:
Default output format [None]:
```

Now upload the certificate and private key:

```
aws iam upload-server-certificate \
   --server-certificate-name YOURNAME \
   --certificate-body file://YOURSIGNEDCERT.pem \
   --private-key file://YOURPRIVATEKEY.pem \
   --certificate-chain file://INTERMEDIATECERT.pem \
   --path /cloudfront/
```

where

* `YOURNAME` – a way for you to identify the certificate once it’s uploaded in the admin area
* `YOURSIGNEDCERT` – the certificate sent to you from your CA
* `YOURPRIVATEKEY` – your private key, which you generated as part of your certificate process
* `INTERMEDIATECERT` – The intermediate key provided by your CA

> We have add the extra –path /cloudfront/ to let Amazon know we will be using this on CloudFront, and it can be used across multiple distributions, though in reality it will be used on only one.

Here is an example:

```
aws iam upload-server-certificate \
   --server-certificate-name tabulator_io \
   --certificate-body file://tabulator_io_cert.pem \
   --private-key file://tabulator_io_key_no_passphrase.pem \
   --certificate-chain file://sub.class1.server.sha2.ca.pem \
   --path /cloudfront/
```

> Note: running in Windows Git bash does NOT work. It fails with an obscure, misleading "UploadServerCertificate operation: The specified value for path is invalid." error. Run in a Windows command shell.

You can verify that the key and certificate was successfully uploaded:

```console
$ aws iam get-server-certificate --server-certificate-name tabulator_io
```

delete the key/certificate

```console
$ aws iam delete-server-certificate --server-certificate-name tabulator_io
```

or list all keys/certificates

```console
$ aws iam list-server-certificates
{
    "ServerCertificateMetadataList": [
        {
            "ServerCertificateId": "ASCAIEXUKJXBF47QU2PIY",
            "ServerCertificateName": "tabulator_io",
            "Expiration": "2016-01-04T00:45:15Z",
            "Path": "/cloudfront/",
            "Arn": "arn:aws:iam::931347297591:server-certificate/cloudfront/tabulator_io",
            "UploadDate": "2015-01-03T17:04:13Z"
        }
    ]
}
```

# TLS Certificates

As soon as the [Let's encrypt](https://letsencrypt.org/) initiative starts (should be middle of 2015), we want our certificates issued by them.

Until, we will continue to use [StartSSL](https://www.startssl.com/).
