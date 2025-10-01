''' 
This is my own work as defined by the SAIBT Academic Integrity Policy. 
I am fully aware of the consequences of academic misconduct as defined 
by the SAIBT Academic Integrity Policy. 
SAIBT ID: 50587
Name:  Kazuya Nakayama
Date: 11/05/2025
''' 
import random
import abc

class Treasure: 
    ''' 
    A class to represent the Treasure items that will be stored in a TreasureContainer. 
    '''
    __possible_names = ["Vase", "Chair", "Ship","Pen","Stethoscope","Duck","Egg","Butterfly","Chrysalis","Caterpilar","Shelf","Boat", "Hammer","Screw","Book"]

    def __init__(self,name=None ,value=None): 
        '''
        Construct a Treasure name of treasure and value
        '''
        if name is None:
            self.__name= self.get_random_name()
        else:
            self.__name = name
        if value is None:
            self.__value= self.get_random_value()
        else:
            self.__value = value

    @classmethod
    def get_random_name(cls):
        '''Get name from the list'''
        return random.choice(cls.__possible_names)        
    
    def get_name(self):
        '''Return name'''
        return self.__name
    
    def get_random_value(self):
        '''set value as random'''
        
        return random.randint(10,1000)

    def get_value(self):
        '''Get value'''
        return self.__value
    
    def __lt__(self,other):
        '''To compare the value'''
        if isinstance(other, Treasure):
            return self.__value < other.__value
        return NotImplemented
    
    def __str__(self):
        '''Return string of the Treasure'''
        return f"{self.get_name()} worth {self.get_value()} gold"

    def __repr__(self):
        '''Return condition of objects'''
        return f"Treasure(name={self.get_name()},value={self.get_value()})"

class TreasureContainer:
    '''The class to represent the treasure container'''
    def __init__(self):
        '''Contain treasure'''
        self.__treasure = []
        

    def have_treasure(self,treasure=Treasure):
        '''Append treasure to the list and set the max number by using self maximum number of treasures'''
        if not isinstance(treasure,Treasure):
            raise TypeError(f"Error: Invalid argument for treasure: {repr(treasure)}")
        else:    
            self.__treasure.append(treasure)
    
    def get_treasure_value(self):
        '''Get treasure value'''
        total=0
        for treasure in self.__treasure: 
            value = treasure.get_value()
            total += value
        return f"{total}"
    
    def destroy(self):
        '''Destroy it self'''
        pass
    
    def get_treasures(self):
        '''Get treasures'''
        return self.__treasure
    
    def __str__(self):
        '''Return string of TreasureContainer'''
        return f"TreasureContainer:{self.get_treasures()}"
    
    def __repr__(self):
        '''Return conditions of TreasureContainer'''
        return f"TreasureContainer(treasure={self.get_treasures()})"
  
class GameEntity(TreasureContainer):

    '''A class to represent the showing the positon and store treasure that will be inheritanced in Pirate and Ship.'''
    def __init__(self, health,x, y):
        '''Construct health, x,y'''

        self.__x=x
        self.__y=y
        self.__health = health
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
        elif not 0 <= x <= 20 or not 0 <= y <= 50:
            print(f"Can not move out of 0 to 20: {self.get_position_x()},{self.get_position_y()}")
        else:
            self.__x = x
            self.__y = y
    
    def have_treasure(self,treasure):
        '''Append treasure to the list and set the max number by using self maximum number of treasures'''
        if not isinstance(treasure,Treasure):
            raise Exception("Error: Invalid argument for treasure:",repr(treasure))
        elif len(self.__treasure) >= self.__maximum_number_of_teasures:
            print(f"Alredy have {self.__maximum_number_of_teasures} (MAX:{self.__maximum_number_of_teasures})")
        else:    
             self.__treasure.append(treasure)

    def change_maximum_number(self,number):
        '''To change the number'''
        self.__maximum_number_of_teasures=number

    def get_maximum_number(self):
        '''Get maximum number'''
        return self.__maximum_number_of_teasures
        
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
    
    def get_health(self):
        '''Get health'''
        return self.__health
     

    def keep_most_valuable(self):
        '''FInd max value in the treasure'''
        if not self.__treasure:
            return None
        most_value = max(self.__treasure)
        self.__treasure = [most_value]
        return most_value

    
    def __str__(self):
        '''Return string of the position'''
        return f"Name:{self.get_health()} Position: {self.get_position_x()} , {self.get_position_y()} "
    
    def __repr__(self):
        '''Return condition of objects'''
        return f"Actor(name={self.get_health()},x={(self.get_position_x())},y={self.get_position_y()}"


    

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
            raise TypeError("Error: Invalid argument for cannon:",repr(ball))
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
  

