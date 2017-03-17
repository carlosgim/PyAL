.. DS_PyTA documentation master file, created by
   sphinx-quickstart on Fri Nov  4 15:43:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Análisis Exploratorio (ed_analysis)
===================================

ed_show_info
************

Esta es la primer aproximación que hacemos al conjunto de 
datos de interés. **ed_show_info** permite explorar en 
forma inmediata el tamaño de la tabla, cuartiles, tipos 
de datos, etc. (En desarrollo)

show_info
^^^^^^^^^

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
    	 return df2

ed_visplot
**********