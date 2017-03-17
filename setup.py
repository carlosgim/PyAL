#**************************************************************************************************
#
# Develop in Buenos Aires - Argentina
#
__maintainer__ = "Carlos A. Gimenez"
__status__ = "Testing"
__version__= "1.0.4"
#**************************************************************************************************

import sys

if sys.version >= '2.8':
    print('# Usted tiene la version')
    print(sys.version)
    sys.exit(1)

try:
    from setuptools import setup
except (ImportError):
    from distutils.core import setup

__about__ = {}

with open("__about__.py") as fp:
    exec(fp.read(), None, __about__)

setup(
    name="PyAL",
    version=__about__["__version__"],
    author="Carlos A. Gimenez",
    description="Python package for Analytics Work",
    long_description=open('README.rst').read(),
    packages=["pytl"],
    license='BSD License',
    keywords='setup',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Script',
        'Intended Audience :: Developers',
        'License :: Apache Software License',
        'Operating System :: Linux and Windows',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
	'scipy',
        'sklearn',
        'pandas',
        'numpy'
    ],
)

import subprocess
import os

url = "doc/build/html/index.html"

if sys.platform=='win32':
    os.startfile(os.getcwd()+'/'+url)
elif sys.platform=='darwin':
    subprocess.Popen(['open', url])
else:
    try:
        subprocess.Popen(['xdg-open', url])
    except OSError:
        print 'Please open a browser on: '+url


print "======================================================="
print "======================================================="
print "======================================================="
print "****************Instalacion correcta*******************"
print ""
print "Usted instalo la libreria PyAL"
print "Version:", __version__
print ""
print "-------------------------------------------------------"
print ""
print ""
print "****************MANUAL DE PYAL*************************"
print ""
print "Al finalizar la instalacion deberia abrirse un navegador"
print "apuntando al manual de PyAL."
print "Por favor marque esa pagina para su futuro uso."
print "Si no se abre el manual, por favor abrir el siguiente"
print "archivo con su navegador habitual y marcar la pagina"
print "/doc/build/html/index.html"
print ""
print "Muchas gracias"
print "======================================================="
print "======================================================="
print "======================================================="

