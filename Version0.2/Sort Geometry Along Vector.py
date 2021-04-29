"""

This is a python component that sort input geometries based on special direction. This component works with point, curve and brep class.

Compent name: Sort Geometry Along Vector     
Input Parameter:
        Geometry(Type:Point, Curve and Brep): The geometries are needed to sort.
        Direction(Type:Vector): Sort breps based on this curve. 
        Reverse(Type:Boolen): Whether reverse the output list.
Output:
        Geometey: Sorted geometries.
        
__author__ = "Liang Mayuqi"
__version__ = "2021.04.20"
        
"""
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

def average_point_calculator(list):
  
  '''
  __name__: average_point_calculator
  __msg__: To find the center point of input point list; the center point are calculated as the average point.
  __paras__: 
        list: List of points. 
  __return__: 
        point: Center point.
  '''
    
    length = len(list)
    average_x = sum([point.X for point in list]) / length
    average_y = sum([point.Y for point in list]) / length
    average_z = sum([point.Z for point in list]) / length
    return rg.Point3d(average_x, average_y, average_z)

def find_center(geometry):
  
  '''
  __name__: find_center
  __msg__: To find the center point of input brep; the center point are calculated by the average point of brep's vertexes.
  __paras__: 
        geometry: Single brep that needed to find center point. 
  __return__: 
        point: Center point.
  '''
  
    if type(geometry) == type(rg.NurbsCurve(3,4)):
      tValue_list = geometry.DivideByCount(100,True)
      point_list = [geometry.PointAt(t) for t in tValue_list]
    else:
      vertex_list = geometry.Vertices #return BrepVertexList, not list need to convert to list.
      vertex_list = list(vertex_list)
      point_list = [vertex.Location for vertex in vertex_list]  #vertice don't have coordinate properties, use Vertex.Location to get point.
    return average_point_calculator(point_list)

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

def sort_list_point_object(list, vector):
    length = len(list)
    index_list = [i for i in range(length)]
    vector.Unitize()
    if vector  == rg.Vector3d(1,0,0):
      X_value = [point.X for point in list]
      sorted_index = [index_list for X_value, index_list in sorted(zip(X_value, index_list))]
    elif vector  == rg.Vector3d(0,1,0):
      Y_value = [point.Y for point in list]
      sorted_index = [index_list for Y_value, index_list in sorted(zip(Y_value, index_list))]
    elif vector == rg.Vector3d(0,0,1):
      Z_value = [point.Z for point in list]
      sorted_index = [index_list for Z_value, index_list in sorted(zip(Z_value, index_list))]
    elif vector == None:
        sorted_index = index_list
    else:
        new_point_list = [orient(vector) * point for point in list]
        new_X_value = [point.X for point in new_point_list]
        sorted_index = [index_list for new_X_value, index_list in sorted(zip(new_X_value, index_list))]
    return sorted_index

def sort_list_object(list, vector):
  
  '''
  __name__: sort_list_object
  __msg__: 
  __paras__: 
        geometry: Breps or curves that needed to sorted.
        vector: The vector to sort breps or curves.
  __return__: 
        index list: Sorted index list of input geometry.
  '''
    
    length = len(list)
    index_list = [i for i in range(length)]
    center_point_list = [find_center(item) for item in list]
    if vector  == rg.Vector3d(1,0,0):  # Branching, can use dictionary to simplfy
       X_value = [point.X for point in center_point_list]
       sorted_index = [index_list for X_value, index_list in sorted(zip(X_value, index_list))]
    elif vector  == rg.Vector3d(0,1,0):
       Y_value = [point.Y for point in center_point_list]
       sorted_index = [index_list for Y_value, index_list in sorted(zip(Y_value, index_list))]
    elif vector == rg.Vector3d(0,0,1):
       Z_value = [point.Z for point in center_point_list]
       sorted_index = [index_list for Z_value, index_list in sorted(zip(Z_value, index_list))]
    elif vector == None:
        sorted_index = index_list
    else:
        new_point_list = [orient(vector) * point for point in center_point_list]
        new_X_value = [point.X for point in new_point_list]
        sorted_index = [index_list for new_X_value, index_list in sorted(zip(new_X_value, index_list))]
    return sorted_index
        
if "__main__":
    point_boolen = type([rs.coerce3dpoint(item) for item in Geometry][0]) == type(rg.Point3d(0,0,0))
    try:
      curve_boolen = type([rs.coercecurve(item) for item in Geometry][0].ToNurbsCurve()) == type(rg.NurbsCurve(3,4))
    except:
      curve_boolen = 0 #defind variable name curve_boolen for branching
      brep_boolen =  type([rs.coercebrep(item) for item in Geometry][0]) == type(rg.Brep())

    if point_boolen:
        Geometry_convert = [rs.coerce3dpoint(item) for item in Geometry]
        sorted_geometry_index = sort_list_point_object(Geometry_convert,Direction)
        Geometry = [Geometry[i] for i in sorted_geometry_index]
    elif curve_boolen:
        Geometry_convert = [rs.coercecurve(item).ToNurbsCurve() for item in Geometry]
        sorted_geometry_index = sort_list_object(Geometry_convert, Direction)
        Geometry = [Geometry[i] for i in sorted_geometry_index]
    elif brep_boolen:
        Geometry_convert = [rs.coercebrep(item) for item in Geometry]
        sorted_geometry_index = sort_list_object(Geometry_convert,Direction)
        Geometry = [Geometry[i] for i in sorted_geometry_index]
    else:
        Geometry = Geometry

    if Reverse ==True:
        Geometry = Geometry[::-1]
