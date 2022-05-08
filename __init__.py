bl_info = {
    "name": "Convert Selected Mesh To Bounding Mesh",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "View3D > Object > Convert Selected Mesh to Bounding Mesh",
    "description": "Convert Selected Mesh To Bounding Mesh",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


import bpy
import bmesh

def convert_selected_mesh_to_bounding_mesh(context):
    
    selected_objects = context.selected_objects
    bm = bmesh.new()
    mesh_obs = [o for o in selected_objects if o.type == 'MESH']
    for ob in mesh_obs:
        me = ob.data 

        verts = [bm.verts.new(b) for b in ob.bound_box]
        bmesh.ops.convex_hull(bm, input=verts)
        bm.to_mesh(me)
        ob.data = me
        bm.clear()
    bm.free()


class OBJECT_OT_Convert_Selected_Mesh_To_Bounding_Mesh(bpy.types.Operator):
    """Convert Selected Mesh to Bounding Mesh"""
    bl_idname = "object.convert_selected_mesh_to_bounding_mesh"
    bl_label = "Convert Selected Mesh To Bounding Mesh"
    bl_options = {'UNDO', 'REGISTER'}


    def execute(self, context):

        convert_selected_mesh_to_bounding_mesh(context)

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_Convert_Selected_Mesh_To_Bounding_Mesh.bl_idname, text=OBJECT_OT_Convert_Selected_Mesh_To_Bounding_Mesh.bl_label)


def register():
    bpy.utils.register_class(OBJECT_OT_Convert_Selected_Mesh_To_Bounding_Mesh)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Convert_Selected_Mesh_To_Bounding_Mesh)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

