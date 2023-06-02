import datetime
from flask import jsonify


def calculate_quote(person, vehicle, coverage, report):
    current_date = datetime.datetime.now()

    try:
        # get vehicle age
        vehicle_year = vehicle['year']
        person_age = person['age']
        year = int(vehicle_year.split('-')[0])
        month = int(vehicle_year.split('-')[1])

        vehicle_age = current_date.year - year
        if current_date.month < month:
            vehicle_age -= 1

        premium = 1000

        # calculate premium
        if vehicle_age > 5:
            premium += (vehicle_age - 5) * 100
        if person_age < 25:
            premium += (25 - person_age) * 50

        mismatch = {}
        mismatched = False
        for coverages in coverage:
            match coverages:
                case 'Property Damage':
                    premium += (coverage['Property Damage'] // 10000) * 50
                case 'Bodily Injury - Per Person':
                    premium += (coverage['Bodily Injury - Per Person'] // 25000) * 100
                # add cases for each coverage type
                case 'Bodily Injury - Per Accident':
                    premium += (coverage['Bodily Injury - Per Accident'] // 25000) * 100
                case 'Uninsured Motorist - Per Person':
                    premium += (coverage['Uninsured Motorist - Per Person'] // 10000) * 20
                case 'Uninsured Motorist - Per Accident':
                    premium += (coverage['Uninsured Motorist - Per Accident'] // 10000) * 20
                case 'Underinsured Motorist - Per Person':
                    premium += (coverage['Underinsured Motorist - Per Person'] // 10000) * 20
                case 'Underinsured Motorist - Per Accident':
                    premium += (coverage['Underinsured Motorist - Per Accident'] // 10000) * 20
                case 'Collision':
                    premium -= (coverage['Collision'] // 1000) * 30
                case 'Comprehensive':
                    premium -= (coverage['Comprehensive'] // 1000) * 10
                case _:
                    mismatched = True
                    mismatch.update({coverages: coverage[coverages]})
        if report is not None:
            for coverages in report:
                match coverages:
                    case 'violations':
                        premium += (report['violations'] * 100)
                    case 'accidents':
                        premium += (report['accidents'] * 500)
                    case _:
                        mismatched = True
                        mismatch.update({coverages: report[coverages]})
        if mismatched:
            return jsonify({'Quote Premium': premium}, {"Mismatching coverage values": mismatch}), 200
        else:
            return jsonify({'Quote Premium': '$'+str(premium)}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': 'Invalid request'}), 400
