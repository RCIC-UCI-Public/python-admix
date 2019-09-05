# python-admix
Python2 and python3 and supporting RPMS created via YAML2RPM

##  Prerequisites
Make sure the developemnt RPMs are installed. Follow the `Quickstart`
section of the guide in https://github.com/RCIC-UCI-Public/yaml2rpm/blob/master/README.md

##  Build python
These include packages pip, numpy and setuptools for python2/3.
Environment modules are build  for python2/3

1. Download the repo
   ```bash
   git clone https://github.com/RCIC-UCI-Public/python-admix
   ```

1. Download the python sources needed to build basic distro. 
   ```bash
   cd python-admix/
   make download
   ls sources/
   ```

1. Create and install basic distro 
   ```bash
   cd yamlspecs/
   make bootstrap | tee out-make-bootstrap 2>&1
   ```

## Building addiitonal packages

To build additional packages, create yaml files and add definitions of 
the packages to one of 3 files:

- versions.yaml if want to buld this package for python 2 and python 3
- versions2.yaml if want to buld this package only for python 2 
- versions3.yaml if want to buld this package only for python 3

1. Download sources, for example
   ```bash
   make download PKG=graphviz
   make download -f Makefile3 PKG=mypy
   ```

1. Run to build packages for both python versions
   ```bash
   cd yamlspecs/
   make
   ```
