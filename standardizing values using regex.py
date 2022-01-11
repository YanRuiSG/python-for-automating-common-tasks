import re
import pandas as pd


# @memoize
def nationalities(nationality_input):
    '''
    Convert the input nationality to a standard nationality value based on a set of standard nationality values. 
    Return the converted standard nationality value.
    
    Args:
        nationality_input (str) : The nationality value to be converted to a standard value
    
    Returns:
        str
    
    Raises:
        ValueError: if the input nationality is not of string type
    
    
    '''
    
    if isinstance(nationality_input,str) != True:
        raise ValueError('The input value is not of string type')
    
    nationality = str(nationality_input)
    
    if re.search('[d,D][e,E][s,S][h,H]|[b,B][a,A][n,N][g,G]', nationality):

        return "Bangladesh"

    elif re.search('[i,I][n,N][d,D]', nationality):

        return "India"

    elif re.search('[c,C][h,H]|[p,P][r,R][c,C]', nationality):

        return "China"

    elif re.search('[m,M][y,Y]|[b,B][u,U]', nationality):

        return "Myanmar"

    elif re.search('[t,T][h,H][a,A][i,I]', nationality):

        return "Thailand"

    elif re.search('[m,M][a,A][l,L][a,A][y,Y]', nationality):

        return "Malaysia"

    elif re.search('[v,V][i,I][e,E][t,T]', nationality):

        return "Vietnam"

    elif re.search('[s,S][i,I][n,N]', nationality):

        return "Singaporean PR"

    elif re.search('[s,S][r,R][i,I]', nationality):

        return "Sri Lankan"

    elif re.search('[f,F][i,I]', nationality):

        return "Filipino"     

    else:

        return nationality
    
    
# apply the function to standardize the nationality values in the dataframe
main_df['Nationality'] = main_df['Nationality'].apply(nationalities)





# @memoize
def remove_ws_upper(string_value):
    """
    Take in a string value and remove the white spaces in the string value.
    Change the characters in the string value to upper case and return the string value
    
    Args:
        string_value (str): The string value for removing white spaces and converting the characters to upper case
        
    Returns:
        str
    
    Raises:
        ValueError: if the input argument is not of string type
    
    """
    
    try:
        # remove the white spaces if there are any white spaces in the input string value
        remove_ws = lambda string_value : re.sub('\s+','',str(string_value)) if re.search('\s+',str(string_value)) else string_value.upper()
     
        # return the FIN number in upper case
        return remove_ws(string_value)
    
    except:
        print('The input value is not of string type or re is not defined.')
    
    
    
# apply the function to the values in the FIN number column in the dataframe

main_df['FIN'] = main_df['FIN'].apply(remove_ws_upper)
