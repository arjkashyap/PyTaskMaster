import tweepy
import yfinance as yf
import creds
import pandas as pd
import matplotlib.pyplot as plt


# Authenticate to Twitter
auth = tweepy.OAuthHandler(creds.auth_key, creds.auth_secret)
auth.set_access_token(creds.auth_token, creds.auth_token_secret)

# Create API object
api = tweepy.API(auth)

test_tweet_num = 1

price_graph_path = "./BitCointon/assets/PriceGraph.png"
priceUpImg = "./BitCointon/assets/Happy.png"
priceDownImg = "./BitCointon/assets/Angry.png"


def btc_has_dipped():
    """
    Function analysis the Bitcoin data
    :return: true if the coin value has dropped
            false if the coin value has risen
    """
    btc_data = yf.download(tickers='BTC-USD', period="3d", interval='1d')    # coin value for last 3 days at 0000
    current = btc_data['Adj Close'][-1]
    last = btc_data['Adj Close'][-2]
    print("Current price: " + str(current))
    print("Last price: " + str(last))
    return current < last


def plot_data():
    """
    Function takes the bitcoin price data from last 20 Days
    plots a graph: Date, Price relation
    And saves the plot as image in assets (overrides existing)
    """
    data = yf.download(tickers='BTC-USD', period="10d", interval='1d')    # coin value for last 3 days at 0000
    # df = pd.DataFrame({'lab': data['Adj Close'], 'val': data['Adj Close']})
    # ax = df.plot.bar(x='lab', y='val', rot=0)
    x = ["".join(str(date_time).split()[0]) for date_time in data['Adj Close'].index]    # x axis for graph
    y = [float(price) for price in data['Adj Close']]
    relation = pd.DataFrame({'date': x, 'BTC_price': y})
    relation.plot('date', 'BTC_price',  marker='o', color='b')
    plt.xticks(rotation=0)
    # plt.show()
    plt.savefig(price_graph_path)


def main():
    try:
        msg = "#bitcoin #BTC #cryptocurrency #crypto #Bitcoin2021 #bitcoinmining #bitcoinnews"
        plot_data()
        media_ids = []
        if btc_has_dipped():
            # Bitcoin has dropped
            images = (price_graph_path, priceDownImg)
            media_ids = [api.media_upload(i).media_id_string for i in images]
        else:
            images = (price_graph_path, priceUpImg)
            media_ids = [api.media_upload(i).media_id_string for i in images]

        api.update_status(status=msg, media_ids=media_ids)
        print("Tweet success")
    except Exception as e:
        print("An error occurred: ")
        print(e)


if __name__ == '__main__':
    main()

