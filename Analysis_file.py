
import pandas as pd

dict1=pd.read_csv("dataset.csv")

df=pd.DataFrame(dict1)

df_2=df[["product_category","revenue"]]
v=df_2["product_category"].value_counts().index.to_list()



coffee_rev=0
coffe=df_2[df_2["product_category"]=="Coffee"]
for i in coffe["revenue"]:
    coffee_rev+=i
    coffee_rev=round(coffee_rev,2)
    coffee_rev

print(coffee_rev)

tea_rev1=0
tea=df_2[df_2["product_category"]=="Tea"]
for i in tea["revenue"]:
    tea_rev1+=int(i)
    tea_rev1=round(tea_rev1,2)

bakery_rev=0
bakery=df_2[df_2["product_category"]=="Bakery"]
for i in bakery["revenue"]:
    bakery_rev+=i
    bakery_rev=round(bakery_rev,2)


drnking_choco_rev=0
drnking_choco=df_2[df_2["product_category"]=="Drinking Chocolate"]
for i in drnking_choco["revenue"]:
    drnking_choco_rev+=i
    drnking_choco_rev=round(drnking_choco_rev,2)

prodct_compar=pd.DataFrame({"Product Category":[v[0],v[1],v[2],v[3]],"Revenue":[coffee_rev,tea_rev1,bakery_rev,drnking_choco_rev]})

times_occured=df["hour_of_day"].value_counts().values.tolist()
hours_of_the_days=df["hour_of_day"].value_counts().index.tolist()

dict2={"Hours":[],"Revenue Generated":[]}

counter_var=0

for i in hours_of_the_days:
    
    if i == 13:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue=0
            
        for j in df_3["revenue"]:
            rvnue+=j
        dict2["Revenue Generated"].append(rvnue)
        dict2["Hours"].append(i)
    
    if i == 12:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue2=0
            
        for j in df_3["revenue"]:
            rvnue2+=j
        dict2["Revenue Generated"].append(rvnue2)
        dict2["Hours"].append(i)
            
    if i == 11:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue3=0
            
        for j in df_3["revenue"]:
            rvnue3+=j
        dict2["Revenue Generated"].append(rvnue3)
        dict2["Hours"].append(i)
        
        
    if i == 10:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue4=0
            
        for j in df_3["revenue"]:
            rvnue4+=j
        dict2["Revenue Generated"].append(rvnue4)
        dict2["Hours"].append(i)
            
            
    if i == 9:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue5=0
            
        for j in df_3["revenue"]:
            rvnue5+=j
        dict2["Revenue Generated"].append(rvnue5)
        dict2["Hours"].append(i)
            
            
    if i == 8:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue6=0
            
        for j in df_3["revenue"]:
            rvnue6+=j
        dict2["Revenue Generated"].append(rvnue6)
        dict2["Hours"].append(i)
            
    if i == 7:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)
            
    if i == 14:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)

    if i == 15:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)
    
    if i == 16:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)

    if i == 17:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)

    if i == 17:
        
        
        df_3=df[df["hour_of_day"] == i]
        rvnue7=0
            
        for j in df_3["revenue"]:
            rvnue7+=j
        dict2["Revenue Generated"].append(rvnue7)
        dict2["Hours"].append(i)
            
                

        
         
            
dict2=pd.DataFrame(dict2)
rvnue_by_hour=dict2.sort_values(by="Hours") 

var=0
for i in df["revenue"]:
     var+=i

Total_Revenue=var            

cffe_srvd=df[df["product_category"]=="Coffee"]
cffe_srvd=cffe_srvd["product_category"].count()