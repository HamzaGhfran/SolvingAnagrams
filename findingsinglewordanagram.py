"""Code to find single word anagrams"""
import loaddictionary as ld
word_list = ld.load("2of4brif.txt")
name = input("Enter a word to find its anagram: ")
name = name.lower()

name_sorted = sorted(name)
anagram_list = []
for word in word_list:
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

print(anagram_list)
