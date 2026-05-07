import employee_info as employee
import pytest
def test_get_employee_by_age_range():
    result = []
    result = employee.get_employees_by_age_range(20,30)
    answer = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(answer==result)
def test_calculate_average_salary():
    result = []
    result = employee. calculate_average_salary()
    assert result == pytest.approx(60166.667,rel=1e-3)
def test_get_employee_by_dept():
    result=[]
    result = employee.get_employees_by_dept("Marketing")
    answer = [ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    assert answer == result