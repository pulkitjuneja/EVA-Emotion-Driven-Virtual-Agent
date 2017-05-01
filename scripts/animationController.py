import bpy
import json

shapeKeyNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X']
dataPathPrefix = "key_blocks[\""
dataPathSuffix = "\"].value"


def getShapeKeyAnimationInfo(mouthCue, fps):
    frames = (float(mouthCue['end']) - float(mouthCue['start'])) * fps
    frames = round(frames)
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
    if previousKeyName != None and previousKeyName != shapeKeyName:
        dataPathPrevious = dataPathPrefix + previousKeyName + dataPathSuffix
        faceShapeKeyParent.key_blocks[previousKeyName].value = 0.0
        faceShapeKeyParent.keyframe_insert(dataPathPrevious, frame=finalFrame)
    faceShapeKeyParent.keyframe_insert(dataPath, frame=finalFrame)


def addJawShapeKeyFrame(shapeKeyName, previousKeyName, startFrame, frameCount):
    jawShapeKeyParent = bpy.data.meshes['jaw'].shape_keys
    jawKeyName = getJawKeyName(shapeKeyName)
    dataPath = dataPathPrefix + jawKeyName + dataPathSuffix
    previousJawKeyName = None
    if previousKeyName:
        previousJawKeyName = getJawKeyName(previousKeyName)
        dataPathPrev = dataPathPrefix + previousJawKeyName + dataPathSuffix
    finalFrame = startFrame + frameCount
    print (jawKeyName , previousJawKeyName)
    if previousJawKeyName != None and previousJawKeyName != jawKeyName:
        jawShapeKeyParent.key_blocks[jawKeyName].value = 0.0
        jawShapeKeyParent.keyframe_insert(dataPath, frame=startFrame)
        jawShapeKeyParent.key_blocks[previousJawKeyName].value = 0.0
        jawShapeKeyParent.keyframe_insert(dataPathPrev, frame=finalFrame)
    jawShapeKeyParent.key_blocks[jawKeyName].value = 1.0
    jawShapeKeyParent.keyframe_insert(dataPath, frame=finalFrame)


def getJawKeyName(shapeKeyName):
    if shapeKeyName in ['D', 'H']:
        return 'W'
    if shapeKeyName in ['C', 'E', 'F', 'G']:
        return 'M'
    if shapeKeyName in ['X', 'A', 'B']:
        return 'C'


def main(context, data):
    scene = context.scene
    scene.render.fps = 60
    fps = scene.render.fps
    clearAllAnimation()
    phonemes = json.loads(data)
    mouthCues = phonemes['mouthCues']
    previousKey = None
    framecounter = 1
    for x in mouthCues:
        animationData = getShapeKeyAnimationInfo(x, fps)
        addFaceShapeKeyFrame(animationData[1], previousKey, framecounter, animationData[0])
        addJawShapeKeyFrame(animationData[1], previousKey, framecounter, animationData[0])
        previousKey = animationData[1]
        framecounter += animationData[0]
    scene.frame_set(1)
    scene.frame_end = framecounter + 1
    bpy.ops.screen.animation_play()


def clearAllAnimation():
    faceShapeKeyParent = bpy.data.meshes['face'].shape_keys
    faceShapeKeyParent.animation_data_clear()


if (__name__ == "__main__"):
    main()
