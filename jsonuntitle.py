import pandas as pd
import json
#The pandas library is imported and assigned the alias pd.
#The json library is imported.

# Read the data from the JSON file
with open('people_info.json') as file:
    data = json.load(file)
#Open the file named 'people_info.json' using the open() function, and assign it to the variable file.

#Use the json.load() function to load the contents of the file into the data variable.

# Extract the city information of people with IDs 5-10
cities = []
for person in data:
    if 5 <= person['id'] <= 10:
        cities.append(person['city'])

#Extract the city info for specific IDS, Initialize an empty list called cities. And literate over each person in the data list 

#Make sure the person Ids is between 5 and 10; if condition is met, extract the persons city info and append it to cities list 


# Create a dataframe with the cities column
df = pd.DataFrame({'City': cities})

# Use the pd.DataFrame() function to create a DataFrame called df with a single column named 'City'.
print(df['City'])

#Use print(df['City']) to display the contents of the 'City' column in the DataFrame df.

# Convert the column to JSON
cities_json = df.to_json(orient='records')

#Use the to_json() method on the DataFrame df to convert the 'City' column to JSON format.
#Set the orient parameter to 'records' to create a JSON array of records.Set the orient parameter to 'records' to create a JSON array of records.

# Save the JSON file
with open('cities.json', 'w') as file:
    json.dump(cities_json, file)

#Open the file named 'cities.json' in write mode ('w') using the open() function and assign it to the variable file.
#Use the json.dump() function to write the JSON string cities_json to the file.

