from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Abbas Currency Rate API</h1>  <p>Example URL:  /api/v1/usd-jpy<p>'

app.run(host='0.0.0.0')
