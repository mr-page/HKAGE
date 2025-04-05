from datetime import  datetime



# ts = '2023-02-01 14:30:00'
tstamp = datetime.strptime('3:59',
                  '%H:%M')

Orderliness={
    'patient1':1,
    'patient2':2,
}


Db  = [
    {
    'patient1':{'1:00':['Location','comment'],
                '2:00':['Location','comment'],


    }
    },
        {
    'patient2':{'1:00':['Location','comment'],
                '2:00':['Location','comment'],
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
    for patient in db:
        for event in patient.values():
            temp_db.append([patient.values(),event])
    return temp_db
print(time_resort(Orderliness,Db))
print(time_resort(Orderliness,Db)[0])

