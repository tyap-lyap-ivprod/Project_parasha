from random import randint

cell_title = {                                                              #тайтлы для клетки
    "wall" : "#",   0 : "■",            
    "floar": ' ',   1 : '□',
    "door" : '◁',   2 : '◁',
    4: ' '
}

class cell1:                                                          #класс клетки
    def __init__(self,x,y,vek=1,title=0):
        self.x = x
        self.y = y
        self.title = title
        self.block = [3]                         #заблокировано движение [0,1,2,3]
        self.vek = vek                                                 
        #напрвление создания клетки: 
        # 0 ; 
        #3 1; 
        # 2 ; 



class map_cl:                                                         #класс карты
    def __init__(self,type_of_map):
        self.type_of_map   = type_of_map
        self.cell_list     = [cell1(0,0,1,cell_title['door'])]
        self.cell_array    = []
        self.raw_cell_list = [0]

    def _if_emrt(self,x,y):
        for i in self.cell_list:
            if x == i.x and y == i.y:
                return False
            else:
                return True

    def new_cell(self,x,y,title,v=1):                                     #функция создания новой клетки в <<cell_list>>
        if not self._if_emrt(x,y):
            return False

        self.cell_list.append(cell1(x,y,title=title,vek=v))
        return True

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

        #print(max_x - min_x)
       # print(max_y - min_y)

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
            buf=''
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

    def _vek_plus(self,vek,max_t=3):
        if vek == max_t:
            return 0
        else:
            return vek + 1

    def _vek_min(self,vek,max_t=3):
        if vek == 0:
            return max_t
        else:
            return vek - 1

    def _turn(self,vek,napr,max):
        if (napr == "LEFT"):
            pass
    def _set_block(self,block):
        for i in range(len(self.cell_list)):
            for j in block:
                if j not in self.cell_list[i].block:
                    self.cell_list[i].block.append(int(j))


    def step(self):
        if len(self.raw_cell_list) > 0:                               #если есть не обработанные клетки
            last_n = self.raw_cell_list.pop(randint(0,len(self.raw_cell_list)-1))                         #снимается адресс последний не обработанной клетки
            #print(last_n)
            last_cell = self.cell_list[last_n]  
            len_block = 4 - len(last_cell.block)  
            print("len = " + str(len(self.cell_list)))                    #в переменную <<last_cell>> передаётся необработанная клетка
            if len_block < 4:
                if last_cell.vek not in last_cell.block:
                    #print('f')
                    #print(last_cell.vek)
                    vx,vy = self._step_by_vector(last_cell.vek)
                    #print('vx = ' + str(vx) + '\nvy = '+ str(vy))
                    if self.new_cell(last_cell.x+vx, last_cell.y+vy,
                                     cell_title[1], last_cell.vek):
                        #print("yes!")
                        self.raw_cell_list.append(len(self.cell_list)-1)
                        self.cell_list[-1].block = [
                            self._vek_min(self._vek_min(last_cell.vek))
                            ]


                    vek_min  = self._vek_min (last_cell.vek)
                    vek_plus = self._vek_plus(last_cell.vek)
                    
                    vxmin,vymin   = self._step_by_vector(vek_min)
                    vxplus,vyplus = self._step_by_vector(vek_plus)

                    vxmin += last_cell.x
                    vymin += last_cell.y

                    vxplus+= last_cell.x
                    vyplus += last_cell.y

                    print('- ' + str(vxmin) + ' ' + str(vymin) + ' ' + str(vek_min))
                    print('+ ' + str(vxplus) + ' ' + str(vyplus) + ' ' + str(vek_plus))
                    if (randint(0,4) > 3):
                        variant  = []
                        print("F")
                        
                        if (self._if_emrt(vxmin, vymin)   
                            and (vek_min not in last_cell.block)):
                            variant.append([vxmin, vymin, vek_min])

                        elif (self._if_emrt(vxplus, vyplus) 
                            and (vek_plus not in last_cell.block)):
                            variant.append([vxplus, vyplus, vek_plus])       

                        if len(variant)>0:
                            cell_xy = variant[randint(0,len(variant)-1)]
                            print(cell_xy[-1])
                            self.new_cell(cell_xy[0],cell_xy[1],
                                title=cell_title[1],v=cell_xy[2])
                            self.raw_cell_list.append(len(self.cell_list)-1)
                            self.cell_list[-1].block = [
                                self._vek_min(self._vek_min(cell_xy[-1]))
                                ]

                   # for i in range(last_cell.y-1,last_cell.y+1):
                    #    for j in range(last_cell.x-1,last_cell.x+1):
                     #       self.new_cell(j,i,title=cell_title[0])
    def connect_two_point_line(self,point1_xy,point2_xy):
        if   point1_xy[1] == point2_xy[1]:
            if point2_xy[0] < point1_xy[0]:
                step_in_range = -1
            else:
                step_in_range = 1
            for i in range(point1_xy[0],point2_xy[0],step_in_range):
                self.new_cell(i,point1_xy[1],title=cell_title[1],v=1)
            print(1)
        elif point1_xy[0] == point2_xy[0]:
            if point2_xy[1] < point1_xy[1]:
                step_in_range = -1
            else:
                step_in_range = 1
            for i in range(point1_xy[1],point2_xy[1],step_in_range):
                self.new_cell(point1_xy[0],i,title=cell_title[1],v=1)
            print(point1_xy)
            print(point2_xy)

        self.new_cell(point2_xy[0],point2_xy[1],title=cell_title[1],v=1)

    def connect_two_point(self,point1_xy,point2_xy):
        if (point1_xy[0] != point2_xy[0] and
            point1_xy[1] != point2_xy[1]):
            print(1)

            if randint(0,1):
                self.connect_two_point_line([point1_xy[0],point1_xy[1]]
                                           ,[point2_xy[0],point1_xy[1]])

                self.connect_two_point_line([point2_xy[0],point1_xy[1]]
                                           ,[point2_xy[0],point2_xy[1]])
            else:

                self.connect_two_point_line([point1_xy[0],point1_xy[1]]
                                           ,[point1_xy[0],point2_xy[1]])

                self.connect_two_point_line([point1_xy[0],point2_xy[1]]
                                           ,[point2_xy[0],point2_xy[1]])

        else:
            print(2)
            self.connect_two_point_line(point1_xy,point2_xy)
def test_map():
    cl1 = map_cl('room')
    for i in range(100):
        cl1.step()
    cl1.step()
    cl1.step()
    cl1.step()
    cl1.step()
    cl1.step()
    cl1.step()
    
    cl1.print_array()

def test_map1():
    cl1 = map_cl('room')
    cl1.connect_two_point([0,0],[randint(-15,15),randint(-15,15)
        ])
    cl1.print_array()

test_map1()
