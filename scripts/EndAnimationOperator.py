import bpy 
import sys 


class EndAnimationOperator(bpy.types.Operator):

    bl_idname = "object.End_Animation_Operator"
    bl_label = "End Animation Operator"
    _timer = None
    

    def __init__(self):
        self.port = 1301

    def __del__(self):
        print("Listen End")

    def execute (self, context):
