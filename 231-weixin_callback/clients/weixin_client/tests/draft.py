"""
pytest weixin_client/tests/draft.py -s
"""
import os
import sys
from dotenv import load_dotenv
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.getcwd())

env_path = os.path.join(os.getcwd(), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

WEIXIN_APPID = os.getenv('WEIXIN_APPID')
WEIXIN_APPSECRET = os.getenv('WEIXIN_APPSECRET')
if not WEIXIN_APPID:
    raise ValueError('appid错误')
if not WEIXIN_APPSECRET:
    raise ValueError('appsecret错误')

from weixin_client.client import WeiXinClient


def test_get_draft_list():
    """测试获取草稿列表
    pytest weixin_client/tests/draft.py::test_get_draft_list -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_draft_list(token)
    # print(resp_json)
    assert 'item_count' in resp_json
    assert 'total_count' in resp_json
    assert 'item' in resp_json


def test_get_draft_count():
    """测试获取草稿总数
    pytest weixin_client/tests/draft.py::test_get_draft_count -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_draft_count(token)
    # print(resp_json)
    assert 'total_count' in resp_json


def test_add_draft():
    """测试添加草稿
    pytest weixin_client/tests/draft.py::test_add_draft -s
    """
    from weixin_client.schemas import make_article

    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    media_id = resp_json['media_id']

    article = make_article('这是测试标题', '这是测试内容', media_id)
    articles = [article]
    resp_json = wx_client.add_draft(token, articles)
    # print(resp_json)
    # assert "url" in resp_json
    assert "media_id" in resp_json


def test_add_many_article():
    """测试添加草稿的时候创建多个文章
    pytest weixin_client/tests/draft.py::test_add_many_article -s
    """
    from weixin_client.schemas import make_article

    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    media_id = resp_json['media_id']

    article1 = make_article('这是第一个测试标题', '这是第二个测试内容', media_id)
    article2 = make_article('这是第二个测试标题', '这是第二个测试内容', media_id)
    articles = [article1, article2]
    resp_json = wx_client.add_draft(token, articles)
    # print(resp_json)
    # assert "url" in resp_json
    assert "media_id" in resp_json


def test_get_draft_detail():
    """测试获取草稿详情
    pytest weixin_client/tests/draft.py::test_get_draft_detail -s
    """
    from weixin_client.schemas import make_article

    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    media_id = resp_json['media_id']

    article = make_article('这是测试标题', '这是测试内容', media_id)
    articles = [article]
    resp_json = wx_client.add_draft(token, articles)
    print(f'add_draft:{resp_json}')
    # assert "url" in resp_json
    # assert "media_id" in resp_json
    media_id = resp_json['media_id']

    resp_json = wx_client.get_article(token, media_id)
    print(resp_json)
    # assert 'item_count' in resp_json
    # assert 'total_count' in resp_json
    assert 'item' in resp_json


def test_update_draft():
    """测试更新草稿
    pytest weixin_client/tests/draft.py::test_update_draft -s
    """
    from weixin_client.schemas import make_article

    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    media_id = resp_json['media_id']

    article = make_article('这是测试标题', '这是测试内容', media_id)
    articles = [article]
    resp_json = wx_client.add_draft(token, articles)
    draft_id = resp_json['media_id']

    article = make_article('这是修改后的测试标题', '这是修改后的测试内容', media_id)
    resp_json = wx_client.update_draft(token, draft_id, article)
    # print(resp_json)
    # assert "url" in resp_json
    assert resp_json["errcode"] == 0


def test_del_draft():
    """测试删除草稿
    pytest weixin_client/tests/draft.py::test_del_draft -s
    """
    from weixin_client.schemas import make_article

    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    media_id = resp_json['media_id']

    article = make_article('这是测试标题', '这是测试内容', media_id)
    articles = [article]
    resp_json = wx_client.add_draft(token, articles)
    draft_id = resp_json['media_id']

    resp_json = wx_client.del_draft(token, draft_id)
    # print(resp_json)
    # assert "errcode" in resp_json
    assert resp_json['errcode'] == 0
