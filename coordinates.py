import math 
import copy 
# A class to represent a Point in 3D plane 
class Point(): 
    def __init__(self, index, x, y, z): 
        self.index = index 
        self.x = x 
        self.y = y 
        self.z = z 
 
# Driver code 
P = [ 
Point (0, 
    -2.398075290337787, 
    0.6193962115546964, 
    2.255628308811044), 
Point (1, 
    -2.398075290337787, 
    1.02, 
    2.255628308811044), 
Point (2, 
    -2.337539776280398, 
    0.5827625021617828, 
    -1.02), 
Point (3, 
    -2.337539776280398, 
    0.5827625021617828, 
    2.2882975878119773), 
Point (4, 
    -2.2813869564183515, 
    0.6329092708217572, 
    2.2779522684962554), 
Point (5, 
    -2.2492862920142325, 
    0.6323626143562094, 
    2.3003740232994843), 
Point (6, 
    -2.204470002708219, 
    0.630991945801995, 
    2.28134301489324), 
Point (7, 
    -1.7653851523766402, 
    0.6614743454692962, 
    1.02), 
Point (8, 
    -1.7653851523766402, 
    0.6614743454692962, 
    2.249163840021526), 
Point (9, 
    -1.7340417007510676, 
    -1.02, 
    2.2466034244552686), 
Point (10, 
    -1.7340417007510676, 
    0.6699755762570548, 
    1.02), 
Point (11, 
    -1.6778585396045373, 
    0.6442924392229483, 
    2.221188272810865), 
Point (12, 
    -1.4309194536527523, 
    0.680238461822629, 
    2.218502156709797), 
Point (13, 
    -1.02, 
    -1.02, 
    2.2466034244552686), 
Point (14, 
    -0.7312808385525805, 
    0.7340645498359639, 
    2.08592827516374), 
Point (15, 
    1.02, 
    -1.02, 
    2.2466034244552686)] 
 
point_to_check = Point (16, 
    -2.2813869564183515, 
    0.6329092708217572, 
    1.02) 
     
n = len(P) 
mid = n//2 #taking integer = 8 
 
print("Point for checking is {X=",point_to_check.x,",Y=",point_to_check.y,",Z=",point_to_check.z,"}") 
 
def dist(p1, p2): 
    return math.sqrt((p1.x - p2.x) * 
                     (p1.x - p2.x) + 
                     (p1.y - p2.y) * 
                     (p1.y - p2.y)) 
 
def binary_check(P, mid, point_to_check): # mid 8 
    flag = mid; #8 
     
    while (flag>2): #4 
        i = mid #4 
         
        p1_x=P[i].x-point_to_check.x # P4 
        p2_x=P[i+1].x-point_to_check.x # P5 
        pmin = min (p1_x, p2_x) #min = P4 
        flag=flag//2; #2 
         
        if p1_x<= p2_x: 
            mid=mid//2 # mid 2 
             
        else: 
            mid=mid+flag # mid  
    j=mid # P2, P3, P4, P5 
    A=abs(P[j].x-point_to_check.x) 
    A1=abs(P[j+1].x-point_to_check.x) 
    A2=abs(P[j+2].x-point_to_check.x) 
    print (A) 
    print (A1) 
    print (A2) 
    x_min = min( A, A1, A2) 
    #x_min = P4 
    print (x_min) 
    print (j) 
     
    if x_min==A:
        j=j+0
    if x_min==A1:
        j=j+1
    if x_min==A2:
        j=j+2



         
    #P4, P5 
    dist1 = dist(P[j], point_to_check) 
    dist2 = dist(P[j+1], point_to_check) 
     
    dist_min=min (dist1, dist2) 
     
    if (dist_min==dist2): 
        print("The closest point is",P[j+1].x, P[j+1].y, P[j+1].z) 
         
    if (dist_min==dist1): 
        print("The closest point is",P[j].x, P[j].y, P[j].z) 
 
 
binary_check(P, mid, point_to_check)
