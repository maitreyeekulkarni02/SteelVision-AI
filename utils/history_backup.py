import sqlite3
from datetime import datetime
import pandas as pd


DB_NAME = "steelvision_history.db"



def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inspections
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            machine_id TEXT,

            inspection_date TEXT,

            defects TEXT,

            defect_count INTEGER,

            health_score INTEGER,

            machine_status TEXT,

            maintenance_priority TEXT
        )
        """
    )


    conn.commit()

    conn.close()



def save_inspection(
        machine_id,
        defects,
        health_score,
        status,
        priority
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO inspections
        (
            machine_id,
            inspection_date,
            defects,
            defect_count,
            health_score,
            machine_status,
            maintenance_priority
        )

        VALUES (?,?,?,?,?,?,?)
        """,

        (
            machine_id,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            str(defects),
            len(defects),
            health_score,
            status,
            priority
        )

    )


    conn.commit()

    conn.close()



def get_history():

    create_table()

    conn = sqlite3.connect(DB_NAME)


    df = pd.read_sql_query(
        """
        SELECT *
        FROM inspections
        ORDER BY id DESC
        """,
        conn
    )


    conn.close()


    return df

def format_history(df):

    if df.empty:
        return df


    df = df.copy()


    df.columns = [
        col.replace("_", " ").title()
        for col in df.columns
    ]


    return df