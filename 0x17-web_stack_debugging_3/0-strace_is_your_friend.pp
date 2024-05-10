# A puppet manuscript to fix an Apache Server.

$file = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php".

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}
