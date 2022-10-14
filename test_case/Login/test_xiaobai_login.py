#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-10-13 10:12:54


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['login_xiaobai_01', 'login_xiaobai_02', 'login_xiaobai_03', 'login_xiaobai_04', 'login_xiaobai_05', 'login_xiaobai_06', 'login_xiaobai_07', 'login_xiaobai_08']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("小白商城接口")
@allure.feature("登录模块")
class TestLogin:

    @allure.story("登录")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_xiaobai_login(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_xiaobai_login.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
