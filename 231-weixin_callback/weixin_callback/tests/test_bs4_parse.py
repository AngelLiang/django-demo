from bs4 import BeautifulSoup


def test_parse_publish_callback():
    html_doc = """
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
    """
    soup = BeautifulSoup(html_doc, features="html.parser")
    assert soup.xml.msgtype.string == 'event'
    assert soup.xml.event.string == 'PUBLISHJOBFINISH'
    assert soup.xml.publisheventinfo.publish_status.string == '0'
    article_url = soup.xml.publisheventinfo.article_detail.item.article_url.string
    assert article_url.startswith('http://mp.weixin.qq.com')
