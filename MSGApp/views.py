from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  
from MSGApp.functions import handle_uploaded_file  #functions.py
from MSGApp.forms import UploadForm #forms.py
   
def index(request):  
    if request.method == 'POST':  
        upload = UploadForm(request.POST, request.FILES)  
        if upload.is_valid():  
            model_instance = upload.save(commit=False)
            model_instance.save() #save the instance first so that the file can be uploaded and read
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("Data imported successfuly")  
    else:  
        upload = UploadForm()  
        return render(request,"index.html",{'form':upload}) 