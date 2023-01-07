import bpy

class CreateMaterialForObjects(bpy.types.Operator):
    """Create a new material for each object in the scene and assign it as the main material"""
    bl_idname = "object.create_material_for_objects"
    bl_label = "Create Material for Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get a list of all objects in the scene
        objects = bpy.context.scene.objects

        # Iterate over all objects
        for obj in objects:
            # Create a new material for the object
            mat = bpy.data.materials.new(name=obj.name)
            # Assign the material to the object as the main material
            obj.data.materials.append(mat)
            obj.active_material = mat

        return {'FINISHED'}

def register():
    bpy.utils.register_class(CreateMaterialForObjects)
    # Set the shortcut for the operator
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(CreateMaterialForObjects.bl_idname, 'M', 'PRESS', ctrl=True, shift=False)

def unregister():
    # Remove the shortcut for the operator
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps['Object Mode']
    for kmi in km.keymap_items:
        if kmi.idname == CreateMaterialForObjects.bl_idname:
            km.keymap_items.remove(kmi)
    bpy.utils.unregister_class(CreateMaterialForObjects)

if __name__ == "__main__":
    register()