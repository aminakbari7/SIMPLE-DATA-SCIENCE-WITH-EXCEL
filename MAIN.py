import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
   
    def diplay2dplot(self):
            npx=np.asarray(self.Full_Names)
            npy=np.asarray(self.Genders)
            plt.plot(npx,npy)
            plt.show()
def main():
    dataframe = pd.read_excel('data.xlsx')
    My_Analysis_Data=Analysis_Data(dataframe= dataframe)
    
    
    #print("min salary = ",My_Analysis_Data.full_name_of_min_salary(),My_Analysis_Data.Annual_Salarys.min())
    #print("max salary = ",My_Analysis_Data.full_name_of_max_salary(),My_Analysis_Data.Annual_Salarys.max())
    ###->plot two of header list
    My_Analysis_Data.diplay2dplot()
  
if __name__=="__main__":
    main()
