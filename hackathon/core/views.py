from django.shortcuts import render

# Create your views here.

def view(reqest):
    if reqest.method == 'GET':
        X_axis = int(reqest.GET.get('X'))
        Y_axis = int(reqest.GET.get('Y'))

        context:dict = {'X_axis':X_axis,
                        'Y_axis':Y_axis
                        }
        
    return render(reqest,'grid.html', context=context)

