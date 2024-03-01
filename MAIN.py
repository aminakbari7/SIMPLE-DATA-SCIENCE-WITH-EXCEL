import pandas as pd
###########---> read file
dataframe1 = pd.read_excel('data.xlsx')

#########-->first get header xlsx
Full_Names=dataframe1['Full Name']
Job_Titles=dataframe1['Job Title']
Departments=dataframe1['Department']
Business_Units=dataframe1['Business Unit']
Genders=dataframe1['Gender']
Ethnicitys=dataframe1['Ethnicity']
Ages=dataframe1['Age']
Hire_Dates=dataframe1['Hire Date']
Annual_Salarys=dataframe1['Annual Salary']
Bonus=dataframe1['Bonus %']
Countrys=dataframe1['Country']
Citys=dataframe1['City']






print(dataframe1['Full Name'])