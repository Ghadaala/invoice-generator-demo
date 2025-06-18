from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def invoice_form():
    return render_template('invoice_form.html')

@app.route('/generate', methods=['POST'])
def generate_invoice():
    client_name = request.form.get('client_name')
    client_address = request.form.get('client_address')
    company_name = request.form.get('company_name')
    descriptions = request.form.getlist('description')
    quantities = request.form.getlist('quantity')
    unit_prices = request.form.getlist('unit_price')

    max_items = 1  # نسخة تجريبية: بند واحد فقط
    items = list(zip(descriptions, quantities, unit_prices))[:max_items]

    total_amount = 0.0
    processed_items = []
    for desc, qty, price in items:
        line_total = int(qty) * float(price)
        total_amount += line_total
        processed_items.append({
            'description': desc,
            'quantity': qty,
            'price': price,
            'line_total': f"{line_total:.2f}"
        })

    return render_template('invoice_demo.html',
                           client_name=client_name,
                           client_address=client_address,
                           company_name=company_name,
                           items=processed_items,
                           total=f"{total_amount:.2f}",
                           date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)