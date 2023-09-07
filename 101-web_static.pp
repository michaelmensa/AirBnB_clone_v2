#

# Install nginx package
package { 'nginx':
  ensure   => 'installed',
  provider => apt,
}

# Create necessary directories
-> file { '/data/':
  ensure => 'directory',
}

-> file { '/data/web_static':
  ensure => 'directory'
}

-> file { '/data/web_static/releases':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

-> file { '/data/web_static/shared/':
  ensure => 'directory',
}

# Create index.html file
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
}

# Create symbolic link
-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => 'true',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

file { '/var/www':
  ensure => 'directory',
}

-> file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "This is my first upload  in /var/www/index.html***\n",
}

-> file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page - Error page\n"
}

# Update nginx configuration
-> file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://linktr.ee/firdaus_h_salim/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}",
}

# Create symbolic link to nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  force  => 'true',
}

# Restart nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => File['/etc/nginx/sites-enabled/default'],
}
