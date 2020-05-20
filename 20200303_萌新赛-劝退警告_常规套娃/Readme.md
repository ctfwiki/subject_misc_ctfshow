## 题目名称
劝退警告

## 题目描述
题如其名

hint：python lambda参考的unctf2019-Think ,混淆用的这个http://www.onelinerizer.com/

final hint: 你与flag的距离可能只是一个数字（check[0]改为check[1]）


## 出题/解题思路

第一关：解压缩的套路：爆破、明文攻击、伪加密、信息提示。稍微改变了一下套路的呈现方式，还加入了数独游戏

第二关：silenteye图片隐写

第三关：使用uncompyle6反编译pyc文件

第四关：python混淆，无奈hint给出了修改方法

其他

一、明文攻击的坑
1. 保存文件的大小不一致：电脑记事本保存时文件编码是ANSI（另存为时可以看到编码），每个汉字2字节；使用文本编辑器保存utf-8时需要没有bom头，bom头多占3字节
2. 明文攻击无法停止：明文攻击时指定秘钥（文件crc32），明文攻击开始后第一步是恢复文件，当看到第二步的恢复口令时就可以停止了

二、最后一步也可以当做re做
```python
import time

# 代码

time.sleep(3)
```

## flag
```
略
```
