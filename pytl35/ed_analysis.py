#**************************************************************************************************
__copyright__ = "in revision"
__license__ = "in revision"
__version__ = "1.0.1"
__status__ = "Testing"
#**************************************************************************************************

import pandas as pd

def show_info(df):
	print('El numero de registros en la tabla es:')
	print(len(df))
	print(df.info())
	print('Describe *************************************************************')
	print(df.describe())
