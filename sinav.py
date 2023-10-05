x = 5

while (x != 2):
    print(x)
    x = x-1


x = "Go"

if (x == "Go"):
    print('Go')
else:
    print('Stop')

print('Mike')




class Points(object): 
    def __init__(self,x,y): 

        self.x=x 
        self.y=y 

    def print_point(self): 
        print('x=',self.x,' y=',self.y) 

p1=Points("A","B") 
p1.print_point()


class Points(object): 
    def __init__(self,x,y): 

        self.x=x 
        self.y=y 

    def print_point(self): 
        print('x=',self.x,' y=',self.y) 
p2=Points(1,2) 
p2.x=2 

p2.print_point()