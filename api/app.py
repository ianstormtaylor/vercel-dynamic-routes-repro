from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/python/tickers/<ticker>')
def index(ticker):
    return 'Python success: ' + ticker

if __name__ == '__main__':
    app.run()