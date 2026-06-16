from flask import Flask, render_template, request, redirect
from database import (
    setup_database,
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    get_summary_stats
)

app = Flask(__name__)

setup_database()


@app.route('/')
def home():
    transactions = view_transactions()

    current_balance, total_income, total_expense = get_summary_stats()

    return render_template(
        'index.html',
        transactions=transactions,
        current_balance=current_balance,
        total_income=total_income,
        total_expense=total_expense
    )


if __name__ == '__main__':
    app.run(debug=True)
