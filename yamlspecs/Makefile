PYTHON2_ENV = BOOTSTRAP_MODULES_FILE=modules.bootstrap.python2
PYTHON2_ENV += MODULES_FILE=modules.build.python2
PYTHON2_ENV += DEFAULTS=pkg-defaults2.yaml

PYTHON3_ENV = BOOTSTRAP_MODULES_FILE=modules.bootstrap
PYTHON3_ENV += MODULES_FILE=modules.build
PYTHON3_ENV += DEFAULTS=pkg-defaults.yaml

MAKEFILE_GENERIC = Makefile.generic


default:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) 
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) clean
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) 

%:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) $@ 
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) clean
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) $@

%.pkg: FORCE
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) $@ 
	- /bin/rm $@
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) $@
	
FORCE:


#bootstrap:
#	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) bootstrap
#	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) bootstrap
#
#unbootstrap:
#	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) unbootstrap
#	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) unbootstrap
#
#clean:
#	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) clean
#	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) clean 
