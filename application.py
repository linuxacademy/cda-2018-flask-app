from flask import Flask, render_template

application =  Flask(__name__)

@application.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    application.run(debug = True)