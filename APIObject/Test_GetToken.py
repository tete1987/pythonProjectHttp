#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 14:33 
# @Author : TETE
# @File : Test_GetToken.py
from APIObject.get_token import GetToken


class TestGetToken:
    def setup(self):
        self.gettoken = GetToken()

    def test_get_token(self):
        assert self.gettoken.get_token().json()["errcode"] == 0