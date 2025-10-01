''' 
This is my own work as defined by the SAIBT Academic Integrity Policy. 
I am fully aware of the consequences of academic misconduct as defined 
by the SAIBT Academic Integrity Policy. 
SAIBT ID: 50587
Name:  Kazuya Nakayama
Date: 02/04/2025
''' 


class Treasure: 
    ''' 
    A class to represent the Treasure items that will be stored in a Ship or Pirate. 
    '''

    def __init__(self, name, value): 
        '''
        Construct a Treasure set_name and value
        '''
        self.set_name(name)
        self.set_value(value)
    
    def set_name(self,name):
        '''Set name and validate whether str or empthy'''
        if type(name) != str or len(name) == 0:
            print("Error: Invalid argument for name:",repr(name))
        else:
            self.__name = name
    
    def get_name(self):
        '''Return name'''
        return self.__name
    
    def set_value(self, value):
        '''set value'''
        if type(value) != int or type(value) == "":
            print("Error: Invalid argument for value:",repr(value))
        else:
            self.__value = value

    def get_value(self):
        '''Get value'''
        return self.__value
    
    def __str__(self):
        '''Return string of the Treasure'''
        return f"{self.get_name()} worth {self.get_value()} gold"

    def __repr__(self):
        '''Return condition of objects'''
        return f"Treasure(name={self.get_name()},value={self.get_value()})"
  

  
class Actor:

    '''A class to represent the showing the positon and store treasure that will be inheritanced in Pirate and Ship.'''
    def __init__(self, name,x, y):
        '''Construct x,y'''
        self.__x=x
        self.__y=y
        self.set_name(name)
        self.__treasure=[]
        self.__maximum_number_of_teasures=1

    def move(self, dx, dy):
        '''To move of position from x and y'''
        if type(dx) != int and type(dy) != int:
            print("Error: Must be number:",repr(dx) ,repr(dy))
        else:    
            new_x = self.__x + dx
            new_y = self.__y + dy
            self.set_position(new_x, new_y)
                      
    
    def set_position(self,x,y):
        '''Set a position'''
        if type(x) != int and type(y) != int:
            print("Error: Must be number:", repr(x),repr(y))
        elif not 0 <= x <= 20 or not 0 <= y <= 20:
            print(f"Can not move out of 0 to 20: {self.get_position_x()},{self.get_position_y()}")
        else:
            self.__x = x
            self.__y = y
    
    def have_treasure(self,treasure):
        '''Append treasure to the list and set the max number by using self maximum number of treasures'''
        if not isinstance(treasure,Treasure):
            print("Error: Invalid argument for treasure:",repr(treasure))
        elif len(self.__treasure) >= self.__maximum_number_of_teasures:
            print(f"The {self.__name} alredy have {self.__maximum_number_of_teasures} (MAX:{self.__maximum_number_of_teasures})")
        else:    
             self.__treasure.append(treasure)

    def change_maximum_number(self,number):
        '''To change the number'''
        self.__maximum_number_of_teasures=number

    def get_maximum_number(self):
        '''Get maximum number'''
        return self.__maximum_number_of_teasures
    
    def get_treasure_value(self):
        '''Get treasure value'''
        total=0
        for treasure in self.__treasure: 
            value = treasure.get_value()
            total += value
        return f"{total}"
        
    def get_treasure_list(self):
        '''Get treasure list of Pirate'''
        print(self.__treasure)

    def reset_treasure_list(self):
        '''Reset_treasure'''
        self.__treasure=[]
        print (f"The {self.__name} do not have treasure")

    def get_position_x(self):
        '''Get position x'''
        return self.__x
    
    def get_position_y(self):
        '''Get position y'''
        return self.__y
    
    def set_name(self,name):
        '''Set name and validate whether str or empthy'''
        if type(name) != str or len(name) == 0:
            print("Error: Invalid argument for name:",repr(name))
        else:
            self.__name = name
    
    def get_name(self):
        '''Get name'''
        return self.__name

    
    def __str__(self):
        '''Return string of the position'''
        return f"Name:{self.get_name()} Position: {self.get_position_x()} , {self.get_position_y()} "
    
    def __repr__(self):
        '''Return condition of objects'''
        return f"Actor(name={self.get_name()},x={(self.get_position_x())},y={self.get_position_y()}"


    

