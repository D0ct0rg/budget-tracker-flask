from flask import Flask, render_template, request, redirect
from database import (
    setup_database,
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    get_summary_stats,
    get_transaction,
    filter_transactions,
    get_expenses_by_category
)

app = Flask(__name__)

setup_database()


@app.route('/')
def home():

    current_balance, total_income, total_expense = get_summary_stats()

    filter_type = request.args.get('filter', 'all')

    if filter_type == 'income':
        transactions = filter_transactions('Income')
    elif filter_type == 'expense':
        transactions = filter_transactions('Expense')
    else:
        transactions = view_transactions()

    expenses_by_category = get_expenses_by_category()

    chart_labels = [row[0] for row in expenses_by_category]
    chart_values = [row[1] for row in expenses_by_category]

    return render_template(
        'index.html',
        transactions=transactions,
        current_balance=current_balance,
        total_income=total_income,
        total_expense=total_expense,
        filter_type=filter_type,
        chart_labels=chart_labels,
        chart_values=chart_values
    )


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    transaction_type = request.form['transaction_type']
    date = request.form['date']

    if name.strip() != '' and amount.strip() != '':
        add_transaction(name, amount, category, transaction_type, date)

    return redirect('/')


@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete(transaction_id):
    delete_transaction(transaction_id)
    return redirect('/')


@app.route('/edit/<int:transaction_id>')
def edit(transaction_id):
    transaction = get_transaction(transaction_id)

    return render_template(
        'edit.html',
        transaction=transaction
    )


@app.route('/update/<int:transaction_id>', methods=['POST'])
def update(transaction_id):
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    transaction_type = request.form['transaction_type']
    date = request.form['date']

    update_transaction(transaction_id, name, amount,
                       category, transaction_type, date)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
