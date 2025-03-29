# Whole schedule
Schedule = []
# In format of :
[
    Patient
]



# The task list of different member







Todo = {}

# Given the tasklist depend on the user id
def reader(read_obj,user_id):
    tasklist = []
    for i in read_obj[user_id]:
        for j in i:
            tasklist.append(j)
    return  tasklist

