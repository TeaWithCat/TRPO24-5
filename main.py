import random

class ship:
    def __init__(self, size: int):
        self.d_cord = 0    # 0 ~ 99
        self.p_cord = 0    # 2^x + 2^y + .... + 2^z
        self.type = 0      # 0 - vertical, 1 - horizontal
        self.degree = []   # x, y, ... , z
        self.size = size   # 1 ~ 4
        
    def make_ship(self):
        self.type = random.randint(0, 1)
        
        if self.type == 0:
            self.d_cord = random.randint(0, 10 - self.size) * 10 + random.randint(0, 9)
            for i in range(0, self.size):
                self.p_cord += 2**(self.d_cord + i * 10)
                self.degree.append(self.d_cord + i * 10)
        else:
            self.d_cord = random.randint(0, 9) * 10 + random.randint(0, 10 - self.size)
            for i in range(0, self.size):
                self.p_cord += 2**(self.d_cord + i)
                self.degree.append(self.d_cord + i)
                
        return self  
    
    def update_ship(self, amount: int):
        if amount > 0:
            self.p_cord = self.p_cord << amount
        else:
            self.p_cord = self.p_cord >> -amount
            
        self.d_cord = self.d_cord + amount
        for i in range(0, len(self.degree)):
            self.degree[i] += amount

class math_battlefield:
    def __init__(self):
        self.math_import = 0                            # temporary field for creating ships
        self.math_field = sum(2**i for i in range(99)) # final field with ships
        self.ships = []                                # list of ships p_cord
        self.make_field()
    
    def place_ship(self, ship: ship):
        while (self.math_field & ship.p_cord) != ship.p_cord: 
            if ship.type == 0:
                if ship.p_cord >= 2**100:
                    ship.update_ship(-10 * (11 - ship.size))
                else:
                    ship.update_ship(1)
            elif ship.type == 1:
                if ship.degree[ship.size - 1] % 10 == 9:
                    ship.update_ship(ship.size)
                else:
                    ship.update_ship(1)
                    
                if ship.p_cord >= 2**100:
                    ship.update_ship(-10 * (11 - ship.size))
        
        self.make_waves(ship)
        self.math_import = self.math_import | ship.p_cord
        self.ships.append(ship.p_cord)
        
    def make_waves(self, ship: ship):
        waves = ship.p_cord
        if ship.degree[0] % 10 != 0:
            waves |= (ship.p_cord >> 1) | (ship.p_cord >> 11) # change +
        
        if ship.degree[ship.size - 1] % 10 != 9:
            waves |= (ship.p_cord << 1) | (ship.p_cord >> 9) # change -
        
        if ship.degree[ship.size - 1] < 90:
            waves |= (ship.p_cord << 10)
            if ship.degree[0] % 10 != 0:
                waves |= (ship.p_cord << 9)
            if ship.degree[ship.size - 1] % 10 != 9:
                waves |= (ship.p_cord << 11)
        
        waves |= (ship.p_cord >> 10)
        self.math_field = self.math_field & (~waves)
        
    def make_field(self):
        ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            self.place_ship(ship(size).make_ship())
        
    def get_field(self):
        return self.math_import

    def get_ships(self):
        return self.ships
    
class game:
    def __init__(self, battlefield: math_battlefield):
        self.answer = battlefield.get_field()
        self.field = 0
        self.ships = battlefield.get_ships()

    # def test(self):
    #     for i in range(0, 10):
    #         for j in range(0, 10):
    #             if (self.answer & 2**(i * 10 + j)) != 0:
    #                 print("ロ", end = "")
    #             else:
    #                 print("ー", end = "")
    #         print()
    
    def print_field(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if (self.field & 2**(i * 10 + j)) != 0:
                    if (self.answer & 2**(i * 10 + j)) != 0:
                        print("ロ", end = " ")
                    else:
                        print("メ", end = " ")
                else:
                    print("ー", end = " ")
            print()
            
    def strike(self, cord):
        self.field = self.field | (2**int(cord))
        
    def ship_update_status(self):          
        for i in range(0, len(self.ships)):
            if (self.ships[i] & self.field) == self.ships[i]:
                self.ships.pop(i)
                print("Корабль уничтожен!")
                break
         
def input_cords():
    x = input("Введите координаты выстрела через пробел: (x y): x∈N, y∈N, 1 <= x,y <= 10\nВвод: ").split(" ")
    if len(x) != 2:
        return (False, -1)
    if x[0].isdigit() and x[1].isdigit():
        x_1, x_2 = int(x[0]) - 1, int(x[1]) - 1
        if x_1 < 0 or x_1 > 9 or x_2 < 0 or x_2 > 9:
            return (False, -1)
        return (True, x_1 * 10 + x_2) 
    else:
        return (False, -1)
 
def run_the_game():
    current_game = game(math_battlefield())
    
    while current_game.field & current_game.answer != current_game.answer:
        x = input_cords()
        if x[0] == True:
            current_game.strike(x[1])
            current_game.print_field()
            current_game.ship_update_status()
        else:
            print("Неверный ввод!")
            
    return True

if __name__ == "__main__":
    if run_the_game() == True:
        print("Поздравляем! Вы победили!")
            
        
        
        
        