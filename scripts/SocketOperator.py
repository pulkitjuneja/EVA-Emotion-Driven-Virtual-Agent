import bpy
import socket
import os
import sys

absolutePath = "/Users/pulkitjuneja/Documents/projects/EVA/scripts"
sys.path.append(absolutePath)

from animationController import main


class socketModal(bpy.types.Operator):
    bl_idname = "object.modal_operator"
    bl_label = "Lip synch Operator"
    _timer = None

    def __init__(self):
        print("Listen Start")
        os.chdir(absolutePath)
        self.port = 1301

    def __del__(self):
        print("Listen End")

    def execute(self, context):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setblocking(0)
        self.socket.bind(("127.0.0.1", self.port))
        print('socket listening on port', self.port)
        self._timer = context.window_manager.event_timer_add(1.0, context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):

        if event.type == "TIMER":
            data = None
            try:
                data = self.socket.recv(1024 * 1024)
            except socket.error:
                print ("no data") 
                return {"RUNNING_MODAL"}
            print(data)
        if event.type == 'BACK_SLASH':
            self.socket.close()
            return {'FINISHED'}
        return {'PASS_THROUGH'}


bpy.utils.register_class(socketModal)

import bpy
