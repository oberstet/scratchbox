<!doctype html>
<html>
   <body>
      <pre>
      <?php
         $headers = apache_request_headers();
         foreach ($headers as $header => $value) {
             echo "$header: $value <br />\n";
         }
      ?>
      </pre>
      <pre>
      <?php
         echo $_SERVER["REQUEST_URI"];
      ?>
      </pre>
      <?php
         phpinfo();
      ?>
   </body>
</html>
