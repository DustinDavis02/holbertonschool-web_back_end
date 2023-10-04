#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
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

if __name__ == "__main__":
    unittest.main()