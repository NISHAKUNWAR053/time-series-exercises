import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import os
import datetime
import requests



def get_planets_data():
    # Initialize the URL for the first page
    data = []
    url = 'https://swapi.dev/api/planets/'  
    
    while True:
        # Send a GET request to the SWAPI
        response = requests.get(url)  
        if response.status_code == 200:
            json_data = response.json()
            results = json_data['results']
            data.extend(results)
            url = json_data['next']  

            if url is None:
                break
        else:
            print(f"Error: {response.status_code}")
            break
    # Create a DataFrame using the collected data
    df = pd.DataFrame(data)  
    return df


def get_starships_data():
    # Initialize the URL for the first page
    data = []
    url = 'https://swapi.dev/api/starships/'
    
    while True:
        # Send a GET request to the SWAPI
        response = requests.get(url)  
        if response.status_code == 200:
            json_data = response.json()
            results = json_data['results']
            data.extend(results)
            url = json_data['next']  

            if url is None:
                break
        else:
            print(f"Error: {response.status_code}")
            break
    # Create a DataFrame using the collected data
    df = pd.DataFrame(data)  
    return df


def get_starwars_data(starwars_df):
    '''This function creates a csv for concat wine csv'''
    # Assuming you have a function 'get_starwars_data()' that retrieves the starwars data and returns a DataFrame
    df_starwars = starwars_df

    # Save the DataFrame to a CSV file
    df_starwars.to_csv("starwars.csv", index=False)  # Specify 'index=False' to exclude the index column in the CSV

    filename = 'wine.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)

def get_power_data():
    '''
    This function acquires the Open Power Systems Data for Germany csv
    '''
    filename = 'opsd_germany_daily.csv'

    # Verify if file exists
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    # Download data if file doesn't exist
    else:
        url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
        try:
            df = pd.read_csv(url)
            df.to_csv(filename, index=False)
            print("Data acquired and saved successfully.")
            return df
        except Exception as e:
            print("Error while downloading the data:", e)
            return None
get_power_data()


