## 题目名称
爱拼才会赢

## 题目描述
规则很简单，拼完就给flag

题目地址：http://ctfshow.gitee.io/subject_puzzle/

## 出题/解题思路

4600*1950=2x2x2x5x5x23 x 2x3x5x5x13=50*4*23 * 50*3*13=200*150 * 23*13

23*13的拼图，拼上给flag，每块一个图，一个value值。图是乱序可拼，value是纯乱序无规律，最后的flag值是md5(18进制乱序值串)

验证逻辑：每个图片碎片的文件名（如0a、0b）从左到右从上到下串成一个字符串，当字符串的

sha256=be2b50b9468fae9a9dd7990d51270bcafccc6d34c2e1aeb7308d0f99634ca2d0

时alert弹出flag: flag{md5(字符串)}，最终拼成的字符串为
```
5c2b316b52956639ece7fegac857dabcf8g0fff582b4b724d8cha4ag3341094d03760108290e04f1f38a70e1e25edcc50d96e6e53837g81a9f7ca1f77f835380614a435d7915403646ddf4ae5h1d026922458e994c0c1gehb875g2g926f997e41cfc1471c2ahc9fdd60f3234c08f8c922f3afaea72cbb23060g3fbf23cdh2ee0f6dgc613b0749d1h1e19db182cc1a89b8h5g6f472g2d4ef0d28g3b7b786g5554affgeg49b66a4b3gb99a7a77bhb3cc51874he9100bed94ac67dece86a0c4aabbfh7hg59e0a0h3hd45a4f123e642365a7cd11a97gbg2abd275f215025eeg67d9ca62881cgd9598990b19h8842bfef633fg11febc36c586h16b50gg784627e3556a3c7856dd5cae39g8d6edf173d1b068b44d3g420abd0a25ba59398d791cf2h734gba4868d10507e8adbe
```

可以用python脚本自动匹配跑出一个差不多的字符串（碎片图自行下载，放到data文件夹），配合js，把剩下的手动拼好，为了查看方便还可以把下面css去掉
```css
.hang div {
    width: 60px;
    height: 45px;
    float: left;
    background-repeat: round;
    /* margin-left: 1px; */
    /* margin-top: 1px; */
}
```

另外，拼图有解：
1.把格子中数横向排成一行，
2.f(s)表示s前比s小的数的数目，计算f(8)+f(7)+...+f(1)
3.若结果为偶数，则有解，否则无解。


## flag
```
flag{a2b91480e984bc6da4a98ae0fc990214}
```
