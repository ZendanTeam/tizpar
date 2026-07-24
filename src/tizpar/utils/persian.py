"""
Persian Text Utilities — ابزارهای کار با متن فارسی
===================================================

توابع مفید برای کار با متن، اعداد و کاراکترهای فارسی
"""

import re
from typing import Tuple

# محدوده یونیکد کاراکترهای فارسی
PERSIAN_CHARS_RANGE: str = r"[\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u06CC\u0621-\u0628\u062A-\u063A\u0641-\u0652]"

# اعداد فارسی
PERSIAN_DIGITS: str = "۰۱۲۳۴۵۶۷۸۹"
ENGLISH_DIGITS: str = "0123456789"

# کاراکترهای اعراب (diacritics)
PERSIAN_DIACRITICS: str = "\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652"


def to_persian_digits(text: str, keep_non_digits: bool = True) -> str:
    """
    تبدیل اعداد انگلیسی به فارسی
    
    Args:
        text: متن ورودی
        keep_non_digits: اگر True باشد، کاراکترهای غیرعددی را حفظ می‌کند
    
    Returns:
        متن با اعداد فارسی
    
    مثال:
        >>> to_persian_digits("Hello 123")
        'Hello ۱۲۳'
    """
    if not text:
        return text
    
    digit_map = str.maketrans(ENGLISH_DIGITS, PERSIAN_DIGITS)
    return text.translate(digit_map)


def to_english_digits(text: str, keep_non_digits: bool = True) -> str:
    """
    تبدیل اعداد فارسی به انگلیسی
    
    Args:
        text: متن ورودی
        keep_non_digits: اگر True باشد، کاراکترهای غیرعددی را حفظ می‌کند
    
    Returns:
        متن با اعداد انگلیسی
    
    مثال:
        >>> to_english_digits("سلام ۱۲۳")
        'سلام 123'
    """
    if not text:
        return text
    
    digit_map = str.maketrans(PERSIAN_DIGITS, ENGLISH_DIGITS)
    return text.translate(digit_map)


def is_persian_text(text: str, threshold: float = 0.3) -> bool:
    """
    تشخیص فارسی بودن متن بر اساس نسبت کاراکترهای فارسی
    
    Args:
        text: متن ورودی
        threshold: آستانه تشخیص (نسبت کاراکترهای فارسی به کل)
    
    Returns:
        True اگر متن فارسی باشد
    
    مثال:
        >>> is_persian_text("سلام دنیا")
        True
        >>> is_persian_text("Hello World")
        False
    """
    if not text:
        return False
    
    text_without_spaces = text.replace(" ", "").replace("\t", "").replace("\n", "")
    if not text_without_spaces:
        return False
    
    persian_chars = re.findall(PERSIAN_CHARS_RANGE, text_without_spaces)
    ratio = len(persian_chars) / len(text_without_spaces)
    
    return ratio >= threshold


def get_persian_chars_count(text: str) -> int:
    """
    تعداد کاراکترهای فارسی در متن
    
    Args:
        text: متن ورودی
    
    Returns:
        تعداد کاراکترهای فارسی
    """
    if not text:
        return 0
    return len(re.findall(PERSIAN_CHARS_RANGE, text))


def remove_diacritics(text: str) -> str:
    """
    حذف اعراب (فَتْحه، کَسْرِه، ضَمَّه، تنوین، تشدید و ...) از متن فارسی
    
    Args:
        text: متن ورودی با اعراب
    
    Returns:
        متن بدون اعراب
    
    مثال:
        >>> remove_diacritics("مُتَرْجِم")
        'مترجم'
    """
    if not text:
        return text
    
    diacritic_map = str.maketrans("", "", PERSIAN_DIACRITICS)
    return text.translate(diacritic_map)


def extract_persian_words(text: str) -> list:
    """
    استخراج کلمات فارسی از متن
    
    Args:
        text: متن ورودی
    
    Returns:
        لیست کلمات فارسی
    """
    if not text:
        return []
    
    # الگوی کلمات فارسی (حروف فارسی تکراری)
    pattern = r"[\u0600-\u06FF]+"
    return re.findall(pattern, text)


def convert_finglish_to_persian(text: str) -> str:
    """
    تبدیل ساده فینگلیش به فارسی (نگاشت حروف)
    
    توجه: این یک تبدیل ساده است و ممکن است 100% دقیق نباشد
    
    Args:
        text: متن فینگلیش
    
    Returns:
        متن فارسی تقریبی
    """
    # نگاشت ساده حروف انگلیسی به فارسی
    finglish_map = {
        'a': 'ا', 'b': 'ب', 'p': 'پ', 't': 'ت', 's': 'س', 'j': 'ج',
        'ch': 'چ', 'h': 'ح', 'kh': 'خ', 'd': 'د', 'z': 'ز', 'r': 'ر',
        'zh': 'ژ', 'sh': 'ش', 'gh': 'غ', 'f': 'ف', 'q': 'ق', 'k': 'ک',
        'g': 'گ', 'l': 'ل', 'm': 'م', 'n': 'ن', 'v': 'و', 'y': 'ی',
        'i': 'ای', 'o': 'او', 'u': 'او',
    }
    
    # این یک تبدیل ساده است
    result = text.lower()
    for eng, per in finglish_map.items():
        result = result.replace(eng, per)
    
    return result
