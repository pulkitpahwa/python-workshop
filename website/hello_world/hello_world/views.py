from django.http import HttpResponse
from student.models import Student


def home(request):
    return HttpResponse("Hello world")
    
def hello(request, enrollment_number):
    st = Student.objects.get(enrollment_number=enrollment_number)

    return HttpResponse("Hello "+st.course)
    
def add(request, num1, num2):
    result = "sum of %s and %s is %s" %(  num1 , num2, str(int(num1) + int(num2)))
    return HttpResponse(result)    
    
