import bpy;

faceMesh = bpy.data.meshes['face'];
faceShapeKeys = faceMesh.shape_keys;
dataPathAIE = "key_blocks[\"AIE\"].value";
dataPathO = "key_blocks[\"O\"].value"

frameCounter = 0 ;

for i in range(0,10) :
    for shape_key in faceShapeKeys.key_blocks :
        shape_key.value = 0 ;
    faceShapeKeys.key_blocks['AIE'].value = i%2 ;
    faceShapeKeys.key_blocks['O'].value = 1 - i%2;
    faceShapeKeys.keyframe_insert(dataPathAIE,frameCounter);
    faceShapeKeys.keyframe_insert(dataPathO,frameCounter);
    frameCounter+=10;

bpy.ops.screen.animation.play();
    