class CannonBall:
    '''Class to represent the cannonball that will set the damage of ball to Cannon on the Ship.'''
    def __init__(self,damage):
        '''Initialized and set damage and number of ball'''
        self.set_damage(damage)
    
    def set_damage(self,damage):
        '''Set damage and Check data type of damage'''
        if type(damage) != float and type(damage) != int:
            print("Error: Enter int or float:",repr(damage))
        else:
            self.__damage=float(damage)
    
    def get_damage(self):
        '''To show damage'''
        return self.__damage 
                  
    def __str__(self):
        '''Return string of the CannonBall'''
        return f"The CannonBall damage is :{self.get_damage()}"
    def __repr__(self):
        '''Rreturn the condition of CannonBall'''
        return f"CannnonBall(damage={self.get_damage()})"


class Cannon:
    '''Class to represent the Cannon that will show damage of cannonball and is constituted in Ship class.'''
    def __init__(self):
        '''list for cannonball'''
        self.__barrel=[]

    def set_cannon(self,ball):
        '''Check whether Cannonball object and error if barrel is max after that, append to list'''
        if not isinstance(ball,CannonBall):
            print("Error: Invalid argument for cannon:",repr(ball))
        elif len(self.__barrel) >= 1:
            print(f"The barrrel is full: {self.__barrel} (MAX 1)")
        else:
            self.__barrel.append(ball)
                    
    def get_cannon(self):
        '''Show the barrel'''
        print( f"In the barrel: {self.__barrel}")
    
    def _fire(self):
        '''Return the damage of cannonball and delete the cannonball,  if there is no cannonball, return 0'''
        if self.__barrel == []:
            return 0
        else:
            fire = 0
            for damage in self.__barrel:
                result = damage.get_damage()
                fire += result
            self.__barrel=[]
            return fire
                  
    def __str__(self):
        '''Return string of the Cannon'''
        return f"The Cannon reloaded :{self.__barrel}"
    
    def __repr__(self):
        '''Return the condition of Cannon'''
        return f"Cannon({self.__barrel})"
  

class Pirate(Actor):
    '''A class to represent the pirate name and stored Treasure and inheritanced method.'''
    def __init__(self, name,x,y):
        '''Inheritance x,y and set_name, stored treasure '''
        super().__init__(name,x,y)
        self.__ship=None
        self.change_maximum_number(5)

    def set_ship(self,ship):
        '''Ride Ship and check whether Ship object, else, ship =ship and set same location'''
        if not isinstance(ship,Ship):
            print("Error: Invalid argument for set_ship:",repr(ship))
        else:
            self.__ship = ship
            super().set_position(self.__ship.get_position_x(), self.__ship.get_position_y())
            
   
    def get_ship(self):
        '''Check whether Pirate on the Ship'''
        return self.__ship
    
    def get_off_ship(self):
        '''Get off ship turn into None'''
        self.__ship = None

    def move(self, dx, dy):
        '''if Pairate on the Ship,Pirate and Ship turn into  same location, else only move Pirate'''
        if self.__ship:
            super().set_position(self.__ship.get_position_x()+ dx, self.__ship.get_position_y()+ dy)
            self.__ship.move(dx,dy)
        else:
            super().move(dx, dy)
     
    

class CannonBall:
    '''Class to represent the cannonball that will set the damage of ball to Cannon on the Ship.'''
    def __init__(self,damage):
        '''Initialized and set damage and number of ball'''
        self.set_damage(damage)
    
    def set_damage(self,damage):
        '''Set damage and Check data type of damage'''
        if type(damage) != float and type(damage) != int:
            print("Error: Enter int or float:",repr(damage))
        else:
            self.__damage=float(damage)
    
    def get_damage(self):
        '''To show damage'''
        return self.__damage 
                  
    def __str__(self):
        '''Return string of the CannonBall'''
        return f"The CannonBall damage is :{self.get_damage()}"
    def __repr__(self):
        '''Rreturn the condition of CannonBall'''
        return f"CannnonBall(damage={self.get_damage()})"


class Cannon:
    '''Class to represent the Cannon that will show damage of cannonball and is constituted in Ship class.'''
    def __init__(self):
        '''list for cannonball'''
        self.__barrel=[]

    def set_cannon(self,ball):
        '''Check whether Cannonball object and error if barrel is max after that, append to list'''
        if not isinstance(ball,CannonBall):
            print("Error: Invalid argument for cannon:",repr(ball))
        elif len(self.__barrel) >= 1:
            print(f"The barrrel is full: {self.__barrel} (MAX 1)")
        else:
            self.__barrel.append(ball)
                    
    def show_barrel(self):
        '''Show the barrel'''
        print( f"In the barrel: {self.__barrel}")
        
    
    def _fire(self):
        '''Return the damage of cannonball and delete the cannonball,  if there is no cannonball, return 0'''
        if self.__barrel == []:
            return 0
        else:
            fire = 0
            for damage in self.__barrel:
                result = damage.get_damage()
                fire += result
            self.__barrel=[]
            return fire
                  
    def __str__(self):
        '''Return string of the Cannon'''
        return f"The Cannon reloaded :{self.__barrel}"
    
    def __repr__(self):
        '''Return the condition of Cannon'''
        return f"Cannon({self.__barrel})"



