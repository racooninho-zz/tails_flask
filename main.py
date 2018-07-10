
###################################
#Json to post
#{ "order": { "id": 12345, "customer": { }, "items": [ { "product_id": 1, "quantity": 1 }, { "product_id": 2,
#  "quantity": 5 }, { "product_id": 3, "quantity": 1 } ] } }

#URL = http://127.0.0.1:5000/order?currency=USD
###################################

from flask import Flask, request, json, render_template, jsonify
import web
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('template.html')


@app.route("/order", methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        currency = request.args.get('currency', default='GBP')

        result = web.Order.post(request.data, currency)
        return jsonify(result)
    else:
        return render_template('template.html')

if __name__ == "__main__":
    app.run()