#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', PropertyMock(return_value={"repos_url": "https://api.github.com/orgs/google/repos"}))
    def test_public_repos_url(self, mock_org):
        """Test that result of _public_repos_url is expected one based on mocked payload"""
        github_client = GithubOrgClient("google")
        self.assertEqual(github_client._public_repos_url, "https://api.github.com/orgs/google/repos")

if __name__ == "__main__":
    unittest.main()