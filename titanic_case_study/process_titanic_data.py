import numpy as np

data=np.genfromtxt("titanic_case_study\\passenger.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")

print(data.shape)

# total number of survivals

survival=data[data[:,1].astype('int')==1]
print("survival",survival.shape)


# total number of death
death=data[data[:,1].astype("int")==0]
print("death",death.shape)

# survival rate
survived_unsurvived=data[:,1].astype("int")
survived=survived_unsurvived[survived_unsurvived==1]
print(f" total number of survived {survived_unsurvived.size}")

survival_rate=(survived.size/ survived_unsurvived.size)*100
print(f"survival rate={survival_rate}")

#death 
death=survived_unsurvived[survived_unsurvived==0]
print(f" total number of death {death.size}")

death_rate=(death.size/survived_unsurvived.size)*100
print(f"death_rate={death_rate}")

# gender analysis
# total number of males
# total number of females
# male survival rate
# female survival rate

genders=data[:,3]

male_count=genders[genders=="male"].size
print(f"male count {male_count}")

female_count=genders[genders=="female"].size
print(f"female count {female_count}")

survived_males=data[(data[:,3]=="male")&(data[:,1].astype("int")==1)]
survived_male_count=survived_males[:,0].size
print(f"survival rate {survived_males}")
male_survival_rate =(survived_male_count/male_count)*100
print(f"male survival rate {male_survival_rate}")

survived_females=data[(data[:,3]=="female")&(data[:,1].astype('int')==1)]
survived_females_count=survived_females[:,0].size
print(f"survival rate {survived_females}")
female_survival_rate=(survived_females_count/female_count)*100
print(f"female survival rate {female_survival_rate}")

ages=data[:,4].astype('int')
print(f"minimum age {np.min(ages)}")
print(f"maxmium age {np.max(ages)}")
print(f"average age {np.average(ages)}")

#fare analysis

fare=data[:,5].astype('float')
print(f"minimum fare {np.min(fare)}")
print(f"maxmium fare {np.max(fare)}")
print(f"average fare {np.average(fare)}")

print(data[np.argsort(data[:,2].astype('float'))])