#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 14:19 
# @Author : TETE
# @File : base_api.py
import requests


class BaseApi:
    def send(self,**data):
        return requests.request(**data).json()
