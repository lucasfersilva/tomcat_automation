from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        client_name = request.form.get('client_name', 'Lucas Fernandes')
        item1 = request.form.get('item1')
        subtotal1 = request.form.get('subtotal1')
        item2 = request.form.get('item2')
        subtotal2 = request.form.get('subtotal2')
        item3 = request.form.get('item3')
        subtotal3 = request.form.get('subtotal3')
        # You can now use these variables in your application
        # For now, we'll just print them
        print(client_name, item1, subtotal1, item2, subtotal2, item3, subtotal3)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, send_file
import jinja2
import pdfkit
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        client_name = request.form['client_name']
        item1 = request.form['item1']
        subtotal1 = int(request.form['subtotal1'])
        item2 = request.form['item2']
        subtotal2 = int(request.form['subtotal2'])
        item3 = request.form['item3']
        subtotal3 = int(request.form['subtotal3'])
        total = subtotal1 + subtotal2 + subtotal3
        today_date = datetime.date.today()
        invoice_number = 1

        context = {'client_name': client_name,
                   'item1': item1,
                   'item2': item2,
                   'item3': item3,
                   'subtotal1':subtotal1,
                   'subtotal2': subtotal2,
                   'subtotal3': subtotal3,
                   'total': total,
                   'invoice_number': invoice_number,
                   'today_date': today_date}

        template_loader = jinja2.FileSystemLoader('pdf_generation/')
        template_env = jinja2.Environment(loader=template_loader)

        template = template_env.get_template('invoice.html')

        output_text = template.render(context)

        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        pdfkit.from_string(output_text, 'invoice_generated.pdf', configuration=config, css='pdf_generation/invoice.css')

        return "Invoice generated successfully", 200

        return "Invoice generated successfully", 200

    return render_template('index.html')

@app.route('/invoice', methods=['GET'])
def get_invoice():
    try:
        return send_file('invoice_generated.pdf', attachment_filename='invoice.pdf')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
