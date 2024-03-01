import pandas as pd


class Analysis_Data:
    def __init__(self,dataframe, ):
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
       return self.Full_Names[self.Annual_Salarys.idxmax()],

def main():
    dataframe = pd.read_excel('data.xlsx')
    My_Analysis_Data=Analysis_Data(dataframe= dataframe)
    
    #####-> who get most salary?
    print(My_Analysis_Data.full_name_of_max_salary())
    
if __name__=="__main__":
    main()
