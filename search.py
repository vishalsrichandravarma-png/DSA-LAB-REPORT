def search_employee(emp_list, key, index):
    if index == len(emp_list):
        return False
    if emp_list[index] == key:
        return True
    return search_employee(emp_list, key, index + 1)

# Driver Code
employees = [101, 102, 103, 104, 105]

key = int(input("Enter Employee ID to search: "))

if search_employee(employees, key, 0):
    print("Employee ID Found")
else:
    print("Employee ID Not Found")