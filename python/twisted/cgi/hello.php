<!doctype html>
<html>
   <body>

<?php
function curPageURL() {
 $pageURL = 'http';
 if ($_SERVER["HTTPS"] == "on") {$pageURL .= "s";}
 $pageURL .= "://";
 if ($_SERVER["SERVER_PORT"] != "80") {
  $pageURL .= $_SERVER["SERVER_NAME"].":".$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"];
 } else {
  $pageURL .= $_SERVER["SERVER_NAME"].$_SERVER["REQUEST_URI"];
 }
 return $pageURL;
}

 //echo curPageURL();
?>
      <?php
      $headers = apache_request_headers();

      foreach ($headers as $header => $value) {
          echo "$header: $value <br />\n";
      }
      ?>
      <?php
         echo $_SERVER["REQUEST_URI"];
//         print_r($_REQUEST);
//         print_r($_SERVER);
//         var_dump($_HTTP_REQUEST);
         phpinfo();
      ?>
   </body>
</html>
