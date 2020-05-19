<?php
require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/dotenv-loader.php';

$domain = getenv('AUTH0_DOMAIN');
$client_id = getenv('AUTH0_CLIENT_ID');

$auth0 = new Auth0\SDK\Auth0([
    'domain' => $domain,
    'client_id' => $client_id,
    'redirect_uri' => getenv('AUTH0_CALLBACK_URL'),
]);

$auth_api = new \Auth0\SDK\API\Authentication( $domain, $client_id );

$auth0->logout();
$return_to = 'http://' . $_SERVER['HTTP_HOST'];
$logout_url = sprintf('http://%s/v2/logout?client_id=%s&returnTo=%s', 'dev-5l2mcnx9.auth0.com', 'UtYO13tBQFB563V5eXRn4zvg4603GRjr', $return_to);
header('Location: ' . $logout_url);
die();