class Ship(Actor):
    '''Class to represent Ship that is inheritanced MoveableObject.'''
    def __init__(self,name,x,y):
        '''Constract shipName, treasureList for store, constitute Cannon Object and inheritance x,y from Actor class so that it can store Treasure object'''
        super().__init__(name,x,y)
        self.__cannon=Cannon()
        self.__barrel=[]
        self.__damage = 0.0
        self.change_maximum_number(20)
    
    def fire_cannon(self):
        '''Return damage of cannonball, if there is no cannonball return 0'''
        return self.__cannon._fire()

    def reload_cannon(self,cannonball):
        '''Reload cannonball to the cannon'''
        self.__cannon.set_cannon(cannonball)
    
    def create_cannon_ball(self,damage):
        '''Create cannonball'''
        cannonball = CannonBall(damage)
        return cannonball
        
    

    
def main():
    #Test for MoveableObject#
    print("Test Actor")
    a =Actor("actor",0,0)
    print(a)
    a.move("a","b")
    print(a.get_position_x())
    print(a.get_position_y())
    a.set_position(-1,0)
    print(a.get_position_x())
    print(a.get_position_y())
    a.set_position("","")
    a.set_position(21,0)
    a.set_position(0,-1)
    a.set_position(0,21)
    a.move(-1,0)
    a.move(21,0)
    a.move(0,-1)
    a.move(0,21)
    a.move("","")
    a.move(5,5)
    print(a.get_position_x())
    print(a.get_position_y())
    book = Treasure("bbok", 1)
    a.have_treasure(book)
    duck = Treasure("Duck", 1)
    a.have_treasure(duck)
    a.get_treasure_value()
    a.reset_treasure_list()
    mlist=[a]
    print(a)
    print("Finish test Actor")
    print("")

    print("Test Treasure")     
    treasure = Treasure("book", 3)
    print(treasure.get_name()) 
    treasure.set_name("")
    treasure.set_name(1)
    treasure.set_name("hammer")
    print(treasure.get_name())
    treasure.set_name(None)
    print(treasure.get_name())

    print(treasure.get_value()) 
    treasure.set_value("hammer")
    treasure.set_value("")
    treasure.set_value(1)
    print(treasure.get_value())
    treasure.set_value("")
    print(treasure.get_value())
    treasure.set_value(None)
    print(treasure.get_value())

    print(treasure)

    alist=[treasure]
    print(alist)
    print("Finish test Treasure")
    print("")


    print("Test Pirate")    
    k=Pirate("Kazuya", 0,0)
    print(k)   
    print(k.get_name()) 
    k.set_name("")
    k.set_name("KazuyaNakayama")
    print(k.get_name())
    k.set_name(1)
    print(k.get_name())
    k.set_name(None)
    print(k.get_name())
    print(k)

    k.have_treasure(treasure)
    k.get_treasure_list()
    vase = Treasure("vase", 100)
    k.have_treasure(2)
    k.have_treasure(vase)
    k.get_treasure_list()
    k.get_treasure_value()
    print(f"Treasure value is: {k.get_treasure_value()}")

    desk=Treasure("Desk",10)
    chair=Treasure("chair",15)
    shelf=Treasure("shelf",50)
    ship=Treasure("Ship",3000)
    k.have_treasure(desk)
    k.have_treasure(chair)
    k.have_treasure(shelf)
    k.have_treasure(ship)
    k.get_treasure_list()
    total=k.get_treasure_value()
    print(total)
    print(f"Treasure value is: {total}")
    k.reset_treasure_list()
    k.get_treasure_list()
    print("Finish Test pirate")
    print("")

    print("Test Cannon ball")
    cannonball=CannonBall("")
    cannonball=CannonBall("fadsa")
    cannonball=CannonBall(None)
    cannonball=CannonBall(15.0)

    print(cannonball)
    clist=[cannonball]
    print(clist)
    cannonball.set_damage("")
    cannonball.set_damage("asda")
    cannonball.set_damage(None)
    cannonball.set_damage(10)
    print(cannonball.get_damage())
    print(cannonball)
    print("Finish Cannon ball")

    print("")

    print("Test Cannon")
    cannon=Cannon()
    print(cannon)
    cannon.set_cannon(cannonball)
    cannon.set_cannon(cannonball)
    print(cannon)
    cannon.show_barrel()
    cannon.set_cannon("")
    cannon.set_cannon(2)
    print(cannon._fire())
    print(cannon._fire())
    print("Finish test Cannon")
    print("")

    print("Test Ship")
    blackpearl = Ship("Going Merry",10,10)
    print(blackpearl)
    print(blackpearl.get_name())
    blackpearl.set_name("Black Pearl")
    print(blackpearl.get_name())
    blackpearl.set_name("")
    blackpearl.set_name(2)
    blackpearl.move(5,5)
    blackpearl.get_position_x()
    blackpearl.get_position_y()
    blackpearl.move("","")
    blackpearl.move("f","h")
    blackpearl.move(5,5)
    blackpearl.move(5,5)
    print(blackpearl)
    blackpearl.create_cannon_ball("")
    blackpearl.create_cannon_ball("ffsdfs")
    cannonball2 = blackpearl.create_cannon_ball(10)
    print(cannonball2)
    blackpearl.reload_cannon(cannonball2)
    blackpearl.reload_cannon(cannonball2)
    
    print(blackpearl.fire_cannon())
    print(blackpearl.fire_cannon())
    blackpearl.have_treasure(shelf)
    blackpearl.have_treasure(ship)
    blackpearl.have_treasure(chair)
    blackpearl.have_treasure(desk)
    blackpearl.have_treasure(treasure)
    print(blackpearl.get_treasure_value())
    print(blackpearl.get_treasure_list())
    blackpearl.have_treasure("")
    blackpearl.have_treasure(1)
    
    container=Treasure("Container", 100)
    blackpearl.have_treasure(container)
    rubberboat = Treasure("RubberBoat", 50)
    blackpearl.have_treasure(rubberboat)
    nail = Treasure("Nail", 5)
    blackpearl.have_treasure(nail)
    plier = Treasure("Plier",10)
    blackpearl.have_treasure(plier)
    vase= Treasure("Base", 20)
    blackpearl.have_treasure(vase)
    egg = Treasure("Egg", 5)
    blackpearl.have_treasure(egg)
    butterfly = Treasure("Butterfly", 10)
    blackpearl.have_treasure(butterfly)
    caterpillar = Treasure("Caterpillar", 5)
    blackpearl.have_treasure(caterpillar)
    snake = Treasure("Snake", 5)
    blackpearl.have_treasure(snake)
    brige = Treasure("Brige", 100)
    blackpearl.have_treasure(brige)
    duck= Treasure("BigDuck", 200)
    blackpearl.have_treasure(duck)
    boat = Treasure("Boat", 200)
    blackpearl.have_treasure(boat)
    miniduck = Treasure("MiniDuck", 100)
    blackpearl.have_treasure(miniduck)
    buliding= Treasure("Building", 50)
    blackpearl.have_treasure(buliding)
    motorboat = Treasure("MotorBoat", 10000)
    blackpearl.have_treasure(motorboat)
    crysalis = Treasure("Crysalis" ,10)
    blackpearl.have_treasure(crysalis)
    blackpearl.get_treasure_list()
    print(f"The treasure value is: {blackpearl.get_treasure_value()}")
    blackpearl.reset_treasure_list()
    print(f"The treasure value is: {blackpearl.get_treasure_value()}")
    print("Finish test ship")
    print("")

    print("Test move ship and pirate")
    ("")
    k.set_ship(1)
    k.set_ship("")
    k.set_ship(blackpearl)
    print(k.get_position_x())
    print(k.get_position_y())
    print(k)
    print(k.get_off_ship())
    print(k)
    k.set_ship(blackpearl)
    k.move(5,5)
    k.move(-10,-10)
    k.get_off_ship()
    print(k)
    print(blackpearl)
    print(k.get_off_ship())
    print(k)
    print(blackpearl)
    k.move(5,5)
    print(k.get_position_x())
    print(k.get_position_y())
    print(k)
    k.set_ship(blackpearl)
    k.move(5,5)
    print(k)
    print(blackpearl)
    k.get_off_ship()
    print(k)
    print(blackpearl)
    k.move(-1, 30)
    print(k)
    print(blackpearl)
    k.move(2,-30)
    k.move(-20,-20)
    k.set_ship(blackpearl)
    print(k.get_position_x())
    print(k.get_position_y())
    print(k)
    k.move(-15,-15)
    print(k.get_position_x())
    print(k.get_position_y())
    k.move(-1,0)
    k.move(0,-1)

    print("Finish all test")




if __name__ == "__main__":
    main()


















    
        

    





     