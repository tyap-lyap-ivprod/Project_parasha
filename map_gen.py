from random import randint

cell_title = {                                                              #тайтлы для клетки
    "wall" : "#",   0 : "#",            
    "floar": ' ',   1 : '□',
    "door" : '|',   2 : '|',
    4: ' '
}

class cell1:                                                          #класс клетки
    def __init__(self,x,y,vek=1,title=0):
        self.x = x
        self.y = y
        self.title = title
        self.block = [3]                         #заблокировано движение [0,1,2,3]
        self.vek = 0                                                  
        #напрвление создания клетки: 
        # 0 ; 
        #3 1; 
        # 2 ; 



class map_cl:                                                         #класс карты
    def __init__(self,type_of_map):
        self.type_of_map   = type_of_map
        self.cell_list     = [cell1(0,0,1,2)]
        self.cell_array    = []
        self.raw_cell_list = [0]

    def new_cell(self,x,y,title,v=1):                                     #функция создания новой клетки в <<cell_list>>
        for i in self.cell_list:
            if x == i.x and y == i.y:
                return False

        self.cell_list.append(cell1(x,y,title=title,vek=v))

    def _build_cell_array(self):
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0

        cell_array = []

        for i in self.cell_list:                                           #узнаём размеры карты
            if i.x < min_x:
                min_x = i.x

            elif i.x > max_x:
                max_x = i.x

            if i.y < min_y:
                min_y = i.y

            elif i.y > max_y:
                max_y = i.y

        vx = 0 - min_x                                                #смещение координат по x
        vy = 0 - min_y                                                #смещение координат по y

        print(max_x - min_x)
        print(max_y - min_y)

        for i in range(max_y-min_y+1):
            cell_array.append([])
            for j in range(max_x-min_x+1):
                cell_array[-1].append(cell1(j,i,0,cell_title[0]))

        for i in self.cell_list:
            cell_array[i.y+vy][i.x+vx] = i

        self.cell_array = cell_array

    def print_array(self):
        self._build_cell_array()
        transp_array = []
        for i in self.cell_array:
            for j in i:
                buf+=str(j.title)
            
            print(buf)

    def _step_by_vector(self,vek):
        if   vek == 0:
            return 0,-1

        elif vek == 1:
            return 1,0
            
        elif vek == 2:
            return 0,1
            
        elif vek == 3:
            return -1,0

        elif vek == 0.5:                                              #зачем? Пусть будет
            return 1,-1

        elif vek == 1.5:
            return 1,1
            
        elif vek == 2.5:
            return -1,1
            
        elif vek == 3.5:
            return -1,-1

    def step(self):
        if len(self.raw_cell_list) > 0:                               #если есть не обработанные клетки
            last_n = self.raw_cell_list.pop()                         #снимается адресс последний не обработанной клетки
            last_cell = self.cell_list[last_n]                        #в переменную <<last_cell>> передаётся необработанная клетка

            if len(last_cell.block) < 4:
                






                        




def test_map():
    cl1 = map_cl('room')
    cl1.new_cell(0,0,cell_title[2])
    cl1.new_cell(0,1,cell_title[1])
    cl1.new_cell(-1,1,cell_title[0])
    cl1.new_cell(1,1,cell_title[0])
    cl1.new_cell(0,2,cell_title[1])
    cl1.new_cell(-1,2,cell_title[0])
    cl1.new_cell(1,2,cell_title[0])

    cl1.print_array()

test_map()















    def step1(self):
        if len(self.raw_cell_list) > 0:
            last_n = self.raw_cell_list.pop()
            last_cell = self.cell_list()
            for i in [0,1,2,3]:
                if i not in last_cell.block:
                    if i == last_cell.vek:
                        if randint(0,100)>60:
                            vx,vy = self._step_by_vector(last_cell.vek)
                            if new_cell(last_cell.x+vx, last_cell.y+vy, vek=vek, title=cell_title[1]):
                                self.raw_cell_list.append(len(self.cell_list)-1)

                            else:
                                self.raw_cell_list.append(last_n)
                else