import bpy
import socket


class socketModal(bpy.types.Operator):
  bl_idname = "object.modal_operator"
  bl_label = "Lip synch Operator"

  def __init__(self):
        print("Listen Start")
        self.port = 1301

  def __del__(self):
        print("Listen End")

  def invoke(self, contect, event):
      self.execute(context)
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.socket.bind(("127.0.0.1", self.port))
      print('socket listening on port', port)
      return {'RUNNING_MODAL'}

  def execute(self, context):
      print("execute function called")
      return {'FINISHED'}

  def modal (self, context, event):
      data,addr = self.socket.recvfrom (1024*1024)
      print data
      if event.type == 'BACK_SLASH':
        return {'FINISHED'}



bpy.utils.register_class (socketModal)        
