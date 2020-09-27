# ubuntu_mirror = 'http://mirror.its.sfu.ca/mirror/ubuntu/'
# ubuntu_mirror = 'http://mirror.csclub.uwaterloo.ca/ubuntu/'
ubuntu_mirror = 'http://ubuntu.mirror.rafal.ca/ubuntu/'
ubuntu_release = 'bionic'
ubuntu_version = '18.04'
username = 'vagrant'
user_home = '/home/' + username
project_home = user_home + '/project/calculatorApp' # you may need to change the working directory to match your project
project_functions = project_home + '/home/functions' # where to compile the functions

python3_packages = '/usr/local/lib/python3.6/dist-packages'
ruby_gems = '/var/lib/gems/2.5.0/gems/'


# Get Ubuntu sources set up and packages up to date.

template '/etc/apt/sources.list' do
  variables(
    :mirror => ubuntu_mirror,
    :release => ubuntu_release
  )
  notifies :run, 'execute[apt-get update]', :immediately
end
execute 'apt-get update' do
  action :nothing
end
execute 'apt-get upgrade' do
  command 'apt-get dist-upgrade -y'
  only_if 'apt list --upgradeable | grep -q upgradable'
end
directory '/opt'
directory '/opt/installers'


# Basic packages many of us probably want. Includes gcc C and C++ compilers.

package ['build-essential', 'cmake']

# Other core language tools you might want

package ['python3', 'python3-pip', 'python3-dev']  # Python
package 'golang-go'  # Go

# SWIG

package 'swig'

# Django 

execute 'pip3 install django' do
  not_if "pip3 list | grep django"
end

# Build SWIG files

execute 'swig -c++ -python -py3 -modern calc.i' do 
  cwd project_functions
  user username
  environment 'HOME' => user_home
end

execute 'g++ -fPIC -c calc.cpp calc_wrap.cxx -I/usr/include/python3.6' do
  cwd project_functions
  user username
  environment 'HOME' => user_home
end

execute 'g++ -shared calc.o calc_wrap.o -o _calc.so' do
  cwd project_functions
  user username
  environment 'HOME' => user_home
end

# Build Go Shared files

execute 'go build -o conversion.so -buildmode=c-shared conversion.go' do 
  cwd project_functions
  user username
  environment 'HOME' => user_home
end

# Migrate django server

execute 'python3 manage.py migrate' do
  cwd project_home
  user username
  environment 'HOME' => user_home
end

# Run Django server

execute 'python3 manage.py runserver 0.0.0.0:8000 &' do
  cwd project_home
  user username
  environment 'HOME' => user_home
end
