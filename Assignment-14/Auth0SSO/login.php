<?php
require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/dotenv-loader.php';

$auth0 = new Auth0\SDK\Auth0([
    'domain' => 'dev-5l2mcnx9.auth0.com',
  'client_id' => 'UtYO13tBQFB563V5eXRn4zvg4603GRjr',
  'client_secret' => 'YOUR_CLIENT_SECRET',
  'redirect_uri' => 'http://ec2-3-83-96-252.compute-1.amazonaws.com/SSOLoginJSONEditor/',
  'scope' => 'openid profile email',
]);

$auth0->login();
