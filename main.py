from alice_blue import *
user="****"
pwd="****"
yob="****"
secKey="****"
appCode='****'
access_token = AliceBlue.login_and_get_access_token(username=user, password=pwd, twoFA=yob, api_secret=secKey, app_id=appCode)
alice = AliceBlue(username=user, password=pwd, access_token=access_token)
print(
   alice.place_order(transaction_type = TransactionType.Buy,
                     instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Market,
                     product_type = ProductType.Delivery,
                     price = 0.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
   )