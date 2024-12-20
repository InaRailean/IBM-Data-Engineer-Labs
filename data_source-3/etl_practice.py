import pandas as pd
import glob 
import xml.etree.ElementTree as ET
from datetime import datetime

log_file1 = "log_file.txt"
target_file1 = "transformed_data1.csv"

# Extraction
def extract_from_csv(file_to_process):
    dataframe1 = pd.read_csv(file_to_process)
    return dataframe1

def extract_from_json(file_to_process):
    dataframe1 = pd.read_json(file_to_process, lines = True)
    return dataframe1

def extract_from_xml(file_to_process):
    # create an empty data frame to hold extracted data 
    dataframe1 = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find('car_model').text 
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe1 = pd.concat([dataframe1, pd.DataFrame([{'car_model': car_model, 'year_of_manufacture': year_of_manufacture, 'price': price, 'fuel': fuel}])])
    return dataframe1

#  Extract all the files
def extract(): 
    extracted_data1 = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data1 = pd.concat([extracted_data1, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data1 = pd.concat([extracted_data1, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data1 = pd.concat([extracted_data1, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data1 

# Transformation 
def transform(data):
    # transform price values to max 2 decimal places
    data["price"] = round(data["price"], 2)
    return data

# Loading
def load_data(target_file1, transformed_data1):
    transformed_data1.to_csv(target_file1)

# Logging
def log_progress(message):
    # Year-Monthname-Day-Hour-Minute-Second 
    timestamp_format = "%Y-%h-%d-%H:%M:%S"  
    # Get current timestamp
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file1, "a") as f:
        f.write(timestamp + "," + message + "\n")

# Log the initialization of the process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data1 = extract()

# Log the complition of the extraction process
log_progress("Extract phase Ended")

# Log the beginning of the transformation process
log_progress("Transformation phase Started")
transformed_data1 = transform(extracted_data1)
print("Data transformed")
print(transformed_data1)

# Log the end of the transformation Process
log_progress("Transformation phase Ended")

# Log the beginning of the loading process
log_progress("Loading phase Started")
load_data(target_file1, transformed_data1)

# Log the end of the loading process
log_progress("Loading phase Ended")

# Lof the completion of the ETL process
log_progress("ETL process Ended")
