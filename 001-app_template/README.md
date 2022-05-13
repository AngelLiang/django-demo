# 使用模板创建django的app

    django-admin startapp --template=app_name my_app

## 目录说明

```
├─admin         # 本app的admin管理端
├─apis          # 本app的api代码
├─forms         # 本app的表单代码
├─management    
│  └─commands   # 本app的 django 命令
├─migrations    # 本app的数据库迁移文件
├─models        # 本app的模型代码
├─resources     # 和import_export插件相关，存放导入导出类
├─selectors     # 存放从数据库读取的业务代码
├─serializers   # 和api相关，序列化和反序列化的代码
├─services      # 存放写入数据库的业务代码
├─templates     # django 的模板
│   └─admin     # 本app的django admin的模板
├─__init__.py   # 本目录作为python包
├─tests.py      # 测试代码
├─urls.py       # URL路由
└─views.py      # 视图代码
```
