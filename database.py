import sqlite3


def setup_database():
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   transaction_type TEXT NOT NULL,
                   date TEXT NOT NULL)
    ''')

    connection.commit()
    connection.close()


setup_database()


def add_transaction(name, amount, category, transaction_type, date):
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO transactions(name, amount, category, transaction_type, date)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, amount, category, transaction_type, date))

    connection.commit()
    connection.close()


def view_transactions():
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM transactions')

    transactions = cursor.fetchall()

    connection.close()

    return transactions


def update_transaction(transaction_id, name, amount, category, transaction_type, date):
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    UPDATE transactions
    SET name = ?, amount = ?, category = ?, transaction_type = ?, date = ?
    WHERE id = ?
    ''', (name, amount, category, transaction_type, date, transaction_id))

    connection.commit()
    connection.close()


def delete_transaction(transaction_id):
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    DELETE FROM transactions
    WHERE id = ?
    ''', (transaction_id,))

    connection.commit()
    connection.close()


def get_summary_stats():
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT SUM(amount)
    FROM transactions
    WHERE transaction_type = 'Income'
    ''')

    result = cursor.fetchone()

    total_income = result[0]

    cursor.execute('''
    SELECT SUM(amount)
    FROM transactions
    WHERE transaction_type = 'Expense'
    ''')

    result = cursor.fetchone()

    total_expense = result[0]

    if total_income is None:
        total_income = 0
    if total_expense is None:
        total_expense = 0

    current_balance = total_income - total_expense
    connection.close()

    return current_balance, total_income, total_expense


def get_transaction(transaction_id):
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT * FROM transactions
    WHERE id = ?
    ''', (transaction_id,))

    transaction = cursor.fetchone()

    connection.close()

    return transaction
