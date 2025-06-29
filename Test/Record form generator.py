from openpyxl import Workbook, load_workbook
from datetime import datetime, timedelta
import re

def read_and_write(import_text):
    number = re.findall(r'\d+', import_text)[0]
    # WRITE to Excel
    def write_to_excel(filename, data):
        """Write data to Excel file"""
        wb = Workbook()
        ws = wb.active
        
        # Add headers


        # Add data rows
        for row in data:
            ws.append(row)

        wb.save(filename)
        print(f"Data written to {filename}")


    # READ from Excel
    def read_from_excel(filename):
        """Read data from Excel file"""
        wb = load_workbook(filename)
        ws = wb.active

        data = []
        for row in ws.iter_rows(values_only=True):
            data.append(row)

        return data

    def find_cell_by_value(file_path, search_value):
        wb = load_workbook(file_path)
        for sheet in wb:
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value == search_value:
                        return {
                            'sheet': sheet.title,
                            'row': cell.row,
                            'column': cell.column,
                            'address': cell.coordinate,
                            'value': cell.value
                        }
        return None


    day = []
    for i in range(31):
        day.append(str(i + 1))

    def generate_time_intervals():
        start_time = datetime.strptime("00:00", "%H:%M")
        end_time = datetime.strptime("23:59", "%H:%M")
        delta = timedelta(minutes=15)

        times = []
        current = start_time
        while current <= end_time:
            times.append([current.strftime("%H:%M")])
            current += delta
        return times

    time_list = generate_time_intervals()
    # Example usage
    data = [
        ['Name','','',str(datetime.now().strftime('%Y/%m'))],
        ['Birth date',''],
        ['Number',str(number)],
        ['','Day']+day,
        ['Month',''],
        *time_list
    ]



    write_to_excel("record document/"+number+".xlsx", data)
    print("Data from file:", read_from_excel("record document/"+number+".xlsx"))
for i in range(50):
    read_and_write(str(i+1))


