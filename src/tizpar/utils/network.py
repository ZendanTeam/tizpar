"""
Network Utilities — ابزارهای شبکه
==================================

توابع مفید برای بررسی وضعیت شبکه و اینترنت
"""

import subprocess
import platform
import socket
from typing import Dict, Optional, Union

import requests


def check_url(url: str, timeout: int = 10) -> Dict[str, Union[bool, int, float, str]]:
    """
    بررسی وضعیت یک URL
    
    Args:
        url: آدرس مورد نظر
        timeout: تایم‌اوت به ثانیه
    
    Returns:
        دیکشنری شامل وضعیت، کد وضعیت، زمان پاسخ و ...
    
    مثال:
        >>> check_url("https://google.com")
        {'success': True, 'status_code': 200, 'response_time': 0.45, 'url': 'https://google.com'}
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    try:
        start_time = __import__("time").time()
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "Tizpar/0.0.1"},
            allow_redirects=True,
        )
        response_time = round(__import__("time").time() - start_time, 3)
        
        return {
            "success": response.ok,
            "status_code": response.status_code,
            "response_time": f"{response_time} ثانیه",
            "url": url,
            "redirects": len(response.history),
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "تایم‌اوت",
            "url": url,
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "خطا در اتصال",
            "url": url,
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "url": url,
        }


def get_public_ip() -> str:
    """
    دریافت آدرس IP عمومی
    
    Returns:
        آدرس IP عمومی
    
    مثال:
        >>> get_public_ip()
        '1.2.3.4'
    """
    services = [
        "https://api.ipify.org",
        "https://icanhazip.com",
        "https://checkip.amazonaws.com",
    ]
    
    for service in services:
        try:
            response = requests.get(service, timeout=5)
            if response.ok:
                return response.text.strip()
        except requests.exceptions.RequestException:
            continue
    
    raise ConnectionError("عدم دسترسی به سرویس‌های تشخیص IP")


def ping_host(host: str, count: int = 4) -> Dict[str, Union[bool, str, float]]:
    """
    پینگ یک هاست
    
    Args:
        host: آدرس هاست
        count: تعداد پینگ‌ها
    
    Returns:
        دیکشنری شامل نتایج پینگ
    """
    try:
        # رزولوشن DNS
        ip = socket.gethostbyname(host)
        
        if platform.system().lower() == "windows":
            cmd = ["ping", "-n", str(count), host]
        else:
            cmd = ["ping", "-c", str(count), host]
        
        start_time = __import__("time").time()
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        elapsed = round(__import__("time").time() - start_time, 2)
        
        if result.returncode == 0:
            # استخراج آمار پینگ از خروجی
            output = result.stdout
            
            # تلاش برای استخراج میانگین زمان
            import re
            time_stats = {}
            
            # الگوی لینوکس
            linux_pattern = r"min/avg/max(?:/mdev)? = [\d.]+/([\d.]+)/[\d.]+"
            match = re.search(linux_pattern, output)
            if match:
                time_stats["average_ping"] = f"{match.group(1)} ms"
            
            # الگوی مک
            mac_pattern = r"min/avg/max/stddev = [\d.]+/([\d.]+)/[\d.]+/[\d.]+"
            match = re.search(mac_pattern, output)
            if match:
                time_stats["average_ping"] = f"{match.group(1)} ms"
            
            # الگوی ویندوز
            win_pattern = r"متوسط = ([\d]+)"
            match = re.search(win_pattern, output)
            if match:
                time_stats["average_ping"] = f"{match.group(1)} ms"
            
            # الگوی انگلیسی ویندوز
            win_en_pattern = r"Average = ([\d]+)"
            match = re.search(win_en_pattern, output)
            if match:
                time_stats["average_ping"] = f"{match.group(1)} ms"
            
            # بررسی packet loss
            loss_pattern = r"(\d+)% (packet loss|گم شدن)"
            match = re.search(loss_pattern, output)
            if match:
                time_stats["packet_loss"] = f"{match.group(1)}%"
            else:
                time_stats["packet_loss"] = "0%"
            
            return {
                "success": True,
                "host": host,
                "ip": ip,
                "time": f"{elapsed} ثانیه",
                **time_stats,
            }
        else:
            return {
                "success": False,
                "host": host,
                "ip": ip,
                "error": "هاست پاسخ نمی‌دهد",
                "output": result.stderr[:200] if result.stderr else "",
            }
    except socket.gaierror:
        return {
            "success": False,
            "host": host,
            "error": "نام هاست معتبر نیست",
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "host": host,
            "error": "تایم‌اوت",
        }
    except Exception as e:
        return {
            "success": False,
            "host": host,
            "error": str(e),
        }
