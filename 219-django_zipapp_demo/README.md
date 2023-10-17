# 使用 zipapp 打包 django 示例


1、用 pip 将应用程序的所有依赖项装入 dist 目录

```
python -m pip install -r requirements.txt --target dist
```

2、把相关程序拷贝进dist

```
cp app dist/
cp config dist/
cp manage.py dist/
```

3、打包

```
python -m zipapp -p "interpreter" dist
```

运行程序

```
python dist.pyz
```

ref: https://docs.python.org/zh-cn/3/library/zipapp.html
