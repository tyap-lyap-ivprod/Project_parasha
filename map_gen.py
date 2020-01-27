from random import randint
import math

cell_title = {                                                                  #тайтлы для клетки
    "wall" : "■",   0 : "■",            
    "floar": '□',   1 : '□',
    "door" : '|',   2 : '|',
    4: ' '
}

class cell1:                                                                    #класс клетки
    def __init__(self, x, y, vek=1, title=2, type_s='Room'):
        self.x = x
        self.y = y
        self.title = title
        self.block = [3]                                                        #заблокировано движение [0,1,2,3]
        self.vek = vek
        self.type_s = type_s                                                 
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
        return True

    def nearby_xy(self,x=None,y=None,cell=None):
        if (x == None) or (y == None):
            if cell != None:
                x,y = cell.x,cell.y

            else:
            #print("Введите x,y или cell")
                pass

        buf_list = []

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self._if_emrt(i,j):
                    pass
                else:
                    #print(self.find_xy(i,j))
                    buf_cell = self.find_xy(i,j)
                    buf_list.append(buf_cell)

        return buf_list

    def new_cell(self,x,y,title,v=1, type_s="Room"):                                           #функция создания новой клетки в <<cell_list>>
        if not self._if_emrt(x,y):
           #V1 print("false" + str(x)+ " "+ str(y))
            return False


        self.cell_list.append(cell1(x,y,title=title,vek=v,type_s=type_s))
        return True

    def append_cell(self,cell):
        self.cell_list.append(cell)

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
                cell_array[-1].append(cell1(j,i,vek=0,title=cell_title[0]))

        for i in self.cell_list:
            cell_array[i.y+vy][i.x+vx] = i

        self.cell_array = cell_array

    def print_array(self):
        self._build_cell_array()
        transp_array = []
        for i in self.cell_array:
            buf=''
            for j in i:
                buf+=str(j.title)+" "
            
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

    def _vek_plus(self, vek, max_t=3):
        if vek == max_t:
            return int(0)

        else:
            return int(vek + 1)

    def _vek_min(self, vek, max_t=3):
        if vek == 0:
            return max_t

        else:
            return vek - 1

    def _set_vek(self, vek, add_vek, max_t=3):
        #print(vek)
        buf_vek = int(vek)
        if   add_vek > 0:
            buf_fun = self._vek_plus

        elif add_vek < 0:
            buf_fun = self._vek_min


        for i in range(add_vek):
            buf_vek = buf_fun(buf_vek)

        return int(buf_vek)
        
    def _set_block(self,block):
        for i in range(len(self.cell_list)):
            for j in block:
                if j not in self.cell_list[i].block:
                    self.cell_list[i].block.append(int(j))

    def _line(self,point1,point2):                                              #линия от точки до точки
        #V1 print("ASUKA" + str(point1))
        #V! print("BSUKA" + str(point2))
        if point1.y == point2.y:
            if point2.x < point1.x:
                step_in_range = -1
                v=1

            else:
                step_in_range = 1
                v=3    
            for i in range(point1.x,point2.x,step_in_range):
                self.new_cell(i,point1.y,title=cell_title[1],v=v,type_s="Corridor")

            #V1 print(1)
        elif point1.x == point2.x:
            if point2.y < point1.y:
                step_in_range = -1
                v=2
            else:
                step_in_range = 1
                v=0

            for i in range(point1.y,point2.y,step_in_range):
                self.new_cell(point1.x,i,title=cell_title[1] ,v=v)

            #V1 print(point1)
            #V1 print(point2)

        self.new_cell(point2.x,point2.y,title=cell_title[1] ,v=1)

    def _connect_corner(self,point1,point2,rand=2):                             #connection by cornet(угловое соединение)
        if (point1.x != point2.x and
            point1.y != point2.y):

            if rand not in [0,1]:
                rand == randint(0,1)

            if rand:
                self._line(point1,
                           cell1(point2.x,point1.y))

                self._line(cell1(point2.x,point1.y),
                           point2)
            else:
                self._line(point1,
                           cell1(point1.x,point2.y))

                self._line(cell1(point1.x,point2.y),
                           point2)

        else:
            self._line(point1,point2)

    def _connect_strench(self,point1,point2,vek=1):                             #connection by strench(соединение растяжкой)                            

        ax = point2.x - point1.x
        ay = point2.y - point1.y
        #V1 print(ay)
        if ax == 0 or ay == 0:
            self._line(point1,point2)
            return

        vx = ax / math.fabs(ax)
        vy = ay / math.fabs(ay)

        medium_point = cell1(math.floor(point1.x + ax/2),
                        math.floor(point1.y + ay/2))
        #V1 print("Cредняя точка по X = " + str(math.floor(point1.x + ax/2)))
        #V1 print("Cредняя точка по Y = " + str(math.floor(point1.y + ay/2)))

        if (vek == 1):
            self._line(point1,
                       cell1(medium_point.x, point1.y))

            self._line(cell1(medium_point.x, point1.y),
                       cell1(medium_point.x, point2.y))

            self._line(cell1(medium_point.x, point2.y),
                       point2)

        else:
            self._line(point1,
                       cell1(point1.x, medium_point.y))

           # print(medium_point)
            self._line(cell1(point1.x, medium_point.y),
                       cell1(point2.x, medium_point.y))

            self._line(cell1(point2.x, medium_point.y),
                       point2)

    def _not_null_wall(self,doors):
        buf = []
        for i in renge(len(doors)):
            if len(doors[i]) == 0:
                buf.append(i)

        return buf

    def _tunnels(self, point1, point2):                                         #неработающая функция создания тунелей
        mainer = cell1(point1.x, point1.y)
        ##V1 print("X: " + str(point1.x)+' '+str(point2.x))
        #print("Y: " + str(point1.y)+' '+str(point2.y))
        turn = 0
        while not(mainer.x == point2.x and mainer.y == point2.y):
            ax = point2.x - mainer.x   
            ay = point2.y + mainer.y   
            if(ax == ay == 0):
                break

            if turn == 0:
               
                if(ax != 0):
                    v1 = math.fabs(ax)/ax
                    mainer.x += v1

                else:
                    v1 = [-1, 1][randint(0, 1)]
                    mainer.x += v1

                turn = 1
                self.new_cell(int(mainer.x),int(mainer.y),
                    v = v1+2,title=cell_title[1])

            else:
                    
                if(ay != 0):
                    v1 = math.fabs(ay)/ay
                    mainer.y += v1

                else:
                    v1 = [-1, 1][randint(0, 1)]
                    mainer.y += v1

                turn = 0
                self.new_cell(int(mainer.x),int(mainer.y),
                              v = v1+1,title=cell_title[1])

    def _diagonal(self, point1, point2):                                        #не отлаженая функция соединения диагоналями
        mainer = cell1(point1.x, point1.y)
        dxy = [math.fabs(point2.x - point1.x),math.fabs(point2.y - point1.y)]
        #print ('высота - '+str(dxy[0]) + 'ширина - '+str(dxy[1]))
        if 0 in dxy or 1 in dxy:
            self._connect_corner(point1,point2)
            return 0

        if dxy[0] > dxy[1]:
            small_d = dxy[1] - 1
            big_d   = dxy[0] - 1
            orent = 0
        
        else:
            small_d = dxy[0] - 1
            big_d   = dxy[1] - 1
            orent = 1
            
        if point1.x < point2.x:
            plinx = 1

        else:
            plinx = -1

        if point1.y < point2.y:
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
                mainer.x+=plinx
                matr.append(cell1(mainer.x, mainer.y))

            mainer.y+=pliny
            matr.append(cell1(mainer.x, mainer.y))

        for i in range(dobav):
                mainer.x+=plinx
                matr.append(cell1(mainer.x, mainer.y))

        for i in matr:
            if orent == 0:
                self.new_cell(i.x, i.y, title=cell_title[1],v=1)

            else:
                self.new_cell(i.y, i.x, title=cell_title[1],v=1)

    def door_xy(self,raw_doors,wid,hid):                                        #вывод координат дверей
        return_doors = [[],[],[],[]]
        for i in range(len(raw_doors)):
            for j in raw_doors[i]:
                if i == 0:
                    return_doors[0].append(cell1(int(j), 0, vek = i, title = cell_title[2]))
                if i == 1:
                    return_doors[1].append(cell1(wid, int(j), vek = i, title = cell_title[2]))
                if i == 2:
                    return_doors[2].append(cell1(int(j), hid, vek = i, title = cell_title[2]))
                if i == 3:
                    return_doors[3].append(cell1(0, int(j), vek = i, title = cell_title[2]))

        return return_doors

    def door_list(self,doors):                                                  #вывод списка дверей
        buf_list = []   #тут храним список для выдачи
        for i in doors:
            for j in i:
                #print(j.x)
                buf_list.append(j)

        return buf_list

    def _cavity_gen(self,point1,point2):                                        #создание полостей
        ax = int(point2.x - point1.x)
        ay = int(point2.y - point1.y)
        vx = int(ax / math.fabs(ax))
        vy = int(ay / math.fabs(ay))
        ax = math.fabs(ax)
        ay = math.fabs(ay)

        for i in range(point1.x,point2.x+1,vx):
            for j in range(point1.y,point2.y+1,vy):
                #print(str(i) + " " + str(j))
                self.new_cell(i,j,title=cell_title[1],v=1,type_s="Cavity")

    def _room_gen(self, wid, hid, doors=[], start=cell1(0,0)):                  #создание комнаты с door
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
                    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    pass

        _doors_xy = self.door_xy(doors,wid,hid)
        #V1 print(_doors_xy)
        for i in _doors_xy:
            self.cell_list[self.find_xy(i[0],i[1])].replace_title(cell_title[2])

    def _connect_room(self,doors):
        doors_all = []
        kol_doors = 0 
        for i in doors:
            for j in i:
                doors_all.append(j)
                kol_doors +=1

        kol_connection = kol_doors + math.floor(kol_doors * randint(0,4)/2)-1

        for i in range(kol_doors):
            #V1 print("Дверь:" + str(doors_all[i]))
            pass

    def _gen_point(self, kol_point, point_min, point_max):
        for i in range(kol_point):
            self._room_gen()

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
    cl1._connect_corner([0,0],[4,16],0)
    cl1._connect_corner([1,1],[4,15],0)
    cl1.print_array()

