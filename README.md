# Data-cleaning
For this project was based on cleaning Data. Where you replace, modify, or delete unwanted data to transform it into "clean" desired data.

the problem was too.
Write a program that:
removes all the duplicates from the data_combined.csv file. 
combine the first_name and last_name column into just one column called full_name
replace all 10s in the ratings column with 0s. 
create a column named vowel. If the person's full_name begins with a vowel, set the column to True; if it does not, set it to false.

Output this file to a .csv file called clean_data.csv


This code reads data from a JSON file, processes it, and extracts specific city information based on the 'id' field of people. It then creates a DataFrame with the extracted city information and converts it to a JSON array. The JSON data is saved to a new file named 'cities.json'.

import pandas as pd and import json: These lines import the pandas library with the alias pd and the json library, which are required for data manipulation and JSON operations.
with open('people_info.json') as file:: This block of code opens the file named 'people_info.json' using the open() function in a with statement. The with statement ensures that the file is properly closed after its suite finishes.

cities = []: An empty list called cities is initialized to store the city information of people with IDs between 5 and 10.
cities.append(person['city']): If the person's 'id' satisfies the condition, the code extracts the 'city' information from the person's dictionary and appends it to the cities list.
json.dump(cities_json, file): The json.dump() function writes the JSON string cities_json to the file 'cities.json'. The JSON data is saved in the specified file, ready for further use or storage.
