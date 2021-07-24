import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from pyowm.utils import timestamps
import base64



st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )



st.title("Weather tool")
st.write("### Enter the city name and select the temperature unit and graph type from the sidebar")


st.markdown("![Alt Text](https://media.giphy.com/media/xThta7J2onElox6EWQ/giphy.gif)")

city_name=st.sidebar.text_input("Enter city name :", "Delhi")

add_selectbox = st.sidebar.selectbox(
    'Temperature in :',
    ('Celsius', 'Fahrenheit')
)

from pyowm.owm import OWM
owm = OWM('f2d524a814548379c2c9edb6ff510ecc')  # My api ID
mgr = owm.weather_manager()


observation = mgr.weather_at_place(city_name)  # the observation object is a box containing a weather object



weather = observation.weather
st.write("**_Current weather status_** : "+str(weather.detailed_status))      


weather = mgr.weather_at_place(city_name).weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)

if add_selectbox=='Celsius':
    temp_dict_celsius = weather.temperature('celsius')
    st.write("### In celsius")
    #Current temp
    st.write("**_Current temperature_** :" + str(temp_dict_celsius['temp']))
    #Mininmum temp
    st.write("_Minimum temperature_ :" + str(temp_dict_celsius['temp_min']) )
    #Maximum temperature
    st.write("_Maximum temperature_ :" + str(temp_dict_celsius['temp_max']))
else:
    st.write("### In Fahrenheit")
    temp_dict_fahrenheit = weather.temperature('fahrenheit')
    #Current temp
    st.write("**_Current temperature_** :" + str(temp_dict_fahrenheit['temp']))
    #Mininmum temp
    st.write("_Minimum temperature_ :" + str(temp_dict_fahrenheit['temp_min']))
    #Maximum temperature
    st.write("Maximum temperature :" + str(temp_dict_fahrenheit['temp_max']))

wind_dict_in_meters_per_sec = observation.weather.wind()   # Default unit: 'meters_sec'
st.write("**_Wind speed_** : "+ str(wind_dict_in_meters_per_sec['speed'])+" m/s")
st.write("Wind angle : "+ str(wind_dict_in_meters_per_sec['deg'])+ " degrees")

st.write(
    
)

mgr = owm.weather_manager()
st.write("## _Forecasts_")

forecaster = mgr.forecast_at_place(city_name, '3h')    # this gives you a Forecaster object
st.write("Forecasting from : " + str( forecaster.when_starts('iso')))                
st.write("Forecasting till : " + str( forecaster.when_ends('iso')))  




st.write("## Rain :")
if forecaster.will_have_rain()==True:
    st.markdown("![Alt Text](https://media.giphy.com/media/l0HlPwMAzh13pcZ20/giphy.gif)")
    st.write("#### Carry your umbrella , its gonna rain")
else:
    st.write("Travel worry free")

st.write("## Storm :")
if forecaster.will_have_storm()==True:
    st.markdown("![Alt Text](https://media.giphy.com/media/3orieZMmRdBlKk5nY4/giphy.gif)")
    st.write("### Stay inside ! \n STORM warning")
else:
    st.write("Travel worry free , no storm forecasted")

st.write("## Cloudy :")
if forecaster.will_have_clouds()==True:
    st.markdown("![Alt Text](https://media.giphy.com/media/dWIau1ZRyIj3j6YEaL/giphy.gif)")
    st.write("Cloudy enough, visiblity affected!")
else:
    st.write("Not cloudy , full visibility")








