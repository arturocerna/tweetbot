import twitter_bot as tb

api = tb.setUpAPI()
quote = tb.retrieveQuote()
api.update_status(quote)
