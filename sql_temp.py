import openpyxl as pyxl

from threading import Thread
 
import sqlite3 as sql3

conn = sql3.connect("data/collectedData.db")
cur = conn.cursor()

#Task 2
''' Find cities in southern hemisphere first "where location = "*S"" '''

#Query: list major cities in southern hemisphere ordered by country. name,country,location 
def Task2():
    taks = cur.execute("Select distinct City, Country, Lat, Long from City where Lat LIKE '%S'  Order By Country;")
    TMP = []
    for row in taks:
       print ("City = ", row[0])
       print ("Country = ", row[1])
       print ("Lat= ", row[2])
       print ("Long = ", row[3], "\n")
       for i in range(4):
           TMP.append(row[i])

    #append to database
    count = [0,1,2,3]
    T = True
    while T == True:
        for i in range(4):
            try:
                cur.execute("INSERT INTO SouthernCities VALUES ( ?, ?, ?, ?);", (TMP[count[0]], TMP[count[1]], TMP[count[2]], TMP[count[3]]))
                conn.commit()
                count[0] = count[0] + 4
                count[1] = count[1] + 4
                count[2] = count[2] + 4
                count[3] = count[3] + 4
            except:
                print("fin")
                T = False
                break
    

def QueryQLD():
    #find max min avg temp of QLD for year 2000 print in consol
    '''
    taks = cur.execute("Select Date, AverageTemp , State, Country from State where Date LIKE '2000%' and State == 'Queensland';")
    for row in taks:
       print ("Date = ", row[0])
       print ("AverageTemp = ", row[1])
       print ("State = ", row[2])
       print ("Country= ", row[3],"\n")
    '''
    print("QLD Results:")
    taks1 = cur.execute("Select max(AverageTemp) as Max from State where Date LIKE '2000%' and State == 'Queensland';")
    for row in taks1:
       print ("Max = ", row[0],"\n")

    taks2 = cur.execute("Select min(AverageTemp) as Min from State where Date LIKE '2000%' and State == 'Queensland';")
    for row in taks2:
       print ("Min = ", row[0],"\n")

    taks3 = cur.execute("Select avg(AverageTemp) as Avg from State where Date LIKE '2000%' and State == 'Queensland';")
    for row in taks3:
       print ("Avg = ", row[0],"\n")

#end

if __name__ == "__main__":
    Task2()
    QueryQLD()

    conn.close()
