package main

import (
	"fmt"
	"strconv"
)

func removeStars(s string) string {
	stack := []byte{}
	for i := range s {
		if s[i] != '*' {
			stack = append(stack, s[i])
		} else {
			if len(stack) != 0 {
				stack = stack[:len(stack)-1]
			}
		}
	}
	return string(stack)
}
func asteroidCollision(asteroids []int) []int {
	stack := []int{}
	for _, astr := range asteroids {
		if astr > 0 {
			stack = append(stack, astr)
		} else {
			isDestr := false
			for len(stack) > 0 && stack[len(stack)-1] > 0 {
				val := stack[len(stack)-1]
				if val < (-astr) {
					stack = stack[:len(stack)-1]
				} else {
					if val == (-astr) {
						stack = stack[:len(stack)-1]
					}
					isDestr = true
					break
				}
			}
			if isDestr {
				stack = append(stack, astr)
			}
		}
	}
	return stack
}
func reverseRunes(runes []rune) {
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
}
func kDuplicate(runes []rune, k int) []rune {
	if k <= 0 {
		return []rune{}
	}
	original := append([]rune(nil), runes...)
	for i := 1; i < k; i++ {
		runes = append(runes, original...)
	}
	return runes
}

func decodeString(s string) string {
	stack := []rune{}
	for _, rn := range s {
		if rn != ']' {
			stack = append(stack, rn)
		} else {
			wrd := []rune{}
			kr := []rune{}
			for len(stack) > 0 && stack[len(stack)-1] != '[' {
				val := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				wrd = append(wrd, val)
			}
			stack = stack[:len(stack)-1]
			for len(stack) > 0 && stack[len(stack)-1] >= '0' && stack[len(stack)-1] <= '9' {
				val := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				kr = append(kr, val)
			}
			reverseRunes(wrd)
			reverseRunes(kr)
			k, _ := strconv.Atoi(string(kr))
			stack = append(stack, kDuplicate(wrd, k)...)

		}

	}
	return string(stack)
}
func main() {
	ast := []int{8, -8}
	fmt.Println(asteroidCollision(ast))

}
