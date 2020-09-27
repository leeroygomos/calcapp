package main

import "C"
import (
	"strconv"
)

//export DecToBin
func DecToBin(n int64) *C.char {
	binary := strconv.FormatInt(n, 2)
	return C.CString(binary)
}

//export BinToDec
func BinToDec(n *C.char) int64 {
	decimal, _ := strconv.ParseInt(C.GoString(n), 2, 64)
	return decimal
}

//export DecToHex
func DecToHex(n int64) *C.char {
	hex := strconv.FormatInt(n, 16)
	return C.CString(hex)
}

//export HexToDec
func HexToDec(n *C.char) int64 {
	decimal, _ := strconv.ParseInt(C.GoString(n), 16, 64)
	return decimal
}

func main() {
	// test := DecToBin(123)
	// fmt.Println(test)
	// test2 := BinToDec("1111011")
	// fmt.Println(test2)
	// test3 := DecToHex(10)
	// fmt.Println(test3)
	// test4 := HexToDec("ff6")
	// fmt.Println(test4)
}
