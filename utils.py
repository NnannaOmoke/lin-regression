"""
    This function serves to calculate the percentage of all the features missing in a datafame
    It returns a Pandas DataFrame
"""
def percent_missing(matrix_data):
    val = matrix_data.isnull().sum()/len(matrix_data) * 100
    val = val[val > 0].sort_values()
    return val
