from django.shortcuts import render
from .controller import Controller
from .exceptions import *


# Create your views here.
def view(request):
    if request.method == 'GET':
        try:
            X_axis = [None] * int(request.GET.get('X'))
            Y_axis = [None] * int(request.GET.get('Y'))
            axis_flag = True
            message = 'okk'
        except (TypeError, ArithmeticError, Exception):
            X_axis = 0
            Y_axis = 0
            axis_flag = False
            message = 'input error'

        context:dict = {'X_axis': X_axis,
                        'Y_axis': Y_axis,
                        'axis_flag': axis_flag,
                        'message': message
                        }
        
    return render(request,'grid.html', context=context)


def shape(reqest):
    controller = Controller()
    if reqest.method == 'GET':
        try:
            arr_info = controller.shape_generator(str(reqest.GET.get('option')))
            axis_flag = True
            message = 'ok'
        except (TypeError, ArithmeticError):
            axis_flag = False
            message = 'input error, give only latters'
        except EmplyParameterError:
            axis_flag = False
            message = 'give a later'
        
        context:dict = {'arr_info': arr_info,
                        'axis_flag': axis_flag,
                        'message': message
                        }

    return render(reqest,'shapes.html', context=context)