.. DS_Pyal documentation master file, created by
   sphinx-quickstart on Fri Nov  4 15:43:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Funciones de Spark
==================

df_shape
********

Módulo destinado a la busqueda en Hive y exploracion de tablas.

**Descripción** 

Brinda informacion sobre el tamaño de la tabla (cantidad de filas y columnas)

**Ejecución**

.. code-block:: python

	import pyal.sp_func as sp

	
**Ejemplo**

.. code-block:: python

  sp.df_shape(dataframe)

field_in_db
***********

**Descripción** 

Busca la columna deseada entre todas las tablas de la base de datos.

**Ejecución**

.. code-block:: python

	import pyal.sp_func as sp

**Ejemplo**

.. code-block:: python

	sp.field_in_db(field, db)

