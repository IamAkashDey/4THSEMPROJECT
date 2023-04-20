import streamlit as st
from stocknews import StockNews

tickers = st.sidebar.text_input('Pick Your Stock')


st.title('Top 10 News of')


st.header(f'News of {tickers}')
sn=StockNews(tickers,save_news=False)
df_news=sn.read_rss()
for i in range(10):
	st.subheader(f'News {i+1}')
	st.write(df_news['published'][i])
	st.write(df_news['title'][i])
	st.write(df_news['summary'][i])
	title_sentiment=df_news['sentiment_title']
	st.write(f'Title Sentiment {title_sentiment}')
	news_sentiment = df_news['sentiment_summary'][i]
	st.write(f'News Sentiment {news_sentiment}')