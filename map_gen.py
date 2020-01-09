from random import randint
import math

cell_title = {                                                                  #тайтлы для клетки
    "wall" : "#",   0 : "■",            
    "floar": ' ',   1 : '□',
    "door" : '◁',   2 : '◁',
    4: ' '
}

class cell1:                                                                    #класс клетки
    def __init__(self,x,y,vek=1,title=0):
        self.x = x
        self.y = y
        self.title = title
        self.block = [3]                                                        #заблокировано движение [0,1,2,3]
        self.vek = vek                                                 
        #напрвление создания клетки: 
        # 0 ; 
        #3 1; 
        # 2 ; 
    def replace_title(self,new_title):
        self.title = new_title

    def _set_block(self,block):
        if block not in self.block:
            self.block.append(i)

class map_cl:                                                                   #класс карты
    def __init__(self,type_of_map):
        self.type_of_map   = type_of_map
        self.cell_list     = []
        self.cell_array    = []
        self.raw_cell_list = [0]

    def _if_emrt(self,x,y):
        for i in self.cell_list:
            if x == i.x and y == i.y:
                return False
   #     print("a1")
        return True

    def new_cell(self,x,y,title,v=1):                                           #функция создания новой клетки в <<cell_list>>
        if not self._if_emrt(x,y):
            print("false" + str(x)+ " "+ str(y))
            return False


        self.cell_list.append(cell1(x,y,title=title,vek=v))
        return True

    def find_xy(self,x,y):
        for i in range(len(self.cell_list)):
            if ((self.cell_list[i].x == x) and 
                (self.cell_list[i].y == y)):
                    return i

    def _build_cell_array(self):
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0

        cell_array = []

        for i in self.cell_list:                                                #узнаём размеры карты
            if i.x < min_x:
                min_x = i.x

            elif i.x > max_x:
                max_x = i.x

            if i.y < min_y:
                min_y = i.y

            elif i.y > max_y:
                max_y = i.y

        vx = 0 - min_x                                                          #смещение координат по x
        vy = 0 - min_y                                                          #смещение координат по y

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
    


    def get_vektor(self,vek):
        if   vek == 0:
            return 0,-1

        elif vek == 1:
            return 1,0
            
        elif vek == 2:
            return 0,1
            
        elif vek == 3:
            return -1,0

        elif vek == 0.5:                                                        #зачем? Пусть будет
            return 1,-1

        elif vek == 1.5:
            return 1,1
            
        elif vek == 2.5:
            return -1,1
            
        elif vek == 3.5:
            return -1,-1

    def step_by_vektor(self,vek):
        x, y = self.get_vektor(vek)
        return self.new_cell(x,y,cell_title[1],vek)

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
        if len(self.raw_cell_list) > 0:                                         #если есть не обработанные клетки
            last_n = self.raw_cell_list.pop(randint(0,
                        len(self.raw_cell_list)-1)
                    )                                                           #снимается адресс последний не обработанной клетки
            #print(last_n)
            last_cell = self.cell_list[last_n]  
            len_block = 4 - len(last_cell.block)  
            print("len = " + str(len(self.cell_list)))                          #в переменную <<last_cell>> передаётся необработанная клетка
            if len_block < 4:
                if last_cell.vek not in last_cell.block:
                    #print('f')
                    #print(last_cell.vek)
                    vx,vy = self.get_vektor(last_cell.vek)
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
                    
                    vxmin,vymin   = self.get_vektor(vek_min)
                    vxplus,vyplus = self.get_vektor(vek_plus)

                    vxmin += last_cell.x
                    vymin += last_cell.y

                    vxplus+= last_cell.x
                    vyplus += last_cell.y

                    #print('- ' + str(vxmin) + ' ' + str(vymin) + ' ' + str(vek_min))
                    #print('+ ' + str(vxplus) + ' ' + str(vyplus) + ' ' + str(vek_plus))
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
    def _connect_two_point_line(self,point1_xy,point2_xy):
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

    def _connect_two_point(self,point1_xy,point2_xy,rand=2):
        if (point1_xy[0] != point2_xy[0] and
            point1_xy[1] != point2_xy[1]):
            print(1)
            if rand not in [0,1]:
                rand == randint(0,1)

            if rand:
                self._connect_two_point_line([point1_xy[0],point1_xy[1]]
                                           ,[point2_xy[0],point1_xy[1]])

                self._connect_two_point_line([point2_xy[0],point1_xy[1]]
                                           ,[point2_xy[0],point2_xy[1]])
            else:

                self._connect_two_point_line([point1_xy[0],point1_xy[1]]
                                           ,[point1_xy[0],point2_xy[1]])

                self._connect_two_point_line([point1_xy[0],point2_xy[1]]
                                           ,[point2_xy[0],point2_xy[1]])

        else:
            print(2)
            self._connect_two_point_line(point1_xy,point2_xy)


    def _tunnels(self, p0, p1):
        mainer = [p0.x, p0.y]
        #print("X: " + str(p0.x)+' '+str(p1.x))
        #print("Y: " + str(p0.y)+' '+str(p1.y))
        turn = 0
        while not(mainer[0] == p1.x and mainer[1] == p1.y):
            ax = p1.x - mainer[0]   
            ay = p1.y + mainer[1]   
            if(ax == ay == 0):
                break

            if turn == 0:
               
                if(ax != 0):
                    v1 = math.fabs(ax)/ax
                    mainer[0] += v1

                else:
                    v1 = [-1, 1][randint(0, 1)]
                    mainer[0] += v1

                turn = 1
                self.new_cell(int(mainer[0]),int(mainer[1]),
                    v = v1+2,title=cell_title[1])

            else:
                    
                if(ay != 0):
                    v1 = math.fabs(ay)/ay
                    mainer[1] += v1

                else:
                    v1 = [-1, 1][randint(0, 1)]
                    mainer[1] += v1

                turn = 0
                self.new_cell(int(mainer[0]),int(mainer[1]),v = v1+1,title=cell_title[1])

    def _diagonal(self, p0, p1):
        mainer = [p0.x, p0.y]
        dxy = [math.fabs(p1.x - p0.x),math.fabs(p1.y - p0.y)]
        #print ('высота - '+str(dxy[0]) + 'ширина - '+str(dxy[1]))
        if dxy[0] > dxy[1]:
            small_d = dxy[1] - 1
            big_d   = dxy[0] - 1
            orent = 0
        
        else:
            small_d = dxy[0] - 1
            big_d   = dxy[1] - 1
            orent = 1
            
        if p0.x < p1.x:
            plinx = 1
        else:
            plinx = -1

        if p0.y < p1.y:
            pliny = 1
        else:
            pliny = -1

        koll_step = big_d / small_d
        koll_pere = big_d / koll_step
        dobav = 0
        while not(koll_step.is_integer()):
            big_d -= 1
            koll_step = big_d / small_d
            koll_pere = big_d / koll_step
            dobav += 1

        matr = []               
        for i in range(int(koll_pere)):
            for j in range(int(koll_step)):
                mainer[0]+=plinx
                matr.append([mainer[0], mainer[1]])

            mainer[1]+=pliny
            matr.append([mainer[0], mainer[1]])
            #self.new_cell(mainer[0], mainer[1], title=cell_title[1],v=1)

        for i in range(dobav):
                mainer[0]+=plinx
                matr.append([mainer[0], mainer[1]])
                #self.new_cell(mainer[0], mainer[1], title=cell_title[1],v=1)

        for i in matr:
            if orent == 0:
                self.new_cell(i[0], i[1], title=cell_title[1],v=1)

            else:
                self.new_cell(i[1], i[0], title=cell_title[1],v=1)

    def door_xy(self,doors,wid,hid):
        return_doors = []
        for i in range(len(doors)):
            for j in doors[i]:
                if i==0:
                    return_doors.append([int(j),0,i])
                elif i==1:
                    return_doors.append([wid - 1, int(j),i])

                elif i==2:
                    return_doors.append([int(j), hid - 1,i])
                   
                elif i==3:
                    return_doors.append([0,int(j),i])
        return return_doors


    def _room_gen(self, wid, hid, doors=[], start={'x':0,'y':0}):
        for i in range(wid):
            for j in range(hid):
                if ((i==0 or j==0) or 
                    (i==wid-1 or j==hid-1)):
                    title1 = cell_title[0]

                else:
                    title1 = cell_title[1]

                if self._if_emrt(start["x"]+i,start["y"]+j):
                    self.new_cell(start["x"]+i,start["y"]+j, title=title1,v=1)
                else:
         #           print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    pass

        _doors_xy = self.door_xy(doors,wid,hid)
        print(_doors_xy)
        for i in _doors_xy:
            self.cell_list[self.find_xy(i[0],i[1])].replace_title(cell_title[2])

            

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
    cl1._connect_two_point([0,0],[4,16],0)
    cl1._connect_two_point([1,1],[4,15],0)
    cl1.print_array()

