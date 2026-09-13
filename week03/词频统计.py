# 1. 让用户输入一段英文句子（提示：input）
sentence = input("请输入一个英文句子：")

# 2. 用 split() 把它拆成单词列表
words = sentence.split()

# 3. 建一个空字典 counts = {}
counts = {}

# 4. 遍历每个单词：如果已在字典里就+1，否则设成1
for w in words:
    counts[w] = counts.get(w, 0) + 1
#    （提示：用 counts.get(w, 0) 这一行能省掉if判断）
# 5. 打印每个词和它的次数
for w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(w, c)
# for w in counts:
#     print(w, counts[w])
