from pandas import read_csv
from matplotlib import pyplot as plt

def histogram():
    Iris_file= "iris.csv"
    datasets = read_csv(Iris_file,skiprows=[1])
    print(datasets.dtypes)      #gives details of datatypes of attributes
    datasets.hist(color='RED')             #makes a histogram
    plt.show()           #displays the graph

if __name__ == '__main__':
    histogram()
