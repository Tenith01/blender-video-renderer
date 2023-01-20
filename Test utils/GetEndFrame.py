import bpy

# Set the location of the blend file
blend_file = '/home/tenith/Downloads/untitledfolder3/0.blend'

# Open the blend file
bpy.ops.wm.open_mainfile(filepath=blend_file)

# Get the end frame of the blend file
end_frame = bpy.context.scene.frame_end

# Print the end frame
print("End Frame:", end_frame)