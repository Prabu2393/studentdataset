import pandas as pd
from datetime import datetime,date
df=pd.read_csv(r"C:\Users\Prabhu\Downloads\student.csv")
print(df)
#Extracting firstname and last name and storing it to a new variable fullname
df[df.columns[1:2]]
df['Full_name'] = df['stuf_name'] + df['stul_name']

#User name creation by extracting first 4 letters from first name and last name
df['username'] = df['stuf_name'].str[:4]+(df['stul_name'].str[:4])

# age calculation from DOB 
def stu_age(born):
    born=datetime.strptime(born,'%Y-%m-%d').date()
    today=date.today()
    return today.year - born.year - ((today.month,today.day)<(born.month,born.day))

df['stu_age'] = df['stu_dob'].apply(stu_age)


#age criteria condition
def age(x):
    if x<18:
        return 'Minor'
    elif x>18 & x<40:
        return 'Major'
    else:
        return 'Senior'
df['Age_criteria'] = df['stu_age'].apply(age)
print(df)
    
