#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 14:09 
# @Author : TETE
# @File : get_token.py
from string import Template

import yaml

from APIObject.base_api import BaseApi


class GetToken(BaseApi):
     _corpid = "wwa76b0bc5194f5f49"
     _corpsecret = "c6CHn3fyR7L3MWL1JbLXUWqaKidNX9MJ9YluAFMtVm0"

     def template(self):
         with open("get_token.yaml") as f:
             data = {
                 "corpid" : self._corpid,
                 "corpsecret":self._corpsecret

             }
             re = Template(f.read()).substitute(data)
             return yaml.safe_load(re)

     def get_token(self):
         res = self.template()
         r =self.requests_http(res)
         return r


