#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/30 10:12 
# @Author : TETE
# @File : test_yaml.py
import yaml


def test_yaml():
    env = {
        "default": "dev",
        "testing": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }
    }

    with open("env.yaml","w") as f:
        yaml.safe_dump(data = env,stream=f)