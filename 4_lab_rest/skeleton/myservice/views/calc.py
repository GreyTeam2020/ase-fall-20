from flask import Blueprint, jsonify, request
from myservice import calculator as util

calc = Blueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = util.sum(m, n)

    return jsonify({'result': result})


@calc.route('/calc/div', methods=['GET'])
def div():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    
    result = util.divide(m, n)
    return jsonify({'result': result})


@calc.route('/calc/mol', methods=['GET'])
def mol():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m * n
    return jsonify({'result': result})


@calc.route('/calc/sub', methods=['GET'])
def sub():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m - n
    return jsonify({'result': result})
