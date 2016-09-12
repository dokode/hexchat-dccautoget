#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 

# Author: hakim.hexchat 
# 			[a t] gmail 

# Auto-loading INSTALL: copy to ~/.config/hexchat/addons/
# To load in hexchat: /py dccautoget.py
# To unload: /py unload dccautoget.py
# hexchat API doc: https://hexchat.readthedocs.io/en/2.9.6/script_python.html

# TODO : checking that the nickname is registered before accepting (option, enabled by default)

import xchat

__module_name__ = "dccautoget"
__module_version__ = "1.0"	
__module_description__ = ("Auto-allows dcc-get from specific nicknames. "  
						"For defining the granted nicknames start with /help dccautoget.")

PREF_ID=xchat.strip(__module_name__)

DEBUG=False

def get_network():
	ctxt = xchat.get_context()
	net = ctxt.get_info("network")
	return net 

def dcc_cb(word, word_eol, userdata, priority):
	net = get_network()
	nick = word[0]
	auto_nicks = xchat.get_pluginpref(PREF_ID+"."+net).split(",");
	DEBUG and xchat.prnt(__module_name__+": DCC offer from "+repr(word)+" on network: "+net)
	if(auto_nicks != None and nick in auto_nicks):
		xchat.prnt(__module_name__+": Auto-accepting the DCC offer from "+repr(word)+" on network: "+net)
		xchat.command("dcc get "+nick);
		
def format_list_str(l):
	""" Transforms a list to a str with comma-separated elements  
	"""
	str =""
	for i in range(0,len(l)):
		if(l[i] != ""):
			str += l[i]
			if(i < len(l)-1):
				str +=","
	return str
		
def dccautoget_add(nick,auto_nicks="", net = get_network()):
	auto_nicks = auto_nicks.split(",")
	if(auto_nicks != None and nick in auto_nicks):
		xchat.prnt(__module_name__+": "+nick+" already granted for the network: "+net)
	else:
		auto_nicks.append(nick)
		ret = xchat.set_pluginpref(PREF_ID+"."+net, format_list_str(auto_nicks))
		if(ret):
			xchat.prnt(__module_name__+": "+nick+" is now granted for auto. dcc-get in the network: "+net)

def dccautoget_del(nick,auto_nicks="", net = get_network()):
	auto_nicks = auto_nicks.split(",")
	if(auto_nicks == None or not nick in auto_nicks):	
		xchat.prnt(__module_name__+": "+nick+" not found in granted list for the network: "+net)
	else:
		auto_nicks.remove(nick)
		ret = xchat.set_pluginpref(PREF_ID+"."+net, format_list_str(auto_nicks))
		if(ret):
			xchat.prnt(__module_name__+": "+nick+" isn't granted anymore for auto. dcc-get in the network: "+net)

def dccautoget_list(net, auto_nicks="none"):
	xchat.prnt(__module_name__+": for the network "+net+", the nicks granted are: "+(auto_nicks or "none"))
	
def dccautoget(word, word_eol, userdata):
	net = get_network()
	cmd = word[1]
	auto_nicks = xchat.get_pluginpref(PREF_ID+"."+net) or ""
	DEBUG and xchat.prnt(__module_name__+": nicks granted before cmd: "+repr(auto_nicks or "none"))
	if(len(word) > 2):
		nick = word[2]
	if(cmd == "add"):
		dccautoget_add(nick,auto_nicks,net)
	elif(cmd == "del"):
		dccautoget_del(nick,auto_nicks,net)
	elif(cmd == "list"):
		dccautoget_list(net,auto_nicks)
	else:
		xchat.prnt(__module_name__+": error, the command "+cmd+" is not recognized. For help, type /help dccautoget.")
	return xchat.EAT_ALL

xchat.hook_print_attrs("DCC Send Offer", dcc_cb)

xchat.hook_command("dccautoget", dccautoget, help="""/dccautoget <add|del|list> <nick>
add command to allow a nickname to have its dcc-sends auto-allowed from you on the current network only.
del command to remove the authorization for a nickname.
list command to list all nicknames you have granted for the current network.
Example: /dccautoget add lambda_nick
			 The user lambda_nick's DCC offers will be accepted automatically.
""")

xchat.prnt(__module_name__+" loaded")

xchat.hook_unload(lambda user_data : xchat.prnt(__module_name__+" unloaded"))
