# Make a program to translate what user put and get him or her greatings

#---------------------------------------------------------------------------
#Import
     
import googletrans
from googletrans import *    #import * -> import everything
 
#---------------------------------------------------------------------------
#Set up

translation = googletrans.Translator()

#---------------------------------------------------------------------------

translate = translation.translate("Hello my name is someting", dest='zh-CN')
print(translate.text)

