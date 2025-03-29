# Whole schedule
Schedule = {"worker1":{"patient1":['time','detail information'],"patient2":['time','detail information']},"worker2":{}}


# Given the tasklist depend on the user id
def reader(read_obj,user_id):
    tasklist = []
    for i in read_obj[user_id]:
        tasklist.append(i)
    return  tasklist

