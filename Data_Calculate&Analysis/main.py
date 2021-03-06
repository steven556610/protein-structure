# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 23:44:51 2019
@author: steven
"""
import numpy as np
import math
from analysis_document import *
from distane_between_axis import *
from sympy import *
from projection_PlaneAndPoint import *


pdb_name = r"E:\First_project\frame\1.pdb" 
scale_factor = 10
xyz = read_pdb_xyz_ligand(pdb_name)[0]
HeadOfLigandDomin = np.array(read_pdb_xyz_ligand(pdb_name)[1])
ForSecond = np.array(read_pdb_xyz_ligand(pdb_name)[2])
ForThird = np.array(read_pdb_xyz_ligand(pdb_name)[3])
coord = np.array(xyz, float) 
center = np.mean(coord, 0)  
coord = coord - center   
inertia = np.dot(coord.transpose(), coord)  
e_values, e_vectors = np.linalg.eig(inertia) 
for i in range(len(e_values)):  
     if e_values[i] == max(e_values):  
          eval1 = e_values[i]
          axis1 = e_vectors[:,i]   
     elif e_values[i] == min(e_values): 
          eval3 = e_values[i] 
          axis3 = e_vectors[:,i]  
     else:
          eval2 = e_values[i] 
          axis2 = e_vectors[:,i]  
#固定特徵值的指向
examine_vector1_1 = np.array(axis1)
examine_vector1_2 = HeadOfLigandDomin - center
examine_angle1 = calculate_angle(examine_vector1_1,examine_vector1_2)
if examine_angle1 >=90:
    axis1 = -1 * axis1
examine_vector2_1 = np.array(axis2)
examine_vector2_2 = ForSecond - center
examine_angle2 = calculate_angle(examine_vector2_1,examine_vector2_2)
if examine_angle2 >=90:
    axis2 = -1 * axis2
examine_vector3_1 = np.array(axis3)
examine_vector3_2 = ForThird - center
examine_angle3 = calculate_angle(examine_vector3_1,examine_vector3_2)
if examine_angle3 >=90:
    axis3 = -1 * axis3

point1 = 3 * scale_factor * axis1 + center
point2 = 2 * scale_factor * axis2 + center  
point3 = 1 * scale_factor * axis3 + center 

xyz2 = read_pdb_xyz_domin2(pdb_name)  
coord2 = np.array(xyz2, float)  
center2 = np.mean(coord2, 0)   
coord2 = coord2 - center2   
inertia2 = np.dot(coord2.transpose(), coord2) 
e_values2, e_vectors2 = np.linalg.eig(inertia2)  
for k in range(len(e_values2)):
    if e_values2[k] == max(e_values2): 
          eval4 = e_values2[k]
          axis4 = e_vectors2[:,k] 
    elif e_values2[k] == min(e_values2):
          eval6 = e_values2[k] 
          axis6 = e_vectors2[:,k]
    else: 
          eval5 = e_values2[k] 
          axis5 = e_vectors2[:,k]
point4 = 1 * scale_factor * axis4 + center2  
point5 = 1 * scale_factor * axis5 + center2
point6 = 1 * scale_factor * axis6 + center2 

xyz3 = read_pdb_xyz_domin3(pdb_name) 
coord3 = np.array(xyz3, float)
center3 = np.mean(coord3, 0) 
coord3 = coord3 - center3
inertia3 = np.dot(coord3.transpose(), coord3) 
e_values3, e_vectors3 = np.linalg.eig(inertia3)
for m in range(len(e_values3)): 
    if e_values3[m] == max(e_values3): 
          eval7 = e_values3[m]   
          axis7 = e_vectors3[:,m]
    elif e_values3[m] == min(e_values3): 
          eval9 = e_values3[m]
          axis9 = e_vectors3[:,m] 
    else:
          eval8 = e_values3[m] 
          axis8 = e_vectors3[:,m]
point7 = 1 * scale_factor * axis7 + center3 
point8 = 1 * scale_factor * axis8 + center3
point9 = 1 * scale_factor * axis9 + center3 

center_vector1 = np.array(center2-center)
center_vector2 = np.array(center3-center)
standard_vector = list(point3-center)      #投影x軸
projection_vector1 = list(point1 - center) #法向量
projection_vector2 = list(point2 - center) #投影y軸
projection_point_domin2_center = np.array(projection_point(center2,center,point2,point3,projection_vector1))  
projection_point_domin2_pca = np.array(projection_point(point4,center,point2,point3,projection_vector1))     #domin2 pca 在平面上的投影  
projection_point_domin3_center = np.array(projection_point(center3,center,point2,point3,projection_vector1)) #domin3 center 在平面上的投影 
projection_point_domin3_pca = np.array(projection_point(point7,center,point2,point3,projection_vector1))     #domin3 pca 在平面上的投影 
#domin2 center 在平面上的投影，轉換成numpy的陣列，才可以直接相減 
#用一般list並沒有直接鄉間的功能，要一個個index的位置做相減 
projection_vector_d2_ct = list(projection_point_domin2_center - center)  
projection_vector_d3_ct = list(projection_point_domin3_center - center)  
projection_vector_d2_pca = list(projection_point_domin2_pca - projection_point_domin2_center) 
projection_vector_d3_pca = list(projection_point_domin3_pca - projection_point_domin3_center)  
#print(math.sqrt(projection_vector_d2_ct[0]**2 + projection_vector_d2_ct[1]**2+projection_vector_d2_ct[2]**2))
#print(math.sqrt(projection_vector_d3_ct[0]**2 + projection_vector_d3_ct[1]**2+projection_vector_d3_ct[2]**2))
ProjectAngleDomin2 = calculate_angle(center_vector1,projection_vector_d2_ct)
ProjectAngleDomin3 = calculate_angle(center_vector2,projection_vector_d3_ct)
#print(ProjectAngleDomin2,ProjectAngleDomin3)
check_angle = calculate_angle(projection_vector_d2_ct,standard_vector)        #與x軸的夾角
compare_angle = calculate_angle(projection_vector_d2_ct,projection_vector2)   #與y軸的夾角
check_angle2 = calculate_angle(projection_vector_d3_ct,standard_vector)       #與x軸的夾角
compare_angle2 = calculate_angle(projection_vector_d3_ct,projection_vector2)  #與y軸的夾角


'''
#檔案的寫出
output_point = open('E:\paris_專題_大三寒假\投影_寒假專題\domin2的平面投影點與軸的距離寫入aa.csv','a')   
output_point.write(str(x1)) 
output_point.write(',')  
output_point.write(str(y1)) 
output_point.write('\n')  
output_point.close() 
output_point = open('E:\paris_專題_大三寒假\投影_寒假專題\domin3的平面投影點與軸的距離寫入aa.csv','a')  
output_point.write(str(x2)) 
output_point.write(',')  
output_point.write(str(y2))  
output_point.write('\n')  
output_point.close()  
'''

'''
idx = e_values.argsort()[::-1]   
e_values = e_values[idx]
e_vectors = e_vectors[:,idx]
point1 = 3 * scale_factor * e_vectors[0] + center
point2 = 2 * scale_factor * e_vectors[1] + center  
point3 = 1 * scale_factor * e_vectors[2] + center 
print(e_values)
print(e_vectors)
print(center)
print(point1,point2,point3,sep='\n')

vector_picture = r'E:\3.pdb_vector.bild' 
picture = open(vector_picture,'w') 
picture.write('.color blue\n')
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],point1[0],point1[1],point1[2]))  
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],point2[0],point2[1],point2[2]))   
picture.write('.arrow %f %f %f %f %f %f\n'\
                     %(center[0],center[1],center[2],point3[0],point3[1],point3[2]))
picture.close()
'''
#print(projection_vector_d2,projection_vector_d3,sep='\n')
#print(get_projection_axis_value(projection_vector_d2,projection_vector2))
#print(projection_point_domin2_center,projection_point_domin2_pca,projection_point_domin3_center,projection_point_domin3_pca,sep='\n')
#projection_vector_domin2 = list(projection_point_domin2_pca - projection_point_domin2_center)
#print(projection_vector_domin2)
#projection_vector_domin3 = list(projection_point_domin3_pca - projection_point_domin3_center)
#驗證是否向量內積為零，但Python的向量內積只能非常趨近於零

def main(): #主程式
    for j in range(1,2001):
        print(j)
        pdb_name = r"E:\First_project\frame" +"\\"+ str(j) + r'.pdb'
        scale_factor = 20 
        #angle_list_dm2 = [0]
        #angle_list_dm3 = [0]
        xyz = read_pdb_xyz_ligand(pdb_name)[0]  
        HeadOfLigandDomin = np.array(read_pdb_xyz_ligand(pdb_name)[1])
        ForSecond = np.array(read_pdb_xyz_ligand(pdb_name)[2])
        ForThird = np.array(read_pdb_xyz_ligand(pdb_name)[3])
        coord = np.array(xyz, float) 
        center = np.mean(coord, 0)
        coord = coord - center 
        inertia = np.dot(coord.transpose(), coord) 
        e_values, e_vectors = np.linalg.eig(inertia) 
        #特徵值排序
        for i in range(len(e_values)):
            if e_values[i] == max(e_values): 
                eval1 = e_values[i] 
                axis1 = e_vectors[:,i] 
            elif e_values[i] == min(e_values):  
                eval3 = e_values[i]
                axis3 = e_vectors[:,i] 
            else:
                eval2 = e_values[i] 
                axis2 = e_vectors[:,i]  

        #固定特徵值的指向
        examine_vector1_1 = np.array(axis1)
        examine_vector1_2 = HeadOfLigandDomin - center
        examine_angle1 = calculate_angle(examine_vector1_1,examine_vector1_2)
        if examine_angle1 >=90:
            axis1 = -1 * axis1
        examine_vector2_1 = np.array(axis2)
        examine_vector2_2 = ForSecond - center
        examine_angle2 = calculate_angle(examine_vector2_1,examine_vector2_2)
        if examine_angle2 >=90:
            axis2 = -1 * axis2
        examine_vector3_1 = np.array(axis3)
        examine_vector3_2 = ForThird - center
        examine_angle3 = calculate_angle(examine_vector3_1,examine_vector3_2)
        if examine_angle3 >=90:
            axis3 = -1 * axis3

        point1 = 3 * scale_factor * axis1 + center 
        point2 = 2 * scale_factor * axis2 + center
        point3 = 1 * scale_factor * axis3 + center  

        xyz2 = read_pdb_xyz_domin2(pdb_name) 
        coord2 = np.array(xyz2, float) 
        center2 = np.mean(coord2, 0) 
        coord2 = coord2 - center2  
        inertia2 = np.dot(coord2.transpose(), coord2)   
        e_values2, e_vectors2 = np.linalg.eig(inertia2) 
        for k in range(len(e_values2)): 
            if e_values2[k] == max(e_values2):
                eval4 = e_values2[k] 
                axis4 = e_vectors2[:,k] 
            elif e_values2[k] == min(e_values2): 
                eval6 = e_values2[k]
                axis6 = e_vectors2[:,k] 
            else:
                eval5 = e_values2[k] 
                axis5 = e_vectors2[:,k] 
        point4 = 1 * scale_factor * axis4 + center2 
        point5 = 1 * scale_factor * axis5 + center2
        point6 = 1 * scale_factor * axis6 + center2    

        xyz3 = read_pdb_xyz_domin3(pdb_name)  
        coord3 = np.array(xyz3, float)
        center3 = np.mean(coord3, 0) 
        coord3 = coord3 - center3
        inertia3 = np.dot(coord3.transpose(), coord3) 
        e_values3, e_vectors3 = np.linalg.eig(inertia3) 
        for m in range(len(e_values3)): 
            if e_values3[m] == max(e_values3):
                eval7 = e_values3[m] 
                axis7 = e_vectors3[:,m] 
            elif e_values3[m] == min(e_values3): 
                eval9 = e_values3[m]  
                axis9 = e_vectors3[:,m] 
            else:
                eval8 = e_values3[m] 
                axis8 = e_vectors3[:,m] 
        point7 = 1 * scale_factor * axis7 + center3
        point8 = 1 * scale_factor * axis8 + center3 
        point9 = 1 * scale_factor * axis9 + center3

        center_vector1 = list(center2-center)
        center_vector2 = list(center3-center)
        standard_vector = list(point3-center)      #投影x軸
        projection_vector1 = list(point1 - center) #法向量
        projection_vector2 = list(point2 - center) #投影y軸

        #沒有用numpy.array不能直接做陣列內的值相減
        projection_point_domin2_center = np.array(projection_point(center2,center,point2,point3,projection_vector1)) 
        projection_point_domin3_center = np.array(projection_point(center3,center,point2,point3,projection_vector1)) 
        #projection_point_domin2_pca = np.array(projection_point(point4,center,point2,point3,projection_vector1))   
        #projection_point_domin3_pca = np.array(projection_point(point7,center,point2,point3,projection_vector1)) 
        #projection_vector_d2_pca = list(projection_point_domin2_pca - projection_point_domin2_center) 
        #projection_vector_d3_pca = list(projection_point_domin3_pca - projection_point_domin3_center)  
        projection_vector_d2_ct = np.array(projection_point_domin2_center - center)
        projection_vector_d3_ct = np.array(projection_point_domin3_center - center)

        ProjectAngleDomin2 = calculate_angle(center_vector1,projection_vector_d2_ct)  #與平面的投影角度
        ProjectAngleDomin3 = calculate_angle(center_vector2,projection_vector_d3_ct)  #與平面的投影角度
        
       
        check_angle = calculate_angle(projection_vector_d2_ct,standard_vector)        #domin2與第三特徵向量的夾角
        compare_angle = calculate_angle(projection_vector_d2_ct,projection_vector2)   #domin2與第二特徵向量的夾角

        check_angle2 = calculate_angle(projection_vector_d3_ct,standard_vector)       #domin3與第三特徵向量的夾角
        compare_angle2 = calculate_angle(projection_vector_d3_ct,projection_vector2)  #domin3與第二特徵向量的夾角

        quadrant_d2 = 0 #d2向量
        quadrant_d3 = 0 #d3向量

        if check_angle > 90 and compare_angle < 90:
            #print(1)
            quadrant_d2 = 1
            angle_x = check_angle
            x1 = get_projection_axis_value_firstZone(projection_vector_d2_ct,standard_vector)[0]
            y1 = get_projection_axis_value_firstZone(projection_vector_d2_ct,standard_vector)[1]

        elif check_angle < 90 and compare_angle < 90 :
            #print(2)
            quadrant_d2 = 2
            angle_x = check_angle
            x1 = get_projection_axis_value_secondZone(projection_vector_d2_ct,standard_vector)[0]
            y1 = get_projection_axis_value_secondZone(projection_vector_d2_ct,standard_vector)[1]

        elif check_angle < 90 and compare_angle > 90:
            #print(3)
            quadrant_d2 = 3
            angle_x = check_angle
            x1 = get_projection_axis_value_thirdZone(projection_vector_d2_ct,standard_vector)[0]
            y1 = get_projection_axis_value_thirdZone(projection_vector_d2_ct,standard_vector)[1]

        elif check_angle > 90 and compare_angle > 90:
            #print(4)
            quadrant_d2 = 4
            angle_x = check_angle
            x1 = get_projection_axis_value_forthZone(projection_vector_d2_ct,standard_vector)[0]
            y1 = get_projection_axis_value_forthZone(projection_vector_d2_ct,standard_vector)[1]

        if check_angle2 > 90 and compare_angle2 < 90:
            #print(1)
            quadrant_d3 = 1
            angle_x2 = check_angle2
            x2 = get_projection_axis_value_firstZone(projection_vector_d3_ct,standard_vector)[0]
            y2 = get_projection_axis_value_firstZone(projection_vector_d3_ct,standard_vector)[1]

        elif check_angle2 < 90 and compare_angle2 < 90 :
            #print(2)
            quadrant_d3 = 2
            angle_x2 = check_angle2
            x2 = get_projection_axis_value_secondZone(projection_vector_d3_ct,standard_vector)[0]
            y2 = get_projection_axis_value_secondZone(projection_vector_d3_ct,standard_vector)[1]

        elif check_angle2 < 90 and compare_angle2 > 90:
            #print(3)
            quadrant_d3 = 3
            angle_x2= check_angle2
            x2 = get_projection_axis_value_thirdZone(projection_vector_d3_ct,standard_vector)[0]
            y2 = get_projection_axis_value_thirdZone(projection_vector_d3_ct,standard_vector)[1]

        elif check_angle2 > 90 and compare_angle2 > 90:
            quadrant_d3 = 4
            #print(4)
            angle_x2 = check_angle2
            x2 = get_projection_axis_value_forthZone(projection_vector_d3_ct,standard_vector)[0]
            y2 = get_projection_axis_value_forthZone(projection_vector_d3_ct,standard_vector)[1]

        output_projection_angle_domin2 = open(r'E:\project_angle_domin2.csv','a')
        output_projection_angle_domin2.write(str(ProjectAngleDomin2) + '\n')
        
        output_projection_angle_domin3 = open(r'E:\project_angle_domin3.csv','a')
        output_projection_angle_domin3.write(str(ProjectAngleDomin3) + '\n')

#執行主程式

main()


#輸出檔(for csv)
'''
        output_angle = open('E:\domin2的平面投影點與center和軸的角度寫入.csv','a')
        output_angle.write(str(angle_x) +',' + str(quadrant_d2) + '\n')
        output_angle.close()

        output_angle = open('E:\domin3的平面投影點與center和軸的角度寫入.csv','a')
        output_angle.write(str(angle_x2) +',' + str(quadrant_d3) + '\n')
        output_angle.close()
        
        output_point = open('E:\domin2的平面投影點與軸的距離寫入_new.csv','a')
        output_point.write(str(x1) + ',' + str(y1) + '\n' )
        output_point.close()
        
        output_point = open('E:\domin3的平面投影點與軸的距離寫入_new.csv','a')
        output_point.write(str(x2))
        output_point.write(',')
        output_point.write(str(y2) + '\n')
        output_point.close()
        

        angle_list_dm2[j] = angle_x
        angle_list_dm3[j] = angle_x2
        print(j)
    angle_list_dm2.sort()
    angle_list_dm3.sort()
    output_angle_sort = open('E:\paris_專題_大三寒假\投影_寒假專題\domin2的sort角度寫入.csv','a')
    for i in range(1,2001):
        output_angle_sort.write(angle_list_dm2[i] + '\n')
    output_angle_sort = open('E:\paris_專題_大三寒假\投影_寒假專題\domin3的sort角度寫入.csv','a')
    for i in range(1,2001):
        output_angle_sort.write(angle_list_dm3[i] + '\n')

        output_point = open('E:\paris_專題_大三寒假\投影_寒假專題\domin2的平面投影點與軸的距離寫入qq.csv','a')
        output_point.write(str(x1))
        output_point.write(',')
        output_point.write(str(y1) + '\n'
        output_point.close()
        
        output_point = open('E:\paris_專題_大三寒假\投影_寒假專題\domin3的平面投影點與軸的距離寫入qq.csv','a')
        output_point.write(str(x2))
        output_point.write(',')
        output_point.write(str(y2) + '\n')
        output_point.close()
        
        output_projection_point = open('E:\paris_專題_大三寒假\投影_寒假專題\更新後_domin2的平面投影點寫入.csv','a')
        output_projection_point.write(str(projection_point_domin2_center[0]))
        output_projection_point.write(',')
        output_projection_point.write(str(projection_point_domin2_center[1]))
        output_projection_point.write(',')
        output_projection_point.write(str(projection_point_domin2_center[2]))
        output_projection_point.write('\n')
        output_projection_point.close()

        output_projection_point = open('E:\paris_專題_大三寒假\投影_寒假專題\更新後_domin3的平面投影點寫入.csv','a')
        output_projection_point.write(str(projection_point_domin3_center[0]))
        output_projection_point.write(',')
        output_projection_point.write(str(projection_point_domin3_center[1]))
        output_projection_point.write(',')
        output_projection_point.write(str(projection_point_domin3_center[2]))
        output_projection_point.write('\n')
        output_projection_point.close()

        output_projection_domin2_pca = open('E:\paris_專題_大三寒假\投影_寒假專題\domin2的pca投影點寫入.csv','a')
        output_projection_domin2_pca.write(str(projection_point_domin2_pca[0]))
        output_projection_domin2_pca.write(',')
        output_projection_domin2_pca.write(str(projection_point_domin2_pca[1]))
        output_projection_domin2_pca.write(',')
        output_projection_domin2_pca.write(str(projection_point_domin2_pca[2]))
        output_projection_domin2_pca.write('\n')
        output_projection_domin2_pca.close()

        output_projection_domin2_pca = open('E:\paris_專題_大三寒假\投影_寒假專題\domin3的pca投影點寫入.csv','a')
        output_projection_domin2_pca.write(str(projection_point_domin3_pca[0]))
        output_projection_domin2_pca.write(',')
        output_projection_domin2_pca.write(str(projection_point_domin3_pca[1]))
        output_projection_domin2_pca.write(',')
        output_projection_domin2_pca.write(str(projection_point_domin3_pca[2]))
        output_projection_domin2_pca.write('\n')
        output_projection_domin2_pca.close()
 '''

#寫成chimera讀的向量檔案，使用的話，只要把段落上下的三引號刪除即可

'''
vector_picture = r'E:\專題__vector.bild' 
picture = open(vector_picture,'w') 
picture.write('.color red\n')
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],center2[0],center2[1],center2[2]))  
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],center3[0],center3[1],center3[2])) 
picture.write('.color blue\n')
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],point1[0],point1[1],point1[2]))  
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],point2[0],point2[1],point2[2]))   
picture.write('.arrow %f %f %f %f %f %f\n'\
                     %(center[0],center[1],center[2],point3[0],point3[1],point3[2]))
picture.write('.color green\n')
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],projection_point_domin2_center[0],projection_point_domin2_center[1],projection_point_domin2_center[2]))   
picture.write('.arrow %f %f %f %f %f %f\n'\
                     %(center2[0],center2[1],center2[2],point4[0],point4[1],point4[2])) 
picture.write('.arrow %f %f %f %f %f %f\n' \
                     %(center[0],center[1],center[2],projection_point_domin3_center[0],projection_point_domin3_center[1],projection_point_domin3_center[2]))   
picture.write('.arrow %f %f %f %f %f %f\n'\
                     %(center3[0],center3[1],center3[2],point7[0],point7[1],point7[2]))  
# print('.arrow',center,center3,sep=' ',end = '\n',file=vector_picture)   
picture.close() 
'''

'''
print("Ligand的物理中心",center) 
print("domin2的物理中心",center2) 
print("domin3的物理中心",center3)
print('兩個向量:\n',center_vector1,'\n',center_vector2)
print('ligand:%f %f %f' %(center[0],center[1],center[2]))
print('domin2:%f %f %f' %(center2[0],center2[1],center2[2]))
print('domin3:%f %f %f' %(center3[0],center3[1],center3[2]))  
print('point1:%f %f %f' %(point1[0],point1[1],point1[2]))   
print('point2:%f %f %f' %(point2[0],point2[1],point2[2])) 
print('point3:%f %f %f' %(point3[0],point3[1],point3[2]))  
print('domin2與domin3與ligand的角度:%f' %calculate_angle(center_vector1,center_vector2))  
print('domin2與point3與ligand的角度:%f' %calculate_angle(standard_vector,center_vector1))   
print('domin3與point3與ligand的角度:%f' %calculate_angle(standard_vector,center_vector2))  
'''

#寫出Output檔案 
'''
output_cos_angle = open('domin2和domin3的角度寫入.csv','a')
output_cos_angle.write(str(calculate_angle(center_vector1,center_vector2)))
output_cos_angle.write('\n')
output_cos_angle.close()

output_cos_angle = open('domin2和基準的角度寫入.csv','a')
output_cos_angle.write(str(calculate_angle(center_vector1,standard_vector)))
output_cos_angle.write('\n')
output_cos_angle.close()

output_cos_angle = open('domin3和基準的角度寫入.csv','a')
output_cos_angle.write(str(calculate_angle(center_vector2,standard_vector)))
output_cos_angle.write('\n')
output_cos_angle.close()
'''

'''
#print(calculate_angle(projection_vector1,projection_vector2)) #證明point1 and point2的角度為90
print(center)
print(point1)
print(point2)
print(point3)
b = np.array([0,0,0])
a = np.array([center,point2,point3])
c = solve(a,b)
print(c)  
'''

'''
output_cos_angle = open('E:\paris_專題_大三寒假\投影_寒假專題\domin2的投影角度寫入.csv','a')
output_cos_angle.write(str(projection_angle(center_vector1,projection_vector1,projection_vector2))) 
output_cos_angle.write('\n')
output_cos_angle.close()

output_cos_angle = open('E:\paris_專題_大三寒假\投影_寒假專題\domin3的投影角度寫入.csv','a')
output_cos_angle.write(str(projection_angle(center_vector2,projection_vector1,projection_vector2)))
output_cos_angle.write('\n')
output_cos_angle.close()
print(j)
print('domin2的投影角度:' ,projection_angle( center_vector1,projection_vector1,projection_vector2))
print('domin3的投影角度:' ,projection_angle(center_vector2,projection_vector1, projection_vector2)) 
'''


 