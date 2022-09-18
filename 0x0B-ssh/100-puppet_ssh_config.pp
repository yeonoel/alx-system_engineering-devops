# Client configuration file (w/ Puppet)
# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up your
# client SSH configuration file so that you can connect to a
# server without typing a password.

include stdlib
file_line { 'No password':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no',
}

file_line {'change private key':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'IdentityFile ~/.ssh/school'
}
