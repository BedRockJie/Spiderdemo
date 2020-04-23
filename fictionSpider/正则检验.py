import re

txt = '<dd><a href="/54_54605/21426429.html">第852章 我们的时代！</a></dd>'
title = re.findall('[\u4e00-\u9fa5].*?！',txt)[0]
#qq=re.findall('[\u4e00-\u9fa5].*?！',txt)
zz = re.findall('".*"',txt)[0]
print(zz)
