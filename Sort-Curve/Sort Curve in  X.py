from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs

class MyComponent(component):
    
    def RunScript(self, Geometry, Reverse):
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
        
        
        def sort_list_object(list):
            length = len(list)
            index_list = [i for i in range(length)]
            center_point_list = [find_center(item) for item in list]
            X_value = [point.X for point in center_point_list]
            sorted_index = [index_list for X_value, index_list in sorted(zip(X_value, index_list))]
            sorted_geometry = [list[i] for i in sorted_index]
            return sorted_geometry
        
        if Reverse == True:
            Geometry = sort_list_object(Geometry)[::-1]
        else:
            Geometry = sort_list_object(Geometry)
        
        # return outputs if you have them; here I try it for you:
        return Geometry