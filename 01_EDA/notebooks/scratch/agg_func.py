import numpy as np
import pandas as pd

def sum_inc(l):
    return sum( [ int(y>x) for x,y in zip(l , l[1:] ) ] )

def sum_dec(l):
    return sum( [ int(y<x) for x,y in zip(l , l[1:] ) ] )

def media_inc(l):
    return np.mean( [ int(y>x) for x,y in zip(l , l[1:] ) ] )

def media_dec(l):
    return np.mean( [ int(y<x) for x,y in zip(l , l[1:] ) ] )

def delta_min(l):
    try:
        return min( [ float( y-x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def delta_max(l):
    try:
        return  max( [ float( y-x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def delta_mean(l):
    try:
        return  np.mean( [ float( y-x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def delta_desv(l):
    try:
        return  np.std( [ float( y-x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan
    
def pct_delta_min(l):
    try:
        return  min( [ float( (y-x)/x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def pct_delta_max(l):
    try:
        return  max( [ float( (y-x)/x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def pct_delta_mean(l):
    try:
        return  np.mean( [ float( (y-x)/x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def pct_delta_desv(l):
    try:
        return  np.std( [ float( (y-x)/x ) for x,y in zip(l , l[1:] ) ]  )
    except:
        return np.nan

def max_racha_inc(l):
    return max( [ len(i) for i in "".join([ str( int(y>x)  ) for x,y in zip(l,l[1:])  ]).split('0')  ]   )

def max_racha_dec(l):
    return max( [ len(i) for i in "".join([ str( int(y<x)  ) for x,y in zip(l,l[1:])  ]).split('0')  ]   )

def media_racha_inc(l):
    return np.mean( [ len(i) for i in "".join([ str( int(y>x)  ) for x,y in zip(l,l[1:])  ]).split('0')  ]   )

def media_racha_dec(l):
    return np.mean( [ len(i) for i in "".join([ str( int(y<x)  ) for x,y in zip(l,l[1:])  ]).split('0')  ]   )  