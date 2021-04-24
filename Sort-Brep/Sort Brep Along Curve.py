'''
This is a python component that sort input breps based on guide curve. Can choose two different ways to sort input breps: to sort breps by the distance between breps'
center points to the cloest points on guide curve; or sort breps along guide curve tangent. 

Compent name: Sort Brep Along Curve
Input Parameter:
        Geometry(Type:Curve): The breps are needed to sort.
        Curve(Type:Curve): Sort breps based on this curve. 
        Distance(Type: Boolen): Whether sort input breps based on distance between breps' center points to the cloesest point on guide curve.
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
        
def sort_list_object(list, curve,boolen):
  '''
  __name__: sort_list_object
  __msg__: Sort index list based on t values of the cloesest points on guide curve correspoinding to the input points; and then access breps list with sorted index list. 
  __paras__: 
        geometry: Breps that needed to sorted.
        curve: The guide curve to sort index values.
        boolen: Whether sort breps based on distance.
  __return__: 
        index list: Sorted index list.
  '''
  
    length = len(list)
    t_value = [curve.ClosestPoint(point) for point in list]
    index_list = [i for i in range(length)]
    if boolen == True:
        point_on_curve = [curve.PointAt(t) for t in t_value]
        distance_index = [list[i].DistanceTo(point_on_curve)[i] for i in range(length)]
        sorted_index = [index_list for distance_list, index_list in sorted(zip(t_value, index_list))]
    else:
        sorted_index = [index_list for t_value, index_list in sorted(zip(t_value, index_list))]
    return sorted_index
        
if "=main=":
    center_point_list = [find_center(item) for item in Geometry] 
    boolen = Distance
    if Reverse == True:
      sort_index  = sort_list_object(center_point_list, Curve, boolen)[::-1]
      Geometry = [Geometry[i] for i in sort_index]
    else:
      sort_index = sort_list_object(center_point_list, Curve, boolen)
      Geometry = [Geometry[i] for i in sort_index]
