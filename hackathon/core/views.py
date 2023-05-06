from django.shortcuts import render

# Create your views here.

def view(reqest):
    if reqest.method == 'GET':
        try:
            X_axis = [None] * int(reqest.GET.get('X'))
            Y_axis = [None] * int(reqest.GET.get('Y'))
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
        
    return render(reqest,'grid.html', context=context)

def shape_generator(shape_form:str):
    if not shape_form:
        return None
    
    rows, cols = (5, 5)
    arr:list = [[0]*cols]*rows

    if shape_form == 'F':
        for i in range(4):
            arr[0][0] = 1
        return arr

    if shape_form == 'I':
        for index in range(5):
            arr[2][index] = 1
        return arr
    
    if shape_form == 'L':
        for index in range(4):
            arr[2][1 + index] = 1
        arr[3][4] = 1
        return arr
    

def shape(reqest):
    if reqest.method == 'GET':
        try:
            arr = shape_generator(str(reqest.GET.get('option')))
            print(arr)
            print(arr[2][2])
            axis_flag = True
            message = 'ok'
        except (TypeError, ArithmeticError):
            X_axis = 0
            Y_axis = 0
            axis_flag = False
            message = 'input error'
        except Exception:
            message = 'wasted'

        context:dict = {'arr': arr,
                        'axis_flag': axis_flag,
                        'message': message
                        }
        
    return render(reqest,'shapes.html', context=context)