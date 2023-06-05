import bpy

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a mesh object
bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=1, depth=1, location=(0, 0, 0))

# Get the reference to the newly created object
pyramid = bpy.context.object

# Set the pyramid's location and scale
pyramid.location = (0, 0, 1)
pyramid.scale = (1, 1, 1)

# Set the pyramid's material
material = bpy.data.materials.new(name="PyramidMaterial")
pyramid.data.materials.append(material)
pyramid.active_material = material

# Set the material's color
material.diffuse_color = (0.8, 0.2, 0.2, 1)

# Set the render engine to Cycles
bpy.context.scene.render.engine = 'CYCLES'
