db = {
    'patient':{3600:['location', 'comment']}
}

# Create the pandas DataFrame
time = input('When?')
patient = input("Who is in need?")
info = db[patient]
keys = list(filter(lambda key: info[key] == ['location', 'comment'], info))
print(keys)
