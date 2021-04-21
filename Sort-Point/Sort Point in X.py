'''
This is a python component that sort input points based on X axis  
'''

__author__ = "jujud"
__version__ = "2021.04.20"
                
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
                
def sort_list_object(list):
    length = len(list)
    index_list = [i for i in range(length)]
    X_value = [point.X for point in list]
    sorted_index = [index_list for X_value, index_list in sorted(zip(X_value, index_list))]
    sorted_geometry = [list[i] for i in sorted_index]
    return sorted_geometry
                
if Reverse == True:
    Geometry = sort_list_object(Geometry)[::-1]
else:
    Geometry = sort_list_object(Geometry)