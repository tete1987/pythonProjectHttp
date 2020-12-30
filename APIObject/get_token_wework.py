#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 13:58 
# @Author : TETE
# @File : get_token_wework.py
import requests


class Test_GetToken:
    corpid = "wwa76b0bc5194f5f49"
    corpsecret = "c6CHn3fyR7L3MWL1JbLXUWqaKidNX9MJ9YluAFMtVm0"

    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        pramas = {
            "corpid":self.corpid,
            "corpsecret":self.corpsecret
        }
        res = requests.get(url=url,params=pramas)
        assert  res.json()["errcode"] == 0