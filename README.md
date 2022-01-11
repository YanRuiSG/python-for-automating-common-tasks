# A repository for python scripts to automate common tasks

### Python script for renaming a large number of files

**Brief outline of steps**

1. Explore the files in the directory
    - create list of file types
    - find the total number of image files for renaming

2. Create a new folder in the directory for storing the renamed image files later

3. Import the data for renaming the file names from the excel/csv file as a dataframe
    - perform any necessary cleaning and tidying of the dataset
    - use a left merge to find the current file names and the corresponding new file names

4. Copy the image files for renaming to the new folder

5. Use a context manager for changing directory and rename the image files in the new folder

