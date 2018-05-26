import csv
import os
file_name=os.path.join("raw_data","employee_data1.csv")
csv_list=[]
us_state_abbrev = {
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR',
     'California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE',
    'Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD','Massachusetts': 'MA', 'Michigan': 'MI',
     'Minnesota': 'MN',  'Mississippi': 'MS', 'Missouri': 'MO','Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
    'New Mexico': 'NM','New York': 'NY', 
    'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK',
     'Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC',
    'South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT',
    'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI', 'Wyoming': 'WY'   
  
}
with open(file_name, "r", newline='') as csv_file:
    csvreader = csv.DictReader(csv_file)
    for row in csvreader:
        csv_list.append(row)
    
for row in csv_list:
    
#split the Name column into separate First Name and Last Name columns
    name_lastname=row['Name'].split(' ')
    row['First Name']=name_lastname[0]
    row['Last Name']=name_lastname[1]
    row.pop('Name')   
    
#re-write DOB data in MM/DD/YYYY format.   
    row['DOB']=row['DOB'][5:7]+"/"+row['DOB'][-2:]+"/"+row['DOB'][:4]
    
# re-write SSN data such that the first five numbers are hidden from view.     
    row['SSN']="***-**-"+row['SSN'][-4:]
    
#re-write State data as simple two-letter abbreviations.  
    if us_state_abbrev.get(row['State']):
       row['State']=us_state_abbrev.get(row['State'])

#export data
with open("results.csv", "w", newline='') as new_file:
     field_names=['Emp ID','First Name','Last Name','DOB','SSN','State']
     csvwriter=csv.DictWriter(new_file, fieldnames=field_names)
     csvwriter.writeheader()
     csvwriter.writerows(csv_list)

