# استفاده از Python 3.11 رسمی
FROM python:3.11-slim

# نصب وابستگی‌های سیستم
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

# تنظیم متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# کپی پروژه
WORKDIR /app
COPY . .

# نصب تیزپر
RUN pip install --no-cache-dir .

# اجرا
ENTRYPOINT ["tizpar"]
CMD ["--help"]
