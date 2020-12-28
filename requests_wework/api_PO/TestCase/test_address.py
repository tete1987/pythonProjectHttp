#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 14:25 
# @Author : TETE
# @File : test_address.py
from requests_wework.api_PO.address import Address

class TestAddress:
    def setup(self):
        self.address = Address()

    def test_createNumber(self):
        assert "created"== self.address.createNumber("tete123", "特特122", "15400010001")['errmsg']

    def test_updateNumber(self):
        assert "updated" ==self.address.updateNumber("tete123", "xiaotete", "15430210001")['errmsg']

    def test_deleteNumber(self):
        assert "deleted" == self.address.deleteNumber("tete123")['errmsg']

