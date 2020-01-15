import sqlite3
from sqlite3 import Error


def createConn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn


def createTable(conn, table):
    try:
        cursor = conn.cursor()
        cursor.execute(table)
    except Error as e:
        print(e)


def addClient(conn, data):
    sql = 'INSERT INTO clients (name, address) VALUES(?, ?)'

    cursor = conn.cursor()
    cursor.execute(sql, data)
    return cursor.lastrowid


def addOrder(conn, data):
    sql = 'INSERT INTO orders (order_name, order_desc, client_id) VALUES (?, ?, ?)'

    cursor = conn.cursor()
    cursor.execute(sql, data)
    return cursor.lastrowid


def showAllOrders(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def showOrderByClient(conn, client_id):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM orders WHERE client_id={client_id}')

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def findClientByName(conn, name):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM clients WHERE name LIKE "%{name}%"')

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def deleteOrder(conn, order_id):
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM orders WHERE id={order_id}')
    conn.commit()


def main():
    db = 'sqlite.db'

    table_clients = """
                    CREATE TABLE IF NOT EXISTS clients (
                    id integer PRIMARY KEY, 
                    name text NOT NULL, 
                    address text NOT NULL
                    );
                    """
    table_orders = """
                    CREATE TABLE IF NOT EXISTS orders (
                    id integer PRIMARY KEY,
                    order_name TEXT NOT NULL,
                    order_desc TEXT NOT NULL,
                    client_id integer NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients (id)
                    );
                    """

    conn = createConn(db)

    if conn is not None:
        print('Creating tables...')
        createTable(conn, table_clients)
        createTable(conn, table_orders)
        print('Inserting data...')
        client1_data = ('Jan Kowalski', 'Warszawa')
        client1 = addClient(conn, client1_data)
        client2_data = ('Mariusz Nowak', 'Krakow')
        client2 = addClient(conn, client2_data)

        client1_order1 = ('Zestaw kluczy', 'profesjonalny zestaw kluczy', client1)
        client1_order2 = ('Wiertarka', 'wiertarka + 10 wierteł', client1)
        client2_order = ('Maszyna do miesa', 'maszyna do miesa ze zmiennymi nakladkami', client2)

        addOrder(conn, client1_order1)
        addOrder(conn, client1_order2)
        addOrder(conn, client2_order)

        print('Getting all orders...')
        showAllOrders(conn)

        print('Getting only client1 orders...')
        showOrderByClient(conn, 1)

        print('Looking for Mariusz in clients...')
        findClientByName(conn, 'Mariusz')

        print('Removing second order...')
        deleteOrder(conn, 2)

        print('Showing changes...')
        showAllOrders(conn)
    else:
        print('Error connecting db!')


if __name__ == '__main__':
    main()
