from Flask import Flask

app = Flask(__name__)
app.run(debug=True, port=8000)