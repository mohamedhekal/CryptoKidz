#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
صفحة تعلم التشفير
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# إضافة المجلد الأب للمسار
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_explainer import CryptoExplainer
from animations import CryptoAnimations

class CryptoPage:
    """صفحة تعلم التشفير"""
    
    def __init__(self, window, progress_manager):
        self.window = window
        self.progress_manager = progress_manager
        self.crypto_explainer = CryptoExplainer()
        
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
        self.current_lesson = 0
        self.lessons = [
            'what_is_crypto',
            'private_vs_public',
            'hash_functions',
            'blockchain',
            'bitcoin'
        ]
    
    def setup_window(self):
        """إعداد النافذة"""
        self.window.title("🔐 تعلم التشفير")
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
        
        # إضافة رمز قفل توضيحي في الأعلى
        self.lock_canvas = tk.Canvas(self.main_frame, width=80, height=80, bg=self.colors['background'], highlightthickness=0)
        self.lock_canvas.pack(pady=(0, 10))
        self.lock_canvas.create_rectangle(20, 40, 60, 70, fill='#FF6B6B', outline='')  # جسم القفل
        self.lock_canvas.create_arc(20, 10, 60, 50, start=0, extent=180, style=tk.ARC, outline='#4ECDC4', width=5)  # قوس القفل
        
        # العنوان
        self.title_label = tk.Label(
            self.main_frame,
            text="🔐 تعلم التشفير",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.title_label.pack(pady=(0, 20))
        
        # رسالة الترحيب
        self.welcome_label = tk.Label(
            self.main_frame,
            text="🐱 مرحباً! سأعلمك أسرار التشفير والرموز السرية",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.welcome_label.pack(pady=(0, 30))
        
        # إطار المحتوى
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # عرض الدرس الحالي
        self.show_current_lesson()
        
        # إطار الأزرار
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.buttons_frame.pack(pady=20)
        
        # أزرار التنقل
        self.create_navigation_buttons()
    
    def show_current_lesson(self):
        """عرض الدرس الحالي"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if self.current_lesson == 0:
            self.show_introduction()
        elif self.current_lesson <= len(self.lessons):
            self.show_lesson(self.current_lesson - 1)
        else:
            self.show_completion()
    
    def show_introduction(self):
        """عرض المقدمة"""
        # إطار المقدمة
        intro_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        intro_frame.pack(expand=True)
        
        # نص المقدمة
        intro_text = """
🔐 ما هو التشفير؟

التشفير هو فن إخفاء الرسائل والبيانات!
مثل لعبة الشفرات السرية التي يلعبها الجواسيس!

🎯 سنتعلم اليوم:
1. ما هو التشفير؟ 🔐
2. المفتاح الخاص vs المفتاح العام 🔑
3. دوال التشفير (Hash Functions) 🔢
4. البلوكتشين ⛓️
5. البيتكوين ₿

🚀 هل أنت مستعد لتعلم أسرار التشفير؟
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
            text="🚀 ابدأ التعلم!",
            command=self.next_lesson,
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
    
    def show_lesson(self, lesson_index):
        """عرض درس معين"""
        lesson_name = self.lessons[lesson_index]
        
        if lesson_name == 'what_is_crypto':
            self.show_what_is_crypto()
        elif lesson_name == 'private_vs_public':
            self.show_private_vs_public()
        elif lesson_name == 'hash_functions':
            self.show_hash_functions()
        elif lesson_name == 'blockchain':
            self.show_blockchain()
        elif lesson_name == 'bitcoin':
            self.show_bitcoin()
    
    def show_what_is_crypto(self):
        """عرض درس ما هو التشفير"""
        # إطار الدرس
        lesson_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        lesson_frame.pack(expand=True)
        
        # عنوان الدرس
        title_label = tk.Label(
            lesson_frame,
            text="🔐 ما هو التشفير؟",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # وصف الدرس
        explanation = self.crypto_explainer.explain_what_is_crypto()
        
        desc_label = tk.Label(
            lesson_frame,
            text=explanation['description'],
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=500
        )
        desc_label.pack(pady=(0, 20))
        
        # الأمثلة
        examples_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        examples_frame.pack(pady=20)
        
        for example in explanation['examples']:
            example_frame = tk.Frame(examples_frame, bg='white', relief=tk.RAISED, bd=2)
            example_frame.pack(fill=tk.X, pady=5, padx=10)
            
            title = tk.Label(
                example_frame,
                text=example['title'],
                font=self.header_font,
                bg='white',
                fg=self.colors['primary']
            )
            title.pack(pady=(10, 5))
            
            desc = tk.Label(
                example_frame,
                text=example['description'],
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                wraplength=400
            )
            desc.pack(pady=(0, 5))
            
            example_text = tk.Label(
                example_frame,
                text=example['example'],
                font=('Courier', 10),
                bg='white',
                fg=self.colors['accent']
            )
            example_text.pack(pady=(0, 10))
        
        # حقيقة ممتعة
        fun_fact_label = tk.Label(
            lesson_frame,
            text=f"💡 {explanation['fun_fact']}",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        fun_fact_label.pack(pady=20)
    
    def show_private_vs_public(self):
        """عرض درس المفتاح الخاص والعام"""
        # إطار الدرس
        lesson_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        lesson_frame.pack(expand=True)
        
        # عنوان الدرس
        title_label = tk.Label(
            lesson_frame,
            text="🔑 المفتاح الخاص vs المفتاح العام",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # وصف الدرس
        explanation = self.crypto_explainer.explain_private_vs_public_key()
        
        # إطار المقارنة
        comparison_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        comparison_frame.pack(pady=20)
        
        # المفتاح الخاص
        private_frame = tk.Frame(comparison_frame, bg='white', relief=tk.RAISED, bd=2)
        private_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        private_title = tk.Label(
            private_frame,
            text=explanation['private_key']['title'],
            font=self.header_font,
            bg='white',
            fg=self.colors['secondary']
        )
        private_title.pack(pady=(10, 10))
        
        private_desc = tk.Label(
            private_frame,
            text=explanation['private_key']['description'],
            font=self.normal_font,
            bg='white',
            fg=self.colors['text'],
            wraplength=200
        )
        private_desc.pack(pady=(0, 10))
        
        for char in explanation['private_key']['characteristics']:
            char_label = tk.Label(
                private_frame,
                text=f"• {char}",
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                anchor=tk.W
            )
            char_label.pack(anchor=tk.W, padx=10)
        
        # المفتاح العام
        public_frame = tk.Frame(comparison_frame, bg='white', relief=tk.RAISED, bd=2)
        public_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        public_title = tk.Label(
            public_frame,
            text=explanation['public_key']['title'],
            font=self.header_font,
            bg='white',
            fg=self.colors['accent']
        )
        public_title.pack(pady=(10, 10))
        
        public_desc = tk.Label(
            public_frame,
            text=explanation['public_key']['description'],
            font=self.normal_font,
            bg='white',
            fg=self.colors['text'],
            wraplength=200
        )
        public_desc.pack(pady=(0, 10))
        
        for char in explanation['public_key']['characteristics']:
            char_label = tk.Label(
                public_frame,
                text=f"• {char}",
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                anchor=tk.W
            )
            char_label.pack(anchor=tk.W, padx=10)
        
        # التشبيه
        analogy_label = tk.Label(
            lesson_frame,
            text=f"🏠 {explanation['analogy']['description']}",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        analogy_label.pack(pady=20)
    
    def show_hash_functions(self):
        """عرض درس دوال التشفير"""
        # إطار الدرس
        lesson_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        lesson_frame.pack(expand=True)
        
        # عنوان الدرس
        title_label = tk.Label(
            lesson_frame,
            text="🔢 دوال التشفير (Hash Functions)",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # وصف الدرس
        explanation = self.crypto_explainer.explain_hash_functions()
        
        desc_label = tk.Label(
            lesson_frame,
            text=explanation['description'],
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=500
        )
        desc_label.pack(pady=(0, 20))
        
        # الأمثلة التفاعلية
        demo_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        demo_frame.pack(pady=20)
        
        # إطار الإدخال
        input_frame = tk.Frame(demo_frame, bg='white', relief=tk.RAISED, bd=2)
        input_frame.pack(pady=10)
        
        input_label = tk.Label(
            input_frame,
            text="جرب بنفسك:",
            font=self.header_font,
            bg='white',
            fg=self.colors['primary']
        )
        input_label.pack(pady=(10, 5))
        
        self.hash_input = tk.Entry(
            input_frame,
            font=self.normal_font,
            width=30
        )
        self.hash_input.pack(pady=(0, 10))
        self.hash_input.insert(0, "مرحبا")
        
        # زر التشفير
        hash_button = tk.Button(
            input_frame,
            text="🔢 تشفير",
            command=self.demo_hash_function,
            font=self.button_font,
            bg=self.colors['secondary'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        hash_button.pack(pady=(0, 10))
        
        # نتيجة التشفير
        self.hash_result_label = tk.Label(
            input_frame,
            text="النتيجة ستظهر هنا...",
            font=('Courier', 12, 'bold'),
            bg='white',
            fg=self.colors['accent']
        )
        self.hash_result_label.pack(pady=(0, 10))
        
        # الخصائص
        characteristics_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        characteristics_frame.pack(pady=20)
        
        for char in explanation['characteristics']:
            char_label = tk.Label(
                characteristics_frame,
                text=f"• {char}",
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text'],
                anchor=tk.W
            )
            char_label.pack(anchor=tk.W, padx=20)
    
    def show_blockchain(self):
        """عرض درس البلوكتشين"""
        # إطار الدرس
        lesson_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        lesson_frame.pack(expand=True)
        
        # عنوان الدرس
        title_label = tk.Label(
            lesson_frame,
            text="⛓️ ما هو البلوكتشين؟",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # وصف الدرس
        explanation = self.crypto_explainer.explain_blockchain_simple()
        
        desc_label = tk.Label(
            lesson_frame,
            text=explanation['description'],
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=500
        )
        desc_label.pack(pady=(0, 20))
        
        # الكتل
        blocks_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        blocks_frame.pack(pady=20)
        
        for block in explanation['blocks']:
            block_frame = tk.Frame(blocks_frame, bg='white', relief=tk.RAISED, bd=2)
            block_frame.pack(fill=tk.X, pady=5, padx=10)
            
            block_title = tk.Label(
                block_frame,
                text=block['title'],
                font=self.header_font,
                bg='white',
                fg=self.colors['accent']
            )
            block_title.pack(pady=(10, 5))
            
            block_desc = tk.Label(
                block_frame,
                text=block['description'],
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                wraplength=400
            )
            block_desc.pack(pady=(0, 5))
            
            for content in block['content']:
                content_label = tk.Label(
                    block_frame,
                    text=f"• {content}",
                    font=self.normal_font,
                    bg='white',
                    fg=self.colors['text'],
                    anchor=tk.W
                )
                content_label.pack(anchor=tk.W, padx=10)
        
        # الخصائص
        characteristics_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        characteristics_frame.pack(pady=20)
        
        for char in explanation['characteristics']:
            char_label = tk.Label(
                characteristics_frame,
                text=f"• {char}",
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text'],
                anchor=tk.W
            )
            char_label.pack(anchor=tk.W, padx=20)
    
    def show_bitcoin(self):
        """عرض درس البيتكوين"""
        # إطار الدرس
        lesson_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        lesson_frame.pack(expand=True)
        
        # عنوان الدرس
        title_label = tk.Label(
            lesson_frame,
            text="₿ ما هو البيتكوين؟",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        title_label.pack(pady=(0, 20))
        
        # وصف الدرس
        explanation = self.crypto_explainer.explain_bitcoin_simple()
        
        desc_label = tk.Label(
            lesson_frame,
            text=explanation['description'],
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=500
        )
        desc_label.pack(pady=(0, 20))
        
        # المميزات
        features_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        features_frame.pack(pady=20)
        
        for feature in explanation['features']:
            feature_frame = tk.Frame(features_frame, bg='white', relief=tk.RAISED, bd=2)
            feature_frame.pack(fill=tk.X, pady=5, padx=10)
            
            feature_title = tk.Label(
                feature_frame,
                text=feature['title'],
                font=self.header_font,
                bg='white',
                fg=self.colors['accent']
            )
            feature_title.pack(pady=(10, 5))
            
            feature_desc = tk.Label(
                feature_frame,
                text=feature['description'],
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                wraplength=400
            )
            feature_desc.pack(pady=(0, 10))
        
        # كيف يعمل
        how_it_works_frame = tk.Frame(lesson_frame, bg=self.colors['background'])
        how_it_works_frame.pack(pady=20)
        
        how_title = tk.Label(
            how_it_works_frame,
            text="كيف يعمل البيتكوين:",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        how_title.pack(pady=(0, 10))
        
        for step in explanation['how_it_works']:
            step_label = tk.Label(
                how_it_works_frame,
                text=step,
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text'],
                anchor=tk.W
            )
            step_label.pack(anchor=tk.W, padx=20)
        
        # حقيقة ممتعة
        fun_fact_label = tk.Label(
            lesson_frame,
            text=f"💡 {explanation['fun_fact']}",
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        fun_fact_label.pack(pady=20)
    
    def show_completion(self):
        """عرض صفحة الإكمال"""
        # إطار الإكمال
        completion_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        completion_frame.pack(expand=True)
        
        # رسالة النجاح
        success_label = tk.Label(
            completion_frame,
            text="🎉 مبروك! لقد أكملت تعلم التشفير!",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['success']
        )
        success_label.pack(pady=(0, 20))
        
        # ملخص ما تعلمته
        summary_text = """
🔐 ما تعلمته اليوم:

✅ ما هو التشفير وكيف يعمل
✅ الفرق بين المفتاح الخاص والعام
✅ كيف تعمل دوال التشفير
✅ ما هو البلوكتشين
✅ ما هو البيتكوين

🎯 الآن يمكنك:
• فهم أساسيات التشفير
• معرفة أهمية الأمان الرقمي
• فهم كيف تعمل العملات الرقمية
• حماية معلوماتك الشخصية

🚀 استعد للاختبار التالي!
        """
        
        summary_label = tk.Label(
            completion_frame,
            text=summary_text,
            font=self.normal_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            justify=tk.LEFT,
            wraplength=500
        )
        summary_label.pack(pady=20)
    
    def create_navigation_buttons(self):
        """إنشاء أزرار التنقل"""
        # إطار الأزرار
        nav_frame = tk.Frame(self.buttons_frame, bg=self.colors['background'])
        nav_frame.pack()
        
        # زر السابق
        self.prev_button = tk.Button(
            nav_frame,
            text="⬅️ السابق",
            command=self.previous_lesson,
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
            command=self.next_lesson,
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
    
    def demo_hash_function(self):
        """عرض دالة التشفير"""
        text = self.hash_input.get()
        if text:
            hash_result = self.crypto_explainer.demonstrate_hash_function(text)
            self.hash_result_label.config(text=hash_result)
    
    def next_lesson(self):
        """الانتقال للدرس التالي"""
        if self.current_lesson > 0 and self.current_lesson <= len(self.lessons):
            # تسجيل إكمال الدرس
            lesson_name = self.lessons[self.current_lesson - 1]
            self.progress_manager.complete_crypto_lesson(lesson_name)
        
        self.current_lesson += 1
        self.show_current_lesson()
        self.update_navigation_buttons()
    
    def previous_lesson(self):
        """الانتقال للدرس السابق"""
        if self.current_lesson > 0:
            self.current_lesson -= 1
            self.show_current_lesson()
            self.update_navigation_buttons()
    
    def update_navigation_buttons(self):
        """تحديث حالة أزرار التنقل"""
        # زر السابق
        if self.current_lesson <= 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
        
        # زر التالي
        if self.current_lesson >= len(self.lessons) + 1:
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)
        
        # تغيير نص زر التالي
        if self.current_lesson == len(self.lessons):
            self.next_button.config(text="إنهاء ✅")
        else:
            self.next_button.config(text="التالي ➡️")
    
    def show_animation(self):
        """عرض الرسوم المتحركة"""
        try:
            animations = CryptoAnimations()
            if self.current_lesson == 3:  # درس دوال التشفير
                animations.animate_hash_function()
            elif self.current_lesson == 4:  # درس البلوكتشين
                animations.animate_blockchain()
            else:
                animations.animate_hash_function()
        except Exception as e:
            messagebox.showinfo("🎬 رسوم متحركة", "سيتم عرض الرسوم المتحركة في نافذة منفصلة!")
    
    def close_window(self):
        """إغلاق النافذة"""
        if self.current_lesson > len(self.lessons):
            messagebox.showinfo("🎉 تهانينا!", "تم تسجيل إكمال تعلم التشفير في تقدمك!")
        
        self.window.destroy() 