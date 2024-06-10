from collections import OrderedDict  

vocab = OrderedDict()  
  
# 向词汇表中添加单词及其含义  
vocab['apple'] = 'A fruit that grows on trees.'  
vocab['banana'] = 'A yellow fruit that monkeys like.'  
vocab['cherry'] = 'A red fruit with a pit inside.'  
vocab['date'] = 'A sweet fruit that grows on palm trees.'  
  
# 遍历 OrderedDict 并打印出单词及其含义  
for word, definition in vocab.items():  
    print(f"{word}: {definition}")

输出：
apple: A fruit that grows on trees.  
banana: A yellow fruit that monkeys like.  
cherry: A red fruit with a pit inside.  
date: A sweet fruit that grows on palm trees.
