import platform
import socket
import os
import sys
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

print(f"\nProcess {os.getpid()} Forking now")
pid = os.fork()

if pid == 0:
    # Child Process
    print(f"\n[Child PID: {pid} has Parent Process ID: {os.getppid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"[Child Process {os.getpid()}] File Contents: {os.read(file_handle, 100).decode()}")

    os.close(file_handle)
    sys.exit(0)
else:
    # Parent Process
    print(f"\n[parent process ID: {os.getpid()}] , Child PID: {pid}")
    print("Wait for the child to complete modification")
    os.wait()
    print("Child Process Finished the modification") 
    file_object_TextIO.close()

print(f"\n[Process {os.getpid()}] File Closed.Exiting now ...")
sys.exit(0)

