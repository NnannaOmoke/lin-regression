def percent_missing(matrix_data):
    """
        This function serves to calculate the percentage of all the features missing in a datafame
        It returns a Pandas DataFrame
    """
    val = matrix_data.isnull().sum()/len(matrix_data) * 100
    val = val[val > 0].sort_values()
    return val
def reader(path = "C://Users//omoke//Downloads//UNZIP_FOR_NOTEBOOKS_FINAL//DATA//Ames_Housing_Feature_Description.txt"):
    """_summary_This simply reads in a file.
    """
    try:
        file = open(path, mode= "r")
        print(file.read())
        file.close()
    except:
        print("Revist path, or check permissions")