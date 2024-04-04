# Use Puppet to:
# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
# - The name of the custom HTTP header must be X-Served-By
# - The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
