from ctypes import *
import os

# lib = cdll.LoadLibrary("./conversion.so")
lib = cdll.LoadLibrary(os.path.abspath("./home/functions/conversion.so"))

lib.DecToHex.argtypes = [c_longlong]
lib.DecToHex.restype = c_char_p
lib.DecToBin.argtypes = [c_longlong]
lib.DecToBin.restype = c_char_p
lib.HexToDec.argtypes = [c_char_p]
lib.HexToDec.restype = c_longlong
lib.BinToDec.argtypes = [c_char_p]
lib.BinToDec.restype = c_longlong


def DecToHex(n):
    val = lib.DecToHex(n)
    return val.decode('utf-8')

def DecToBin(n):
    val = lib.DecToBin(n)
    return val.decode('utf-8')

def HexToBin(n):
    temp = lib.HexToDec(n.encode('utf-8'))
    val = lib.DecToBin(temp)
    return val.decode('utf-8')

def HexToDec(n):
    val = lib.HexToDec(n.encode('utf-8'))
    return val

def BinToHex(n):
    temp = lib.BinToDec(n.encode('utf-8'))
    val = lib.DecToHex(temp)
    return val.decode('utf-8')

def BinToDec(n):
    val = lib.BinToDec(n.encode('utf-8'))
    return val