import pytest


def test_sendsms_cache_success_code():
    from .sendsms import AliyunSendSms
    phone = '134123456798'
    code = '123456'
    aliyun_send_sms = AliyunSendSms()
    aliyun_send_sms.record_phone(phone, code)
    res = aliyun_send_sms.validate_phone(phone, code)
    assert res == True


def test_sendsms_cache_error_code():
    from .sendsms import AliyunSendSms
    phone = '134123456798'
    code = '123456'
    error_code = '654321'
    aliyun_send_sms = AliyunSendSms()
    aliyun_send_sms.record_phone(phone, code)
    res = aliyun_send_sms.validate_phone(phone, error_code)
    assert res == False


def test_sendsms_cache_intime():
    import time
    from .sendsms import AliyunSendSms
    phone = '134123456798'
    code = '123456'
    timeout = 3
    sleep_time = 2
    aliyun_send_sms = AliyunSendSms()
    aliyun_send_sms.record_phone(phone, code, timeout=timeout)
    time.sleep(sleep_time)
    res = aliyun_send_sms.validate_phone(phone, code)
    assert res == True


def test_sendsms_cache_timeout():
    import time
    from .sendsms import AliyunSendSms
    phone = '134123456798'
    code = '123456'
    timeout = 3
    aliyun_send_sms = AliyunSendSms()
    aliyun_send_sms.record_phone(phone, code, timeout=timeout)
    time.sleep(3)
    res = aliyun_send_sms.validate_phone(phone, code)
    assert res == False


if __name__ == '__main__':
    pytest.main()
