"""
Converters — ابزارهای تبدیل فرمت
=================================

توابع تبدیل بین فرمت‌های مختلف مثل JSON، YAML، Base64 و ...
"""

import json
import base64
from typing import Any, Dict, Union


def json_to_yaml(json_string: str) -> str:
    """
    تبدیل JSON به YAML
    
    Args:
        json_string: رشته JSON
    
    Returns:
        رشته YAML
    """
    try:
        import yaml
    except ImportError:
        # YAML پشتیبانی ساده بدون کتابخانه
        data = json.loads(json_string)
        return _simple_json_to_yaml(data)
    
    data = json.loads(json_string)
    return yaml.dump(data, default_flow_style=False, allow_unicode=True)


def yaml_to_json(yaml_string: str) -> str:
    """
    تبدیل YAML به JSON
    
    Args:
        yaml_string: رشته YAML
    
    Returns:
        رشته JSON فرمت‌بندی شده
    """
    try:
        import yaml
        data = yaml.safe_load(yaml_string)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except ImportError:
        # سعی می‌کنیم با روش ساده تبدیل کنیم
        if ":" in yaml_string and not yaml_string.startswith("{"):
            # YAML ساده key: value
            lines = yaml_string.strip().split("\n")
            result = {}
            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    result[key.strip()] = value.strip()
            return json.dumps(result, indent=2, ensure_ascii=False)
        raise ImportError("برای تبدیل YAML لطفاً کتابخانه PyYAML را نصب کنید: pip install pyyaml")


def text_to_base64(text: str, encoding: str = "utf-8") -> str:
    """
    تبدیل متن به Base64
    
    Args:
        text: متن ورودی
        encoding: نوع encoding
    
    Returns:
        رشته Base64
    """
    bytes_data = text.encode(encoding)
    return base64.b64encode(bytes_data).decode("ascii")


def base64_to_text(base64_string: str, encoding: str = "utf-8") -> str:
    """
    تبدیل Base64 به متن
    
    Args:
        base64_string: رشته Base64
        encoding: نوع encoding
    
    Returns:
        متن اصلی
    """
    bytes_data = base64.b64decode(base64_string)
    return bytes_data.decode(encoding)


def _simple_json_to_yaml(data: Any, indent: int = 0) -> str:
    """
    تبدیل ساده JSON به YAML بدون کتابخانه PyYAML
    """
    yaml_str = ""
    prefix = "  " * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                yaml_str += f"{prefix}{key}:\n"
                yaml_str += _simple_json_to_yaml(value, indent + 1)
            else:
                yaml_str += f"{prefix}{key}: {_yaml_value(value)}\n"
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                yaml_str += f"{prefix}- \n"
                yaml_str += _simple_json_to_yaml(item, indent + 1)
            else:
                yaml_str += f"{prefix}- {_yaml_value(item)}\n"
    
    return yaml_str


def _yaml_value(value: Any) -> str:
    """فرمت‌بندی مقدار برای YAML"""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        # اگر شامل کاراکترهای خاص باشد
        if any(c in value for c in [":", "#", "{", "}", "[", "]", "&", "*", "!", "|", ">", "'", '"']):
            return f"'{value}'"
        return value
    return str(value)


def json_pretty(json_string: str) -> str:
    """
    فرمت‌بندی زیبای JSON
    
    Args:
        json_string: رشته JSON
    
    Returns:
        JSON فرمت‌بندی شده
    """
    data = json.loads(json_string)
    return json.dumps(data, indent=2, ensure_ascii=False)


def json_minify(json_string: str) -> str:
    """
    فشرده‌سازی JSON (حذف فاصله‌ها)
    
    Args:
        json_string: رشته JSON
    
    Returns:
        JSON فشرده
    """
    data = json.loads(json_string)
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)
