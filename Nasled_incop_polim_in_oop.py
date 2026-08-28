class Building:
    __year = None #tak mozem ustanovit` znach, no ne mozem vivesti na ekran
    #no esli prosto bez procherkov pisat` to vse ravno vivedetsya
    __city = None
#incapsulyacia - vse polya dolzni bit` zashisheni
#dostyp k polyam tolko cherez metodi i funct
    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

class School(Building): #class naslednik, 1 class- 1 roditel`
    pupils = 0
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) #peredaem v roditelsky class znacheni
        self.pupils = pupils
    def get_info(self):
        super().get_info() #visivaem get_info is roditelya
        print("Pupils:", self.pupils)
#u naslednica mogut byt` nasledniki

class House(Building):
    pass
class Shop(Building):
    pass
school1 = School(1000, 2002, "Moscow")
school1.get_info()
house1 = House(2002, "Moscow")
house1.get_info()
shop1 = Shop(2002, "Moscow")


