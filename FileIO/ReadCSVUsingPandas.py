import pandas
df = pandas.read_csv('C:\\Users\\DELL\\Desktop\\Python\\FileIO\empData.csv')
print(df)

# import pandas
# df = pandas.read_csv('empData.csv', index_col='Name')
# print(df)

# import pandas
# df = pandas.read_csv('empData.csv', index_col='Name', parse_dates=['Hire Date'])
# print(df)

# import pandas
# df = pandas.read_csv('empDdata.csv', 
#             index_col='Employee', 
#             parse_dates=['Hired'], 
#             header=0, 
#             names=['Employee', 'Hired','Salary', 'Sick Days'])
# print(df)



# Write Operation
# import pandas
# df = pandas.read_csv('empData.csv', 
#             index_col='Employee', 
#             parse_dates=['Hired'],
#             header=0, 
#             names=['Employee', 'Hired', 'Salary', 'Sick Days'])
# df.to_csv('hrdata_modified.csv')