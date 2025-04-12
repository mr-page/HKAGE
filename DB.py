from datetime import  datetime

# ts = '2023-02-01 14:30:00'
tstamp = datetime.strptime('3:59',
                  '%H:%M')

Orderliness={
    'patient1':1,
    'patient2':2,
}


Db  =  {
    'patient1':[['1:00','Location','11'],
                ['2:00','Location','12']],


 
    'patient2':[['1:30','Location','13'],
                ['2:30','Location','14']],
        }


#hour = print(assignment[0].split(':')[0])
#minute = print(assignment[0].split(':')[1])
arrangement = []
for assignments in Db.values():
   for assignment in assignments:
      



      

def deleter(patient, time, location, message):
   info = Db[patient]
   task_a = [time, location, message]
   for task in info:
      if task == task_a:
        print('TAT')
        Db[patient].remove(task)
deleter('patient2','1:30','Location','13')
print(Db)
