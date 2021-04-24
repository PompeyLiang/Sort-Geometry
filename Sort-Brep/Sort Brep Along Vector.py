'''

This is a python component that sort input breps based on input vector. To transform all input breps into a new coordinate plane.
And then extract the new center point x values, sort breps baesd on this new x values list.

Compent name: Sort Brep Along Vector
Input Parameter:
        Geometry(Type:Curve): The breps are needed to sort.
        Guide(Type:Vector): Sort breps based on this vector. 
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted breps
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"

'''     

import Rhino.Geometry as rg

def find_center(geometry):
  '''
  __name__: find_center
  __msg__: To find the center point of input brep; the center point are calculated by the average point of brep's vertexes.
  __paras__: 
        geometry: Single curve that needed to find center point. 
  __return__: 
        point: Center point.
  '''
  
    vertex_list = geometry.Vertices     #return BrepVertexList, not list need to convert to list.
    vertex_list = list(vertex_list)
    point_list = [vertex.Location for vertex in vertex_list]      #vertice don't have coordinate properties, use Vertex.Location to get point.
    length = len(vertex_list)
    average_x = sum([point.X for point in point_list])/length
    average_y = sum([point.Y for point in point_list])/length
    average_z = sum([point.Z for point in point_list])/length
    return rg.Point3d(average_x, average_y, average_z)

def orient (vector):
  '''
  __name__: orient
  __msg__: Calculate the rotation matrix that transform WCP X axis to input vector. 
  __paras__: 
        vector: X axis of new coordinate plane, the vector to sort breps. 
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
  __msg__: Transform point to new coordinate plane. Sort index list based on new point.X list; and then access breps list with sorted index list. 
  __paras__: 
        geometry: Breps that needed to sorted.
        guide_vector: The vector to sort breps.
  __return__: 
        curve list: Sorted breps list.
  '''
    length = len(list)
    index_list = [i for i in range(length)]
    center_point_list = [find_center(item) for item in list]
    new_center_point_list = [orient(guide_vector)*point for point in center_point_list]
    value = [point.X for point in new_center_point_list]
    sorted_index = [index_list for value, index_list in sorted(zip(value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    return sorted_geometry
                
        
if Reverse == True:
    Geometry = sort_list_object(Geometry, Guide)[::-1]
else:
    Geometry = sort_list_object(Geometry, Guide)
