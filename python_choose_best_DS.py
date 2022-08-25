# employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"},{"id":7843, "name":"waqar","department":"computer science"}]

# def get_employee(id): 
#     for employee in employee_list:
#         if employee['id'] == id:
#             return employee

# print(get_employee(7843))


# we can also manage this program in much better way because this program have less performance.

employee_list = {
    12345:
    {"id": 12345, "name": "John", "department": "Kitchen"},
    12458:
    {"id": 12458, "name": "Paul", "department": "House Floor"},
    7843:
    {"id":7843, "name":"waqar","department":"computer science"}}
     
def get_employee(id):
   return employee_list[id];

print(get_employee(7843))
#this is the best way to because it improves the performance of the program. This is because like first solution it does not iterate over the whole list of items,it only match the id and will gives us id.