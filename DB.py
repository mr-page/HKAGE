from datetime import  datetime



# ts = '2023-02-01 14:30:00'
tstamp = datetime.strptime('3:59',
                  '%H:%M')

Orderliness=[
    'patient1',
    'patient2',
]


Db  = [
    {
    'patient1':{'1:00':['Location','11'],
                '2:00':['Location','12'],
                }
    },
    {
    'patient2':{'1:00':['Location','21'],
                '2:00':['Location','22'],
                }
    }
]

# # Create the pandas DataFrame
# time = input('When?')
# patient = input("Who is in need?")
# info = db[patient]
# keys = list(filter(lambda key: info[key] == ['location', 'comment'], info))
# print(keys)



def time_resort(orderliness,db):
    temp_db = []
    for patient in orderliness:
        for Val in db[patient]:
            temp_db.append(patient)
            temp_db.append((Val))
    return temp_db
print(time_resort(Orderliness,Db))
print(time_resort(Orderliness,Db)[0])

