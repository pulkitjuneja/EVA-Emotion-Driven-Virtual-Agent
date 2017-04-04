import bpy
import json

shapeKeyNames = ['AIE', 'MBP', 'O', 'UWQ', 'FV', ]
dataPathPrefix = "key_blocks[\""
dataPathSuffix = "\"].value"


def getShapeKeyAnimationInfo(mouthCue, fps):
    frames = (float(mouthCue['end']) - float(mouthCue['start'])) * fps
    frames = round(frames)
    print (frames) 
    phoneme = mouthCue['value']
    for name in shapeKeyNames:
        if phoneme in name:
            return (frames, name)


def addFaceShapeKeyFrame(shapeKeyName, previousKeyName, startFrame, frameCount):
    faceShapeKeyParent = bpy.data.meshes['face'].shape_keys
    dataPath = dataPathPrefix + shapeKeyName + dataPathSuffix
    faceShapeKeyParent.key_blocks[shapeKeyName].value = 0.0
    faceShapeKeyParent.keyframe_insert(dataPath, frame=startFrame)
    faceShapeKeyParent.key_blocks[shapeKeyName].value = 1.0
    finalFrame = startFrame + frameCount
    if previousKeyName != None:
         dataPathPrevious = dataPathPrefix + previousKeyName + dataPathSuffix
         faceShapeKeyParent.key_blocks[previousKeyName].value = 0.0
         faceShapeKeyParent.keyframe_insert(dataPathPrevious, frame=finalFrame)
    faceShapeKeyParent.keyframe_insert(dataPath, frame=finalFrame)


def main():
    fps = bpy.context.scene.render.fps
    clearAllAnimation()
    with open('D:\\Projects\\EVA\\COMPLEX MODEL\\scripts\\phoneme.json') as myfile:
        data = myfile.read().replace('\n', '')
    phonemes = json.loads(data)
    mouthCues = phonemes['mouthCues']
    previousKey = None
    framecounter = 1
    for x in mouthCues:
        animationData = getShapeKeyAnimationInfo(x, fps)
        addFaceShapeKeyFrame(
            animationData[1], previousKey, framecounter, animationData[0])
        previousKey = animationData[1]
        framecounter += animationData[0]+1


def clearAllAnimation():
    faceShapeKeyParent = bpy.data.meshes['face'].shape_keys
    faceShapeKeyParent.animation_data_clear()


if (__name__ == "__main__"):
    main()
