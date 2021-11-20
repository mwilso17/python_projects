# Mike Wilson 20 November 2021. 
# A simple website using the Flask framework and Python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "website content here"

if __name__ == "__main__":
  app.run(debug=True)