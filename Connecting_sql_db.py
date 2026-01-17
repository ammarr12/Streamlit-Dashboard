import mysql.connector

mydb = mysql.connector.connect(
    
    host = "127.0.0.1",
    user = "root",
    password = "ammar123"
)

cursor=mydb.cursor(buffered=True)
cursor.execute("use coffe_cafe")
cursor.execute("select * from dataset")

results = cursor.fetchall()

column_names = cursor.column_names
dict1={}
for i in range(len(column_names)):
    dict1[column_names[i]]=[]

for i in range(len(results)):
    for j in range(14):

        if j == 0:
            dict1[column_names[j]].append(results[i][j])
        if j == 1:
            dict1[column_names[j]].append(results[i][j])
                
        if j == 2:
            dict1[column_names[j]].append(results[i][j])
                    
        if j == 3:
            dict1[column_names[j]].append(results[i][j])
                        
        if j == 4:
            dict1[column_names[j]].append(results[i][j])
                            
        if j == 5:
            dict1[column_names[j]].append(results[i][j])
                                
        if j == 6:
            dict1[column_names[j]].append(results[i][j])
                                    
        if j == 7:
            dict1[column_names[j]].append(results[i][j])
                                        
        if j == 8:
            dict1[column_names[j]].append(results[i][j])
                                            
        if j == 9:
            dict1[column_names[j]].append(results[i][j])
                                                
        if j == 10:
            dict1[column_names[j]].append(results[i][j])
                                                    
        if j == 11:
            dict1[column_names[j]].append(results[i][j])
                                                        
        if j == 12:
            dict1[column_names[j]].append(results[i][j])
                                                            
        if j == 13:
            dict1[column_names[j]].append(results[i][j])


                                                
    
    




cursor.close()
mydb.close()