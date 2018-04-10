from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from right next to __init__.py"
 
if __name__ == "__main__":
    app.run(debug = True)