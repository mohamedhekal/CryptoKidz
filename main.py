#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CryptoKidz - استكشاف عالم البيتكوين
التطبيق الرئيسي
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from ui.main_window import MainWindow
from data.progress_manager import ProgressManager

class CryptoKidzApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧠 CryptoKidz - استكشاف عالم البيتكوين")
        self.root.geometry("1200x800")
        self.root.configure(bg='#FFE5E5')  # لون وردي فاتح للأطفال
        
        # تعيين أيقونة التطبيق
        try:
            self.root.iconbitmap('assets/icon.ico')
        except:
            pass
        
        # تهيئة مدير التقدم
        self.progress_manager = ProgressManager()
        
        # إنشاء النافذة الرئيسية
        self.main_window = MainWindow(self.root, self.progress_manager)
        
        # تعيين الحد الأدنى لحجم النافذة
        self.root.minsize(1000, 700)
        
        # توسيط النافذة
        self.center_window()
        
    def center_window(self):
        """توسيط النافذة على الشاشة"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def run(self):
        """تشغيل التطبيق"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nتم إغلاق التطبيق بواسطة المستخدم")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ غير متوقع: {str(e)}")
        finally:
            # حفظ التقدم قبل الإغلاق
            self.progress_manager.save_progress()

def main():
    """الدالة الرئيسية"""
    print("🚀 بدء تشغيل CryptoKidz...")
    print("🐱 مرحباً بك في عالم البيتكوين الممتع!")
    
    app = CryptoKidzApp()
    app.run()

if __name__ == "__main__":
    main() 