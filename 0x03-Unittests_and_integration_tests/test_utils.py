#!/usr/bin/env python3
""" Module for parameterize tasks """

from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json
from utils import memoize
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """test for the function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path,
                               expected):
        """Tests function's output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """checks cases for exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """function tests a json"""
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, output):
        """tests the function output"""
        output.return_value.json.return_value = test_payload
        output.return_value.status_code = 200
        self.assertEqual(get_json(test_url), test_payload)
        output.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ displays function"""
    def test_memoize(self) -> None:
        """Tests function output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as mem_method:
            test_output = TestClass()
            self.assertEqual(test_output.a_property(), 42)
            self.assertEqual(test_output.a_property(), 42)
            mem_method.assert_called_once()
