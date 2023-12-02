# Creates a file
file { '/root/school':
  ensure   => present,
  content  => 'Hello Edward'
}
