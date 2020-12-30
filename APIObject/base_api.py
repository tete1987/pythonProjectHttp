#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 14:20 
# @Author : TETE
# @File : base_api.py
import requests


class BaseApi:
    def requests_http(self,res):
        '''
        直接使用python关键字传参的方式，将请求结构体传给requests.request 方法
        :param res:
         res = {
             "method":"get",
             "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
             "params" :{
                 "corpid": self._corpid,
                 "corpsecret": self._corpsecret}
         }

        :return:r
        '''
        r= requests.request(**res)
        return r