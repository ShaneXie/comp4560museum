apt-get update

export DEBIAN_FRONTEND=noninteractive
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
dpkg-reconfigure locales
apt-get install language-pack-en build-essential libssl-dev -y

# add ppa
sudo add-apt-repository ppa:fkrull/deadsnakes

apt-get update

# install mysql
sudo bash /home/vagrant/museum/scripts/install-mysql.sh

sudo apt-get install libmysqlclient-dev -y

# update python 
sudo apt-get install python-dev python3-dev python3.5-dev -y
sudo apt-get -y install python3.5
wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py -q
sudo python3.5 /tmp/get-pip.py

cd /home/vagrant/museum
sudo pip install -r requirements.txt

# python3.5 manage.py migrate

# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@430.io', 'hahuahura')" | python3.5 manage.py shell
