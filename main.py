import plotly.graph_objects as go
import yfinance as yf



def main():
    tsla = yf.Ticker('TSLA')
    # info = tsla.info
    tsla_data = tsla.history(period='1y')
    print(tsla_data.head())
    fig = go.Figure(data=go.Scatter(x=tsla_data.index, y=tsla_data["Close"]))
    fig.show()



if __name__ == "__main__":
    main()