def test_map2(x,y):
    cl1 = map_cl('room')
    cl1._diagonal(cell1(0,0,v = 1,title = cell_title[1]),
                  cell1(x,y,v = 1,title = cell_title[1]))
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
    #V1 print(len(cl1.cell_list))
    cl1.print_array()


'''print("Первый тест")
test_map1()
print("Второй тест")
test_map2(4,16)
print("Третий тест")
test_map3(4,16)'''

def create_partmap(wid=40,hid=20,
    doors=[
        [randint(2,18)], #двери сверху
        [4,8],             #двери справа
        [randint(2,18)], #двери снизу
        [5]              #двери слева
    ]):
    cl1 = map_cl('room')
    l1 = cl1.door_xy(doors,wid,hid)
    l2 = cl1.door_list(l1)

    fun_gen = cl1._connect_strench #соедиение "растяжками" и отрезками
    #fun_gen = cl1._connect_corner #соедиение углами и отрезками

    for i in l2:
            cl1.append_cell(i)

    #V1 print(l1)
    for i in range(1,len(l2)):
        fun_gen(l2[i-1],l2[i])
    cl1._connect_room(l1)
    for i in cl1.cell_list:
    #    print(i.title + " " + str(i.x) + " " + str(i.y))
        pass

    cav_list = [l2[0]]

    for i in range(8):
        x1 = randint(2,wid-2)
        y1 = randint(2,hid-2)
        buf_cell = cell1(x1,y1,title=cell_title[1],vek=1)
        cav_list.append(buf_cell)
        cl1.append_cell(buf_cell)
        cl1._cavity_gen(cell1(x1-1,y1-1),cell1(x1+1,y1+1))

        fun_gen(cav_list[-2],cav_list[-1])

    for i in range(len(cl1.cell_list)):
        #print("Клетка номер" + str(i) + "; X = " + str(cl1.cell_list[i].x) + "; y = " + str(cl1.cell_list[i].y)) 
        near_cl = cl1.nearby_xy(cell = cl1.cell_list[i])
        #print(len(near_cl))
        if len(near_cl) in [5,7]:
            #print(near_cl)
            buf_cell = [
                cl1.get_vektor(cl1._set_vek(cl1.cell_list[i].vek, int(-1))),
                cl1.get_vektor(cl1._set_vek(cl1.cell_list[i].vek, int(1)))
            ]
            #print(cl1.cell_list[i].title)
            #print(buf_cell)
            new_buf = list()
            for i1 in buf_cell:
                new_buf.append(cell1(cl1.cell_list[i].x + i1[0], cl1.cell_list[i].y + i1[1]))

            for j in near_cl:
                    #print(near_cl)
                    #print(str(cl1.cell_list[j].x) + " " + str(i1[0]))
                    if ((cl1.cell_list[j].x == new_buf.x) and
                        (cl1.cell_list[j].y == new_buf.y)):
                        #print(str(cl1.cell_list[j].x) + str(cl1.cell_list[j].y))
            #print(cl1.cell_list[i].type_s)
                        if cl1.cell_list[i].type_s == "Corridor":
                            print(vars(cl1.cell_list[i]))
                            print("s " + str(vars(new_buf)))
                            cl1.cell_list[i].title = cell_title['door']

    cl1.print_array()
    return cl1

for i in range(1):
    cl1 = create_partmap()