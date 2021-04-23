'''

This is a python component that sort input points based on input vector. To transform all input points into a new coordinate plane.
And then extract the new points' x values, sort points baesd on this new x values list.
Compent name: Sort Point Along Vector
Input Parameter:
        Geometry(Type:Curve): The points are needed to sort.
        Guide(Type:Vector): Sort points based on this vector. 
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted points
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"

'''     

import Rhino.Geometry as rg
                        
                
def orient (vector):
  '''
  __name__: orient
  __msg__: Calculate the rotation matrix that transform WCP X axis to input vector. 
  __paras__: 
        vector: X axis of new coordinate plane, the vector to sort points. 
  __return__: 
        trans_matrix: Rotation matrix.
  '''
    origin_point = rg.Point3d(0,0,0)
    x_vector = rg.Vector3d(1,0,0)
    origin_plane = rg.Plane(origin_point, rg.Vector3d(0,0,1))
    new_plane = rg.Plane(origin_point, rg.Vector3d(0,0,1))
    rotation_matrix = rg.Transform.Rotation(x_vector, vector, origin_point)
    new_plane.Transform(rotation_matrix)
    trans_matrix = rg.Transform(0)
    trans_matrix = trans_matrix.ChangeBasis(origin_plane, new_plane)
    
    return trans_matrix
                
def sort_list_object(list, guide_vector):
  '''
  __name__: sort_list_object
  __msg__: Transform point to new coordinate plane. Sort index list based on new point.Xs' list; and then access points list with sorted index list. 
  __paras__: 
        geometry: Points that needed to sorted.
        guide_vector: The vector to sort points.
  __return__: 
        curve list: Sorted points list.
  '''
    length = len(list)
    index_list = [i for i in range(length)]
    new_point_list = [orient(guide_vector)*point for point in list]
    value = [point.X for point in new_point_list]
    sorted_index = [index_list for value, index_list in sorted(zip(value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    
    return sorted_geometry
                        
                
if Reverse == True:
    Geometry = sort_list_object(Geometry, Guide)[::-1]
else:
    Geometry = sort_list_object(Geometry, Guide)
