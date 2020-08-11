# -*- coding: utf-8 -*-


import re



def cleanhtml(raw_text):
    try:
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub ( cleanr , ' ' , raw_text )
        return cleantext
    except:
        raise Exception('I know Python!')






