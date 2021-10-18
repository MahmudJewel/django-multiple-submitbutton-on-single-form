# Handling multiple submit buttons on django form
# i) Method-1
```
if request.method=='POST':
	if 'Lower' in request.POST:
            	pass
	elif 'Upper' in request.POST:
           	pass
```
Where 'Lower' and 'Upper' is the submit button’s name
