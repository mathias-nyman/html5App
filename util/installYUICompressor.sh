#!/bin/bash

#--------------------------------------------#
# This script will install YUI Compressor
# from latest release the ../ext directory.
#--------------------------------------------#

tmpFile="yuiCompressor.zip"
dlUrl='http://yui.zenfs.com/releases/yuicompressor/yuicompressor-2.4.6.zip'
extractFolder='yuicompressor-2.4.6'
thisDir="$( cd "$( dirname "$0" )" && pwd )"
installDir="${thisDir}/../ext/"

cd $installDir
rm -rf $extractFolder
wget $dlUrl -O $tmpFile 
unzip $tmpFile

rm -f $tmpFile
mv $extractFolder yuiCompressor

# Done.
exit 0
