import employee_info

def test_bubble_sort_get_employees_by_age_range():
    expected_result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    
    result = employee_info.get_employees_by_age_range(22,31)
    assert ( result == expected_result)

def test_bubble_sort_calculate_average_salary(): 
    result = employee_info.calculate_average_salary()
    expected_result =  60166.67
    assert (result == expected_result)

def test_bubble_sort_get_employees_by_dept(): 
    result = employee_info.get_employees_by_dept("Sales")
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert ( result == expected_result)
    
