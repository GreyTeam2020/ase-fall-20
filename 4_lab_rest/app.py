"""
4th ASE2020 lab

@author Vincenzo Palazzo v.palazzo1@studenti.unipi.it
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST', 'DELETE', 'GET'])
def my_services():
    return jsonify({"response": "Hello ASE 2020 :-)"})


@app.route('/api/person/<int:person_id>')
def get_person(person_id):
    return jsonify({'person': person_id})


if __name__ == '__main__':
    print(app.url_map)
    app.run()
