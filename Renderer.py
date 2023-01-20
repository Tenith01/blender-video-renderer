import subprocess

import bpy


def ImageRenderer(blenderFilePath, exportPath):
    # cmd = "blender -b " + blenderFilePath + " -F " + exportType + " -f " + selectedFrame + " -o " + exportPath
    # cmd = "blender -b " + blenderFilePath + " -o " + exportPath + " -f " + selectedFrame
    # cmd = 'blender -b ' + blenderFilePath + ' -F ' + exportType + ' -o ' + exportPath + ' -f ' + selectedFrame
    # cmd = 'blender -b ' + blenderFilePath + ' -o ' + exportType + ' -F ' + exportPath
    cmd = 'blender -b ' + blenderFilePath + ' -a '
    # blender -b $blend_file -o $output_file -F $output_format
    # blender - b "C:\Users\Tenith\Desktop\Mundus Card\02 Silver Mundus Card.blend" - a

    # Get end frame
    bpy.ops.wm.open_mainfile(filepath=blenderFilePath)
    end_frame = bpy.context.scene.frame_end
    # print("End Frame: " + str(end_frame))

    # subprocess.run(['xdg-open', blenderFilePath])
    # run the command and open a pipe to read its output
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    progressbarValue = 0;
    progressbarValue2 = 0;
    rendererStat = "";
    # read the output line by line
    for line in iter(process.stdout.readline, b''):

        outPutLine = line.decode().strip().split('|')[-1]


        frameline =line.decode().strip().split('|')[0].split(" ")[0].split(":")[-1]
        if frameline.isdigit():
            # print(frameline)
            progressbarValue2 = int(int(frameline) / int(end_frame) * 100)
            # print(progressbarValue2)
        # print(progressbarValue2)
        outPutLine = outPutLine.split(" ")


        # print(outPutLine)
        if len(outPutLine) >= 2:
            if outPutLine[1] == "Syncing":
                rendererStat = "Syncing..."
                a = 0
            elif outPutLine[1] == "Rendering":
                max_value = outPutLine[-2]
                value = outPutLine[-4]
                progressbarValue = int(int(value) / int(max_value) * 100)

                # print("Rendering :", progressbarValue, "%")
                rendererStat = "Rendering..."

            elif outPutLine[1] == "Tile":
                # print(outPutLine)
                max_value = outPutLine[-1].split('-')[-1]
                value = outPutLine[-1].split('-')[-2]
                progressbarValue = int(int(value) / int(max_value) * 100)

                # print("Compositing :", progressbarValue, "%")
                rendererStat = "Compositing..."
            # print(outPutLine)

        yield rendererStat, progressbarValue, progressbarValue2


#
#
def say_hello():
    print("Hello World")
