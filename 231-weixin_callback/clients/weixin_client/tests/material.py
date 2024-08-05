"""
pytest weixin_client/tests/material.py -s
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


def test_upload_img_success():
    """
    pytest weixin_client/tests/material.py::test_upload_img_success -s
    """
    # 模拟成功上传图像
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    img_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.upload_img(token, img_path)
    # print(resp_json)
    assert "url" in resp_json


def test_get_material_list_success():
    """
    pytest weixin_client/tests/material.py::test_get_material_list -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_material_list(token, 'news')
    # print(resp_json)
    assert 'item_count' in resp_json
    assert 'total_count' in resp_json
    assert 'item' in resp_json


def test_get_material_count_success():
    """
    pytest weixin_client/tests/material.py::test_get_material_count -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    resp_json = wx_client.get_material_count(token)
    # print(resp_json)
    assert 'voice_count' in resp_json
    assert 'video_count' in resp_json
    assert 'news_count' in resp_json
    assert 'image_count' in resp_json


def test_add_material_success():
    """测试添加素材
    pytest weixin_client/tests/material.py::test_add_material_success -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    print(resp_json)
    assert "url" in resp_json
    assert "media_id" in resp_json
    media_id = resp_json['media_id']
    wx_client.del_material(token, media_id)


def test_add_material_by_content_success():
    """测试添加素材，传二进制
    pytest weixin_client/tests/material.py::test_add_material_by_content_success -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    with open(media_path, 'rb') as f:
        resp_json = wx_client.add_material_by_content(token, 'image', f, '微信图标', '微信图标')
        print(resp_json)
        assert "url" in resp_json
        assert "media_id" in resp_json
        media_id = resp_json['media_id']
        wx_client.del_material(token, media_id)


def test_add_material_by_io_success():
    """测试添加素材，传二进制
    pytest weixin_client/tests/material.py::test_add_material_by_io_success -s
    """
    import io
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']
    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    with open(media_path, 'rb') as f:
        mem_io = io.BytesIO()
        with open(mem_io, 'wb') as mem_file:
            mem_file.setparams(f.getparams())
            mem_file.writeframes(f.readframes(f.getnframes()))

            resp_json = wx_client.add_material_by_content(token, 'image', mem_file, '微信图标', '微信图标')
            print(resp_json)
            assert "url" in resp_json
            assert "media_id" in resp_json
            media_id = resp_json['media_id']
            wx_client.del_material(token, media_id)


def test_get_material_success():
    """测试获取素材
    pytest weixin_client/tests/material.py::test_get_material -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')
    assert "media_id" in resp_json
    # print(resp_json)
    media_id = resp_json['media_id']
    content = wx_client.get_material(token, media_id)
    # print(content)
    wx_client.del_material(token, media_id)


def test_get_material_not_found():
    """测试获取素材
    pytest weixin_client/tests/material.py::test_get_material_not_found -s
    """
    from weixin_client.errors import InvaildMaterialError
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    with pytest.raises(InvaildMaterialError):
        wx_client.get_material(token, 'invaild_media_id')


def test_del_material_success():
    """测试删除素材
    pytest weixin_client/tests/material.py::test_del_material -s
    """
    wx_client = WeiXinClient()
    resp_json = wx_client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    token = resp_json['access_token']

    media_path = os.path.join(BASE_DIR, 'weixin.jpg')
    resp_json = wx_client.add_material(token, 'image', media_path, '微信图标', '微信图标')

    media_id = resp_json['media_id']

    resp_json = wx_client.del_material(token, media_id)
    # print(resp_json)
    assert "errcode" in resp_json
    assert resp_json["errcode"] == 0
