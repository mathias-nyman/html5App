#!/bin/bash

#--------------------------------------------#
# This script will install django-mediagenerator
# from source under the ~/.local directory.
#--------------------------------------------#

tmpDir="/tmp/$USER-djangoMediaGenerator-install"
tmpFile="$tmpDir/djangoMediaGenerator.zip"
dlUrl='http://pypi.python.org/packages/source/d/django-mediagenerator/django-mediagenerator-1.10.4.zip#md5=d9d03cb441c77ea12380a2c42474cb4f'
extractFolder='django-mediagenerator-1.10.4'

rm -rf $tmpDir
mkdir -p $tmpDir
cd $tmpDir
wget $dlUrl -O $tmpFile 
unzip $tmpFile

cd $extractFolder
python setup.py build
python setup.py install --user

# Done.
exit 0
