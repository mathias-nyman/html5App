#!/bin/bash

#--------------------------------------------#
# This script will install Django from latest
# dev source under the ~/.local directory.
#--------------------------------------------#

tmpDir="/tmp/$USER-django-install"
dlUrl='git://github.com/django/django.git'
name='django'

rm -rf $tmpDir
mkdir -p $tmpDir
cd $tmpDir
git clone $dlUrl

cd $name
python setup.py install --user

# Done.
exit 0
