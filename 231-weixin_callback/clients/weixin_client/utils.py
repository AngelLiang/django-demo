from urllib.parse import unquote


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + unquote(req.url),
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body or '',
        '-----------FINISH-----------',
    ))
