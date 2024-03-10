#!/usr/bin/env python3
"""Module for tasks 4-9"""

import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """tests the Class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, git_org, json_mock):
        """ tests the org class"""
        json_mock.return_value = {"name": git_org}
        client = GithubOrgClient(git_org)
        info = client.org
        json_mock.assert_called_once_with(GithubOrgClient.
                                          ORG_URL.format(org=git_org))
        self.assertEqual(info["name"], git_org)
