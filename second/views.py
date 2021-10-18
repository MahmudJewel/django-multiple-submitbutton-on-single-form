from django.shortcuts import render
print('hello')
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
        
        elif 'WordCount' in request.POST:
            txt=f"Total word = {len(originaltxt.strip().split(' '))}"
            #print(type(originaltxt))


    context={
        'txt': txt,
        'originaltxt':originaltxt,
    }
    return render(request,'home.html',context)