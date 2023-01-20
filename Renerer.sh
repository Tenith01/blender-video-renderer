#!/bin/bash

# Set the path to the blenderplayer executable
BLENDER_BIN="/path/to/blenderplayer"

# Set the path to the input Blender file
BLENDER_FILE="/home/tenith/Downloads/untitledfolder3/0.blend"

# Set the path to the output image
OUTPUT_IMAGE="/home/tenith/Downloads/untitledfolder3/image.blend"

FRAME_NUMBER=80

# Render the Blender file
#blender -b $BLENDER_FILE -o $OUTPUT_IMAGE -f "####" -s $START_FRAME_NUMBER -e $END_FRAME_NUMBER -a
#blender -b $BLENDER_FILE -o $OUTPUT_IMAGE -f $FRAME_NUMBER -a
blender -b $BLENDER_FILE -F PNG -o $OUTPUT_IMAGE -f $FRAME_NUMBER
#blender -b "11.blend" -F PNG -f 160 -o png/image `