
class vec3:

    def __init__(self,v):
        self.x=v[0]
        self.y=v[1]
        self.z=v[2]


    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return(x,y,z)
    
v1=vec3((0,1,0))
v2=vec3((0.5,2,3))

vr=v1+v2

print(vr)
