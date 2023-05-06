from django.shortcuts import render

# Create your views here.

def view(reqest):
    if reqest.method == 'GET':
        try:
            X_axis = [None] * int(reqest.GET.get('X'))
            Y_axis = [None] * int(reqest.GET.get('Y'))
            axis_flag = True
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

def shape_generator(shape_form:str):
    if not shape_form:
        return None
    

    if shape_form == 'F':
        arr:list = [
            [0,0,0,0,0],
            [0,0,1,1,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
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
    
    if shape_form == 'N':
        for index in range(4):
            arr[3][1 + index] = 1
        arr[2][3] = 1
        arr[2][4] = 1
        return arr
    
    if shape_form == 'P':
        for index in range(4):
            arr[2][2 + index] = 1
        arr[3][2] = 1
        arr[3][3] = 1

    if shape_form == 'P':
        arr

    

def shape(reqest):
    if reqest.method == 'GET':
        try:
            arr = shape_generator(str(reqest.GET.get('option')))
            axis_flag = True
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
        
    return render(reqest,'grid.html', context=context)