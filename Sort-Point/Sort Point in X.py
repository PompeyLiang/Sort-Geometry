'''
This is a python component that sort input points based on points' X coordinates.  
Compent name: Sort Point in X
Input Parameter:
        Geometry(Type:Point3d): The points are needed to sort.
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted points
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"
'''     
                
import Rhino.Geometry as rg
                
def sort_list_object(list):
  '''
  __name__: sort_list_object
  __msg__: Sort one index list based on point.X list; and then access points list with sorted index list. 
  __paras__: 
        geometry: Points that needed to sorted in X Axis. 
  __return__: 
        curve list: Sorted points list.
  '''
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
