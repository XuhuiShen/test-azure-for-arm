#! /usr/bin/env python
import ctypes
hello = ctypes.cdll.LoadLibrary('./hello.so')

hello.print_hello_world()
