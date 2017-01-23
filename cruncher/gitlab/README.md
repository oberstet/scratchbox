# Gitlab

## Why?

Gitlab is like Github, but on-premise and OSS.

Gitlab is an **integrated** code collaboration platform, much of the value is in the integration of issues, commits and CI etc.

Look here:

* https://www.youtube.com/watch?t=3&v=raXvuwet78M
* https://about.gitlab.com/2014/09/29/gitlab-flow/

## Setup

Setup is a breeze. I've setup Gitlab on `svr-git01` like this. See [here](https://about.gitlab.com/downloads/#ubuntu1404).

Login

```
ssh git@svr-git01
```

> For some reasons, the ifb admins did setup the VM with user `git` as main user (I minor nuisance). Watch out for this!

Update the system

```
sudo apt-get update
sudo apt-get upgrade
```

Setup Gitlab's Ubuntu package repo:

```
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
```

Install

```
sudo apt-get update --fix-missing
sudo apt-get install gitlab-ce
```

Now, this is ***important**:

```
sudo vim /etc/gitlab/gitlab.rb
```

and configure

```
user['username'] = "gitlab"
user['group'] = "gitlab"
```

Configure and run Gitlab

```
sudo gitlab-ctl reconfigure
```

Now open [http://svr-git01.local.parcit/](http://svr-git01.local.parcit/).
