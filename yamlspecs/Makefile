PYTHON2_ENV = MODULES_BOOTSTRAP_FILE=modules.bootstrap.python2
PYTHON2_ENV += MODULES_FILE=modules.build.python2
PYTHON2_ENV += DEFAULTS=pkg-defaults2.yaml

PYTHON3_ENV = MODULES_BOOTSTRAP_FILE=modules.bootstrap
PYTHON3_ENV += MODULES_FILE=modules.build
PYTHON3_ENV += DEFAULTS=pkg-defaults.yaml

MAKEFILE_GENERIC = Makefile.generic
foo:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) pkg
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) pkg 

bootstrap:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) bootstrap
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) bootstrap

unbootstrap:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) unbootstrap
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) unbootstrap

clean:
	$(PYTHON2_ENV) make -e -f $(MAKEFILE_GENERIC) clean
	$(PYTHON3_ENV) make -e -f $(MAKEFILE_GENERIC) clean 
