from django.shortcuts import render

# Create your views here.

def view(reqest):
    if reqest.method == 'GET':
        try:
            X_axis = str(reqest.GET.get('X'))
            Y_axis = str(reqest.GET.get('Y'))
            axis_flag = True
            message = 'okk'
        except (TypeError, ArithmeticError):
            X_axis = 0
            Y_axis = 0
            axis_flag = False
            message = 'input error'

        context:dict = {'X_axis': X_axis,
                        'Y_axis': Y_axis,
                        'axis_flag': axis_flag,
                        'message': message
                        }
        
    return render(reqest,'grid.html', context=context)

