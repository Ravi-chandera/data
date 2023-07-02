import streamlit as st
import requests
import pandas as pd
import json

def main():
    st.title("Weather Data Visualization")
    
    # Get the city name from the user
    city_name = st.text_input("Enter a city name")
    
    if st.button("Get City Data"):
        # Get the data for the city
        city_data = get_city_data(city_name)
        
        # Display the data
        display_city_data(city_data)

def get_city_data(city):
    # Make an API request to get the JSON data for the city
    url = "http://api.weatherapi.com/v1/current.json?key=73232371a8ea48c4b2a100143230207&q={}&aqi=yes".format(city)
    response = requests.get(url)
    data = response.json()

    # Create DataFrame from the extracted values
    # df = pd.DataFrame(data)

    # Remove NaN values and combine into a single row
    # df = df.fillna('').transpose().reset_index(drop=True)
    # print(data)
    # data = pd.DataFrame(df)
    df_location = pd.DataFrame(data["location"], index=[0])
    df_current = pd.DataFrame(data["current"], index=[0])
    df_air_quality = pd.DataFrame(data["current"]["air_quality"], index=[0])

    df = pd.concat([df_location, df_current,df_air_quality], axis=1)
    df = df.drop("localtime_epoch",axis=1)
    df = df.drop("last_updated_epoch",axis=1)
    df = df.drop("condition",axis=1)
    df = df.drop("air_quality",axis=1)


    return df

def display_city_data(data):
    # Display the JSON object in a visually appealing manner
    st.subheader("City Data")
    st.write(data)

if __name__ == "__main__":
    main()
