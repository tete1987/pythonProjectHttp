#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 14:12 
# @Author : TETE
# @File : address.py
import requests

from requests_wework.api_PO.base_api import BaseApi
from requests_wework.api_PO.wework import WeWork


class Address(BaseApi):

    def __init__(self):
        secret = 'c6CHn3fyR7L3MWL1JbLXUWqaKidNX9MJ9YluAFMtVm0'
        self.token = WeWork().get_token(secret)

    def createNumber(self,userid,name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token":self.token},
            "json":
                {"userid": userid,
                 "name": name,
                 "mobile": mobile,
                 "department": [1]
                 }
        }

        return self.send(**data)

    def getNumber(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.token,
                "userid":userid
            }
        }
        return self.send(**data)

    def updateNumber(self,userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json":
                {"userid": userid,
                 "name": name,
                 "mobile": mobile}
        }

        return self.send(**data)

    def deleteNumber(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
             "params": {
                "access_token": self.token,
                "userid":userid
            }
        }
        return self.send(**data)