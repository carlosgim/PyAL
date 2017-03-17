#**************************************************************************************************
__copyright__ = "in revision"
__license__ = "in revision"
__version__ = "1.0.3"
__status__ = "Testing"
#**************************************************************************************************

from pyspark.sql.functions import col
from pyspark.sql import Row


def df_shape(DF):
	col_size = len(DF.columns)
	row_size = DF.count()
	values = {"rows" : row_size, "cols" : col_size, "textual":"{0} x {1}".format(row_size, col_size)}
	return values


def field_in_db(field, db):
	spark.sql("USE {0}".format(db))
	list_table_names = [x.tableName for x in spark.sql("SHOW tables IN elementos_red").collect()]
	list_table_checks = []
	Bool = True
	for tab in list_table_names:
		try:
			helper = spark.sql("DESCRIBE {0}".format(tab)).filter(col("col_name").like(field))
			if helper.count() == 0: Bool = "False"
			else: Bool = "True"
		except: Bool = "Null"
		list_table_checks.append(Bool)
	data = [[i, j] for i,j in zip(list_table_names, list_table_checks)]
	data = sc.parallelize(data)
	DF = spark.createDataFrame(data, ["tableName", "hasIt"])
	return DF.filter(col("hasIt")=="True")

