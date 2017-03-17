.. Documentation master file
   sphinx-quickstart on Fri Nov  4 15:43:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Funciones de propósito general
==============================

encriptar_basis
***************

**Descripción** 

	Encripta archivos .csv utilizando SHA hash algoritmos (sha1, sha224, sha256, sha384, sha512)

**Ejecución**

.. code-block:: python

	import pyal.fn_general as al

	al.encode(filename)

**Ejemplo**

.. code-block:: text

	Please type the csv file name to encrypt without header (Example: mails.csv)
	mails.csv
	Select the SHA hash algorithm. Formato csv y sin encabezado
	1 = sha1
	2 = sha224
	3 = sha256
	4 = sha384
	5 = sha512
	3
	Encrypted File: encrypted_mails.csv



