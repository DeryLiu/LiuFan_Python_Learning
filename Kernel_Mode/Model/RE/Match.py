'''
# Match
# Match对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。
'''

'''
# 方法：
1. group([group1, …])：获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
group可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。

2. groups([default])：以元组形式返回全部分组截获的字符串。
相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。

3. groupdict([default])：返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。
default表示没有截获字符串的组以这个值替代，默认为None。

4. start([group])：
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。

5. end([group])：返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。
group默认值为0。

6. span([group])：
返回(start(group), end(group))。

7. expand(template)：将匹配到的分组代入template中然后返回。
template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。
'''

import re
# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)
print("m.group():", m.group())
print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\g<2> \g<1>\g<3>'):", m.expand(r'\2 \1\3'))

### print output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
if match:
     # 使用Match获得分组信息
    print(match.group())
### 输出 ###
# hello


s = "12abc345ab"
m = re.match(r"\d+", s)
m.group(), m.span()
# ('12', (0, 2))

m = re.search(r"\d{3,}", s)
m.group(), m.span()
# ('345', (5, 8))

m = re.search(r"\d+", s)
m.group(), m.span()
# ('12', (0, 2))