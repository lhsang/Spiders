import re


def getParamsFromCookie(cookie, params):
    """
    get params from cookie
    :param cookie: cookie
    :param params: list name of params which you want
    :return: dict result
    """
    ans = {}
    for param in params:
        value = re.findall(r'{}=[a-zA-Z0-9]+;'.format(param), cookie)[0]
        ans[param] = value.split('=')[1][:-1]
    return ans


def getCookieFromResponse(response):
    """
    get cookie from response
    :param response: response after request
    :return: string cookie
    """
    return str(response.headers.getlist('Set-Cookie')[0])


def isNullObj(obj):
    for key in obj:
        if obj[key] is not None:
            return False
    return True
