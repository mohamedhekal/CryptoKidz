#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف تشغيل CryptoKidz
"""

import sys
import os

# إضافة المجلد الحالي للمسار
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """تشغيل التطبيق"""
    try:
        from main import main as run_app
        run_app()
    except ImportError as e:
        print(f"خطأ في استيراد المكتبات: {e}")
        print("تأكد من تثبيت جميع المتطلبات:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"خطأ في تشغيل التطبيق: {e}")

if __name__ == "__main__":
    main() 