def d(): 
    from pandas import read_csv
    dataset=read_csv('iris.csv')
    """
    iloc is to referencing rows and columns of matrix of datasets
    .iloc[:,:] for all rows and columns
    """
    X=dataset.iloc[:,:].values
    print(X)
    """
    .iloc[i,:] for ith row and  all columns

    """
    X=dataset.iloc[1,:].values
    print(X)
    """
    .iloc[:,i] for all rows and ith column

    """
    X=dataset.iloc[:,1].values
    print(X)
    print(dataset.head(3))#print only initial three rows 
    X=dataset.iloc[1:,:].values #will not contain first row where head[0]
    print(X)
d();    
