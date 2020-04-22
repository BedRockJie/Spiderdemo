import requests

def get_word(self):
    """
    获取金山词霸每日一句
    :return: msg
    """
    r = requests.get(self.cb_link).json()
    en = r['content']
    cn = r['note']
    indent = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' \
             '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
    # 填充每日一句模板
    msg = '<br><font size=3 color=lightpink><strong><i>' + en + '<br>' + cn + '</strong></font><br>' + \
          '<br>' + indent + '<font size=3 color=#a5673f>—— 最关心你的人儿~' + \
          '<br><html><body><img src={}></body></html>'.format(r['fenxiang_img'])
    return str(msg)