class Pirate(GameEntity):
    '''A class to represent the pirate name and stored Treasure and inheritanced method.'''
    def __init__(self, name,x,y,health=50, map_instance=None):
        '''Inheritance x,y and helath, stored treasure '''
        super().__init__(x,y,health)
        self.__ship=None
        self.change_maximum_number(5)
        self.set_name(name)
        self.__map = map_instance

    def set_ship(self,ship):
        '''Ride Ship and check whether Ship object, else, ship =ship and set same location'''
        if not isinstance(ship,Ship):
            print("Error: Invalid argument for set_ship:",repr(ship))
        else:
            self.__ship = ship
            super().set_position(self.__ship.get_position_x(), self.__ship.get_position_y())
     
    def set_name(self,name):
        '''Set name and validate whether str or empthy'''
        if type(name) != str or len(name) == 0:
            print("Error: Invalid argument for name:",repr(name))
        else:
            self.__name = name
    
    def get_name(self):
        '''Get name'''
        return self.__name
            
   
    def get_ship(self):
        '''Check whether Pirate on the Ship'''
        return self.__ship
    
    def get_off_ship(self):
        '''Get off ship turn into None'''
        self.__ship = None

    def move(self, dx, dy):
        '''if Pairate on the Ship,Pirate and Ship turn into  same location, else only move Pirate'''
        old_x = self.get_position_x()
        old_y= self.get_position_y()
        new_x = old_x + dx
        new_y = old_y + dy

        if self.__ship:
            super().set_position(self.__ship.get_position_x()+ dx, self.__ship.get_position_y()+ dy)
            self.__ship.move(dx,dy)
            # remove self from self.tile and add self to next_tile
            self.update_tile(old_x,old_y, new_x,new_y)
        

        else:
            super().move(dx, dy)
            # remove self from self.tile and add self to next_tile  
            self.update_tile(old_x,old_y, new_x, new_y)
    
    def update_tile(self,old_x,old_y,new_x,new_y):
        if self.__map:
            # Update Pirate's tile
            if 0 <= old_x < len(self.__map.tiles[0]) and 0 <= old_y < len(self.__map.tiles):
                self.__map.get_tile_at(old_x, old_y).set_pirate(False)
                if self.__ship and self.__map.get_tile_at(old_x, old_y) == self.__map.get_tile_at(self.__ship.get_position_x(), self.__ship.get_position_y()):
                    self.__map.get_tile_at(old_x, old_y).set_ship(False) 

            if 0 <= new_x < len(self.__map.tiles[0]) and 0 <= new_y < len(self.__map.tiles):
                self.__map.get_tile_at(new_x, new_y).set_pirate(True)
                if self.__ship and self.__map.get_tile_at(new_x, new_y) == self.__map.get_tile_at(self.__ship.get_position_x(), self.__ship.get_position_y()):
                    self.__map.get_tile_at(new_x, new_y).set_ship(True) 
        else:
            raise Exception("Error: Map instance not set for Pirate.")

            
        
    
    def dig(self):
        '''To get treasure from the Land tile'''
        pass
    

class Ship_move_exception(Exception):
    '''Class to represent the exception when shiip move out of range'''
    def __init__(self):
        '''Construct message when it happen'''
        super(). __init__("Can not move out of tile")


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
            raise Exception("Error: Invalid argument for cannon:",repr(ball))
        elif len(self.__barrel) >= 1:
            print(f"The barrrel is full: {self.__barrel} (MAX 1)")
        else:
            self.__barrel.append(ball)
                    
    def show_barrel(self):
        '''Show the barrel'''
        return self.__barrel
        
    
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



