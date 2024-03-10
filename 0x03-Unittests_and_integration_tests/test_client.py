#!/usr/bin/env python3
"""Module for tasks 4-9"""

import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """testing git class"""
    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """ tests the org class"""
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)

    def test_public_repos_url(self):
        """testing """
        mock_payload = {"repos_url": "http://example.com/repos"}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) \
                as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient("example.org")
            repo_url = client._public_repos_url
            self.assertEqual(mock_payload["repos_url"], repo_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Testfunction"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        expected_result = ["repo1", "repo2"]
        mock_get_json.return_value = mock_payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://example.com/repos"
            client = GithubOrgClient("example")
            result = client.public_repos()
            mock_get_json.assert_called_once_with("https://example.com/repos")
            mock_public_repos_url.assert_called_once_with()
            self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test for license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """displays integration tests"""
    @classmethod
    def setUpClass(cls) -> None:
        """setupclass function"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Testing """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Testing"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """delete function"""
        cls.get_patcher.stop()
