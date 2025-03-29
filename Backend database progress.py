# The task list of different member

Todo = []

def reader(read_obj):
    tasklist = []
    for i in read_obj:
        for j in i:
            tasklist.append(j)
