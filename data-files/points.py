import time
from tracemalloc import get_traced_memory,start,stop


#creating list
def make_list(line):
    cleaned_line=line.strip()
    new_lines=cleaned_line.split()
    parts=[float(part)for part in new_lines]
    return parts

#creating tuple
def make_tuple(line):
    cleaned_line=line.strip()
    new_line=cleaned_line.split()
    parts=[float(parts) for part in new_line]
   
#creating dictionary
def make_dict(line):
    cleaned_line=line.strip()
    parts=cleaned_line.split() 
    return {"x":float(parts[0]),"y":float(parts[1]),"z":float(float(parts[2]))}


class Points: 
    def __init__(self,x,y,z) -> None:
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

def make_instance(line):
    cleaned_line=line.strip()
    parts=cleaned_line.split()
    return Points(parts[0],parts[1],parts[2])


data=[]
def measure_memory(func):
    def wrapper(*args,**kwargs):
        start()
        result=func(*args,**kwargs)
        print(f"memory usage : {get_traced_memory()}")
        stop()
        return result
    return wrapper

@measure_memory
def read_text():
    with open("data-files/points.txt","r") as lines:
         for line in lines:
            data.append(make_instance(line))
    return data         
              
               

d=read_text()





#minimum of x axis y axis z axis
def minimum():
    # x_mini=min([item[0] for item in data])
    # y_mini=min([item[1] for item in data])
    # z_mini=min([item[2] for item in data])

    #dictionary we canot use index we should distionsty loock up 
    # for class using . operator

    x_mini=min([item.x for item in data])
    y_mini=min([item.y for item in data])
    z_mini=min([item.z for item in data])
    return (x_mini,y_mini,z_mini)

#maximum of x axis y axis z max
# def maximum():
#     x_max=max([item[0] for item in data])
#     y_max=max([item[1] for item in data])
#     z_max=max([item[2] for item in data])
#     return (x_max,y_max,z_max)
# #avarage of  x axis y axis z axis
# def  avarage():
#     x_avg=sum([item[0] for item in data])/len(data)
#     y_avg=sum([item[1] for item in data])/len(data)
#     z_avg=sum([item[2] for item in data])/len(data)
    # return (x_avg,y_avg,z_avg)

print(minimum())
# print(maximum())
# print(avarage())


