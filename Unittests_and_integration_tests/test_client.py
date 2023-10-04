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

    def test_public_repos_url(self):
        """Test that result of _public_repos_url is the expected one based on the mocked payload"""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url, "https://api.github.com/orgs/google/repos")

if __name__ == "__main__":
    unittest.main()