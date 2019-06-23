def mssql_bulk_insert(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    with open('tmp_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_iter)
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        table_name = '[dbo].[{}]'.format(table.name)
        command = '''BULK INSERT {}
            FROM {}
            WITH (FORMAT = 'CSV',
            FIELDTERMINATOR = ','
            ) '''.format(table_name, r"'/opt/mssql/data.csv'")
        # shared data file must be copied to non-shared file for bulk insert to work
        os.system("docker exec sql1 cp opt/mssql/tmp_data.csv opt/mssql/data.csv")
        cur.execute(command)
