"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Flask, Blueprint
from flask_cors import CORS, cross_origin

import quandl

api = Blueprint("fetchData", __name__)


@api.route('/')
def fetchData():
    quandl.ApiConfig.api_key = 'xQsG9W4sz9HzLpryaY5E'
    df = quandl.get('EOD/HD', start_date='2015-12-28', end_date='2017-12-28')
    df = df.reset_index()
    # df = df[['Open', 'High', 'Low', 'Close']]

    # return df.to_json(orient='table', index=False)
    return df.to_json(orient='table')


if __name__ == '__main__':
    api.run(debug=True)
