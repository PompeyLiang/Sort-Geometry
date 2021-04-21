'''
This is a python component that sort input points based on Z axis  
'''

__author__ = "jujud"
__version__ = "2021.04.20"
                
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
                
def sort_list_object(list):
    length = len(list)
    index_list = [i for i in range(length)]
    Z_value = [point.Z for point in list]
    sorted_index = [index_list for Z_value, index_list in sorted(zip(Z_value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    return sorted_geometry
                
if Reverse == True:
    Geometry = sort_list_object(Geometry)[::-1]
else:
    Geometry = sort_list_object(Geometry)
