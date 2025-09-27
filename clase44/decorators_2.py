def check_access(func):
    def wrapper(employee):
        if employee.get('role') == "admin":
            return func(employee)
        else:
            print("Access denied. Only admin can delete employees.")
    return wrapper


@check_access
def delete_employee(employee):
    print(f"Employee {employee} has been deleted.")

admin = {'name': 'Alice', 'role': 'admin'}
user = {'name': 'Bob', 'role': 'user'}

# delete_employee(admin)  # Should proceed
delete_employee(user)   # Should deny access