"""
System Utilities — ابزارهای سیستم
==================================

توابع مفید برای دریافت اطلاعات سیستم عامل
"""

import os
import sys
import platform
import subprocess
import shutil
from typing import Dict, Union
from datetime import datetime, timedelta


def get_system_info() -> Dict[str, str]:
    """
    دریافت اطلاعات کلی سیستم
    
    Returns:
        دیکشنری شامل اطلاعات سیستم
    """
    info = {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": " ".join(platform.architecture()),
    }
    
    # تلاش برای دریافت توزیع لینوکس
    try:
        if platform.system() == "Linux":
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        info["distribution"] = line.split("=")[1].strip().strip('"')
                        break
    except (FileNotFoundError, IOError):
        info["distribution"] = "Unknown"
    
    return info


def get_python_info() -> Dict[str, str]:
    """
    دریافت اطلاعات Python
    
    Returns:
        دیکشنری شامل اطلاعات Python
    """
    return {
        "version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "executable": sys.executable,
    }


def cpu_usage() -> float:
    """
    دریافت درصد استفاده از CPU
    
    Returns:
        درصد استفاده از CPU (0-100)
    """
    try:
        if platform.system() == "Linux":
            # خواندن آمار CPU از /proc/stat
            with open("/proc/stat", "r") as f:
                line = f.readline().strip()
            parts = line.split()
            if len(parts) >= 5 and parts[0] == "cpu":
                # cpu  user  nice  system  idle  iowait  irq  softirq  steal
                idle = int(parts[4])
                total = sum(int(x) for x in parts[1:])
                # خواندن مجدد بعد از یک ثانیه (اینجا فقط یک تخمین می‌زنیم)
                return round(100.0 * (1 - (idle / max(total, 1))), 1)
        # fallback
        import psutil
        return psutil.cpu_percent(interval=0.1)
    except (ImportError, FileNotFoundError, IOError, IndexError):
        return 0.0


def memory_usage() -> Dict[str, str]:
    """
    دریافت اطلاعات استفاده از حافظه
    
    Returns:
        دیکشنری شامل اطلاعات RAM
    """
    try:
        if platform.system() == "Linux":
            with open("/proc/meminfo", "r") as f:
                meminfo = {}
                for line in f:
                    parts = line.split(":")
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        meminfo[key] = value
            
            total = _parse_mem_value(meminfo.get("MemTotal", "0 kB"))
            available = _parse_mem_value(meminfo.get("MemAvailable", "0 kB"))
            free = _parse_mem_value(meminfo.get("MemFree", "0 kB"))
            
            used = total - available
            percent = round((used / total) * 100, 1) if total > 0 else 0
            
            return {
                "total": _format_bytes(total),
                "used": _format_bytes(used),
                "free": _format_bytes(free),
                "available": _format_bytes(available),
                "percent": f"{percent}%",
            }
    except (FileNotFoundError, IOError):
        pass
    
    return {
        "total": "N/A",
        "used": "N/A",
        "free": "N/A",
        "available": "N/A",
        "percent": "N/A",
    }


def disk_usage(path: str = "/") -> Dict[str, str]:
    """
    دریافت اطلاعات استفاده از دیسک
    
    Args:
        path: مسیر مورد نظر
    
    Returns:
        دیکشنری شامل اطلاعات دیسک
    """
    try:
        usage = shutil.disk_usage(path)
        total = usage.total
        used = usage.used
        free = usage.free
        percent = round((used / total) * 100, 1) if total > 0 else 0
        
        return {
            "path": path,
            "total": _format_bytes(total),
            "used": _format_bytes(used),
            "free": _format_bytes(free),
            "percent": f"{percent}%",
        }
    except Exception:
        return {
            "path": path,
            "total": "N/A",
            "used": "N/A",
            "free": "N/A",
            "percent": "N/A",
        }


def uptime() -> str:
    """
    دریافت مدت زمان روشن بودن سیستم
    
    Returns:
        رشته نمایشی مدت زمان
    """
    try:
        if platform.system() == "Linux":
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
            
            uptime_delta = timedelta(seconds=uptime_seconds)
            days = uptime_delta.days
            hours, remainder = divmod(uptime_delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            parts = []
            if days > 0:
                parts.append(f"{int(days)} روز")
            if hours > 0:
                parts.append(f"{int(hours)} ساعت")
            if minutes > 0:
                parts.append(f"{int(minutes)} دقیقه")
            parts.append(f"{int(seconds)} ثانیه")
            
            return " ".join(parts)
    except (FileNotFoundError, IOError):
        pass
    
    return "N/A"


def _parse_mem_value(value: str) -> int:
    """تبدیل رشته مقدار حافظه به بایت"""
    try:
        parts = value.split()
        num = int(parts[0])
        unit = parts[1].lower() if len(parts) > 1 else "kb"
        
        if unit == "kb" or unit == "kib":
            return num * 1024
        elif unit == "mb" or unit == "mib":
            return num * 1024 * 1024
        elif unit == "gb" or unit == "gib":
            return num * 1024 * 1024 * 1024
        else:
            return num
    except (ValueError, IndexError):
        return 0


def _format_bytes(bytes_val: int) -> str:
    """فرمت‌بندی بایت به صورت خوانا"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_val < 1024:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024
    return f"{bytes_val:.2f} PB"



