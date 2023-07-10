from db_operations import check_database_exists, create_database, connect_to_database, select_data, insert_data, update_data, delete_data, create_table
import queries_and_procedures as qprocedures
# Configuration for MySQL container
host = "172.20.0.2"
port = 3306
user = "root"
password = "root"
database_name = "nahdi_online_db"

if not check_database_exists(host, port, user, password, database_name):
    create_database(host, port, user, password, database_name)
    print("Database created!")

# Connect to the database
db = connect_to_database(host, port, user, password, database_name)
print("Connected to the database.")

# Example usage of create_table, select_data, insert_data, update_data, delete_data methods
create_table_query = qprocedures.CREATE_NAHDIONLINE_TABLE
create_table(db, create_table_query)

select_query = qprocedures.SELECT_ALL_FROM_NAHDIONLINE_TABLE
select_data(db, select_query)

insert_query = qprocedures.INSERT_INTO_NAHDIONLINE_TABLE
insert_data(db, insert_query)

# update_query = "UPDATE your_table SET age = 30 WHERE name = 'John'"
# update_data(db, update_query)

# delete_query = "DELETE FROM your_table WHERE name = 'John'"
# delete_data(db, delete_query)

# Close the database connection
db.close()
