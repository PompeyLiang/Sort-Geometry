'''
This is a python component that sort input points based on input vector  
'''

__author__ = "jujud"
__version__ = "2021.04.20"
                        
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
                        
                
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
    new_point_list = [orient(guide_vector)*point for point in list]
    value = [point.X for point in new_point_list]
    sorted_index = [index_list for value, index_list in sorted(zip(value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    return sorted_geometry
                        
                
if Reverse == True:
    Geometry = sort_list_object(Geometry, Guide)[::-1]
else:
    Geometry = sort_list_object(Geometry, Guide)