class Ship(GameEntity):
    '''Class to represent Ship that is inheritanced MoveableObject.'''
    def __init__(self,x,y,health=200):
        '''Constract shipName, treasureList for store, constitute Cannon Object and inheritance x,y from Actor class so that it can store Treasure object'''
        super().__init__(x,y,health)
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


class EnemyShip(Ship):
    '''The class to represent enemy ship that might fight with ship'''
    def __init__(self,x,y,health=200):
        '''Construct x,y,health'''
        super().__init__(x, y, health)
        self.change_maximum_number = 5
    
    def update(self):
        '''Update'''
        pass

    

class Tile(abc.ABC):
    '''An abstract class representing a tile on a map'''
    def __init__(self):
        '''Can contain a TreasureContainer'''
        self.__contains= None
        self.__has_ship= False
        self.__has_enemy= False
        self.__has_pirate =False
        self.__has_treasure = False
        

    def add(self, treasure_container=TreasureContainer):
        '''Add on objet to yhe tile'''
        if isinstance(treasure_container, TreasureContainer):
            self.__contains = treasure_container
        else:
            raise Exception("Error: Must use TreasureContainer odject")
    
    def get_contain_item(self):
        '''get the item'''
        return self.__contains
    
    def has_ship(self):
        '''Get ship'''
        return self.__has_ship
    
    def set_ship(self,val):
        '''Set ship as boolean'''
        self.__has_ship = bool(val)

    def has_enemy(self):
        '''Get enemy ship'''
        return self.__has_enemy

    def set_enemy(self,val):
        '''Set enemy ship'''
        self.__has_enemy = bool(val)

    def has_pirate(self):
        '''Get pirate'''
        return self.__has_pirate
    
    def set_pirate(self, val):
        '''Set pirate'''
        self.__has_pirate = bool(val)

    def has_treasure(self):
        '''Get treasure'''
        return self.__has_treasure
    
    def set_has_treasure(self, val):
        '''Set treasure'''
        self.__has_treasure = bool(val)
    
    @abc.abstractmethod
    def __str__(self):
        '''This method will implement to WaterTile and LandTile'''
        pass

    def __repr__(self):
        '''Return the condition of tile'''
        return f"contains={repr(self.get_contain_item())}"
    
class WaterTile(Tile):
    '''To represent water tile'''
    def __str__(self):
        '''If ship on the water tile return U, enemy return u else empty'''
        if self.has_ship(): 
           return "U"
        
        elif self.has_enemy():
           return "u"
        
        else:
            return ""
    def __repr__(self):
        '''Return the condition of tile'''
        return f"contains={repr(self)}"

class LandTile(Tile):
    '''to repreent land tile'''
    def __str__(self):
        '''If pirate and treasure on the land tile return X, pirate return o, else +'''
        if self.has_pirate() and self.has_treasure():
            return "X"
        elif self.has_pirate():
            return "o"
        else:
            return "+"
        
    def __repr__(self):
        '''Return the condition of tile'''
        return f"contains={repr(self)}"


