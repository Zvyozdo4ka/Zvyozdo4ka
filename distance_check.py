import os
import json
import math
import datetime

class Point:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "{}, {}, {}, {}".format(self.id, self.x, self.y, self.z)


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y) **2 + (p1.z - p2.z) **2 )

_start = datetime.datetime.now()

point_to_check = Point(0, -1.4506819364150012, 2.631383057053191, -0.6263092141509432)
data = None
_min = 1000
_coor = None
_id = None
with open('points3D_sorted.json', 'r') as f:

    data = json.loads(f.read())
    f.close()
    interval = len(data)
    P = []
    item = 1
    for item in data:
        P.append(Point(item['id'], item['x'], item['y'], item['z']))


##########################################################################
def Binary_check(P, interval, point_to_check):  # interval 17

        while (interval >= 11):  # interval 17
            interval = interval // 2  # taking integer = 8

            i = interval  # 8

          #  print(P[i]['x'])

            p_left_x = P[i].x - point_to_check.x  # P8
            print("distance to left point=", p_left_x)
            p_right_x = P[i + 1].x - point_to_check.x  # P9
            print("distance to right point=", p_right_x)

            p_flag = p_left_x - p_right_x  # if < 0 => p_left_x < p_right_x => to the left
            print("p_flag", p_flag)

            step = interval // 2;  # 4

            if p_flag == 0:
                p_left_y = P[i].y - point_to_check.y
                p_right_y = P[i + 1].y - point_to_check.y
                p_flag = p_left_y - p_right_y  # if = 0 => p_left_y = p_right_y => check Z

                if p_flag == 0:
                    p_left_z = P[i].z - point_to_check.z
                    p_right_z = P[i + 1].z - point_to_check.z
                    p_flag = p_left_z - p_right_z  # if > 0 => p_left_z > p_right_z => to the right

            elif (p_flag < 0):
                break_point = interval - step  # 4

            else:
                break_point = interval + step  # 12

            interval = interval // 2

            print("break_point", break_point)
            print("interval", interval, '\n')

        j = break_point  # P4
        j = j - 10

        if j < 0:
            j = 0
        elif j > (len(P) - 16):
            j = n - 16

        dist_array = []
        dist_array.append(dist(P[j], point_to_check))  # j=0
        dist_flag = dist_array[0]  # the zero element in dist_flag
        flag = j

        print("j =", j)
        print("dist_array", dist_array[0])
        print("dist_flag", dist_flag)
        print("flag =", flag, "\n")

        j = j + 1

        for k in range(20):  # k=k+1

            print("j =", j)  # j=1
            print("Point  is {X=", P[j].x, ",Y=", P[j].y, ",Z=", P[j].z, "}")

            dist_array.append(dist(P[j], point_to_check))  # P1, dist_flag keeps P0

            if dist_flag > dist_array[j]:
                dist_flag = dist_array[j]
                flag = j

            print("dist_array", dist_array[j])
            print("dist_flag", dist_flag)
            print("flag =", flag, "\n")

            # if (dist_min < dist_flag)

            j = j + 1

        print("The closest point is with id", flag, "\n")
        print("Point  is {X=", P[flag].x, ",Y=", P[flag].y, ",Z=", P[flag].z, "}", "\n")
        print("The distance is", dist_flag, "\n")

        _time = datetime.datetime.now() - _start
        print(_time)


###########################################################################
Binary_check(P, interval, point_to_check)