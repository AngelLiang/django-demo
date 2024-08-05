"""
pytest weixin_client/tests/publish.py -s
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


def test_get_publish_list():
    """
    pytest weixin_client/tests/publish.py::test_get_publish_list -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_success_publish_list(token)
    # print(resp_json)
    assert 'item_count' in resp_json
    assert 'total_count' in resp_json
    assert 'item' in resp_json


def test_publish_article():
    """
    pytest weixin_client/tests/publish.py::test_publish_article -s
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

    article_id = resp_json['media_id']
    resp_json = wx_client.publish_article(token, article_id)
    # print(resp_json)
    assert resp_json['errcode'] == 0
    assert 'publish_id' in resp_json
    assert 'msg_data_id' in resp_json


def test_get_publish():
    """
    pytest weixin_client/tests/publish.py::test_get_publish -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_article(token)
    # print(resp_json)
    assert 'item_count' in resp_json
    assert 'total_count' in resp_json
    assert 'item' in resp_json
