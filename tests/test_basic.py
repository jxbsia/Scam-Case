#!/usr/bin/env python3
"""
Basic tests for the Scam Case project.

This module contains pytest tests for the main functions.
"""

import sys
import os
import pytest

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the functions we want to test
from main import hello_world, get_project_info


class TestBasicFunctions:
    """Test class for basic project functions."""
    
    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_hello_world_content(self):
        """Test that hello_world returns expected content."""
        result = hello_world()
        assert "Hello, World!" in result
        assert "Scam Case" in result
    
    def test_get_project_info_returns_dict(self):
        """Test that get_project_info returns a dictionary."""
        result = get_project_info()
        assert isinstance(result, dict)
    
    def test_get_project_info_has_required_keys(self):
        """Test that project info contains required keys."""
        result = get_project_info()
        required_keys = ['name', 'version', 'description', 'author']
        
        for key in required_keys:
            assert key in result
            assert result[key] is not None
            assert len(str(result[key])) > 0
    
    def test_get_project_info_values(self):
        """Test specific values in project info."""
        result = get_project_info()
        
        assert result['name'] == 'Scam Case'
        assert result['author'] == 'jxbsia'
        assert 'scam case' in result['description'].lower()
        
        # Test version format (should be semantic version)
        version = result['version']
        assert '.' in version
        version_parts = version.split('.')
        assert len(version_parts) >= 2
        
        # Each part should be numeric
        for part in version_parts:
            assert part.isdigit()


class TestIntegration:
    """Integration tests for the project."""
    
    def test_all_functions_work_together(self):
        """Test that all main functions can be called successfully."""
        # Test hello_world
        greeting = hello_world()
        assert greeting
        
        # Test get_project_info
        info = get_project_info()
        assert info
        
        # Test that they don't interfere with each other
        assert isinstance(greeting, str)
        assert isinstance(info, dict)
    
    def test_project_consistency(self):
        """Test consistency between functions."""
        info = get_project_info()
        greeting = hello_world()
        
        # Both should reference the same project name
        project_name = info['name']
        assert project_name in greeting


if __name__ == "__main__":
    # Run tests with pytest when script is executed directly
    pytest.main(["-v", __file__])
