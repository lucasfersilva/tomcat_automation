from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        client_name = request.form.get('client_name')
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
