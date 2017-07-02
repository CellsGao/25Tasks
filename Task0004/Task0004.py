# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

file = open("task0004.txt", "r")
line = file.read()

reObj = re.compile("\b?(\w+)\b?")
words = reObj.findall(line)

word_dict = dict()

for word in words:
    if word.lower() in word_dict:
        word_dict[word.lower()] += 1
    else:
        word_dict[word] = 1

for key, value in word_dict.items():
    print(key+" "+str(value))
