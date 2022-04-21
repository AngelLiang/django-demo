# django 使用 dumpdata 导出数据

对于通常从一个项目转储并加载到另一个项目，您需要 dumpdata排除 ContentType和 Auth Permissions对象的命令，因为这些通常会阻止第一次加载数据。我还希望它进入 JSON 文件并具有缩进以使其更具可读性。执行此操作的命令是：

    python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > dump.json

