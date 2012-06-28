#!/bin/sh

#add the .local and ../ext to path
scriptDir="$(pwd)"
pyjamasDir="$scriptDir/../ext/pyjs/bin"
pyjamasLib="$scriptDir/../ext/pyjs/library"
djangoDir="$scriptDir/../"
oviValpasDir="$scriptDir/../webapp"

export PATH=${HOME}/.local/bin:${pyjamasDir}:${PATH}
export PYTHONPATH=${pyjamasLib}:${djangoDir}:${oviValpasDir}:${PYTHONPATH}
echo $PYTHONPATH
