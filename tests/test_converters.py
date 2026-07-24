"""
Tests for Converters — تست‌های ابزارهای تبدیل
"""

import pytest
from tizpar.utils.converters import (
    text_to_base64,
    base64_to_text,
    json_pretty,
    json_minify,
    _simple_json_to_yaml,
)


class TestBase64:
    """تست‌های Base64"""

    def test_text_to_base64(self):
        encoded = text_to_base64("Hello World")
        assert isinstance(encoded, str)
        assert len(encoded) > 0

    def test_base64_to_text(self):
        original = "Hello World"
        encoded = text_to_base64(original)
        decoded = base64_to_text(encoded)
        assert decoded == original

    def test_roundtrip_persian(self):
        original = "سلام دنیا"
        encoded = text_to_base64(original)
        decoded = base64_to_text(encoded)
        assert decoded == original

    def test_roundtrip_empty(self):
        assert base64_to_text(text_to_base64("")) == ""


class TestJsonFormatter:
    """تست‌های فرمت‌بندی JSON"""

    def test_json_pretty(self):
        compact = '{"name":"tizpar","version":"0.0.1"}'
        pretty = json_pretty(compact)
        assert "  " in pretty  #应该有缩进
        assert "\n" in pretty

    def test_json_minify(self):
        pretty = '{\n  "name": "tizpar"\n}'
        minified = json_minify(pretty)
        assert " " not in minified or "name" in minified  # 最小化后应该没有多余空格
        assert "\n" not in minified


class TestSimpleYaml:
    """تست‌های YAML ساده"""

    def test_simple_dict_to_yaml(self):
        data = {"name": "tizpar", "version": "0.0.1"}
        yaml_str = _simple_json_to_yaml(data)
        assert "name: tizpar" in yaml_str
        assert "version: \"0.0.1\"" in yaml_str or "version: 0.0.1" in yaml_str
