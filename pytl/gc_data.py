#**************************************************************************************************
__copyright__ = "in revision"
__license__ = "in revision"
__version__ = "1.0.1"
__status__ = "Testing"
#**************************************************************************************************

import os
import subprocess

def split_file(file, size):

	msn = 'split --bytes '+str(size)+'M --numeric-suffixes --suffix-length=2 '+ file+' '+file+'par'

	print msn
	
	print 'Fraccionando archivos...'
	
	os.system(msn)

# Tomo la primera linea del archivo f_get_header y agrego a f_add_header

def split_add_header(f_get_header, f_add_header):

	msn1 = 'head -1 ' + f_get_header +' | tail -1'

	header = os.system(str(msn1))

	print '******************header***********************'

	# Warning Arreglar, no guarda bien el mensaje en header
	# Buscar el modo de guardar adecuadamente el header

	header = str(subprocess.check_output(msn1, shell=True))

	print "program output:", str(header)
	
	exit(0)

	sed_sentence = 'sed -i 1i'+ str(header) +' '+ f_add_header

	print 'Agregando encabezados...'
	
	os.system(sed_sentence)

	print 'Verificando los encabezados nuevos...'

	msn2 = 'head -1 ' + f_add_header +' | tail -1'

	print os.system(msn2)
	print '***************END PROCESS****************'

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

# Transformo las variables string a numeros

class MultiColumnLabelEncoder:
    def __init__(self, columns = None):
        self.columns = columns # Arreglo de columnas de interes

    def fit(self,X,y=None):
        return self 

    def transform(self,X):
        '''
        Transforma las columnas indicadas en el array columns,
        si no se especifica, transforma todas las columnas.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)

import pandas as pd

def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum()/len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    return mis_val_table_ren_columns.sort_values('% of Total Values', ascending=False)
