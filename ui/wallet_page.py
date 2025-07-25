#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
صفحة إنشاء المحفظة
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# إضافة المجلد الأب للمسار
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wallet_generator import SimpleWalletGenerator
from animations import CryptoAnimations

class WalletPage:
    """صفحة إنشاء المحفظة"""
    
    def __init__(self, window, progress_manager):
        self.window = window
        self.progress_manager = progress_manager
        self.wallet_generator = SimpleWalletGenerator()
        
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
        
        # متغيرات الحالة
        self.current_step = 0
        self.wallet_data = None
        self.steps = self.wallet_generator.explain_wallet_creation()
    
    def setup_window(self):
        """إعداد النافذة"""
        self.window.title("💼 إنشاء محفظة البيتكوين")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.colors['background'])
        
        # تعيين الخطوط
        self.title_font = ('Arial', 20, 'bold')
        self.header_font = ('Arial', 16, 'bold')
        self.normal_font = ('Arial', 12)
        self.button_font = ('Arial', 14, 'bold')
    
    def create_widgets(self):
        """إنشاء عناصر الواجهة"""
        # الإطار الرئيسي
        self.main_frame = tk.Frame(self.window, bg=self.colors['background'])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # العنوان
        self.title_label = tk.Label(
            self.main_frame,
            text="💼 إنشاء محفظة البيتكوين",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.title_label.pack(pady=(0, 20))
        
        # رسالة الترحيب
        self.welcome_label = tk.Label(
            self.main_frame,
            text="🐱 مرحباً! سأساعدك في إنشاء محفظتك الأولى",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.welcome_label.pack(pady=(0, 30))
        
        # إطار المحتوى
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # عرض الخطوة الحالية
        self.show_current_step()
        
        # إطار الأزرار
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.buttons_frame.pack(pady=20)
        
        # أزرار التنقل
        self.create_navigation_buttons()
    
    def show_current_step(self):
        """عرض الخطوة الحالية"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if self.current_step == 0:
            self.show_introduction()
        elif self.current_step <= len(self.steps):
            self.show_wallet_step(self.current_step - 1)
        else:
            self.show_wallet_result()
    
    def show_introduction(self):
        """عرض المقدمة"""
        # إطار المقدمة
        intro_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        intro_frame.pack(expand=True)
        
        # نص المقدمة
        intro_text = """
🔐 ما هي محفظة البيتكوين؟

محفظة البيتكوين مثل محفظتك العادية، ولكن رقمية!
تحتوي على:
• كلمات سرية سحرية 🔑
• مفتاح سري (مثل مفتاح بيتك) 🔐
• مفتاح عام (مثل عنوان بيتك) 🏠
• عنوان البيتكوين (مثل رقم الهاتف) 📞

🎯 سنتعلم اليوم:
1. كيف تولد الكلمات السرية
2. كيف تنشئ المفاتيح
3. كيف تحصل على العنوان
4. كيف تحمي محفظتك

🚀 هل أنت مستعد للبدء؟
        """
        
        intro_label = tk.Label(
            intro_frame,
            text=intro_text,
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            justify=tk.LEFT,
            wraplength=600
        )
        intro_label.pack(pady=20)
        
        # زر البدء
        start_button = tk.Button(
            intro_frame,
            text="🚀 ابدأ الآن!",
            command=self.next_step,
            font=self.button_font,
            bg=self.colors['primary'],
            fg='white',
            relief=tk.RAISED,
            bd=3,
            padx=30,
            pady=10,
            cursor='hand2'
        )
        start_button.pack(pady=20)
    
    def show_wallet_step(self, step_index):
        """عرض خطوة إنشاء المحفظة"""
        step = self.steps[step_index]
        
        # إطار الخطوة
        step_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        step_frame.pack(expand=True)
        
        # عنوان الخطوة
        step_title = tk.Label(
            step_frame,
            text=f"الخطوة {step['step']}: {step['title']}",
            font=self.header_font,
            bg=self.colors['background'],
            fg=step['color']
        )
        step_title.pack(pady=(0, 20))
        
        # وصف الخطوة
        step_desc = tk.Label(
            step_frame,
            text=step['description'],
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=500
        )
        step_desc.pack(pady=(0, 20))
        
        # كود مبسط
        if step_index == 0:  # توليد الكلمات السرية
            self.show_seed_generation(step_frame)
        elif step_index == 1:  # إنشاء المفتاح الخاص
            self.show_private_key_generation(step_frame)
        elif step_index == 2:  # إنشاء المفتاح العام
            self.show_public_key_generation(step_frame)
        elif step_index == 3:  # إنشاء العنوان
            self.show_address_generation(step_frame)
    
    def show_seed_generation(self, parent_frame):
        """عرض توليد الكلمات السرية"""
        # إطار الكلمات السرية
        seed_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        seed_frame.pack(pady=20)
        
        # زر توليد الكلمات
        generate_button = tk.Button(
            seed_frame,
            text="🎲 توليد الكلمات السرية",
            command=self.generate_seed,
            font=self.button_font,
            bg=self.colors['secondary'],
            fg='white',
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        generate_button.pack(pady=(0, 20))
        
        # عرض الكلمات السرية
        self.seed_label = tk.Label(
            seed_frame,
            text="اضغط على الزر أعلاه لتوليد الكلمات السرية",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=400
        )
        self.seed_label.pack()
    
    def show_private_key_generation(self, parent_frame):
        """عرض إنشاء المفتاح الخاص"""
        # إطار المفتاح الخاص
        private_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        private_frame.pack(pady=20)
        
        # نص توضيحي
        explain_label = tk.Label(
            private_frame,
            text="من الكلمات السرية، نقوم بإنشاء مفتاح سري طويل:",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        explain_label.pack(pady=(0, 10))
        
        # عرض المفتاح الخاص
        self.private_key_label = tk.Label(
            private_frame,
            text="سيظهر المفتاح الخاص هنا...",
            font=('Courier', 10),
            bg='white',
            fg=self.colors['text'],
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=5
        )
        self.private_key_label.pack(pady=10)
        
        # تحذير
        warning_label = tk.Label(
            private_frame,
            text="⚠️ تحذير: هذا المفتاح سري جداً! لا تشاركه مع أحد!",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['warning']
        )
        warning_label.pack(pady=10)
    
    def show_public_key_generation(self, parent_frame):
        """عرض إنشاء المفتاح العام"""
        # إطار المفتاح العام
        public_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        public_frame.pack(pady=20)
        
        # نص توضيحي
        explain_label = tk.Label(
            public_frame,
            text="من المفتاح الخاص، نقوم بإنشاء مفتاح عام يمكن مشاركته:",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        explain_label.pack(pady=(0, 10))
        
        # عرض المفتاح العام
        self.public_key_label = tk.Label(
            public_frame,
            text="سيظهر المفتاح العام هنا...",
            font=('Courier', 10),
            bg='white',
            fg=self.colors['text'],
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=5
        )
        self.public_key_label.pack(pady=10)
        
        # ملاحظة
        note_label = tk.Label(
            public_frame,
            text="💡 ملاحظة: هذا المفتاح آمن للمشاركة مع الآخرين",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        note_label.pack(pady=10)
    
    def show_address_generation(self, parent_frame):
        """عرض إنشاء العنوان"""
        # إطار العنوان
        address_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        address_frame.pack(pady=20)
        
        # نص توضيحي
        explain_label = tk.Label(
            address_frame,
            text="من المفتاح العام، نقوم بإنشاء عنوان قصير وسهل التذكر:",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        explain_label.pack(pady=(0, 10))
        
        # عرض العنوان
        self.address_label = tk.Label(
            address_frame,
            text="سيظهر العنوان هنا...",
            font=('Courier', 12, 'bold'),
            bg='white',
            fg=self.colors['primary'],
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=5
        )
        self.address_label.pack(pady=10)
        
        # ملاحظة
        note_label = tk.Label(
            address_frame,
            text="📍 هذا هو عنوان محفظتك! يمكنك مشاركته مع الآخرين لاستقبال البيتكوين",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        note_label.pack(pady=10)
    
    def show_wallet_result(self):
        """عرض نتيجة إنشاء المحفظة"""
        # إطار النتيجة
        result_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        result_frame.pack(expand=True)
        
        # رسالة النجاح
        success_label = tk.Label(
            result_frame,
            text="🎉 تم إنشاء المحفظة بنجاح!",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        success_label.pack(pady=(0, 20))
        
        # معلومات المحفظة
        if self.wallet_data:
            wallet_info = f"""
📝 الكلمات السرية:
{self.wallet_data['seed_phrase']}

🔐 المفتاح الخاص:
{self.wallet_data['private_key']}

🔑 المفتاح العام:
{self.wallet_data['public_key']}

📍 العنوان:
{self.wallet_data['address']}

💰 الرصيد: {self.wallet_data['balance']}
            """
            
            info_label = tk.Label(
                result_frame,
                text=wallet_info,
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                relief=tk.SUNKEN,
                bd=2,
                padx=15,
                pady=10,
                justify=tk.LEFT
            )
            info_label.pack(pady=20)
        
        # نص مهم
        important_label = tk.Label(
            result_frame,
            text="🔒 مهم: احفظ الكلمات السرية والمفتاح الخاص في مكان آمن!",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['warning']
        )
        important_label.pack(pady=20)
    
    def create_navigation_buttons(self):
        """إنشاء أزرار التنقل"""
        # إطار الأزرار
        nav_frame = tk.Frame(self.buttons_frame, bg=self.colors['background'])
        nav_frame.pack()
        
        # زر السابق
        self.prev_button = tk.Button(
            nav_frame,
            text="⬅️ السابق",
            command=self.previous_step,
            font=self.button_font,
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2',
            state=tk.DISABLED
        )
        self.prev_button.pack(side=tk.LEFT, padx=10)
        
        # زر التالي
        self.next_button = tk.Button(
            nav_frame,
            text="التالي ➡️",
            command=self.next_step,
            font=self.button_font,
            bg=self.colors['primary'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        # زر الرسوم المتحركة
        self.animation_button = tk.Button(
            nav_frame,
            text="🎬 رسوم متحركة",
            command=self.show_animation,
            font=self.button_font,
            bg=self.colors['accent'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        self.animation_button.pack(side=tk.LEFT, padx=10)
        
        # زر الإغلاق
        close_button = tk.Button(
            nav_frame,
            text="❌ إغلاق",
            command=self.close_window,
            font=self.button_font,
            bg=self.colors['primary'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        close_button.pack(side=tk.RIGHT, padx=10)
    
    def generate_seed(self):
        """توليد الكلمات السرية"""
        if not self.wallet_data:
            self.wallet_data = self.wallet_generator.create_wallet()
        
        # عرض الكلمات السرية
        seed_text = f"الكلمات السرية:\n{self.wallet_data['seed_phrase']}"
        self.seed_label.config(text=seed_text)
        
        # تحديث المفاتيح والعنوان
        self.update_wallet_display()
    
    def update_wallet_display(self):
        """تحديث عرض معلومات المحفظة"""
        if self.wallet_data:
            if hasattr(self, 'private_key_label'):
                self.private_key_label.config(text=self.wallet_data['private_key'])
            
            if hasattr(self, 'public_key_label'):
                self.public_key_label.config(text=self.wallet_data['public_key'])
            
            if hasattr(self, 'address_label'):
                self.address_label.config(text=self.wallet_data['address'])
    
    def next_step(self):
        """الانتقال للخطوة التالية"""
        if self.current_step == 0:
            # إنشاء المحفظة في الخطوة الأولى
            if not self.wallet_data:
                self.wallet_data = self.wallet_generator.create_wallet()
                self.update_wallet_display()
        
        self.current_step += 1
        self.show_current_step()
        self.update_navigation_buttons()
    
    def previous_step(self):
        """الانتقال للخطوة السابقة"""
        if self.current_step > 0:
            self.current_step -= 1
            self.show_current_step()
            self.update_navigation_buttons()
    
    def update_navigation_buttons(self):
        """تحديث حالة أزرار التنقل"""
        # زر السابق
        if self.current_step <= 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
        
        # زر التالي
        if self.current_step >= len(self.steps) + 1:
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)
        
        # تغيير نص زر التالي
        if self.current_step == len(self.steps):
            self.next_button.config(text="إنهاء ✅")
        else:
            self.next_button.config(text="التالي ➡️")
    
    def show_animation(self):
        """عرض الرسوم المتحركة"""
        try:
            animations = CryptoAnimations()
            animations.animate_wallet_creation()
        except Exception as e:
            messagebox.showinfo("🎬 رسوم متحركة", "سيتم عرض الرسوم المتحركة في نافذة منفصلة!")
    
    def close_window(self):
        """إغلاق النافذة"""
        if self.wallet_data and self.current_step >= len(self.steps):
            # تسجيل إكمال إنشاء المحفظة
            self.progress_manager.complete_wallet_creation(self.wallet_data)
            messagebox.showinfo("🎉 تهانينا!", "تم تسجيل إكمال إنشاء المحفظة في تقدمك!")
        
        self.window.destroy() 