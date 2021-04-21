'''
This is a python component that sort input curves based on curves' middle points along input curve
'''

__author__ = "jujud"
__version__ = "2021.04.20"
                                        
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
                                        
def find_center(geometry):
    tValue_list = geometry.DivideByCount(100,True)
    point_list = [geometry.PointAt(t) for t in tValue_list]
    length = len(point_list)
    average_x = sum([point.X for point in point_list])/length
    average_y = sum([point.Y for point in point_list])/length
    average_z = sum([point.Z for point in point_list])/length
    return rg.Point3d(average_x,average_y,average_z)
                        
def sort_list_object(list, curve, boolen):
    length = len(list)
    t_value = [curve.ClosestPoint(point)[1] for point in list]
    index_list = [i for i in range(length)]
    if boolen == True:
      point_on_curve = [curve.PointAt(t) for t in t_value]
      distance_list = [list[i].DistanceTo(point_on_curve[i]) for i in range(length)]
      sorted_index = [index_list for distance_list, index_list in sorted(zip(distance_list, index_list))]
    else: 
      sorted_index = [index_list for t_value, index_list in sorted(zip(t_value, index_list))]
    return sorted_index
                                        
if "=main=":
    center_point_list = [find_center(item) for item in Geometry] 
    boolen = Distance
    if Reverse == True:
      sort_index  = sort_list_object(center_point_list, Curve, boolen)[::-1]
      Geometry = [Geometry[i] for i in sort_index]
    else:
      sort_index = sort_list_object(center_point_list, Curve, boolen)
      Geometry = [Geometry[i] for i in sort_index]