class Map:
    '''Class to represent Map that is construct Tile,Pirate,Ship,EnemyShip.'''
    def __init__(self, map_file="map.txt"):
        '''Construct player, ship,enemy ship, read_map, game_object'''
        self.tiles = []
        self.__player = None
        self.__player_ship = None
        self.__enemy_ships= []
        self.__read_map(map_file)
        self.__create_game_objects()

    def __read_map(self, map_file):
        '''Read the file and create the tile grid.'''
        try:
            with open(map_file, "r") as f:
                for i, line in enumerate(f):
                    tile_row = []
                    for j, word in enumerate(line.strip()):
                        if word == "~":
                            tile_row.append(WaterTile())
                        elif word == "+":
                            tile_row.append(LandTile())
                        else:
                            raise ValueError(f"Invalid character ")
                    self.tiles.append(tile_row)
        except FileNotFoundError:
            print(f"Error: Map file '{map_file}' not found. Creating an empty map.")
            self.tiles = [[]]

    def __create_game_objects(self):
        '''Create initial game objects on the map.'''
        start_x, start_y = 0, 0
        self.__player = Pirate("Kazuya_Namakayama", start_x, start_y, map_instance=self)
        self.__player_ship = Ship( start_x, start_y)
        self.__player.set_ship(self.__player_ship)
        self.get_tile_at(start_x, start_y).set_ship(True)
        self.get_tile_at(start_x,start_y).set_pirate(True)
        self.__player_ship.set_position(start_x, start_y)
        

        num_enemy_ships = random.randint(2,5)
        for _ in range(num_enemy_ships):
            enemy_x,enemy_y = random.randint(0, len(self.tiles) -1), random.randint(0,len(self.tiles[0])-1)
            while not isinstance(self.get_tile_at(enemy_x,enemy_y),WaterTile) or self.get_tile_at(enemy_x, enemy_y).has_enemy():
                enemy_x, enemy_y = random.randint(0,len(self.tiles) -1), random.randint(0,len(self.tiles[0])-1)
            enemy_ship = EnemyShip(enemy_x, enemy_y)
            self.__enemy_ships.append(enemy_ship)
            self.get_tile_at(enemy_x, enemy_y).set_enemy(True)
            enemy_ship.set_position(enemy_x,enemy_y)
           

        num_treasure_containers = random.randint(3,7)
        for _ in range(num_treasure_containers):
            treasure_x, treasure_y = random.randint(0, len(self.tiles) -1),random.randint(0,len(self.tiles[0])-1)
            while not isinstance(self.get_tile_at(treasure_x, treasure_y), LandTile) or self.get_tile_at(treasure_x,treasure_y).get_contain_item() is not None:
                treasure_x, treasure_y = random.randint(0, len(self.tiles) -1), random.randint(0, len(self.tiles[0]) -1)
            treasure_container = TreasureContainer() 
            self.get_tile_at(treasure_x, treasure_y).add(treasure_container)
              

    def get_player(self):
        '''Get player'''
        return self.__player

    def get_ship(self):
        '''Get player ship'''
        return self.__player_ship
    
    def get_enemy_ships(self):
        '''Get enemy ship'''
        return self.__enemy_ships
    

    def get_tile_at(self, x, y):
        '''Get the tile at the specified coordinates.'''
        if 0 <= x < len(self.tiles) and 0 <= y < len(self.tiles[x]):
            return self.tiles[x][y]
        else:
            raise Exception(f"Error: Accessing tile at invalid cordinates (x={x}, y={y})")
            

    def display_tiles(self):
        '''Display the visual representation of the tiles in the map.'''
        for row in self.tiles:
            print(" ".join(str(tile) for tile in row))

    def update_game_entities(self):
        '''Update game entities pirate ship, enemy ship'''
        pass

    def move_player(self, dx, dy):
        if self.__player:
            new_x = self.__player.get_position_x() + dx
            new_y = self.__player.get_position_y() + dy
            if 0 <= new_x < len(self.tiles[0]) and 0 <= new_y < len(self.tiles):
                self.__player.move(dx, dy)
            else:
                print("Cannot move off the map.")

    def __str__(self):
        '''Return Map'''
        return f"{self}"

    def __repr__(self):
        '''Return condition of Map'''
        return f"contains={repr(self)}"

# map=Map()
# map.display_tiles()

#for x in range(7):
#    for y in range (11):
#        print(map.get_tile_at(x, y), x, y)
#    print()

    
def main():
   map = Map()

   choice = None
   while choice != "quit":
       if choice == "w":
           map.get_player().move(0,-1)
       elif choice == "a":
           map.get_player().move(-1,0)
       elif choice == "s":
           map.get_player().move(0,1)
       elif choice == "d":
           map.get_player().move(1,0)
       elif choice == "dig":
           map.get_player().dig()
       map.display_tiles()
       choice = input("Enter w,a,s,d,dig,or quit: ")
    #    map.uodate_game_entities()
    
   player = map.get_player()
   ship = map.get_player_ship()
   player.display_treasures()
   ship.display_treasures()

   print("You collected",ship.get_treasure_value() + player.get_treasure_value(), "gold")
   print("Goodbye") 



if __name__ == "__main__":
   main()


















    
        

    





     