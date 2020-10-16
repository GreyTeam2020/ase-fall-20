from flakon import JsonBlueprint
from flask import request, jsonify
from myservice.calculator import calculator as c


calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.sum(m, n)

    return jsonify({'result': str(result)})


@calc.route('/calc/div', methods=['GET'])
def div():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    try:
        return jsonify({'result': str(c.divide(m, n))})
    except ZeroDivisionError:
        return jsonify({'result': 'DivisionByZeroError'})


@calc.route('/calc/mol', methods=['GET'])
def mol():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    return jsonify({'result': str(c.multiply(m, n))})


@calc.route('/calc/sub', methods=['GET'])
def sub():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    return jsonify({'result': str(c.subtract(m, n))})

