from datetime import  datetime

# ts = '2023-02-01 14:30:00'
tstamp = datetime.strptime('3:59',
                  '%H:%M')

Db  =  {
    'patient1':[['1:00','Location','11'],
                ['2:00','Location','12']],


 
    'patient2':[['1:30','Location','13'],
                ['2:30','Location','14']],
        }


#blank lists
arrangement = []
re_arrangement = []
pa_na = []
pa_task = []
#Spliting the tasks out
for patients in Db:
   pa_na.append(patients)
for assignments in Db.values():
   pa_task.append(assignments)
num1 = 0
num2 = 0
#First choose which patient
while num1 < len(Db):
   num2 = 0
   #Then the tasks inside the patient's list
   while num2 < len(pa_task[num1]):
    #Rearrange the tasks into blank list as the format:[time, patient, location, guide_num]
    pa_task[num1][num2].insert(1,pa_na[num1])
    num2 += 1
   num1 += 1
#Put stuff in arrangement (list)
for task_list in pa_task:
   for task in task_list:
      arrangement.append(task)

print(arrangement)
"""
for item in arrangement:
   hour = (item[0].split(':')[0])
   minute = (item[0].split(':')[1])
   time_list = [hour + ':' + minute] # Recommend by pycharm
hour_lt = []
minute_lt = []
for time in time_list:
   hour = time_list(time.split(':')[0])
   minute = time_list(time.split(':')[1])
   hour_lt.append(hour)
   minute_lt.append(minute)
   min_hour = min(hour_lt)
   min_minute = min(minute_lt)
   if min_hour != min_minute and time_list[min_minute].split(':')[0] > time_list[min_hour].split(':')[0]:
      re_arrangement.append(arrangement[min_minute])
      arrangement.remove(arrangement[min_minute])
   else:
      re_arrangement.append(arrangement[min_hour])
      arrangement.remove(arrangement[min_hour])"""
#To delete stuff
def deleter(patient, time, location, message):
   info = Db[patient]
   task_a = [time, patient, location, message]
   for task in info:
      if task == task_a:
        print('TAT')
        Db[patient].remove(task)
deleter('patient1','2:00','Location','12')
