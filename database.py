import sqlite3
import random
from datetime import datetime, timedelta


# Connessione al database SQLite
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


# Pulizia delle tabelle esistenti per partire da un database pulito
cursor.executescript("""
    DROP TABLE IF EXISTS account_managers;
    DROP TABLE IF EXISTS employees;
    DROP TABLE IF EXISTS loans;
    DROP TABLE IF EXISTS transactions;
    DROP TABLE IF EXISTS accounts;
    DROP TABLE IF EXISTS branches;
    DROP TABLE IF EXISTS addresses;
    DROP TABLE IF EXISTS customers;
""")


# Creazione delle tabelle dello schema relazionale
cursor.executescript("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        join_date TEXT
    );


    CREATE TABLE addresses (
        address_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        city TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );


    CREATE TABLE branches (
        branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
        branch_name TEXT,
        city TEXT
    );


    CREATE TABLE accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        branch_id INTEGER,
        account_type TEXT,
        balance REAL,
        open_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
    );


    CREATE TABLE loans (
        loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        loan_type TEXT,
        amount REAL,
        interest_rate REAL,
        status TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
""")


# (Il codice originale continua inserendo dati casuali per clienti, conti, prestiti, ecc.)
conn.commit()
conn.close()
print("Database bancario realistico creato con successo!")

