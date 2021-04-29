'''

This is a python component that sort input points based on guide curve. Can choose two different ways to sort input points: to sort points by the distance between points 
to the cloest points on guide curve; or sort points along guide curve tangent. 
Compent name: Sort Point Along Curve
Input Parameter:
        Geometry(Type:Point3d): The points are needed to sort.
        Curve(Type:Curve): Sort points based on this curve. 
        Distance(Type: Boolen): Whether sort input points based on distance between points to the cloesest point on guide curve.
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted points
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"

'''     

import Rhino.Geometry as rg
        
def sort_list_object(list, curve, boolen):
    '''
  __name__: sort_list_object
  __msg__: Sort index list based on t values of the cloesest points on guide curve correspoinding to the input points; and then access input points list with sorted index list. 
  __paras__: 
        geometry: Points that needed to sorted.
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
    boolen = Distance
    if Reverse == True:
      sort_index  = sort_list_object(Geometry, Curve, boolen)[::-1]
      Geometry = [Geometry[i] for i in sort_index]
    else:
      sort_index = sort_list_object(Geometry, Curve, boolen)
      Geometry = [Geometry[i] for i in sort_index]
