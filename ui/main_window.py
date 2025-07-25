#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
النافذة الرئيسية للتطبيق
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
from .wallet_page import WalletPage
from .crypto_page import CryptoPage
from .quiz_page import QuizPage
from .progress_page import ProgressPage

class MainWindow:
    """النافذة الرئيسية للتطبيق"""
    
    def __init__(self, root, progress_manager):
        self.root = root
        self.progress_manager = progress_manager
        
        # الألوان
        self.colors = {
            'primary': '#FF6B6B',
            'secondary': '#4ECDC4',
            'accent': '#45B7D1',
            'success': '#96CEB4',
            'warning': '#FFEAA7',
            'background': '#FFE5E5',
            'text': '#2C3E50'
        }
        
        # إعداد النافذة
        self.setup_window()
        
        # إنشاء الواجهة
        self.create_widgets()
        
        # تحميل التقدم
        self.load_progress()
    
    def setup_window(self):
        """إعداد النافذة"""
        # تعيين الألوان
        self.root.configure(bg=self.colors['background'])
        
        # تعيين الخطوط
        self.title_font = ('Arial', 24, 'bold')
        self.header_font = ('Arial', 16, 'bold')
        self.normal_font = ('Arial', 12)
        self.button_font = ('Arial', 14, 'bold')
    
    def create_widgets(self):
        """إنشاء عناصر الواجهة"""
        # الإطار الرئيسي
        self.main_frame = tk.Frame(self.root, bg=self.colors['background'])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # العنوان الرئيسي
        self.title_label = tk.Label(
            self.main_frame,
            text="🧠 CryptoKidz - استكشاف عالم البيتكوين",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.title_label.pack(pady=(0, 30))
        
        # رسالة الترحيب
        self.welcome_label = tk.Label(
            self.main_frame,
            text="🐱 مرحباً بك! أنا Crypto the Cat وسأساعدك في تعلم البيتكوين",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.welcome_label.pack(pady=(0, 40))
        
        # إطار الأزرار
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.buttons_frame.pack()
        
        # أزرار التنقل
        self.create_navigation_buttons()
        
        # إطار المعلومات
        self.info_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.info_frame.pack(pady=30)
        
        # معلومات التقدم
        self.create_progress_info()
        
        # إطار الأسفل
        self.bottom_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(20, 0))
        
        # أزرار إضافية
        self.create_bottom_buttons()
    
    def create_navigation_buttons(self):
        """إنشاء أزرار التنقل"""
        buttons_data = [
            {
                'text': '💼 إنشاء محفظة',
                'command': self.open_wallet_page,
                'color': self.colors['primary'],
                'description': 'تعلم كيف تنشئ محفظة بيتكوين'
            },
            {
                'text': '🔐 تعلم التشفير',
                'command': self.open_crypto_page,
                'color': self.colors['secondary'],
                'description': 'اكتشف عالم التشفير والرموز السرية'
            },
            {
                'text': '🎯 اختبارات تفاعلية',
                'command': self.open_quiz_page,
                'color': self.colors['accent'],
                'description': 'اختبر معرفتك وحصل على مكافآت'
            },
            {
                'text': '📊 تقدمي',
                'command': self.open_progress_page,
                'color': self.colors['success'],
                'description': 'شاهد تقدمك ومكافآتك'
            }
        ]
        
        for i, button_data in enumerate(buttons_data):
            # إطار الزر
            button_frame = tk.Frame(self.buttons_frame, bg=self.colors['background'])
            button_frame.grid(row=i//2, column=i%2, padx=20, pady=10)
            
            # الزر الرئيسي
            button = tk.Button(
                button_frame,
                text=button_data['text'],
                command=button_data['command'],
                font=self.button_font,
                bg=button_data['color'],
                fg='white',
                relief=tk.RAISED,
                bd=3,
                padx=30,
                pady=15,
                cursor='hand2'
            )
            button.pack(pady=(0, 5))
            
            # وصف الزر
            desc_label = tk.Label(
                button_frame,
                text=button_data['description'],
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text'],
                wraplength=200
            )
            desc_label.pack()
    
    def create_progress_info(self):
        """إنشاء معلومات التقدم"""
        # عنوان القسم
        progress_title = tk.Label(
            self.info_frame,
            text="📈 تقدمك الحالي",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        progress_title.pack(pady=(0, 10))
        
        # إطار الإحصائيات
        stats_frame = tk.Frame(self.info_frame, bg=self.colors['background'])
        stats_frame.pack()
        
        # الإحصائيات
        self.stats_labels = {}
        stats_data = [
            ('total_quizzes', 'الاختبارات المكتملة', '0'),
            ('total_points', 'النقاط المكتسبة', '0'),
            ('average_score', 'متوسط النتيجة', '0%'),
            ('badges_earned', 'الشارات المكتسبة', '0')
        ]
        
        for i, (key, label, default_value) in enumerate(stats_data):
            stat_frame = tk.Frame(stats_frame, bg=self.colors['background'])
            stat_frame.grid(row=i//2, column=i%2, padx=20, pady=5)
            
            # العنوان
            title_label = tk.Label(
                stat_frame,
                text=label,
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text']
            )
            title_label.pack()
            
            # القيمة
            value_label = tk.Label(
                stat_frame,
                text=default_value,
                font=self.header_font,
                bg=self.colors['background'],
                fg=self.colors['primary']
            )
            value_label.pack()
            
            self.stats_labels[key] = value_label
    
    def create_bottom_buttons(self):
        """إنشاء الأزرار السفلية"""
        # إطار الأزرار
        bottom_buttons_frame = tk.Frame(self.bottom_frame, bg=self.colors['background'])
        bottom_buttons_frame.pack()
        
        # زر المساعدة
        help_button = tk.Button(
            bottom_buttons_frame,
            text="❓ مساعدة",
            command=self.show_help,
            font=self.normal_font,
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        help_button.pack(side=tk.LEFT, padx=10)
        
        # زر الإعدادات
        settings_button = tk.Button(
            bottom_buttons_frame,
            text="⚙️ إعدادات",
            command=self.show_settings,
            font=self.normal_font,
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        settings_button.pack(side=tk.LEFT, padx=10)
        
        # زر الخروج
        exit_button = tk.Button(
            bottom_buttons_frame,
            text="🚪 خروج",
            command=self.exit_app,
            font=self.normal_font,
            bg=self.colors['primary'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        exit_button.pack(side=tk.RIGHT, padx=10)
    
    def load_progress(self):
        """تحميل التقدم وتحديث الواجهة"""
        progress = self.progress_manager.get_progress()
        
        # تحديث الإحصائيات
        self.stats_labels['total_quizzes'].config(text=str(progress.get('total_quizzes', 0)))
        self.stats_labels['total_points'].config(text=str(progress.get('total_points', 0)))
        self.stats_labels['average_score'].config(text=f"{progress.get('average_score', 0):.1f}%")
        self.stats_labels['badges_earned'].config(text=str(len(progress.get('badges', []))))
    
    def open_wallet_page(self):
        """فتح صفحة إنشاء المحفظة"""
        wallet_window = tk.Toplevel(self.root)
        wallet_page = WalletPage(wallet_window, self.progress_manager)
    
    def open_crypto_page(self):
        """فتح صفحة تعلم التشفير"""
        crypto_window = tk.Toplevel(self.root)
        crypto_page = CryptoPage(crypto_window, self.progress_manager)
    
    def open_quiz_page(self):
        """فتح صفحة الاختبارات"""
        quiz_window = tk.Toplevel(self.root)
        quiz_page = QuizPage(quiz_window, self.progress_manager)
    
    def open_progress_page(self):
        """فتح صفحة التقدم"""
        progress_window = tk.Toplevel(self.root)
        progress_page = ProgressPage(progress_window, self.progress_manager)
    
    def show_help(self):
        """عرض المساعدة"""
        help_text = """
🐱 مرحباً بك في CryptoKidz!

هذا التطبيق سيساعدك في تعلم:
• كيفية إنشاء محفظة بيتكوين
• أساسيات التشفير والرموز السرية
• كيف يعمل البلوكتشين
• الأمان الرقمي

💡 نصائح:
• ابدأ بإنشاء محفظة
• ثم تعلم التشفير
• اختبر معرفتك
• راقب تقدمك

🔒 تذكر: هذا تطبيق تعليمي فقط!
        """
        
        messagebox.showinfo("❓ مساعدة", help_text)
    
    def show_settings(self):
        """عرض الإعدادات"""
        settings_text = """
⚙️ إعدادات CryptoKidz

• حجم النافذة: 1200x800
• الألوان: ملونة ومناسبة للأطفال
• اللغة: العربية
• الصوت: متاح (إذا كان مدعوماً)

🔧 إعدادات متقدمة:
• حفظ التقدم: تلقائي
• النسخ الاحتياطي: محلي
• الأمان: تعليمي فقط
        """
        
        messagebox.showinfo("⚙️ إعدادات", settings_text)
    
    def exit_app(self):
        """خروج من التطبيق"""
        if messagebox.askyesno("🚪 خروج", "هل تريد الخروج من التطبيق؟"):
            self.progress_manager.save_progress()
            self.root.quit()
    
    def refresh_progress(self):
        """تحديث معلومات التقدم"""
        self.load_progress() 