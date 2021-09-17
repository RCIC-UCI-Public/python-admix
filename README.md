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

## Building additional packages

To build additional packages, create yaml files and add definitions of 
the packages to one of 3 files:

- versions.yaml if want to buld this package for python 3
- python2.versions.yaml if want to buld this package only for python 2 
  or the version of package differes for python 2/3.

1. Download sources, for example
   ```bash
   make download SET=python2 PKG=scipy  # download version for python2 build
   make download PKG=scipy              # download version for python3 build
   ```

1. Run to build packages for both python versions
   ```bash
   cd yamlspecs/
   make scipy.pkg
   rm scipy.pkg
   make SET=python2 scipy.pkg
   ```
## Python 2

Support for python 2 is dropped and depending on a particular package build outcome will vary. 
Many packages depend on setuptools_scm for legacy dependencies and this package is usually
automaticallty downloaded into temp location during python package build. 

As of setuptools_scm v. 6.0.0 support for python2 is dropped which will result in build failure.

Install setuptools_scm 5.0.2 for python2 during bootstrap to prevent failure of building. 

As of current python2 package list, building dateutils and virtualenv failed without setuptools_scm.
