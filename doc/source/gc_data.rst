.. DS_Pyal documentation master file, created by
   sphinx-quickstart on Fri Nov  4 15:43:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Preprocesamiento de Datos (gc_data)
===================================

gc_data
*******

Módulo destinado al preprocesamiento de datos.

gc_data.MultiColumnLabelEncoder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Descripción** 

Convierte variables nominales (categóricas) a numéricas.

**Ejecución**

.. code-block:: python

	import pyal.gc_data as al

	al.MultiColumnLabelEncoder(dataframe,columnas)

**Ejemplo**

.. code-block:: python

	def _binarizo_variables_(df):
    	 df2 = df['TIPO_EVENTO'].fillna('NO1', inplace=True)
    	 df = al.MultiColumnLabelEncoder(columns = ['TIPO_EVENTO']).fit_transform(df)
    	 return df


gc_data.missing_values_table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Descripción** 

Explora los datos faltantes en una tabla y luego imprime la relación porcentual
de datos faltantes.

**Ejecución**

.. code-block:: python

	import pyal.gc_data as al

	al.gc_miss(dataframe)

gc_fold_data (Solo Linux, de momento)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Descripción** 

Fracciona un archivo grande y devuelve las partes en pequeños archivos

**Ejecución**

.. code-block:: python

	fd.split_file(file, parts)

**Variables**

*file*: Archivo en formato .csv

*parts*: Tamaño de fracciones en Mb

gc_unfold_data (en desarrollo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Descripción** 

Luego de aplicar *gc_fold_data*, es necesario recontruir el archivo
para obtener la base inicial. Esta función se encarga de devolver la 
base final a su estado original, *i.e.* con el scoring.