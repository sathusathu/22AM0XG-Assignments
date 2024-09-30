from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world! " + "sathappan" + "7376222AL197" + "Dept of AIML"

if __name__ == '__main__':
    app.run(debug=True)
