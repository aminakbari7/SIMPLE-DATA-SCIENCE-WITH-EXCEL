import pandas as pd
import numpy as np
from scipy import stats
import statistics
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn import preprocessing
class Analysis_Data:
    def __init__(self,dataframe):
          self.dataframe = dataframe
          self.Full_Names=dataframe['Full Name']
          self.Job_Titles=dataframe['Job Title']
          self.Departments=dataframe['Department']
          self.Business_Units=dataframe['Business Unit']
          self.Genders=dataframe['Gender']
          self.Ethnicitys=dataframe['Ethnicity']
          self.Ages=dataframe['Age']
          self.Hire_Dates=dataframe['Hire Date']
          self.Annual_Salarys=dataframe['Annual Salary']
          self.Bonus=dataframe['Bonus %']
          self.Countrys=dataframe['Country']
          self.Citys=dataframe['City']
           
    def full_name_of_max_salary(self):
       return self.Full_Names[self.Annual_Salarys.idxmax()]
    def full_name_of_min_salary(self):
       return self.Full_Names[self.Annual_Salarys.idxmin()]
    def mean_data(self,data):
        npdata=np.asarray(data)
        return np.mean(npdata)
    def median_data(self,data):
        npdata=np.asarray(data)
        return np.median(npdata)
    def mode_data(self,data):
        npdata=np.asarray(data)
        return stats.mode(npdata)
    def variance_data(self,data):
        npdata=np.asarray(data)
        return statistics.variance(npdata)
    def diplay2dplot(self):
            npx=np.asarray(self.Full_Names)
            npy=np.asarray(self.Genders)
            plt.plot(npx,npy)
            plt.show()
    def boxplot(self,data):
            npdata=np.asarray(data)
            plt.boxplot(npdata)
            plt.show()    
    def give_unique_values_of_list(self,data):
        return set(data) 
    
    def find_outliers(self,data,threshold):
        nplist=np.asarray(data)
        mean = np.mean(data)
        std = np.std(data)
        outliers = []
        for x in data:
            z_score = (x - mean) / std
            if abs(z_score) > threshold:
                outliers.append(x)
        return outliers 
    
    
    def normalize(self,data): #if you want normalize yor list
        npdata=np.asarray(data)
        normalized_arr = preprocessing.normalize([npdata])
        
    def Decision_Trees(self,):
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(0, 0)
def main():
    
    ###------------read file and set class
    dataframe = pd.read_excel('data.xlsx')
    My_Analysis_Data=Analysis_Data(dataframe= dataframe)
    #print(My_Analysis_Data.dataframe.columns)
    #print(My_Analysis_Data.dataframe.head)
    
    ###->plot two of header list
    ##My_Analysis_Data.diplay2dplot()
    #My_Analysis_Data.boxplot(My_Analysis_Data.Annual_Salarys)
    
    
    #print("min salary = ",My_Analysis_Data.full_name_of_min_salary(),My_Analysis_Data.Annual_Salarys.min())
    #print("max salary = ",My_Analysis_Data.full_name_of_max_salary(),My_Analysis_Data.Annual_Salarys.max())
    #print("mean is = ",My_Analysis_Data.mean_data(My_Analysis_Data.Annual_Salarys))
    #print("median is = ",My_Analysis_Data.median_data(My_Analysis_Data.Annual_Salarys))
    #print("mode is = ",My_Analysis_Data.median_data(My_Analysis_Data.Annual_Salarys))
    #print("variance is = ",My_Analysis_Data.variance_data(My_Analysis_Data.Annual_Salarys))
    #print(My_Analysis_Data.dataframe["Full Name"])
    
    #print("list of jobs = \n",My_Analysis_Data.give_unique_values_of_list(My_Analysis_Data.Job_Titles))
    #print(My_Analysis_Data.find_outliers(My_Analysis_Data.Annual_Salarys,1))
    #My_Analysis_Data.Decision_Trees()

if __name__=="__main__":
    main()
