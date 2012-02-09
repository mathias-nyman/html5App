#!/bin/bash

#--------------------------------------------#
# This script will install libcommonDjango from 
# latest dev source under the ~/.local directory.
#--------------------------------------------#

tmpDir="/tmp/$USER-libCommonDjango-install"
dlUrl='http://svn.pimentech.org/pimentech/libcommonDjango'
extractFolder='libcommonDjango'
thisDir="$( cd "$( dirname "$0" )" && pwd )"

rm -rf $tmpDir
mkdir -p $tmpDir
cd $tmpDir
svn checkout $dlUrl

cd $extractFolder
python setup.py install --user


# Done.
exit 0
