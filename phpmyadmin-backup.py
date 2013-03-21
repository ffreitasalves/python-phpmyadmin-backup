#!/usr/bin/python
# -*- coding:utf-8 -*-

# Backup of MySQL database through PhpMyAdmin


import urllib2, urllib, cookielib
import string
from datetime import datetime

base = u'http://Full url to PhpmyAdmin'

username = 'YourPhpMyAdminUser'
password = 'YourPwd'
login_params = urllib.urlencode({
	u'pma_username' : username,
	u'pma_password' : password,
	u'lang' : u'en-utf-8',
	u'convcharset' : u'utf-8',
	u'server' : u'1'
})
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPCookieProcessor()))
f = urllib2.urlopen(base + u'index.php', login_params)
redirect_url = f.geturl()
token_label = "&token="
pos = string.rindex(redirect_url, token_label)
pos2 = string.index(redirect_url, '&', pos + len(token_label))
token = redirect_url[pos + len(token_label):pos2]
f.close()
s = 'something'
backup_params = urllib.urlencode({
	'asfile': 'sendit',
	'token' : token,
	'what' : 'sql',
	'export_type' : 'server',
	'sql_type' : 'INSERT',
	'checkbox_sql_hex_for_binary' : '',
	'checkbox_sql_extended' : '',
	'checkbox_sql_columns' : '',
	'compression' : 'gzip',
	'filename_template' : '__SERVER__',
	'sql_auto_increment' : s,
	'sql_backquotes' : s,
	'sql_columns' : s,
	'sql_data' : s,
	'sql_extended' : s,
	'sql_header_comment' : '',
	'sql_hex_for_binary' : s,
	'sql_max_query_size' : '50000',
	'sql_structure' : s
})
f = urllib2.urlopen(base + u'export.php', backup_params)
arq = open("%sw3fea.sql.gz" % datetime.now().strftime("%d-%m-%Y-%H"),"wb")
arq.write(f.fp.read())
arq.close()
f.close()
