import pytest

from src.controller import app
from test.mock_object import quote1, quote2, quote3


@pytest.fixture
def tester():
    app.config['TESTING'] = True
    tester = app.test_client()
    return tester


def test_create_quote1(tester):
    # create test for flask
    # # send data as POST form to endpoint
    response = tester.post('/api/quote', json=quote1)

    # # check if response data is correct
    assert response.json == {'Quote Premium': '$4450'}


def test_create_quote2(tester):
    # create test for flask
    # # send data as POST form to endpoint
    response = tester.post('/api/quote', json=quote2)

    # # check if response data is correct
    assert response.json == {'Quote Premium': '$4000'}


def test_create_quote3(tester):
    # create test for flask
    # # send data as POST form to endpoint
    response = tester.post('/api/quote', json=quote3)

    # # check if response data is correct
    assert response.json == {'Quote Premium': '$11160'}


def test_create_with_report(tester):
    response = tester.post('/api/OrderReports', json={'person': {'name': 'Bob'}})
    quote3.update(response.json)
    response = tester.post('/api/quote', json=quote3)
    assert response.json == {'Quote Premium': '$13960'}


