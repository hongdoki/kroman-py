# !/usr/bin/python
# -*- coding: utf-8

import sys, math

head_jamos = [
    'g', #ㄱ
    'kk', #ㄲ
    'n', #ㄴ
    'd', #ㄷ
    'tt', #ㄸ
    'r', #ㄹ
    'm', #ㅁ
    'b', #ㅂ
    'pp', #ㅃ
    's', #ㅅ
    'ss', #ㅆ
    '',
    'j', #ㅈ
    'jj', #ㅉ
    'ch', #ㅊ
    'k', #ㅋ
    't', #ㅌ
    'p', #ㅍ
    'h' #ㅎ
]

body_jamos = [
    'a', #ㅏ
    'ae', #ㅐ
    'ya', #ㅑ
    'yae', #ㅒ
    'eo', #ㅓ
    'e', #ㅔ
    'yeo', #ㅕ
    'ye', #ㅖ
    'o', # ㅗ
    'wa', # ㅘ
    'wae', # ㅙ
    'oe', # ㅚ
    'yo', # ㅛ
    'u', # ㅜ
    'wo', # ㅝ
    'we', # ㅞ
    'wi', # ㅟ
    'yu', # ㅠ
    'eu', # ㅡ
    'ui', # ㅢ
    'i' # ㅣ
]

tail_jamos = [
    '',
    'k', # ㄱ
    'kk', # ㄲ
    'ks', # ㄱㅅ
    'n', # ㄴ
    'nj', # ㄴㅈ 
    'nh', # ㄴㅎ
    't', # ㄷ
    'l', # ㄹ
    'lg', # ㄹㄱ
    'lm', # ㄹㅁ
    'lb', # ㄹㅂ
    'ls', # ㄹㅅ
    'lt', # ㄹㅌ
    'lp', # ㄹㅍ
    'lh', # ㄹㅎ
    'm', # ㅁ
    'p', # ㅂ
    'ps', # ㅂㅅ
    't', # ㅅ
    't', # ㅆ
    'ng', # ㅇ
    't', # ㅈ
    't', # ㅊ
    'k', # ㅋ
    't', # ㅌ
    'p', # ㅍ
    't' # ㅎ
]


def parse(text):
    if sys.version_info[0] == 2:
        text = unicode(text, 'utf-8')
    retval = u''
    ga = 0xac00
    hih = 0xd7a3
    interval_head = 588
    interval_body = 28
    last_char_is_hangul = False

    for c in text:
        cint = ord(c)
        if ga <= cint <= hih:
            head = int(math.floor((cint - ga) / interval_head))
            headl = int(math.floor((cint - ga) % interval_head))
            body = int(math.floor(headl / interval_body))
            tail = int(math.floor(headl % interval_body))
            if last_char_is_hangul:
                retval += ''
            retval += head_jamos[head]
            retval += body_jamos[body]
            retval += tail_jamos[tail]
            last_char_is_hangul = True
        else:
            last_char_is_hangul = False
            retval += c
    return retval
