

data = {'tom':
        [["23", 'ga', "19:00"]
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
info = data[worker]
for stu in info:
    if stu == assign:
        print(True)
        data[worker].remove(stu)
print(data)