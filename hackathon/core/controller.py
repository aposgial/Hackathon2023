from hackathon.mixins import ReversableList

class Controller():
    def __init__(self) -> None:
        pass

    def shape_generator(self, shape_form:str):
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
        
    def shape_rotatior(self, shape):
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
    
    def empty_space_counter(array) -> int:
        if not array:
            return None
        
        count:int = 0
        for i in array:
            for j in i:
                if j == 0:
                    count +=1
        return count