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
    datasets.plot.box()
    pyplot.show()
     
def main():
    box()


if __name__ == '__main__':
    main()
