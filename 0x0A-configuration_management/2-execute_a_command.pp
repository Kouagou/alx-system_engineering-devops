# This manifest kills a process named killmenow
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
