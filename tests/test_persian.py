"""
Tests for Persian utilities — تست‌های ابزارهای فارسی
"""

import pytest
from tizpar.utils.persian import (
    to_persian_digits,
    to_english_digits,
    is_persian_text,
    remove_diacritics,
    get_persian_chars_count,
    extract_persian_words,
)


class TestPersianDigits:
    """تست‌های مربوط به اعداد فارسی"""

    def test_to_persian_digits_basic(self):
        assert to_persian_digits("123") == "۱۲۳"
        assert to_persian_digits("Hello 123") == "Hello ۱۲۳"
        assert to_persian_digits("") == ""

    def test_to_persian_digits_all_numbers(self):
        assert to_persian_digits("0123456789") == "۰۱۲۳۴۵۶۷۸۹"

    def test_to_english_digits_basic(self):
        assert to_english_digits("۱۲۳") == "123"
        assert to_english_digits("سلام ۱۲۳") == "سلام 123"
        assert to_english_digits("") == ""

    def test_to_english_digits_all_persian(self):
        assert to_english_digits("۰۱۲۳۴۵۶۷۸۹") == "0123456789"

    def test_roundtrip(self):
        original = "Hello 123 World"
        persian = to_persian_digits(original)
        english = to_english_digits(persian)
        assert english == original


class TestPersianDetection:
    """تست‌های تشخیص متن فارسی"""

    def test_is_persian_text_true(self):
        assert is_persian_text("سلام دنیا") is True
        assert is_persian_text("چطور هستید؟") is True

    def test_is_persian_text_false(self):
        assert is_persian_text("Hello World") is False
        assert is_persian_text("How are you?") is False

    def test_is_persian_text_empty(self):
        assert is_persian_text("") is False
        assert is_persian_text("   ") is False

    def test_is_persian_mixed(self):
        # متن با اکثریت فارسی باید True برگرداند
        assert is_persian_text("سلام دنیا hello") is True
        # متن با اکثریت انگلیسی باید False برگرداند
        assert is_persian_text("Hello World سلام") is False


class TestPersianChars:
    """تست‌های کاراکترهای فارسی"""

    def test_get_persian_chars_count(self):
        assert get_persian_chars_count("سلام") == 4
        assert get_persian_chars_count("Hello") == 0
        assert get_persian_chars_count("") == 0
        assert get_persian_chars_count("Hello سلام") == 4

    def test_remove_diacritics(self):
        assert remove_diacritics("مُتَرْجِم") == "مترجم"
        assert remove_diacritics("کِتاب") == "کتاب"
        assert remove_diacritics("") == ""

    def test_extract_persian_words(self):
        words = extract_persian_words("Hello سلام World دنیا")
        assert "سلام" in words
        assert "دنیا" in words
        assert "Hello" not in words
