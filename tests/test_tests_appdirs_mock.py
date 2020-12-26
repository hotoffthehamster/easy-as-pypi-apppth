# This file exists within 'easy-as-pypi-apppth':
#
#   https://github.com/tallybark/easy-as-pypi-apppth#🛣
#
# Copyright © 2018-2020 Landon Bouma. All rights reserved.
#
# Permission is hereby granted,  free of charge,  to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge,  publish,  distribute, sublicense,
# and/or  sell copies  of the Software,  and to permit persons  to whom the
# Software  is  furnished  to do so,  subject  to  the following conditions:
#
# The  above  copyright  notice  and  this  permission  notice  shall  be
# included  in  all  copies  or  substantial  portions  of  the  Software.
#
# THE  SOFTWARE  IS  PROVIDED  "AS IS",  WITHOUT  WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING  BUT NOT LIMITED  TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE  FOR ANY
# CLAIM,  DAMAGES OR OTHER LIABILITY,  WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,  ARISING FROM,  OUT OF  OR IN  CONNECTION WITH THE
# SOFTWARE   OR   THE   USE   OR   OTHER   DEALINGS  IN   THE  SOFTWARE.

"""Tests the tests subpackage appdirs_mock module."""

import os

import pytest

from easy_as_pypi_apppth import register_application


class TestTestsAppdirsMock():

    @pytest.fixture(autouse=True)
    def register_application(self, app_name):
        register_application(app_name)

    def test_tests_appdirs_mock_side_effect(self, tmp_appdirs):
        adir_path = tmp_appdirs.user_cache_dir
        assert os.path.exists(adir_path)

    def test_tests_appdirs_mock_safe_effect(self, tmp_appdirs):
        adir_path = tmp_appdirs.safe.user_cache_dir
        assert not os.path.exists(adir_path)

