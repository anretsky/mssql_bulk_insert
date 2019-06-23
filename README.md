MSSQL CSV Bulk Insert
-------
This function writes data from a pandas dataframe to a temporary csv file. The temporary file is shared with the Docker container hosting the MSSQL server. The data is then inserted into the database using a bulk insert. Used as a callable for the method parameter of the pandas to_sql() function.


#### Example
~~~ python
df.to_sql('OptionRawIV', engine, if_exists='append', index=False, method=mssql_bulk_insert)
~~~

#### Performance
For a chunksize of 300000 rows with 20 columns of mostly floating numbers:
  * without callable function: ~6 min/chunk
  * with callable function: ~9 sec/chunk

#### Reference
Adapted from pandas sample insertion [method](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-sql-method)
