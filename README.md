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
  
#### Note for MSSQL Server running on macOS in Docker container

The temporary csv file location must be shared with container and must be copied to a non-shared file within the container for the bulk insert to work.

#### Reference
Adapted from pandas sample insertion [method](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-sql-method)
