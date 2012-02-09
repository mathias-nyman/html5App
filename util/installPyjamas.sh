#!/bin/bash

#--------------------------------------------#
# This script will install pyjamas from latest
# dev source under the ~/.local directory.
#--------------------------------------------#

dlUrl='git://pyjs.org/git/pyjamas.git'
extractFolder='pyjamas'
thisDir="$( cd "$( dirname "$0" )" && pwd )"
installDir=${thisDir}/../ext/
echo $installDir

mkdir -p $installDir
cd $installDir
rm -rf $extractFolder
git clone $dlUrl

cd $extractFolder
python bootstrap.py
cd pyjs
python setup.py develop --user

# Done.
exit 0
