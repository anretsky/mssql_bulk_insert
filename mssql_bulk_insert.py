import sys
import os
import csv
from tempfile import NamedTemporaryFile

def mssql_bulk_insert(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    with NamedTemporaryFile() as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_iter)
        dbapi_conn = conn.connection
        tempfile = csvfile.name
        with dbapi_conn.cursor() as cur:
            table_name = '[dbo].[{}]'.format(table.name)
            command = '''BULK INSERT {}
                FROM {}
                WITH (FORMAT = 'CSV',
                FIELDTERMINATOR = ','
                ) '''.format(table_name, tempfile)
            
            # For MSSQL Server running on macOS in docker container:
            # csvfile must be shared with docker container and shared
            # data file must be copied to non-shared file for bulk
            # insert to work. Use line below to copy shared file:
            # os.system("docker exec sql1 cp opt/mssql/{}  opt/mssql/data.csv".format(tempfile))
            
            cur.execute(command)
