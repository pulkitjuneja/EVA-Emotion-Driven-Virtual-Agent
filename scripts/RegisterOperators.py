import sys 
import bpy

absolutePathMac = "/Users/pulkitjuneja/Documents/projects/EVA/scripts"
absolutePathWindows = "D:\\Projects\\EVA\\scripts"
sys.path.append(absolutePathMac)

from SocketOperator import socketModal
from EndAnimationOperator import EndAnimationOperator

try:
  bpy.utils.unregister_class(socketModal)
except BaseException:
  print ("socket modal not registered")
try:  
  bpy.utils.unregister_class(EndAnimationOperator)
except BaseException:
  print ('End Animation not registered');

bpy.utils.register_class(socketModal)
bpy.utils.register_class(EndAnimationOperator)