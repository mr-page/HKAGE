from datetime import  datetime



# ts = '2023-02-01 14:30:00'
tstamp = datetime.strptime('3:59',
                  '%H:%M')

Orderliness={
    'patient1':1,
    'patient2':2,
}


db  = {
    'patient1':{'1:00':['Location','comment'],
                '2:00':['Location','comment'],


    },
    'patient2':{'1:00':['Location','comment'],
                '2:00':['Location','comment'],


    },
}

# # Create the pandas DataFrame
# time = input('When?')
# patient = input("Who is in need?")
# info = db[patient]
# keys = list(filter(lambda key: info[key] == ['location', 'comment'], info))
# print(keys)



def time_resort(orderliness,db):
    for patient in db.value():
        for event in patient.value():
            pass
    return

