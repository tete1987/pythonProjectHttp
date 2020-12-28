#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/21 15:59 
# @Author : TETE
# @File : test_demo.py
import requests


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.json())
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "tete"
        }

        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "post_form"
        }

        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"H": "tete", "name": "huahua"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "tete"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "tete"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['name'] == 'tete'

    def test_request_header(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            "Cookie": "name=tete",
            "User-Agent": "AAAA"
        }
        r = requests.get(url=url, headers=header)
        print(r.request.headers)

    def test_request_header02(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {"User-Agent": "AAAA"}
        cookie_data = {
            "name": "tete",
            "address": "beijing"
        }
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)
