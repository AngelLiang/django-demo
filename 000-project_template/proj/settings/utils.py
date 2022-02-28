def str2bool(s):
    """
    如果 s 为 '0', 'n', 'no', 'false' ，返回 False
    其他情况返回 True
    """
    if isinstance(s, bool):
        return s
    return s.lower() not in ('0', 'n', 'no', 'false')
