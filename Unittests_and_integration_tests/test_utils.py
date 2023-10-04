#!/usr/bin/env python3
"""Unit tests for the utils module."""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """Testing the function access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing the access_nested_map function + different scenarios."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """Testing the function raises KeyError for specific inputs."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception).strip("'"), expected_message)

class TestGetJson(unittest.TestCase):
    """Testing the function get_json."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Testing the get_json function with different scenarios."""
        
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        self.assertEqual(get_json(test_url), test_payload)

        mock_get.assert_called_once_with(test_url)
