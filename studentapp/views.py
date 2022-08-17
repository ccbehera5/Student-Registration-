from django.shortcuts import redirect, render
from studentapp.models import StudentData

# Create your views here.
def fetchingdata(request):
   students=StudentData.objects.all()
   return render(request,'fetchingdata.html',{'students':students})
def studentdata(request):
     if request.method=='POST':
      name=request.POST.get('name')
      department=request.POST.get('department')
      email=request.POST.get('email')
      mobile=request.POST.get('mobile')
      address=request.POST.get('address')

      StudentData(
         Name=name,
         Department=department,
         Email=email,
         Mobile=mobile,
         Address=address
      ).save()
      return redirect('fetchingdata')

         
     else:
        return render(request,'student.html')

