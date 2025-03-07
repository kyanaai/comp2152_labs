import platform
import socket
import os
print("Current machine Type")
print(platform.machine())
print("=====================================")

print("Current Processor Type")
print(platform.architecture())
print("=====================================")

print("Set Socket Time Out to 50 Seconds")
print(socket.setdefaulttimeout(50))
print("Get the Current Socket Timeout")
print(socket.getdefaulttimeout())
print("=====================================")

print("Get the Current Operating System Type")
print(os.name)
print("=====================================")

print("Get the Operating System Name")
print(platform.system())
print("=====================================")

print("Current Process ID")
print(os.getpid())
print("=====================================")

file_name = "fdpractice.txt"
print("\n[Before Fork] Process {os.getpid()}")

file_handle=os.open(file_name , os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] opened file_handle : {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w+")

file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()