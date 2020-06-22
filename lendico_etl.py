# Importing required libraries
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine
import datetime


# Function to connect to source DB
def src_connect():
    conn = None
    src_engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/source')
    conn = src_engine.connect()
    print("Connected to Source DB")

    return conn


# Function to connect to target DB
def target_connect():
    conn = None
    target_engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/target')
    conn = target_engine.connect()
    print("Connected to Target DB")

    return conn


# Delete the existing rows
def cleanup_duplicates(df_name, table_name, dup_col, conn_str):
    sql_query = "select * from " + table_name
    df_name.drop_duplicates(dup_col, keep="last", inplace=True)
    df_name = pd.merge(left=df_name, right=pd.read_sql_query(sql_query, conn_str), how="left", on=dup_col,
                       indicator=True, suffixes=('', '_y'))
    df_name = df_name[df_name["_merge"] == "left_only"]
    df_name.drop(columns=["_merge"], axis=1, inplace=True)
    df_name.drop(df_name.filter(regex='_y').columns, axis=1, inplace=True)

    return df_name


# Error logging function
def etl_error_logging(conn, etl_status, etl_error_code, etl_table_name, etl_row_count):
    today = str(datetime.date.today())
    f = open(today + "_ETL_log.txt", "a+")

    if conn != "NA":

        f.write(
            str(datetime.datetime.now()) + "," + etl_status + "," + etl_error_code + "," + etl_table_name + "," + str(
                etl_row_count) + "\n")
        f.close()

        insert_string = "INSERT INTO etl_process_log values (nextval('error_id')" + ",'" + today + "','" + etl_status + "','" + etl_error_code + "','" + etl_table_name + "','" + str(
            etl_row_count) + "')"
        conn.execute(insert_string)

    else:

        f.write(
            str(datetime.datetime.now()) + "," + etl_status + "," + etl_error_code + "," + etl_table_name + "," + str(
                etl_row_count) + "\n")
        f.close()


# Main ETL Function
def lendico_etl():
    try:
        src_conn = src_connect()
        target_conn = target_connect()

    except (Exception, pg.Error) as error:
        print("Error - ", error)
        etl_error_logging("NA", "Failed", str(error).replace("'", ""), "NA", 0)
        exit()

    last_run_date = None
    cnt_cursor = target_conn.execute("select count(1) from etl_process_log")
    cnt = cnt_cursor.fetchone()[0]

    try:
        if cnt == 0:
            src_address_df = pd.read_sql_query("select * from address", src_conn)
            src_company_df = pd.read_sql_query("select * from company", src_conn)

        else:
            # Fetching last successful load date
            cursor = target_conn.execute("""SELECT etl_run_date from etl_process_log where upper(etl_status) = 'SUCCESS' 
                                         and id in (select MAX(id) from etl_process_log where upper(etl_status) = 'SUCCESS');""")
            last_run_date = cursor.fetchone()

            # Fetching only new records from source
            src_address_df = pd.read_sql_query(
                "select * from address where created_at >" + "'" + str(last_run_date[0]) + "'", src_conn)
            src_company_df = pd.read_sql_query(
                "select * from company where created_at >" + "'" + str(last_run_date[0]) + "'", src_conn)

        # Removing duplicates
        final_address_df = cleanup_duplicates(src_address_df, "address", "id", target_conn)
        final_company_df = cleanup_duplicates(src_company_df, "company", "company_id", target_conn)

    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        etl_error_logging(target_conn, "Failed", str(error).replace("'", ""), "NA", 0)
        exit()
    try:
        final_address_df.to_sql("address", con=target_conn, if_exists="append", index=False)
        print("Address table loaded into Target DB")
        etl_error_logging(target_conn, "Success", "NA", "Address", final_address_df.shape[0])

    except (Exception, pg.Error) as error:
        print("Address Load Error - ", error)
        etl_error_logging(target_conn, "Failed", error, "Address", "NA")

    try:
        final_company_df.to_sql("company", con=target_conn, if_exists="append", index=False)
        print("Company table loaded into Target DB")
        etl_error_logging(target_conn, "Success", "NA", "Company", final_company_df.shape[0])

    except (Exception, pg.Error) as error:
        print("Company Load Error - ", error)
        etl_error_logging(target_conn, "Failed", error, "Company", "NA")
        exit()

    src_conn.close()
    target_conn.close()


lendico_etl()