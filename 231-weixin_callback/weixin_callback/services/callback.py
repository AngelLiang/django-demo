import time
from django.http.request import HttpRequest
from bs4 import BeautifulSoup
from weixin_callback.logger import logger

from .qrcode import LOGIN_SCENE_ID, QrcodeService


class CallBackService:

    def handle(self, message, appid=None):
        self.appid = appid
        html_doc = message.decode()
        self.soup = BeautifulSoup(html_doc, features="html.parser")
        logger.debug(f'soup:{self.soup}')
        # self.handle_text_mesage(self.soup)
        # self.handle_article_push_event()

    def handle_text_mesage(self, soup):
        """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[this is a test]]></Content>
            <MsgId>1234567890123456</MsgId>
            <MsgDataId>xxxx</MsgDataId>
            <Idx>xxxx</Idx>
        </xml>
        """
        pass

    def follow_message(self, soup):
        """关注公众号

        <xml>
            <ToUserName><![CDATA[gh_374784f4f9e0]]></ToUserName>
            <FromUserName><![CDATA[o0ExT6h5zYye3_YHQqVE0XEMAl6s]]></FromUserName>
            <CreateTime>1699953050</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[subscribe]]></Event>
            <EventKey><![CDATA[]]></EventKey>
            <Encrypt><![CDATA[ycXt9kzEzsm1uLRKwlEP8zYrUIFBaeVYINQWwuKFeT8Q2Edi4dQgAfzQL31tGopL1IAlYSMrDA2GhU7hjsSdgc9RmRUEH5wfl6xRZLN8zRq5qUoqqrs3FU7196sFcp2P1MHIVIZUHyLpteNaytwO3MM0M1YZSBSyfS9ZJLzdBQHbTNaosBwjoAAz+ZqNao2rI1CUgyqL5TXcYNlm3zwFXhJNDPtmjnmaqTzqok0BFhXPfaWCFZQngMi/CZ2t0dhiP8/OzSwyESiv2z9ywhFlfo5oI1xsXmVg9F0yjCmMmx8+HAzHP+1A0MAkq2uBN7xsycH0WHGwPQnluohz/Z/+I4L3tUrjZjUBnYUcNb84/H6jCeBC2uFOzHgkeRprrfSwYMt376WSwZyox2yj0lD4aLHnHPCD6LqQn2wCSjPnL6o=]]></Encrypt>
        </xml>
        """
        pass

    def is_event_publish_job_finish(self):
        if self.soup and self.soup.xml and self.soup.xml.event:
            return self.soup.xml.event.string == 'PUBLISHJOBFINISH'

    def get_msgtype(self):
        return self.soup.xml.msgtype.string

    def is_msgtype_event(self):
        return self.get_msgtype() == 'event'

    def get_publish_event_info(self):
        return self.soup.xml.publisheventinfo

    def get_publish_status(self) -> int:
        result = self.get_publish_event_info()
        publish_status = result.publish_status.string
        return int(publish_status)

    def get_publish_id(self) -> str:
        result = self.get_publish_event_info()
        publish_id = result.publish_id.string
        return str(publish_id)

    def get_article_id(self) -> str:
        result = self.get_publish_event_info()
        article_id = result.article_id.string
        return str(article_id)

    def get_article_url(self) -> str:
        result = self.get_publish_event_info()
        article_url = result.article_detail.item.article_url.string
        return str(article_url)

    def handle_article_push_event(self):
        """
        <xml>  
            <ToUserName><![CDATA[gh_374784f4f9e0]]></ToUserName>
            <FromUserName><![CDATA[o0ExT6mBFncZwh-K7-uWK3bVehtM]]></FromUserName>
            <CreateTime>1700126364</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[PUBLISHJOBFINISH]]></Event>
            <PublishEventInfo>
                <publish_id>2247483856</publish_id>
                <publish_status>0</publish_status>
                <article_id><![CDATA[IMXOr-XqmyMqD7EntdIWDTB4cMpm-6slW6U7acl0AO5L4DSwZk-1i74djpweYjLP]]></article_id>
                <article_detail>
                    <count>1</count>
                    <item>
                        <idx>1</idx>
                        <article_url><![CDATA[http://mp.weixin.qq.com/s?__biz=MzkzMTMyNzY5Ng==&mid=2247483856&idx=1&sn=d8c18252828b953668a34a3a454c5978&chksm=c26dfa6ff51a737959da7ce9e347091d0e37c08441123c34c4b5ca353c1f0538b12e08f780fd#rd]]></article_url>
                    </item>
                </article_detail>
            </PublishEventInfo>
            <Encrypt><![CDATA[OMn3RLuktUxMUC3JHG2YuomtgncpLrzawF9KVsZAhOXPjkRHeVi44HEfuDZk2HVR42D+qAOhY111Uyzp4/Szl/qWlm4lGnRjjLvpOTBZLcvN3XdAhKbRTROlgwxO+SJk4jvtuB62MIiWU9JEd/TE8B7rrrygawOdvRuwuv4rA7l0Mvc3yaU+jZ/E5NHJ5foOuWN/vIWON82zO88nkgF/jKR8aRsWA2sznlFkKjwF5xnmD0mjZMBqHA3aiv9G7HFaX9PqyZGUUaCGwSvC1kIIcuerYuFswkZQov3zVuPFmNou/L+Uev78g4C14ntlDCnnJevAmZ/yt9z8jBMfyXw8ljkWRYt6K8cErbrJgUu1W0O9Apjs2NS1aOd45LejMnMT2DkNxGzzoTNX9p9O6OCfq7YIgtZ9nOoUdiZMhvC5q+3DcX2TKr4/EV5oTrlLxDq7u4d/jVvIbEuIbutIq1YtEQWUQmbq850eCVvAfaygc499gFhpIxXmA7bLfaVOllw8LzD9OTH6u/Vq7FCFA88+4Sm0jv3iunNT6/ylDNmB6hcYVGBiu1GfHp4Wm5TSF/osBOiuKTL0skyIzGo/Lz+bwdkre7PoOxZkUKUL8POXyqBDuDxrpp+qH4/gz2iIPKeAmxv6W6/cVEhmWJdGjnlepeV8EqTn7O6hreHsWrpMZF6mX7oH8kzeYqjo7H69eQ3btri90Ym92nnEEAUMvWvV78ykpuoovQ9EkXHDQSJhgrvDCtKJ9C1xX8ULO6Jr+Yglr0rtu6gDUWMZ/0TyJXGqz+OHBj17B++kibUTEvNDLfft1vDLnz/y4tWeD7h3vdIovKrHJeh7ea+fAEMtjTXOUJR5ifaAS6DiNAOQchXdvAyN2S9pi2f8kw+uPT3vKwTZcFA7WoBad7MgmYcerT/5iFB8N1aWD8xuj5jZGKB9FNZT71smQ3TKSMIEvEXmVokyMrhbU2CtDSsVmTaNvZdPPU/S0C8jSWOUKGS9mNkntQabwVbYvH5fY3xjE1FiOR/HOBjgmpZn3riQQ/I5VLPnDpfRjNwWvxB6mH+H6xoElDzvEqmxP9sg5V6yMQGlLKhojvirnVmrYqLZ+oRyC+DncA==]]></Encrypt>
        </xml>

        ref: https://developers.weixin.qq.com/doc/offiaccount/Publish/Callback_on_finish.html
        """
        if not self.is_event_publish_job_finish():
            logger.debug('不是发布结束事件')
            return
        # article_id = self.get_article_id()
        # if not article_id:
        #     logger.debug('没有获取到文章id')
        #     return
        publish_id = self.get_publish_id()
        publish_status = self.get_publish_status()
        article_url = self.get_article_url()

        # WeiXinArticleLogService().update_article_log(publish_id, publish_status, article_url)
        logger.debug(f'update publish_id={publish_id}')

    def handle_scan_qrcode(self, request: HttpRequest):
        """
        扫描带参数二维码事件

        用户未关注时，进行关注后的事件推送，推送XML数据包示例：
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[subscribe]]></Event>
            <EventKey><![CDATA[qrscene_123123]]></EventKey>
            <Ticket><![CDATA[TICKET]]></Ticket>
        </xml>


        用户已关注时的事件推送，推送XML数据包示例：
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[SCAN]]></Event>
            <EventKey><![CDATA[SCENE_VALUE]]></EventKey>
            <Ticket><![CDATA[TICKET]]></Ticket>
        </xml>


        ref: https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_event_pushes.html#%E6%89%AB%E6%8F%8F%E5%B8%A6%E5%8F%82%E6%95%B0%E4%BA%8C%E7%BB%B4%E7%A0%81%E4%BA%8B%E4%BB%B6
        """
        html_doc = request.body.decode()
        if not html_doc:
            logger.debug('html doc empty')
            return 
        soup = BeautifulSoup(html_doc, features="html.parser")
        logger.debug(soup)
        data = self.parse_scan_qrcode_xml(soup)
        scene_int = self.parse_scan_scene_int(data['event'], data['event_key'], data['openid'])
        if scene_int == LOGIN_SCENE_ID:
            return self._handle_login_scene(data['openid'], data['to_user'], data['ticket'])

    def parse_scan_qrcode_xml(self, soup: BeautifulSoup) -> dict:
        logger.debug(soup)
        to_user = soup.xml.tousername.string
        openid = soup.xml.fromusername.string
        create_time = soup.xml.createtime.string
        msg_type = soup.xml.msgtype.string
        event = soup.xml.event.string
        event_key = soup.xml.eventkey.string
        ticket = soup.xml.ticket.string if soup.xml.ticket else None
        result = {
            'to_user': to_user,
            'openid': openid,
            'create_time': create_time,
            'msg_type': msg_type,
            'event': event,
            'event_key': event_key,
            'ticket': ticket,
        }
        logger.debug(result)
        return result

    def parse_scan_scene_int(self, event: str, event_key: str, openid: str):
        if event == 'unsubscribe':
            logger.info(f'【{openid}】取消订阅')
        elif event == 'subscribe':
            logger.info(f'【{openid}】订阅成功')
            scene_int = int(event_key.split('_')[-1])
        elif event.lower() == 'scan':
            logger.info(f'【{openid}】扫码登录')
            scene_int = int(event_key)
        logger.debug(f'scene_int={scene_int}')
        return scene_int

    def _handle_login_scene(self, openid: str, to_user: str, ticket: str):
        now = int(time.time())
        message = '登录成功'
        response_string = f"""
        <xml>
            <ToUserName><![CDATA[{openid}]]></ToUserName>
            <FromUserName><![CDATA[{to_user}]]></FromUserName>
            <CreateTime>{now}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{message}]]></Content>
        </xml>
        """
        from user.services import UserService
        logger.info(f'【{openid}】登录成功')
        token = UserService().weixin_qrcode_login(openid)
        QrcodeService().set_ticket_token(ticket, token)
        return response_string
