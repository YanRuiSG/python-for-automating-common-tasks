'''
Exploring the files current drive
The OS module in Python provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules.

This module provides a portable way of using operating system dependent functionality. The os and os.path modules 
include many functions to interact with the file system.

'''



import os
import pandas as pd

#get the current working drive
wd1 = os.getcwd()

# save the file names in the current drive to a list
file_names = os.listdir(wd1)
#display(file_names)

# create a list of the file names for the excel files in the current drive
excel_files = [file for file in file_names if file.endswith('.xlsx')]

display(excel_files)

#count the total number of 'jpg' image files
image_count = sum(1 for file in file_names if file.endswith('.jpg'))
display(image_count)






'''
Create a new folder in the current drive for storing the image files with the converted file names
'''
# create the name for the new folder
folder_name = 'converted file names'

# error handling
if folder_name in os.listdir(os.getcwd()):
    print('Folder name already exist in current drive')
else:
    # further error handling
    try:
        #create the path for the new folder
        path = os.path.join(wd1, folder_name)
        # create the new folder
        os.mkdir(path)

    except:
        print('Folder name could not be created, please check again.')











'''
Import the excel file data for the countries/capital
Clean and tidy the dataset by removing leading and trailing white spaces
'''

#import the excel file data for the countries/capitals as a dataframe
country_capital_data = pd.read_excel(excel_files[0])

# explore the first 5 rows of the dataframe
display(country_capital_data.head())


# remove any leading and trailing white spaces
country_capital_data['Country'] = country_capital_data['Country'].str.strip()
country_capital_data['Capital'] = country_capital_data['Capital'].str.strip()

display(country_capital_data.head())



import re

# remove the '.jpg' file extension from the file name when creating the list of unconverted image file names 
unconverted_names = [re.sub('.jpg','',file) for file in file_names if file.endswith('.jpg')]

df_unconverted = pd.DataFrame({'File name (country)':unconverted_names})

# explore the first 5 rows of the dataframe
display(df_unconverted.head())











'''
Use a left merge to find the corresponding capital names for the unconverted image file names
Create a list of values for the corresponding capital names
'''
# use a left join
final_df = df_unconverted.merge(country_capital_data, left_on='File name (country)', right_on='Country', how='left')

display(final_df.head())

# creating the list of corresponding capital names
capital_file_names = list(final_df['Capital'].values)

# display the first 9 elements of the list
display(capital_file_names[:8])








'''
Copying the image files over to 'converted file names' Folder
The shutil module provides functions for copying files, as well as entire folders.

For copying multiple files at once, you'll have to have a list of all files you want to copy and loop over them to copy them.
'''

# The shutil module provides functions for copying files, as well as entire folders.
import shutil

image_files_unconverted = [file for file in os.listdir(os.getcwd()) if file.endswith('.jpg')]

for image in image_files_unconverted:
    shutil.copy(image, 'converted file names')







'''
Convert the names of the image files from country to capital
Define and use a context manager to temporary change folder to the 'converted file names' folder and 
carry out the name changing for the image files there.
'''

import contextlib

# defining the context manager to be used
@contextlib.contextmanager
def in_dir(directory):
    """Change current working directory to `directory`,
    allow the user to run some code, and change back.
    
    Args: directory (str): The path to a directory to work in.
    """
    current_dir = os.getcwd()
    
    os.chdir(directory)

    # Add code that lets you handle errors
    try :
      yield
    
    
    
    # Ensure the directory is reset,
    # whether there was an error or not
    # finally ensures that the code gets executed no matter what
    finally :
      os.chdir(current_dir)
    
    
# use the context manager to change directory temporarily and change the unconverted image file names before returning
# use the context manager to change to the drive containing the raw data and import the data

filenames_to_change = [file for file in file_names if file.endswith('.jpg')]

with in_dir(path):
    
    for i in range(len(filenames_to_change)):
        os.rename(filenames_to_change[i], capital_file_names[i] + '.JPG')

    




