#!/bin/sh

#add the .local and ../ext to path
scriptDir="$(pwd)"
pyjamasDir="$scriptDir/../ext/pyjamas/bin"
pyjamasLib="$scriptDir/../ext/pyjamas/library"
djangoDir="$scriptDir/../"
oviValpasDir="$scriptDir/../webapp"

export PATH=${HOME}/.local/bin:${pyjamasDir}:${PATH}
export PYTHONPATH=${pyjamasLib}:${djangoDir}:${oviValpasDir}:${PYTHONPATH}
echo $PYTHONPATH
