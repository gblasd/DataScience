import pandas as pd
import numpy as np

def haversine(lon1, lat1, lon2, lat2):
    
    # lon1 = np.radians(lon1.astype(float))
    # lat1 = np.radians(lat1.astype(float))
    # lon2 = np.radians(lon2.astype(float))
    # lat2 = np.radians(lat2.astype(float))

    lon1 = np.radians(lon1)
    lat1 = np.radians(lat1)
    lon2 = np.radians(lon2)
    lat2 = np.radians(lat2)
    
    r = 6371
    
    dlon = np.subtract(lon2, lon1)
    dlat = np.subtract(lat2, lat1)

    a = np.add(np.power(np.sin(np.divide(dlat, 2)), 2),
               np.multiply(np.cos(lat1),
                           np.multiply(np.cos(lat2),
                                       np.power(np.sin(np.divide(dlon, 2)), 2))
                           )
              )
    c = np.multiply(2, np.arcsin(np.sqrt(a)))

    return c*r

def calcular_proporcion_por_hora( df ):
    """
    Calcula la proporción entre la cantidad de la transacción y la hora del dia.

    Args:
        hr: hora del dia en formato de 24 hrs.
        amt: monto de la transacción correspondiente

    Returns:
        Numpy series, con el valor
    """

    # asignar la hora de la fecha
    df['order_hr'] = df.groupby(['cc_num', 'hour_int']).cumcount() + 1

    # Calcular la proporcion
    df['prop_order_hr'] = df.apply(
        lambda row: row['amt']/row['hour_int'] if row['hour_int'] != 0 else 0,
        axis=1
    )

    return df
    



# Franjas horarias
def franjas_hrs( hr ):
    if hr < 6:
        r = 'madrugada'
    elif hr < 12:
        r = 'mañana'
    elif hr < 18:
        r = 'tarde'
    elif hr < 24:
        r = 'noche'
    else:
        r = 'error'

    return r

def get_prop_order_hr( amt, hr:int ):
    return amt/hr if hr != 0 else 0