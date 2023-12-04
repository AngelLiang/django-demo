import pytest
from model_bakery import baker
from django.contrib.auth.models import User
from action_log.services import ActionLogService
from action_log.models import ActionLog


@pytest.fixture
def create_user():
    return baker.make(User)


@pytest.fixture
def create_action_log(create_user):
    return baker.make(ActionLog, actor=create_user.username)


@pytest.fixture
def action_log_service(create_user):
    service = ActionLogService()
    service.request = type(
        'Request', (), {'remote_user': create_user.username})
    return service


@pytest.mark.django_db
def test_add_add_log(action_log_service, create_user):
    # 创建一个用于测试的模型实例
    fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined']
    test_model = baker.make(User, _fill_optional=fields)

    action_log_service.add_add_log(test_model, fields)

    # 检查日志是否正确添加
    action_log = ActionLog.objects.last()
    print(action_log.change_text)
    assert action_log.action.startswith('添加')
    assert action_log.type == ActionLog.ADD
    assert action_log.actor == create_user.username
    assert action_log.table_name == test_model._meta.db_table
    assert action_log.row_id == str(test_model.pk)


@pytest.mark.django_db
def test_add_update_log(action_log_service, create_user):
    # 创建用于测试的旧模型和新模型实例
    fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined']
    old_model = baker.make(User, _fill_optional=fields)
    new_model = baker.prepare(User, _fill_optional=fields)
    

    action_log_service.add_update_log(old_model, new_model, fields)

    # 检查日志是否正确添加
    action_log = ActionLog.objects.last()
    print(action_log.change_text)
    assert action_log.action.startswith('修改')
    assert action_log.type == ActionLog.UPDATE
    assert action_log.actor == create_user.username
    assert action_log.table_name == old_model._meta.db_table
    assert action_log.row_id == str(old_model.pk)


@pytest.mark.django_db
def test_add_del_log(action_log_service, create_user):
    # 创建一个用于测试的模型实例
    test_model = baker.make(User)

    action_log_service.add_del_log(test_model)

    # 检查日志是否正确添加
    action_log = ActionLog.objects.last()
    print(action_log.change_text)
    assert action_log.action.startswith('删除')
    assert action_log.type == ActionLog.DELETE
    assert action_log.actor == create_user.username
    assert action_log.table_name == test_model._meta.db_table
    assert action_log.row_id == str(test_model.pk)
