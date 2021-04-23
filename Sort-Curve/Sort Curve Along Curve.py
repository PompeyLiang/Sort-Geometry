'''

This is a python component that sort input curves based on guide curve. Can choose two different ways to sort input curves: to sort curves by the distance between curves'
middle points to the cloest points on guide curve; or sort curves along guide curve tangent. 
Compent name: Sort Curve Along Curve
Input Parameter:
        Geometry(Type:Curve): The curves are needed to sort.
        Curve(Type:Curve): Sort curves based on this curve. 
        Distance(Type: Boolen): Whether sort input curves based on distance between curves' middle points to the cloesest point on guide curve.
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted curves
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"

'''     

import Rhino.Geometry as rg
                                        
def find_center(geometry):
  '''
  __name__: find_center
  __msg__: To find the center point of input curve; the center point are calculated by the average point of vertexes that generated by divide curve.
  __paras__: 
        geometry: Single curve that needed to find center point. 
  __return__: 
        point: Center point.
  '''
    tValue_list = geometry.DivideByCount(100,True)
    point_list = [geometry.PointAt(t) for t in tValue_list]
    length = len(point_list)
    average_x = sum([point.X for point in point_list])/length
    average_y = sum([point.Y for point in point_list])/length
    average_z = sum([point.Z for point in point_list])/length
    return rg.Point3d(average_x,average_y,average_z)
                        
def sort_list_object(list, curve, boolen):
  '''
  __name__: sort_list_object
  __msg__: Sort index list based on t values of the cloesest points on guide curve correspoinding to the input points; and then access curves list with sorted index list. 
  __paras__: 
        geometry: Curves that needed to sorted.
        curve: The guide curve to sort index values.
        boolen: Whether sort curves based on distance.
  __return__: 
        index list: Sorted index list.
  '''
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
