<div dir="rtl" align="center">

# ⚡ تیزپر (Tizpar) v0.0.1

**ابزارک توسعه‌دهنده فارسی — سریع و کامل**

[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/ZendanTeam/tizpar)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Tests](https://img.shields.io/badge/pytest-passing-success.svg)]()

</div>

---

## 📋 معرفی (Introduction)

**تیزپر** یک ابزارک توسعه‌دهنده فارسی است که ابزارهای مفید و کاربردی را برای توسعه‌دهندگان ایرانی و فارسی زبان فراهم می‌کند.

با تیزپر می‌توانید:
- اعداد انگلیسی را به فارسی و برعکس تبدیل کنید
- متن فارسی را تشخیص دهید
- اعراب را از متن فارسی حذف کنید
- اطلاعات سیستم خود را مشاهده کنید
- وضعیت شبکه و اینترنت را بررسی کنید
- فرمت‌های مختلف را به هم تبدیل کنید (JSON↔YAML، Base64)
- و کلی امکانات دیگر...

---

## 📦 نصب (Installation)

### نصب با pip (از روی GitHub)

```bash
pip install git+https://github.com/ZendanTeam/tizpar.git
```

### نصب از روی سورس

```bash
git clone https://github.com/ZendanTeam/tizpar.git
cd tizpar
pip install -e .
```

### نصب با uv (سریع‌تر)

```bash
uv pip install git+https://github.com/ZendanTeam/tizpar.git
```

---

## 🚀 استفاده (Usage)

### خط فرمان (CLI)

بعد از نصب، دستور `tizpar` در دسترس شماست:

```bash
# نمایش اطلاعات و راهنما
tizpar

# نمایش نسخه
tizpar --version

# راهنمای کامل
tizpar --help
```

#### 📝 ابزارهای فارسی

```bash
# تبدیل اعداد انگلیسی به فارسی
tizpar persian to-persian "Hello 123 World"

# تبدیل اعداد فارسی به انگلیسی
tizpar persian to-english "سلام ۱۲۳ دنیا"

# تشخیص فارسی بودن متن
tizpar persian detect "سلام دنیا"

# حذف اعراب از متن فارسی
tizpar persian clean "مُتَرْجِم"
```

#### 💻 ابزارهای سیستم

```bash
# اطلاعات سیستم
tizpar system info

# وضعیت CPU
tizpar system cpu

# وضعیت حافظه
tizpar system memory

# وضعیت دیسک
tizpar system disk

# زمان روشن بودن سیستم
tizpar system uptime
```

#### 🌐 ابزارهای شبکه

```bash
# نمایش IP عمومی
tizpar network ip

# بررسی یک URL
tizpar network check https://google.com

# پینگ یک هاست
tizpar network ping google.com
```

#### 🔄 ابزارهای تبدیل

```bash
# تبدیل JSON به YAML
tizpar convert json2yaml '{"name": "tizpar", "version": "0.0.1"}'

# تبدیل YAML به JSON
tizpar convert yaml2json "name: tizpar\nversion: 0.0.1"

# تبدیل متن به Base64
tizpar convert to-base64 "Hello World"

# تبدیل Base64 به متن
tizpar convert from-base64 "SGVsbG8gV29ybGQ="
```

### استفاده در کد Python

```python
from tizpar import (
    to_persian_digits,
    to_english_digits,
    is_persian_text,
    get_system_info,
    get_public_ip,
)

# تبدیل اعداد
print(to_persian_digits("123"))  # ۱۲۳
print(to_english_digits("۱۲۳"))  # 123

# تشخیص فارسی
print(is_persian_text("سلام دنیا"))  # True

# اطلاعات سیستم
info = get_system_info()
print(info["system"], info["machine"])

# IP عمومی
ip = get_public_ip()
print(f"IP شما: {ip}")
```

---

## 🗂 ساختار پروژه (Project Structure)

```
tizpar/
├── src/
│   └── tizpar/
│       ├── __init__.py         # پکیج اصلی
│       ├── core.py             # Rich Console و تنظیمات
│       ├── cli/
│       │   ├── __init__.py
│       │   ├── main.py         # CLI اصلی (Click)
│       │   └── commands/
│       │       ├── __init__.py
│       │       ├── info.py     # دستور info
│       │       ├── persian.py  # دستورات فارسی
│       │       ├── system.py   # دستورات سیستم
│       │       ├── network.py  # دستورات شبکه
│       │       └── convert.py  # دستورات تبدیل
│       └── utils/
│           ├── __init__.py
│           ├── persian.py      # ابزارهای فارسی
│           ├── system.py       # ابزارهای سیستم
│           ├── network.py      # ابزارهای شبکه
│           └── converters.py   # ابزارهای تبدیل
├── tests/
│   ├── __init__.py
│   ├── test_persian.py
│   ├── test_system.py
│   ├── test_network.py
│   └── test_converters.py
├── docs/
├── pyproject.toml
├── setup.cfg
├── Makefile
├── Dockerfile
├── README.md
└── LICENSE
```

---

## 🧪 تست (Testing)

```bash
# نصب وابستگی‌های تست
pip install pytest

# اجرای تست‌ها
pytest

# با جزئیات بیشتر
pytest -v

# با گزارش پوشش
pip install pytest-cov
pytest --cov=src/tizpar
```

---

## 📄 مجوز (License)

این پروژه تحت مجوز MIT منتشر شده است.

---

<div dir="rtl" align="center">

**ساخته شده با ❤️ در ZendanTeam**

</div>
