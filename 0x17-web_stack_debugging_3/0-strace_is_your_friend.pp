#0-strace_is_your_friend.pp

file { '/path/to/httpd.conf':
  ensure => present,
  content => template('my_module/vhost_template.erb'),
}
