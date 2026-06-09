import re
class Solution:
    def evaluateEmployee(self,emp_id,name,attendance,project_completion):
        if not re.match(r"^EMP\d{3,5}$",emp_id):
            return "Invalid Employee ID"
        if not re.match(r"^[A-Za-z ]+$",name):
            return "Invalid Employee Name"
        if attendance<0 or attendance>100:
            return "Invalid attendance percentage"
        if project_completion<0 or project_completion>100:
            return "Invalid project completion percentage"
        score=(attendance*0.4)+(project_completion*0.6)
        if score>=90:
            return "Excellent"
        elif score>=75:
            return "Good"
        elif score>=60:
            return "Average"
        else:
            return "Needs Improvement"
emp_id=input("Enter Employee ID:")
name=input("Enter name:")
attendance=float(input("Enter attendance:"))
project_completion=float(input("Enter Project completion percentage:"))
obj=Solution()
result=obj.evaluateEmployee(emp_id,name,attendance,project_completion)
print("\nEmployee Rating",result)