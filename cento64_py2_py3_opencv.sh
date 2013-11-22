# System Spec
# CentOS release 6.4 (Final)

# step 1: install all packages
sudo yum install boost-python
sudo yum install opencv-python
sudo yum install libdc1394-devel
sudo yum install libdc1394
sudo yum install python-setuptools
sudo yum install git
sudo yum install gcc gcc-g++
sudo yum install readline-devel
sudo yum install sqlite-devel
sudo yum install make cmake
sudo yum install zlib-devel
sudo yum install openssl-devel
sudo yum install gdbm-devel
sudo yum install bzip2-devel
sudo yum install xz-devel
sudo yum install ctags

sudo easy_install virtualenv
sudo easy_install jedi

# step 2: generate direcories
mkdir Downloads Workspace Movies

# step 3: Python2,7, Python3.3 installing
cd ~/Downloads/
wget http://www.python.org/ftp/python/3.3.3/Python-3.3.3.tgz
tar -xzvf Python-2.7.6.tgz 
cd ~/Downloads/Python-2.7.6
./configure --prefix=/usr/local/python2.7 --with-pydebug
make
sudo make install

cd ~/Downloads/
wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
tar -xzvf Python-3.3.3.tgz 
cd ~/Downloads/Python-3.3.3
./configure --prefix=/usr/local/python3.3.3
make
sudo make install
cd ~/Workspace/
virtualenv -p /usr/local/python3.3.3/bin/python3.3 Py33Env

# step 4: vim7.4
cd ~/Downloads/
wget ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2
tar -xvf vim-7.4.tar.bz2 
cd vim74/
./configure --prefix=/usr/local/vim74 --enable-pythoninterp=yes --with-python-config-dir=/usr/local/python2.7/lib/python2.7/config
make
sudo make install
mkdir .vim/
mkdir .vim/bundle
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

# step 5: configure bash & vim
echo 'export PATH=/usr/local/vim74/bin:$PATHA' >> ~/.bashrc
echo 'export PATH=/usr/local/python3.3/bin:$PATH' >> ~/.bashrc
echo 'export PATH=/usr/local/python2.7/bin:$PATH' >> ~/.bashrc
echo 'alias activate="source bin/activate"' >> ~/.bashrc
echo 'export PYTHONPATH+=/usr/lib/python2.6/site-packages:$PYTHONPATH"' >> ~/.bashrc
