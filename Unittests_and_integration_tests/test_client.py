#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Testing the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_return_value, mock_get_json):
        """Testing GithubOrgClient.org returns the correct value"""

        mock_get_json.return_value = expected_return_value

        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org, expected_return_value)

        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test result of _public_repos_url is expected based on payload"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url":
                                     "https://api.github.com/orgs/google/repos"}
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url,
                             "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_value):
        """Test 'has_license' static method returns correct value"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_value)

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test `public_repos` method."""
        mock_public_repos_url.return_value = "https://some_url.com"

        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "license1"}},
            {"name": "repo2", "license": {"key": "license2"}},
            {"name": "repo3", "license": {"key": "license3"}}
        ]

        github_client = GithubOrgClient("google")

        self.assertEqual(github_client.public_repos(),
                         ["repo1", "repo2", "repo3"])

        self.assertEqual(github_client.public_repos("license1"),
                         ["repo1"])

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with
        ("https://some_url.com")


if __name__ == "__main__":
    unittest.main()
