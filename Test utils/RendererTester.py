import Renderer
import os
# file_path = os.path.join("/absolute/directory/path", "file.txt")

# Set the path to the input Blender file
BLENDER_FILE="/home/tenith/Downloads/untitledfolder3/0.blend"

# Set the path to the output image
OUTPUT_IMAGE="/home/tenith/Downloads/untitledfolder3/image.blend"

FRAME_NUMBER=str(90)

for num in Renderer.ImageRenderer(BLENDER_FILE, "PNG", FRAME_NUMBER, OUTPUT_IMAGE):
    print(num)

