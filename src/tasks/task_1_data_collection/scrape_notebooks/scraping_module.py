# Data Manipulation
import pandas as pd
 
 # mathematical computation
import numpy as np

# Visualization
import matplotlib.pyplot as plt 
import seaborn as sns

# Data collection
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

#creating and merging directories
import os

# function to get the soup
def get_soup(url):
    html_page = requests.get(url)
    print(html_page.status_code)
    soup = BeautifulSoup(html_page.content,'html.parser')
    return soup

# function to save data
def save_dataframe(df, folder_path, file_name):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the DataFrame as a CSV file in the folder
    file_path = os.path.join(folder_path, file_name)
    df.to_csv(file_path, index=False)
