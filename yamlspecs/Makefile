# Copyright (c) 2000 - 2019 The Regents of the University of California.
# # All rights reserved.	
# # This includes the Generic yaml2rpm Makefile - most packaging should
# # be able to use this.
#

SUBMAKES = Makefile2 Makefile3
.DEFAULT_GOAL = default

%.pkg:
	for f in $(SUBMAKES); do \
		if [ -f $@ ] ; then /bin/rm $@; fi; \
		$(MAKE) -f $$f $@; \
        done
	
manifest module-provides module-requires:
	$(MAKE) -s -f Makefile2 modules.build $@
	$(MAKE) -s -f Makefile3 modules.build $@

ansible:
	$(MAKE) -s -f Makefile2 modules.build $@
%: 	
	$(MAKE) -f Makefile2 $*
	$(MAKE) -f Makefile2 clean
	$(MAKE) -f Makefile3 $*
