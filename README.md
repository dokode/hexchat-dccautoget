# DCC Auto Get - HexChat Addon

> Auto-allows dcc-get from specific nicknames and network.

> For defining the granted nicknames start with the command 
	
		/help dccautoget

Which should display the following help message:

	**/dccautoget <add|del|list> <nick>**
	**add** command to allow a nickname to have its dcc-sends auto-allowed from you on the current network only.
	**del** command to remove the authorization for a nickname.
	**list** command to list all nicknames you have granted for the current network.
	**Example:** /dccautoget add lambda_nick
	The user lambda_nick's DCC offers will be accepted automatically.


## Installing ##

For auto-loading, copy the script in your hexchat addon folder:

+ On Linux: ~/.config/hexchat/addons 
+ On other OS, find it!

Alternatively you can (un)load a script manually into HexChat through:

The commands:
 
		/py load dccautoget.py
		/py unload dccautoget.py
 
 Or, the hexchat GUI: 
 
		Window > Plugins and Scripts.
		
## Downloading HexChat ##

If you don't know HexChat yet, this is an IRC client.

[Follow this link to download HexChat.](https://hexchat.github.io/downloads.html)

## Contact ##

hakim.hexchat 
[[[a t]]] gmail

