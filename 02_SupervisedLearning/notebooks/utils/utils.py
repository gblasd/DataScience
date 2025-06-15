import io
import requests
import pandas as pd

def read_url(link):
    """ Creates a Pandas Dataframe from online data
    - Parameters:
        - link = Link to the zipped data
    - Output:
        - Pandas Dataframe
    """
    # Define URL and extract information
    response = requests.get(link)
    content = response.content
    # Convert into a Pandas Dataframe
    data = pd.read_csv(io.BytesIO(content), sep=',', compression='gzip')
    return data


def host_in_location(str_location):
    """ Return 1 if the host_location in Mexico, else 0
    - Parameters:
        - str_location = data location
    - Output:
        - bin: int
    """
    str_loc = str(str_location).upper()
    str_mex = ['MEXICO', 'MÉXICO', 'CDMX', 'CIUDAD DE MEXICO', 
               'DISTRITO FEDERAL', 'MX', 'MEX.', 'MEX']
    for loc in str_mex:
        if loc in str_loc:
            return 1
    return 0


