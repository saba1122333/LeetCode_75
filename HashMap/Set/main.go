package main

import (
	"sort"
	"strconv"
	"strings"
)

func findDifference(nums1 []int, nums2 []int) [][]int {
	nums1Map, nums2Map := make(map[int]bool), make(map[int]bool)
	diff1, diff2 := []int{}, []int{}

	for _, v := range nums1 {
		if _, ok := nums1Map[v]; !ok {
			nums1Map[v] = true
		}
	}
	for _, v := range nums2 {
		if _, ok := nums2Map[v]; !ok {
			nums2Map[v] = true
		}
	}
	for v := range nums1Map {
		if _, ok := nums2Map[v]; ok {
			delete(nums1Map, v)
			delete(nums2Map, v)
		}
	}
	for v := range nums1Map {
		diff1 = append(diff1, v)
	}
	for v := range nums2Map {
		diff2 = append(diff2, v)
	}
	return [][]int{diff1, diff2}

}

func uniqueOccurrences(arr []int) bool {
	arrMap := make(map[int]int)
	occurances := []int{}
	for _, v := range arr {
		arrMap[v]++
	}

	for _, v := range arrMap {
		occurances = append(occurances, v)
	}
	sort.Ints(occurances)
	for i := 0; i < len(occurances)-1; i++ {
		if occurances[i] == occurances[i+1] {
			return false
		}
	}
	return true
}

func closeStrings(word1 string, word2 string) bool {
	freq1 := make(map[rune]int)
	freq2 := make(map[rune]int)
	if len(word1) != len(word2) {
		return false
	}
	for _, k := range word1 {
		freq1[k]++
	}
	for _, k := range word2 {
		freq2[k]++
	}

	for k := range freq1 {
		if _, ok := freq2[k]; !ok {
			return false
		}
	}

	f1 := []int{}
	f2 := []int{}
	for _, v := range freq1 {
		f1 = append(f1, v)
	}
	for _, v := range freq2 {
		f2 = append(f2, v)
	}
	sort.Ints(f1)
	sort.Ints(f2)
	for i := range f1 {
		if f1[i] != f2[i] {
			return false
		}
	}
	return true
}
func hash(nums []int) string {
	strs := []string{}
	for _, num := range nums {
		strs = append(strs, strconv.Itoa(num))
	}
	return strings.Join(strs, ",")
}
func equalPairs(grid [][]int) int {
	ans := 0
	hasMap := make(map[string]int)
	for _, row := range grid {
		key := hash(row)
		if _, ok := hasMap[key]; !ok {
			hasMap[key] = 1
		} else {
			hasMap[key]++
		}
	}
	for col := 0; col < len(grid[0]); col++ {
		column := []int{}
		for row := range grid {
			column = append(column, grid[row][col])
		}
		key := hash(column)
		if v, ok := hasMap[key]; ok {
			ans += v
		}
	}
	return ans
}