def test_map2(x,y):
    cl1 = map_cl('room')
    cl1._diagonal(cell1(0,0,1,cell_title[1]),
                 cell1(x,y,1,cell_title[1]))
    cl1.print_array()

def test_map3(x,y):
    cl1 = map_cl('room')
    cl1._tunnels(cell1(0,0,1,cell_title[1]),cell1(x,y,1,cell_title[1]))
    cl1.print_array()

def test_map4(x,y):
    cl1 = map_cl('room')
    doors = [[],
             [5],
             [],
             [2]]
    cl1._room_gen(x,y,doors=doors)
    print(len(cl1.cell_list))
    cl1.print_array()


'''print("Первый тест")
test_map1()
print("Второй тест")
test_map2(4,16)
print("Третий тест")
test_map3(4,16)'''

def create_partmap(wid=20,hid=20,doors=[[],[5],[],[2]]):
    cl1 = map_cl('room')
    for i in cl1.door_xy(doors,wid,hid):
        print(i)
        cl1.new_cell(i[0],i[1],v=i[2],title=cell_title[2])
        #print(cl1.cell_list[cl1.find_xy(i[0],i[1])].title)
    cl1._room_gen(wid,hid)
    for i in cl1.cell_list:
    #    print(i.title + " " + str(i.x) + " " + str(i.y))
        pass
    cl1.print_array()
    return cl1

cl1 = create_partmap()