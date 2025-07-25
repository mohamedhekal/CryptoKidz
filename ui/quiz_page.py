#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
صفحة الاختبارات التفاعلية
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# إضافة المجلد الأب للمسار
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quiz_engine import QuizEngine

class QuizPage:
    """صفحة الاختبارات التفاعلية"""
    
    def __init__(self, window, progress_manager):
        self.window = window
        self.progress_manager = progress_manager
        self.quiz_engine = QuizEngine()
        
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
        self.current_question = 0
        self.questions = []
        self.answers = []
        self.quiz_started = False
        self.selected_answer = None
    
    def setup_window(self):
        """إعداد النافذة"""
        self.window.title("🎯 اختبارات تفاعلية")
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
            text="🎯 اختبارات تفاعلية",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.title_label.pack(pady=(0, 20))
        
        # رسالة الترحيب
        self.welcome_label = tk.Label(
            self.main_frame,
            text="🐱 مرحباً! حان وقت اختبار معرفتك!",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.welcome_label.pack(pady=(0, 30))
        
        # إطار المحتوى
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # عرض المحتوى الحالي
        self.show_quiz_selection()
        
        # إطار الأزرار
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.buttons_frame.pack(pady=20)
        
        # أزرار التنقل
        self.create_navigation_buttons()
    
    def show_quiz_selection(self):
        """عرض اختيار نوع الاختبار"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # إطار الاختيار
        selection_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        selection_frame.pack(expand=True)
        
        # عنوان القسم
        title_label = tk.Label(
            selection_frame,
            text="اختر نوع الاختبار:",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        title_label.pack(pady=(0, 30))
        
        # أزرار الاختبارات
        quiz_types = [
            {
                'title': '💼 إنشاء المحافظ',
                'description': 'اختبر معرفتك في إنشاء محافظ البيتكوين',
                'category': 'wallet_creation',
                'color': self.colors['primary']
            },
            {
                'title': '🔐 التشفير',
                'description': 'اختبر فهمك لمفاهيم التشفير',
                'category': 'cryptography',
                'color': self.colors['secondary']
            },
            {
                'title': '⛓️ البلوكتشين',
                'description': 'اختبر معرفتك بالبلوكتشين',
                'category': 'blockchain',
                'color': self.colors['accent']
            },
            {
                'title': '₿ البيتكوين',
                'description': 'اختبر فهمك للبيتكوين',
                'category': 'bitcoin',
                'color': self.colors['success']
            },
            {
                'title': '🎲 اختبار عشوائي',
                'description': 'اختبار شامل من جميع الفئات',
                'category': 'random',
                'color': self.colors['warning']
            }
        ]
        
        for i, quiz_type in enumerate(quiz_types):
            quiz_frame = tk.Frame(selection_frame, bg='white', relief=tk.RAISED, bd=2)
            quiz_frame.pack(fill=tk.X, pady=10, padx=20)
            
            # عنوان الاختبار
            quiz_title = tk.Label(
                quiz_frame,
                text=quiz_type['title'],
                font=self.header_font,
                bg='white',
                fg=quiz_type['color']
            )
            quiz_title.pack(pady=(15, 5))
            
            # وصف الاختبار
            quiz_desc = tk.Label(
                quiz_frame,
                text=quiz_type['description'],
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                wraplength=400
            )
            quiz_desc.pack(pady=(0, 15))
            
            # زر البدء
            start_button = tk.Button(
                quiz_frame,
                text="🚀 ابدأ الاختبار",
                command=lambda cat=quiz_type['category']: self.start_quiz(cat),
                font=self.button_font,
                bg=quiz_type['color'],
                fg='white',
                relief=tk.RAISED,
                bd=2,
                padx=20,
                pady=5,
                cursor='hand2'
            )
            start_button.pack(pady=(0, 15))
    
    def start_quiz(self, category):
        """بدء الاختبار"""
        if category == 'random':
            self.questions = self.quiz_engine.get_random_quiz(5)
        else:
            self.questions = self.quiz_engine.get_quiz_by_category(category, 3)
        
        if not self.questions:
            messagebox.showwarning("تحذير", "لا توجد أسئلة متاحة لهذا النوع!")
            return
        
        self.quiz_started = True
        self.current_question = 0
        self.answers = []
        self.selected_answer = None
        
        self.show_current_question()
        self.update_navigation_buttons()
    
    def show_current_question(self):
        """عرض السؤال الحالي"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if not self.quiz_started or self.current_question >= len(self.questions):
            self.show_quiz_result()
            return
        
        question = self.questions[self.current_question]
        
        # إطار السؤال
        question_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        question_frame.pack(expand=True)
        
        # رقم السؤال
        question_number = tk.Label(
            question_frame,
            text=f"السؤال {self.current_question + 1} من {len(self.questions)}",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        question_number.pack(pady=(0, 20))
        
        # نص السؤال
        question_text = tk.Label(
            question_frame,
            text=question['question'],
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text'],
            wraplength=600,
            justify=tk.CENTER
        )
        question_text.pack(pady=(0, 30))
        
        # إطار الخيارات
        options_frame = tk.Frame(question_frame, bg=self.colors['background'])
        options_frame.pack()
        
        # متغير للخيار المحدد
        self.selected_answer = tk.IntVar()
        
        # الخيارات
        for i, option in enumerate(question['options']):
            option_frame = tk.Frame(options_frame, bg='white', relief=tk.RAISED, bd=2)
            option_frame.pack(fill=tk.X, pady=5, padx=20)
            
            option_radio = tk.Radiobutton(
                option_frame,
                text=option,
                variable=self.selected_answer,
                value=i,
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                selectcolor=self.colors['accent'],
                cursor='hand2'
            )
            option_radio.pack(anchor=tk.W, padx=15, pady=10)
        
        # زر التلميح
        hint_button = tk.Button(
            question_frame,
            text="💡 تلميح",
            command=lambda: self.show_hint(question),
            font=self.normal_font,
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            bd=2,
            padx=15,
            pady=5,
            cursor='hand2'
        )
        hint_button.pack(pady=20)
    
    def show_hint(self, question):
        """عرض تلميح للسؤال"""
        hint = self.quiz_engine.get_hint(question)
        messagebox.showinfo("💡 تلميح", hint)
    
    def show_quiz_result(self):
        """عرض نتيجة الاختبار"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # إطار النتيجة
        result_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        result_frame.pack(expand=True)
        
        # حساب النتيجة
        score = self.quiz_engine.calculate_score(self.answers)
        
        # رسالة النجاح
        if score['percentage'] >= 80:
            result_text = "🎉 مبروك! نتيجة ممتازة!"
            result_color = self.colors['success']
        elif score['percentage'] >= 60:
            result_text = "👍 جيد! استمر في التعلم!"
            result_color = self.colors['accent']
        else:
            result_text = "💪 لا تستسلم! الممارسة تجعل الكمال!"
            result_color = self.colors['warning']
        
        result_label = tk.Label(
            result_frame,
            text=result_text,
            font=self.title_font,
            bg=self.colors['background'],
            fg=result_color
        )
        result_label.pack(pady=(0, 20))
        
        # تفاصيل النتيجة
        details_frame = tk.Frame(result_frame, bg='white', relief=tk.RAISED, bd=2)
        details_frame.pack(pady=20, padx=20, fill=tk.X)
        
        details_text = f"""
📊 تفاصيل النتيجة:

✅ الإجابات الصحيحة: {score['correct_answers']} من {score['total_questions']}
📈 النسبة المئوية: {score['percentage']:.1f}%
🏆 المستوى: {score['level']}
⭐ المكافأة: {score['reward']}
        """
        
        details_label = tk.Label(
            details_frame,
            text=details_text,
            font=self.normal_font,
            bg='white',
            fg=self.colors['text'],
            justify=tk.LEFT
        )
        details_label.pack(pady=20, padx=20)
        
        # رسالة تشجيعية
        encouragement = self.quiz_engine.get_encouragement_message(score)
        encouragement_label = tk.Label(
            result_frame,
            text=encouragement,
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        encouragement_label.pack(pady=20)
        
        # تسجيل النتيجة
        quiz_data = {
            'category': 'general',
            'score': score['percentage'],
            'points': score['total_points']
        }
        self.progress_manager.add_quiz_result(quiz_data)
    
    def create_navigation_buttons(self):
        """إنشاء أزرار التنقل"""
        # إطار الأزرار
        nav_frame = tk.Frame(self.buttons_frame, bg=self.colors['background'])
        nav_frame.pack()
        
        # زر السابق
        self.prev_button = tk.Button(
            nav_frame,
            text="⬅️ السابق",
            command=self.previous_question,
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
            command=self.next_question,
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
        
        # زر إعادة الاختبار
        self.restart_button = tk.Button(
            nav_frame,
            text="🔄 اختبار جديد",
            command=self.restart_quiz,
            font=self.button_font,
            bg=self.colors['accent'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
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
    
    def next_question(self):
        """الانتقال للسؤال التالي"""
        if self.quiz_started:
            if self.current_question < len(self.questions):
                # حفظ الإجابة الحالية
                if self.selected_answer is not None:
                    question = self.questions[self.current_question]
                    answer = self.quiz_engine.check_answer(question, self.selected_answer.get())
                    self.answers.append(answer)
                
                self.current_question += 1
                self.selected_answer = None
                self.show_current_question()
                self.update_navigation_buttons()
        else:
            self.show_quiz_selection()
    
    def previous_question(self):
        """الانتقال للسؤال السابق"""
        if self.quiz_started and self.current_question > 0:
            self.current_question -= 1
            self.selected_answer = None
            self.show_current_question()
            self.update_navigation_buttons()
    
    def restart_quiz(self):
        """إعادة بدء الاختبار"""
        self.quiz_started = False
        self.current_question = 0
        self.questions = []
        self.answers = []
        self.selected_answer = None
        
        self.show_quiz_selection()
        self.update_navigation_buttons()
    
    def update_navigation_buttons(self):
        """تحديث حالة أزرار التنقل"""
        if self.quiz_started:
            # زر السابق
            if self.current_question <= 0:
                self.prev_button.config(state=tk.DISABLED)
            else:
                self.prev_button.config(state=tk.NORMAL)
            
            # زر التالي
            if self.current_question >= len(self.questions):
                self.next_button.config(text="إنهاء ✅")
            else:
                self.next_button.config(text="التالي ➡️")
        else:
            self.prev_button.config(state=tk.DISABLED)
            self.next_button.config(text="التالي ➡️")
    
    def close_window(self):
        """إغلاق النافذة"""
        self.window.destroy() 