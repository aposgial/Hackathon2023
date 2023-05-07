from django.shortcuts import render
from hackathon.mixins import ReversableList
from .forms import CHOICES

# Create your views here.
context = {}
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
        return {"arr":arr,
                "photo":"BLUE.png"}
    
    if shape_form == 'F90':
        arr = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,1,1,0],
            [0,0,0,1,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"BLUE.png"}

    if shape_form == 'I':
        arr = [
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
            ]
       
        return {"arr":arr,
                "photo":"RED.png"}
    
    if shape_form == 'L':
        arr = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,1,0]
            ]
        return {"arr":arr,
                "photo":"YELLOW.png"}
    
    if shape_form == 'N':
        arr = [
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,0,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
            ]
        return {"arr":arr,
                "photo":"PING.png"}
    
    if shape_form == 'P':
        arr = [
            [0,0,0,0,0],
            [0,0,1,1,0],
            [0,0,1,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"LIGHTBLUE.png"}

    if shape_form == 'T':
        arr = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"LIGHTGRAY.png"}

    if shape_form == 'U':
        arr = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"GREEN.png"}
    
    if shape_form == 'V':
        arr = [
            [0,0,0,0,0],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"ORANGE.png"}
    
    if shape_form == 'W':
        arr = [
            [0,0,0,0,0],
            [0,1,0,0,0],
            [0,1,1,0,0],
            [0,0,1,1,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"LIGHTGRAY.png"}
    
    if shape_form == 'X':
        arr = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"BLUE.png"}
    
    if shape_form == 'Y':
        arr = [
            [0,0,1,0,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"PING2.png"}
    
    if shape_form == 'Z':
        arr = [
            [0,0,0,0,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,1,1,0],
            [0,0,0,0,0]
            ]
        return {"arr":arr,
                "photo":"RED2.png"}

def shape_rotatior(shape):
    if not shape:
        return None

    rotated = []
    for array in shape:
        if 1 in array:
            reversible = ReversableList(array)
            rotated.append(reversible.reverse())
        else:
            rotated.append(array)
    return rotated



def rotate(request):
    form = CHOICES(request.POST)
    data = request.POST
    print(data['NUMS'])
    data1 = shape_generator(str(data['NUMS']))
    data2 = shape_rotatior(data1['arr'])
    
    print(data1['arr'])
    print(data2)
    return render(request,'rotates.html', {'form':form})

def shape(reqest):
    if reqest.method == 'GET':
        try:
            arr_info = shape_generator(str(reqest.GET.get('option')))
            axis_flag = True
            message = 'ok'
        except (TypeError, ArithmeticError):
            axis_flag = False
            message = 'input error'
        except Exception:
            message = 'wasted'
        
        context:dict = {'arr_info': arr_info,
                        'axis_flag': axis_flag,
                        'message': message
                        }

        
    return render(reqest,'shapes.html', context=context)

