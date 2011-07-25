#!/usr/bin/env python
# Copyright (C) 2007-2010 PlayOnLinux Team

import os, random
import wx

# Un ptit check
try :
	os.environ["POL_OS"]
except :
	print "ERROR ! Please define POL_OS environement var first."
	exit
# Variables mixte 1 (Ben ouai, ya un ordre ...)
os.environ["PLAYONLINUX"] = os.path.realpath(os.path.realpath(__file__)+"/../../../")
	
# Variables PlayOnMac
if (os.environ["POL_OS"] == "Mac"):
	os.environ["PLAYONMAC"] = os.environ["PLAYONLINUX"]
	os.environ["REPERTOIRE"] = os.environ["HOME"]+"/Library/PlayOnMac/"
	os.environ["APPLICATION_TITLE"] = "PlayOnMac"
	windows_add_size = 20;
	widget_borders = wx.SIMPLE_BORDER
	
# Variables PlayOnLinux
if (os.environ["POL_OS"] == "Linux"):
	os.environ["REPERTOIRE"] = os.environ["HOME"]+"/.PlayOnLinux/"
	os.environ["APPLICATION_TITLE"] = "PlayOnLinux"
	windows_add_size = 0;
	widget_borders = wx.RAISED_BORDER
	
	
# Variables mixtes
os.environ["POL_USER_ROOT"] = os.environ["REPERTOIRE"]
os.environ["TITRE"] = "PlayOnMac"
os.environ["SITE"] = "http://repository.playonlinux.com"
os.environ["VERSION"] = "4.0-dev"
os.environ["POL_ID"] = str(random.randint(1,100000000))
os.environ["WINEPREFIX"] = os.environ["REPERTOIRE"]+"/wineprefix/default"
homedir = os.environ["HOME"]

# Si DYLD_LIBRARY_PATH n'existe pas, on la defini pour etre sur	
try :
	os.environ["DYLD_LIBRARY_PATH"]
except:
	os.environ["DYLD_LIBRARY_PATH"] = ""

# Pareil pour LD
try :
	os.environ["LD_LIBRARY_PATH"]
except:
	os.environ["LD_LIBRARY_PATH"] = ""

os.environ["PATH_ORIGIN"] = os.environ["PATH"]
os.environ["LD_PATH_ORIGIN"] = os.environ["LD_LIBRARY_PATH"]
os.environ["DYLDPATH_ORIGIN"] = os.environ["DYLD_LIBRARY_PATH"]


if (os.environ["POL_OS"] == "Mac"):
	os.environ["MAGICK_HOME"] = os.environ["PLAYONLINUX"]+"/../unix/image_magick/"
	
	os.environ["PATH"] = os.environ["PLAYONLINUX"]+"/../unix/wine/bin:" + os.environ["PLAYONLINUX"]+"/../unix/image_magick/bin:" + os.environ["PLAYONLINUX"]+"/../unix/tools/bin/:" + os.environ["PATH"]
	
	os.environ["LD_LIBRARY_PATH"] =  os.environ["PLAYONLINUX"]+"/../unix/wine/lib/:"  + os.environ["PLAYONLINUX"]+"/../unix/image_magick/lib:"+ os.environ["PLAYONLINUX"]+"/../unix/tools/lib/ld:/usr/X11/lib/" + os.environ["LD_LIBRARY_PATH"]
	
	os.environ["DYLD_LIBRARY_PATH"] = os.environ["PLAYONLINUX"]+"/../unix/tools/lib/dyld:" + os.environ["PLAYONLINUX"]+"/../unix/image_magick/lib:"+ os.environ["DYLD_LIBRARY_PATH"]


playonlinux_env = os.environ["PLAYONLINUX"]
playonlinux_rep = os.environ["REPERTOIRE"]
version = os.environ["VERSION"]
current_user = os.environ["USER"]

# Je sais plus a quoi ca sert, mais ca sert
os.environ["SHLVL"]="2"

# On fait le minimum avant de lancer l'interface
os.system("bash "+playonlinux_env+"/bash/startup &")