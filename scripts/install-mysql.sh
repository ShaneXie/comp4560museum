#!/usr/bin/env bash
# Check If mysql Has Been Installed

if [ -f /home/vagrant/.mysql ]
then
    echo "MySQL already installed."
    exit 0
fi

touch /home/vagrant/.mysql

# Remove MySQL

apt-get remove -y --purge mysql-server mysql-client mysql-common
apt-get autoremove -y
apt-get autoclean

rm -rf /var/lib/mysql
rm -rf /var/log/mysql
rm -rf /etc/mysql

# Set The Automated Root Password

debconf-set-selections <<< 'mysql-server mysql-server/root_password password secret'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password secret'

# Install MySQL

apt-get install -y mysql-server

# Configure Password Expiration

echo "default_password_lifetime = 0" >> /etc/mysql/my.cnf

# Configure Maria Remote Access

sed -i '/^bind-address/s/bind-address.*=.*/bind-address = 0.0.0.0/' /etc/mysql/my.cnf

mysql --user="root" --password="secret" -e "GRANT ALL ON *.* TO root@'0.0.0.0' IDENTIFIED BY 'secret' WITH GRANT OPTION;"
service mysql restart

mysql --user="root" --password="secret" -e "CREATE DATABASE IF NOT EXISTS museum DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_unicode_ci;"
mysql --user="root" --password="secret" -e "CREATE USER 'museumadmin'@'0.0.0.0' IDENTIFIED BY 'robin';"
mysql --user="root" --password="secret" -e "GRANT ALL ON *.* TO 'museumadmin'@'0.0.0.0' IDENTIFIED BY 'robin' WITH GRANT OPTION;"
mysql --user="root" --password="secret" -e "GRANT ALL ON *.* TO 'museumadmin'@'%' IDENTIFIED BY 'robin' WITH GRANT OPTION;"
mysql --user="root" --password="secret" -e "FLUSH PRIVILEGES;"
service mysql restart
