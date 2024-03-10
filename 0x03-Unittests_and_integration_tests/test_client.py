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

    def test_public_repos_url(self) -> None:
        """ test function"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, json_mock):
        """Testing"""
        data = [{"name": "repo1"}, {"name": "repo2"}]
        outcome = ["repo1", "repo2"]
        json_mock.return_value = data
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://example.com/repos"
            client = GithubOrgClient("example")
            result = client.public_repos()
            json_mock.assert_called_once_with("https://example.com/repos")
            mock_public_repos_url.assert_called_once_with()
            self.assertEqual(result, outcome)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
