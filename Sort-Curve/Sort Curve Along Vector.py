  '''
This is a python component that sort input curves based on curves' middle points in input vector  
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
        
def orient (vector):
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
