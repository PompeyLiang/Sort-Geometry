  '''
This is a python component that sort input points based on points' Z coordinates.  
Compent name: Sort Point in Z
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
  __msg__: Sort one index list based on point.Z list; and then access points list with sorted index list. 
  __paras__: 
        geometry: Points that needed to sorted in Z Axis. 
  __return__: 
        curve list: Sorted points list.
  '''
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
