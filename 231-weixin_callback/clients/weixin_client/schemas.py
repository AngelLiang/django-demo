from pydantic import BaseModel, Field


class QrcodeOut(BaseModel):
    ticket: str = Field(..., description="获取的二维码ticket，凭借此ticket可以在有效时间内换取二维码。")
    expire_seconds: int = Field(..., description="该二维码有效时间，以秒为单位。")
    url: str = Field(..., description="二维码图片解析后的地址，开发者可根据该地址自行生成需要的二维码图片")


def make_article(
    title,
    content,
    thumb_media_id,
    author=None,
    digest=None,
    content_source_url: str = None,
    need_open_comment: int = 0,
    only_fans_can_comment: int = 0
) -> dict:
    """

    参数	是否必须	说明
    title	是	标题
    author	否	作者
    digest	否	图文消息的摘要，仅有单图文消息才有摘要，多图文此处为空。如果本字段为没有填写，则默认抓取正文前54个字。
    content	是	图文消息的具体内容，支持HTML标签，必须少于2万字符，小于1M，且此处会去除JS,涉及图片url必须来源 "上传图文消息内的图片获取URL"接口获取。外部图片url将被过滤。
    content_source_url	否	图文消息的原文地址，即点击“阅读原文”后的URL
    thumb_media_id	是	图文消息的封面图片素材id（必须是永久MediaID）
    need_open_comment	否	Uint32 是否打开评论，0不打开(默认)，1打开
    only_fans_can_comment	否	Uint32 是否粉丝才可评论，0所有人可评论(默认)，1粉丝才可评论

    ref: https://developers.weixin.qq.com/doc/offiaccount/Draft_Box/Add_draft.html

    """
    article = {
        "title": title,
        "content": content,
        "thumb_media_id": thumb_media_id
    }

    if author is not None:
        article["author"] = author

    if digest is not None:
        article["digest"] = digest

    if content_source_url is not None:
        article["content_source_url"] = content_source_url

    article["need_open_comment"] = need_open_comment
    article["only_fans_can_comment"] = only_fans_can_comment

    return article
