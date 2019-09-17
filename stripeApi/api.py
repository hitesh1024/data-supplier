from flask import Flask, request, redirect, render_template, url_for, Blueprint

import pandas as pd
import logging
from kiteconnect import KiteConnect
import stripe

# from database import function as f
from .models import function as f

server = Blueprint('stripeApi', __name__)

tickers = pd.read_csv('list.csv')
trading_symbol = tickers.tradingsymbol
kite = KiteConnect(api_key="duny7h29mk27ippz")
logging.basicConfig(level=logging.DEBUG)

stripe_keys = {
    'secret_key': 'sk_test_MRtCOjSvWl7nBhbyv3EKHLXb00tujkTaau',
    'publishable_key': 'pk_test_gKsV5GwiR9khB25jhrYVjV2d00ze2Zychb'
}

stripe.api_key = stripe_keys['secret_key']


@server.route('/kite/', methods=['GET', 'POST'])
def index():
    try:
        data = kite.generate_session(request.args.get('request_token'), api_secret="58bgtms9o49k9fa4dbpsx1box7frarxz")
        kite.set_access_token(data["access_token"])
        kite.orders()

        return redirect(url_for('payment'))


    except:
        print('')

    return redirect(kite.login_url())
