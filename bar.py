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
    color=["REd","BLUE","BLACK","GREEN"]
    datasets.plot(kind="bar",color=color)
    pyplot.show()

    datasets.plot.bar()#vertical bar plot
    pyplot.show()
    datasets.plot.barh()#horizontal bar plot
    pyplot.show()
  
def main():
    box()


if __name__ == '__main__':
    main()
