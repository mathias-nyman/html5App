#----------------------------------------------
# A simple Makefile for a simple job
#----------------------------------------------


# Try to determine IP address to broadcast on
# TODO: get active ip_address in a better way!
IP_ADDRESS=$(shell ifconfig wlan0 | /bin/grep -P " addr:\d+\.\d+.\.\d+\.\d+" | cut -d: -f2 | cut -d' ' -f1)
ifeq ($(strip $(IP_ADDRESS)),)
	IP_ADDRESS=$(shell ifconfig eth0 | /bin/grep -P " addr:\d+\.\d+.\.\d+\.\d+" | cut -d: -f2 | cut -d' ' -f1)
endif

PORT = 8000


default: run

compile:
	@ echo "Compiling Pyjamas code to JavaScript."
	@ cd webapp/media; ../../ext/pyjs/bin/pyjsbuild ExampleApp


# Will run the development server
run: compile
	@ echo "Running development server"
	@ echo "Broadcast address:port : $(IP_ADDRESS):$(PORT)"
	@ cd webapp; python manage.py syncdb
	@ cd webapp; python manage.py runserver

run-broadcasted: compile
	@ echo "Running broadcasted server"
	@ cd webapp; python manage.py syncdb
	@ cd webapp; python manage.py runserver $(IP_ADDRESS):$(PORT)

# Will generate and compress code for production
# FIXME: this is not applicable anymore, how do we deploy?
production:
	@ echo "Generating production code"
	@ cd webapp; python manage.py generatemedia


# Will fetch and install all needed external dependencies
dependencies:
	@ echo "Installing external dependecies inti ./ext"
	./util/installDjango.sh
	./util/installDjangoMediaGenerator.sh
	./util/installPyjamas.sh
	./util/installYUICompressor.sh
	./util/installLibCommonDjango.sh
	easy_install --prefix=~/.local httplib2

crawlers:
	@ echo "Running crawlers."
	@ cd util; source env.sh; cd -; python crawlers/ExampleCrawler.py

clean:
	@$(RM) -rf **/*.pyc

.PHONY: crawlers
