from database_handler import execute_query, create_connection
import misc_handler
import lookups

def truncate_staging_tables(schema_name, table_list, db_session):
    for table in table_list:
        dst_table = f"{table}"
        truncate_query = f"""
        TRUNCATE TABLE IF EXISTS {schema_name}.{dst_table}"""
        execute_query(db_session, truncate_query)

def execute_posthook():
    print("posthook")
    db_session = create_connection()
    tables = misc_handler.return_staging_tables_as_list()
    truncate_staging_tables(lookups.DESTINATION_SCHEMA.DESTINATION_NAME.value,tables,db_session)
   