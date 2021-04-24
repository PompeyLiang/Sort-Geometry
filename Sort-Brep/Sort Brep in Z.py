"""

This is a python component that sort input breps based on breps' center points in Z axis  

Compent name: Sort Brep in Z
Input Parameter:
        Geometry(Type:Brep, Box, Surface): The Breps are needed to sort.
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted breps

__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"

"""

import Rhino.Geometry as rg

def find_center(geometry):
  '''
  __name__: find_center
  __msg__: To find the center point of input brep; the center point are calculated by the average point of brep's vertexes.
  __paras__: 
        geometry: Single brep that needed to find center point. 
  __return__: 
        point: Center point.
  '''
  
    vertex_list = geometry.Vertices #return BrepVertexList, not list need to convert to list.
    vertex_list = list(vertex_list)
    point_list = [vertex.Location for vertex in vertex_list]  #vertice don't have coordinate properties, use Vertex.Location to get point.
    length = len(vertex_list)
    average_x = sum([point.X for point in point_list])/length
    average_y = sum([point.Y for point in point_list])/length
    average_z = sum([point.Z for point in point_list])/length
    return rg.Point3d(average_x, average_y, average_z)

def sort_list_object(list):
  '''
  __name__: sort_list_object
  __msg__: Sort one index list based on point.Z list; and then access breps list with sorted index list. 
  __paras__: 
        geometry: Breps that needed to sorted in Z Axis. 
  __return__: 
        curve list: Sorted breps list.
  '''
  
    length = len(list)
    index_list = [i for i in range(length)]
    center_point_list = [find_center(item) for item in list]
    z_value = [point.Z for point in center_point_list]
    sorted_index = [index_list for z_value, index_list in sorted(zip(z_value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    return sorted_geometry

if "__main__":
    if Reverse ==True:
        Geometry = sort_list_object(Geometry)[::-1]
    else:
        Geometry = sort_list_object(Geometry)
