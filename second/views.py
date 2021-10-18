from django.shortcuts import render

# Create your views here.
def home(request):
    txt,originaltxt='',''
    if request.method=='POST':
        originaltxt=request.POST.get('tarea')
        if 'Lower' in request.POST:
            txt=originaltxt.lower()
        
        elif 'Upper' in request.POST:
            txt=originaltxt.upper()
        
        elif 'Title' in request.POST:
            txt=originaltxt.title()

        elif 'Capitalize' in request.POST:
            txt=originaltxt.capitalize()

    context={
        'txt': txt,
        'originaltxt':originaltxt,
    }
    return render(request,'home.html',context)