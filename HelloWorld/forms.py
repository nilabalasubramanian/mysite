from django import forms
from .models import Employee


# creating a form

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        #We can specify all the fields from table like the above or the below(any one is specified.
        #Even we can specify the needed fields also
        # fields = ["empNo", "empName", "empSalary", "empAddress", ]
        # labels = {"empNO": "EmpNo", "empName": "EmpName", "empSalary": "EmpSalary", "empAddress": "EmpAddress", }
