"""
Tests for Network utilities — تست‌های ابزارهای شبکه
"""

import pytest
from tizpar.utils.network import check_url


class TestCheckUrl:
    """تست‌های بررسی URL"""

    def test_check_url_invalid(self):
        """تست URL نامعتبر"""
        result = check_url("https://this-domain-does-not-exist-123456789.com", timeout=3)
        assert result["success"] is False
        assert "error" in result

    def test_check_url_empty_string(self):
        """تست رشته خالی"""
        result = check_url("", timeout=3)
        assert result["success"] is False
