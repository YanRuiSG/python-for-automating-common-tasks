# A repository for python scripts to automate common tasks

### Python script for renaming a large number of files (renaming_files.py)

The general idea is to create a folder in the current directory where the image files to be renamed will
be copied over to the folder and be renamed based on a dataframe of the corresponding old and new file names.

A context manager will be defined and used for temporary access to the new folder and rename the image files copied there.


### Python script for converting values to a homogeneous set (standardizing_values_using_regex.py)

Regular expression from the re library will be used for testing matches before converting each different expression
of values to a homogeneous set of values
