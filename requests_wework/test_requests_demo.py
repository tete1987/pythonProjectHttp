#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/25 17:17 
# @Author : TETE
# @File : test_requests_demo.py
import re

import pytest
import requests

from filelock import FileLock


@pytest.fixture(scope="session")
def test_get_token():
    res = None

    while FileLock("session.lock"):
        corpid = 'wwa76b0bc5194f5f49'
        corpsecret = 'c6CHn3fyR7L3MWL1JbLXUWqaKidNX9MJ9YluAFMtVm0'
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")

        return res.json()["access_token"]


def test_create(userid, name, mobile, test_get_token):
    data ={
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department":[1]
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token}", json=data)
    return res.json()


def test_get(userid, test_get_token):
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token}&userid={userid}")
    return res.json()


def test_update(userid, name, mobile, test_get_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token}", json=data)
    return res.json()


def test_delete(userid, test_get_token):
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token}&userid={userid}")
    return res.json()

def test_create_data():
    data = [("tete"+str(x),"特特","153%08d"%x) for x in range(10)]
    return data


@pytest.mark.parametrize("userid, name, mobile", test_create_data())
def test_all(userid, name, mobile,test_get_token):
    try:
        assert "created" == test_create(userid, name, mobile, test_get_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)", e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid=re_userid[:-1]
            assert "deleted" == test_delete(re_userid, test_get_token)["errmsg"]
            assert 60111 == test_get(re_userid, test_get_token)["errcode"]
            assert "created" == test_create(userid, name, mobile, test_get_token)["errmsg"]

    assert name == test_get(userid, test_get_token)["name"]
    assert "updated" == test_update(userid, "特特123445", mobile, test_get_token)["errmsg"]
    assert "特特123445" == test_get(userid, test_get_token)['name']
    assert "deleted" == test_delete(userid, test_get_token)["errmsg"]
    assert 60111 == test_get(userid, test_get_token)["errcode"]
