

data = {'tom':
        [["23", 'ga', "19:00"]
         ['20', 'ba', '20:00']
        ], 'nick': 
        [["19", "feed pills", "20:30"]
         ], 'juli': [["12", "provide meds", "15:15"]]}

# Create the pandas DataFrame

worker = input('Who to do?')
task = input('What task to do?')
time = input('When?')
patient = input("Who is in need?")
assign = [patient, task, time]
print(assign)
#Chooses the assigned worker
info = data[worker]
#Checks if any task is the same as the finished one
for stu in info:
    if stu == assign:
        print(True)
        data[worker].remove(stu)
print(data)

def deleter(patient, time, location, message):
   info = Db[patient]
   task_a = [time, location, message]
   for task in info:
      if task == task_a:
        print('TAT')
        Db[patient].remove(task)
deleter('patient2','1:30','Location','13')
print(Db)