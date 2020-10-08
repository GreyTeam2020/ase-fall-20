"""
4th ASE2020 lab

@author Vincenzo Palazzo v.palazzo1@studenti.unipi.it
"""
from flask import Flask
from teams import teams

app = Flask(__name__)
app.register_blueprint(teams)

if __name__ == '__main__':
    app.run(debug=True)
