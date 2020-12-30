#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/29 16:24 
# @Author : TETE
# @File : test_encryption.py
from encryption import Encryption


class TestEncryption:

    def test_encryption(self):
        req_data = {
            "method": "get",
            "url": "http://127.0.0.1:9999/demo1.txt",
            "headers": None,
            "encoding": "base64"
        }
        ar = Encryption().send(req_data)
        print(ar)

