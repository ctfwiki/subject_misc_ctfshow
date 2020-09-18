## 题目名称
迷惑行为大赏（之）无中生you

## 题目描述
![](xpy.png)

## 出题/解题思路

图片高度改为1024可以看见“密码：没技术，是菜鸡”（出题时既改了高度也改了crc32，所以不会报错）

图片附加加密压缩包，密码是“没技术，是菜鸡”，解压后得到文本文件

https://offdev.net/demos/zwsp-steg-js
https://www.umpox.com/zero-width-detection/
https://github.com/Macr0phag3/Zero-Width-Spaces-Hiden
0宽度字符解码，得到类似aes密码，先base64解码，去掉Salted__头，然后再TripleDes解码。

`SNOW.EXE -C -p "没技术，是菜鸡" -m "flag{l0ts_0f_?????????????}" infile.txt outfile.txt`
`SNOW.EXE -C -p "没技术，是菜鸡" outfile.txt`
得到空白，是SNOW隐写，解码得到flag

## flag

```
flag{l0ts_0f_?????????????}
```
