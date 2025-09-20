#!/usr/bin/env python3
"""
Scam Case - Main module

This module contains the main functions for the Scam Case project.
"""


def hello_world():
    """Returns a hello world message for the Scam Case project.
    
    Returns:
        str: A greeting message
    """
    return "Hello, World! Welcome to the Scam Case project!"


def get_project_info():
    """Returns basic information about the Scam Case project.
    
    Returns:
        dict: Project information
    """
    return {
        "name": "Scam Case",
        "version": "1.0.0",
        "description": "A project for tracking and analyzing scam cases",
        "author": "jxbsia"
    }


if __name__ == "__main__":
    print(hello_world())
    print(f"Project: {get_project_info()['name']}")
    print(f"Version: {get_project_info()['version']}")
