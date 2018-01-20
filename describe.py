from pandas import read_csv
from matplotlib import pyplot 
   
def box():
    filename="iris.csv"
    """
    DataFrame([data, index, columns, dtype, copy])
    Two-dimensional size-mutable, potentially heterogeneous tabular data
    structure with labeled axes (rows and columns).
     here dataset is a dataframe
    """
    datasets=read_csv(filename,skiprows=[1])
    X=datasets.iloc[:,:].values
    datasets.plot(kind="box",color="RED")
    pyplot.show()
    print(datasets.describe())#central tendency of data as mean,count,min,max,std,
    datasets.plot()
    pyplot.show() 
    """
    Return Series with number of non-NA/null observations over requested axis.
    Works with non-floating point data as well (detects NaN and None)
    """
 
    print("count\n",datasets.count())   
    """
    dataFrame.max(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)[source]
    This method returns the maximum of the values in the object.
    If you want the index of the maximum, use idxmax. This is the equivalent of the numpy.ndarray method argmax.
    Parameters:	
    axis : {index (0), columns (1)}

    skipna : boolean, default True

    Exclude NA/null values when computing the result.

    level : int or level name, default None

    If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series

    numeric_only : boolean, default None

    Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series.

    Returns:	
    max : Series or DataFrame (if level specified)
    """
       
    print("max\n",datasets.max())
    # same as max but min return min value
    print(datasets.min())
    """
    DataFrame.select_dtypes(include=None, exclude=None)[source]
    Return a subset of a DataFrame including/excluding columns based on their dtype.

    Parameters:	
    include, exclude : scalar or list-like

    A selection of dtypes or strings to be included/excluded. At least one of these parameters must be supplied.

    Returns:	
    subset : DataFrame

    The subset of the frame including the dtypes in include and excluding the dtypes in exclude.

    Raises:	
    ValueError

    If both of include and exclude are empty
    If include and exclude have overlapping elements
    If any kind of string dtype is passed in.
    """
    #printing the standard deviation
    print("standard deviation\n",datasets.std())
    print(datasets.idxmin())
    X=datasets.select_dtypes(include='bool')
    print(X)    
    X=datasets.select_dtypes(include=['float64'])
    print(X)  
    X=datasets.select_dtypes(exclude=['floating'])
    print(X)                 

def main():
    box()


if __name__ == '__main__':
    main()
