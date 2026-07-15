"""
Basic test for Analytics Dashboard import.
"""

from ui.analytics_dashboard import show_analytics_dashboard


def test_import():
    assert callable(show_analytics_dashboard)
