#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 9:45 
# @Author : TETE
# @File : test_env.py
from requests_env.demoApi import DemoApi


class TestEnv:
    data = {
        "method": "get",
        "url": "http://baidu:9999/demo1.txt",
        "headers": None
    }

    def test_env(self):
        r= DemoApi().send(self.data)
        print(r)

