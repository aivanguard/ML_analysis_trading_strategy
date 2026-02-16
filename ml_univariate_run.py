import streamlit as st
import sys

st.write("Input Financial indicator information")

if len(sys.argv) > 1:
    etf_name = sys.argv[1]
    num_periods = sys.argv[2]
    period = sys.argv[3]
    st.write(f"Running TA analysis for this stock, {etf_name}!")
else:
    st.write("Not enough ticker info was  provided. Input all 3 selections")

import streamlit as st
import streamlit.components.v1 as stc
# Import all the TA indicator apps for the menu


# Load Financial Data & Visualization Pkgs
from twelvedata import TDClient
#Get 12Data API
with open('api_key.txt', 'r') as file:
  api_key = file.read().strip()

#Use the API key for the session
from twelvedata import TDClient
td = TDClient(apikey=api_key)

from autots_app import trend_data
from autogluon_app import trend_data
from stats_exposmooth_app import trend_data

#Add HTML components
html_temp = """

		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Twelve Data ETF Trends App </h1>
		<h4 style="color:white;text-align:center;">Technical indicators </h4>
		</div>
		"""

def ta_type(ETF,num_periods,period,td):
  #Select the sidebar menu options

	stc.html(html_temp)
	menu = ["Home","Autots_ML","Autogluon_ML","EXPO_smooth_ML"]
	choice = st.sidebar.selectbox("Menu",menu)


	if choice == "Home":

		st.subheader("Home")
		st.write("""
			### Trading with Forecast Price App
			This dataset contains the price future forecast  for a stock ticker such as Goog.
			#### Datasource
				- https://twelvedata.com/docs
			#### App Content
				- Data Analysis of Trades
				- Technical Indicators
				- Price Trend
			""")






	elif choice == "Autots_ML":
		trend_data(ETF,num_periods,period,td)
	elif choice == "EXPO_smooth_ML":
		trend_data(ETF,num_periods,period,td)
	else:
		trend_data(ETF,num_periods,period,td)

  #else:
  #  st.subheader("About")
  #  st.text("Use Technical Trading or AI/ML")

ta_ETF = etf_name
#num_periods = 100
#period = '1h'

if __name__ == '__main__':
	ta_type(ta_ETF,num_periods,period,td)