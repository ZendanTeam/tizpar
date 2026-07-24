"""
Tests for System utilities — تست‌های ابزارهای سیستم
"""

import pytest
from tizpar.utils.system import (
    get_system_info,
    get_python_info,
    _format_bytes,
    _parse_mem_value,
)


class TestSystemInfo:
    """تست‌های اطلاعات سیستم"""

    def test_get_system_info(self):
        info = get_system_info()
        assert "system" in info
        assert "machine" in info
        assert info["system"] in ("Linux", "Darwin", "Windows", "Java")

    def test_get_python_info(self):
        info = get_python_info()
        assert "version" in info
        assert "implementation" in info
        assert "executable" in info


class TestFormatBytes:
    """تست‌های فرمت‌بندی بایت"""

    def test_format_bytes(self):
        assert _format_bytes(0) == "0.00 B"
        assert _format_bytes(1024) == "1.00 KB"
        assert _format_bytes(1024 * 1024) == "1.00 MB"
        assert _format_bytes(1024 * 1024 * 1024) == "1.00 GB"


class TestParseMemValue:
    """تست‌های تبدیل مقدار حافظه"""

    def test_parse_kb(self):
        assert _parse_mem_value("1024 kB") == 1024 * 1024
        assert _parse_mem_value("0 kB") == 0

    def test_parse_mb(self):
        assert _parse_mem_value("1 MB") == 1024 * 1024

    def test_parse_without_unit(self):
        result = _parse_mem_value("1024")
        assert result == 1024 * 1024  # default kb
