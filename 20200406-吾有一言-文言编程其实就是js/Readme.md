## 题目名称
吾有一言

## 题目描述
吾有一言，不知当讲否。

hint: https://github.com/LingDong-/wenyan-lang

## 出题/解题思路
这种花里胡哨又没有什么实际用途的东西最适合用来出题了。把flag进行base16编码，然后字符替换成十二生肖+驴（因为base16后有13种字符）。

先写js，为了转文言后不突兀，变量名方法名都使用的中文，去掉最后的function调用，在线工具转为文言文代码: https://zxch3n.github.io/wenyanizer/

解题可以使用在线IDE: https://ide.wy-lang.org/

调用“弗萊格”方法flag就会输出。可以转为js代码调用执行，也可以直接在原文言上调用运行。

## 非预期
人工翻译成其他语言、人工解密。本来不复杂，自己增加题目难度。

## flag

```
flag{can~you~speak~chi~ness~}
```
