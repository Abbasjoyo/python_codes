class Car:
    brand=""
    color=""
    speed=""

    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=int(speed)

    def describe(self):
        print("Brand!",self.brand,"Color!",self.color,"|","Top Speed""Km/Hr","speed_category",self.speed,self.speed_category())
        
    def speed_category(self):
        if self.speed>140:
            return "FAST"

        else:
            return "NORMAL"
    
Car1=Car("Toyata","Red",130)
Car1.describe()
Car2=Car("Honda","Black",210)
Car2.describe()
