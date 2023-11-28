#  Copyright (c) Ioannis E. Kommas 2023. All Rights Reserved

import os
from sqlalchemy import text
import pandas as pd
import logging
from Private import sql_connect

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", None)

logging.basicConfig(level=logging.INFO)


def get_sql_data(
    sql_file: object,
    params: object = None,
    tuple_data: tuple = None,
    connection: object = sql_connect.connect(),
) -> object:
    """
    Executes a SQL query and returns the result as a pandas DataFrame.
    The query is read from a file and optional bind parameters can be provided.

    :param tuple_data:
    :param sql_file: The file name (including its path) that contains the SQL query.
    :param connection: The connection object to the SQL database.
    :param params: An optional dictionary to be sent to the SQL query with bind parameters.
                   Default is None, which means no parameters will be provided to the query.
    :return: A pandas DataFrame with the results obtained from the SQL query.
             Returns None if an error occurred or no query was executed.
    """
    if connection == "2":
        connection = sql_connect.connect_lato()

    def get_query_from_file(sfile):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(f"{script_directory}/{sfile}", "r") as file:
                query = file.read()
                if tuple_data and isinstance(tuple_data, tuple):
                    query = query.replace("{tuple_data}", str(tuple_data))
                return query
        except FileNotFoundError:
            logging.error("File not found: %s", sfile)
        except Exception as e:
            logging.exception("Error occurred: %s", e)

    query = get_query_from_file(sql_file)

    if query:
        try:
            # Check if params is not None before calling bindparams
            if params:
                df = pd.read_sql_query(text(query).bindparams(**params), connection)
            else:
                df = pd.read_sql_query(text(query), connection)
            return df
        except Exception as e:
            logging.exception("Error occurred while executing SQL query: %s", e)

    return None
