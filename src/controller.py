import flask
from flask import request, jsonify

from src.quote_calculator import calculate_quote
from src.validation import validate

app = flask.Flask(__name__)


@app.route('/api/quote', methods=['POST'])
def create_quote():

    if validate(request.json) is False:
        return jsonify({'error': 'Invalid request'}), 400
    else:
        # fetch input json with person. vehicle, and coverage
        person = request.json.get('person') or request.json.get('driver')
        vehicle = request.json['vehicle']
        coverage = request.json['coverage']
        report = request.json.get('report')

        return calculate_quote(person, vehicle, coverage, report)


@app.route('/api/OrderReports', methods=['POST'])
def order_reports():
    person = request.json.get('person')['name'] or request.json.get('driver')['name']

    person_list = {'Bob': {'violations': 3,
                           'accidents': 5},
                   'Alice': {'violations': 0,
                             'accidents': 0},
                   'Eve': {'violations': 1,
                           'accidents': 1}}
    return jsonify({'report': {'violations': person_list[person]['violations'],
                   'accidents': person_list[person]['accidents']}}), 200


if __name__ == '__main__':
    app.run(debug=False)
