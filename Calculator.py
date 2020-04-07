# -*- coding: utf-8 -*-

from __future__ import division


def calc(text):
	whitelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', '+', '-', '*', '/', '(', ')', '<', '>', '=']
	text = text.replace('**', '')  # to avoid eeasee
	text_clean = ''
	for c in text:
		if c in whitelist:
			text_clean += c

	if len(text_clean) == 0:
		return None
	try:
		return str(eval(text_clean))
	except Exception as e:
		return str(e)


def work(server, info):
	if info.content.startswith('=='):
		result = calc(info.content[2:])
		if result is not None:
			server.say(result)


# MCDaemon
def onServerInfo(server, info):
	if info.isPlayer == 1:
		work(server, info)


# MCDReforged
def on_info(server, info):
	if info.is_player:
		work(server, info)


def on_load(server, old):
	server.add_help_message('==<exp>', '计算表达式§7<exp>§r')
