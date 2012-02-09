#!/bin/bash

#--------------------------------------------#
# This script will install Django from latest
# dev source under the ~/.local directory.
#--------------------------------------------#

tmpDir="/tmp/$USER-django-install"
dlUrl='http://code.djangoproject.com/svn/django/trunk/'
name='django-trunk'

rm -rf $tmpDir
mkdir -p $tmpDir
cd $tmpDir
svn co $dlUrl $name

cd $name
python setup.py install --user

# Done.
exit 0
