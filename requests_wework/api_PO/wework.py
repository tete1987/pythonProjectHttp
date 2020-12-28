#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 15:04 
# @Author : TETE
# @File : wework.py
from requests_wework.api_PO.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,secret):
        corpid= 'wwa76b0bc5194f5f49'
        corpsecret= secret
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid" : corpid,
                "corpsecret" : corpsecret
            }
        }

        return self.send(**data)["access_token"]