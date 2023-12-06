#!/usr/bin/env bash
#create a custom HTTP header response, but with Puppet


package {'nginx':
  ensure => installed
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
   listen 80 default_server;
   listen [::]:80 default_server;

   root /var/www/html;
   index index.html;

   location / {
   	add_header X-Served-By \$HOSTNAME;
  }
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
