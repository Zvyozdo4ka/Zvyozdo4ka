import os
import json
import math
import datetime


class Image_List:

    def __init__(self, path=None):
        self.path = path

    def dist(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)

    def ClosestPoints(self, point_to_check):

        data = None
        _min = 1000
        _coor = None
        _id = None
        with open(self.path, 'r') as f:

            data = json.loads(f.read())
            f.close()
            interval = len(data)
            P = []
            P_images = []
            item = 1
            for item in data:
                P.append(Point(item['id'], item['x'], item['y'], item['z'], item['images']))

        list_array = []

        list_array.append(self.dist(P[0], point_to_check))
        print("dist_array_0 =", list_array[0])

        dist_flag = list_array[0]  # the zero element in dist_flag
        dist_flag_lowest2 = None
        flag = 0

        j = 1

        for k in range(interval - 1):

            list_array.append(self.dist(P[j], point_to_check))  # from j=1, from dist_array[1]
            if dist_flag > list_array[j]:

                dist_flag_lowest2 = dist_flag

                dist_flag = list_array[j]
                flag = j
                flag_lowest2 = j
            elif dist_flag_lowest2 == None or dist_flag_lowest2 > list_array[j]:
                dist_flag_lowest2 = list_array[j]
                flag_lowest2 = j

            j = j + 1

 
        return [P[flag].id, P[flag].x, P[flag].y, P[flag].z, P[flag].images,
                P[flag_lowest2].id, P[flag_lowest2].x, P[flag_lowest2].y, P[flag_lowest2].z, P[flag_lowest2].images]


class Point:
    def __init__(self, id, x, y, z, images):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.images = images
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.x, self.y, self.z, self.images)


_start = datetime.datetime.now()

id_2points = Image_List('points3D_sorted.json')
res = id_2points.ClosestPoints(Point(0, -1.4506819364150012, 2.631383057053191, -0.6263092141509432, None))
print(res)