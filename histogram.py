from pandas import read_csv
from matplotlib import pyplot as plt
   
def histogram():
        dataset=read_csv("iris.csv")
        range = (0,8)
        bins=5
        X=dataset.iloc[:,2].values
        print(X)
        plt.hist(X,bins,range,histtype='bar',rwidth=0.5,color='RED',)
        plt.title("petals_histogram")
        plt.show()
    
def main():
     histogram()
    
if __name__ == '__main__':
    main()
