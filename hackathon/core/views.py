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
    

    if shape_form == 'F':
        arr = [
            [0,0,0,0,0],
            [0,0,1,1,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return arr

    if shape_form == 'I':
        arr = [
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
            ]
       
        return arr
    
    if shape_form == 'L':
        arr = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,1,0]
            ]
        return arr
    
    if shape_form == 'N':
        arr = [
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,0,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
            ]
        return arr
    
    if shape_form == 'P':
        arr = [
            [0,0,0,0,0],
            [0,0,1,1,0],
            [0,0,1,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return arr

    if shape_form == 'T':
<<<<<<< HEAD
        arr
=======
        arr = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return arr
>>>>>>> c83931bf4834bd5965fc4cd389ae3c0d0dd674cc

    

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