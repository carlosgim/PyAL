.. DS_Pyal documentation master file, created by
   sphinx-quickstart on Fri Nov  4 15:43:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Guía para el nuevo desarrollador
================================

Los pasos para agregar nuevas funciones son los siguientes:

1. Crear una rama de trabajo.
2. Crear la función en el módulo adecuado.
3. Documentar la función.
4. Hacer un merge request al master.

1. Crear una rama de trabajo
****************************

.. code-block:: bash

	git branch <nombre>

2. Creación de la función
*************************

En primer lugar, debo elegir a que grupo pertenece:

	* Extracción y Preprocesamiento de datos (/pyal/gc_data.py)
	* Análsis Exploratorio /pyal/ed_analysis.py
	* Visualización (/pyal/ed_visplots.py)
	* Propósito General (/pyal/gen_fun.py)

Entre paréntesis se indica el archivo donde guardar la función.

Ejemplo: 

.. code-block :: python

	def missing_values_table(df):
    		mis_val = df.isnull().sum()
    		mis_val_percent = 100 * df.isnull().sum()/len(df)
    		mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    		mis_val_table_ren_columns = mis_val_table.rename(
    		columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    		return mis_val_table_ren_columns.sort_values('% of Total Values', ascending=False)

3. Documentar la Función
************************

Para documentar, ingresamos a la carpeta /doc/source/ y elegimos el archivo, según la función

	* Extracción y Preprocesamiento de datos (/doc/source/gc_data.rst)
	* Análsis Exploratorio (/doc/source/ed_analysis.rst)
	* Visualización (/doc/source/ed_visplots.rst)
	* Propósito General (/doc/source/fn_general.rst)


Elijo una breve descripción y su forma de uso:

Ejemplo:

gc_data.missing_values_table


**Descripción** 

Explora los datos faltantes en una tabla y luego imprime la relación porcentual
de datos faltantes.

**Ejecución**

.. code-block:: python

	import pyal.gc_data as al

	al.gc_miss(dataframe)


4. Hacer un merge request al master
***********************************

Con el objetivo de mantener la integridad del código, es necesario
hacer una solicitud de merge al master. De ese modo las funciones
y documentación pasarán por revisiones para poder integrar al código
sin crear rupturas.

Para ello, hacer un git push a su rama y luego desde la página de
gitlab hacer un merge request.
