from datetime import datetime
tstamp = datetime.strptime('31/01/22 23:59:59.999999',
                  '%d/%m/%y %H:%M:%S.%f')
print(tstamp)