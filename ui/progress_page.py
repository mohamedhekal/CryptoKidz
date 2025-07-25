#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
صفحة عرض التقدم والمكافآت
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# إضافة المجلد الأب للمسار
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProgressPage:
    """صفحة عرض التقدم والمكافآت"""
    
    def __init__(self, window, progress_manager):
        self.window = window
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
        
        # تحميل البيانات
        self.load_progress_data()
    
    def setup_window(self):
        """إعداد النافذة"""
        self.window.title("📊 تقدمي ومكافآتي")
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
        
        # إضافة رمز كأس في الأعلى
        self.cup_canvas = tk.Canvas(self.main_frame, width=80, height=80, bg=self.colors['background'], highlightthickness=0)
        self.cup_canvas.pack(pady=(0, 10))
        self.cup_canvas.create_rectangle(30, 40, 50, 70, fill='#FFD700', outline='')  # جسم الكأس
        self.cup_canvas.create_oval(20, 20, 60, 50, fill='#FFD700', outline='')  # فوهة الكأس
        self.cup_canvas.create_rectangle(35, 70, 45, 80, fill='#B8860B', outline='')  # قاعدة الكأس
        
        # العنوان
        self.title_label = tk.Label(
            self.main_frame,
            text="📊 تقدمي ومكافآتي",
            font=self.title_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.title_label.pack(pady=(0, 20))
        
        # رسالة الترحيب
        self.welcome_label = tk.Label(
            self.main_frame,
            text="🐱 مرحباً! شاهد تقدمك ومكافآتك!",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['text']
        )
        self.welcome_label.pack(pady=(0, 30))
        
        # إطار المحتوى
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # عرض التقدم
        self.show_progress()
        
        # إطار الأزرار
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.buttons_frame.pack(pady=20)
        
        # أزرار إضافية
        self.create_buttons()
    
    def load_progress_data(self):
        """تحميل بيانات التقدم"""
        self.progress = self.progress_manager.get_progress()
        self.stats = self.progress_manager.get_statistics()
    
    def show_progress(self):
        """عرض التقدم"""
        # مسح المحتوى السابق
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # إطار التقدم
        progress_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        progress_frame.pack(expand=True)
        
        # الإحصائيات العامة
        self.show_general_stats(progress_frame)
        
        # الشارات والإنجازات
        self.show_badges_and_achievements(progress_frame)
        
        # التوصيات
        self.show_recommendations(progress_frame)
    
    def show_general_stats(self, parent_frame):
        """عرض الإحصائيات العامة"""
        # عنوان القسم
        stats_title = tk.Label(
            parent_frame,
            text="📈 إحصائياتي العامة",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        stats_title.pack(pady=(0, 20))
        
        # إطار الإحصائيات
        stats_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        stats_frame.pack(pady=10)
        
        # الإحصائيات
        stats_data = [
            ('total_quizzes', 'الاختبارات المكتملة', f"{self.stats['total_quizzes']}"),
            ('total_points', 'النقاط المكتسبة', f"{self.stats['total_points']}"),
            ('average_score', 'متوسط النتيجة', f"{self.stats['average_score']:.1f}%"),
            ('badges_earned', 'الشارات المكتسبة', f"{self.stats['badges_earned']}"),
            ('wallets_created', 'المحافظ المنشأة', f"{self.stats['wallets_created']}"),
            ('lessons_completed', 'الدروس المكتملة', f"{self.stats['lessons_completed']}"),
            ('days_active', 'أيام النشاط', f"{self.stats['days_active']}")
        ]
        
        for i, (key, label, value) in enumerate(stats_data):
            stat_frame = tk.Frame(stats_frame, bg='white', relief=tk.RAISED, bd=2)
            stat_frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky='ew')
            
            # العنوان
            title_label = tk.Label(
                stat_frame,
                text=label,
                font=self.normal_font,
                bg='white',
                fg=self.colors['text']
            )
            title_label.pack(pady=(10, 5))
            
            # القيمة
            value_label = tk.Label(
                stat_frame,
                text=value,
                font=self.header_font,
                bg='white',
                fg=self.colors['primary']
            )
            value_label.pack(pady=(0, 10))
        
        # تكوين الأعمدة
        for i in range(3):
            stats_frame.columnconfigure(i, weight=1)
    
    def show_badges_and_achievements(self, parent_frame):
        """عرض الشارات والإنجازات"""
        # عنوان القسم
        badges_title = tk.Label(
            parent_frame,
            text="🏆 شاراتي وإنجازاتي",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        badges_title.pack(pady=(30, 20))
        
        # إطار الشارات
        badges_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        badges_frame.pack(pady=10)
        
        # الشارات
        badges = self.progress.get('badges', [])
        if badges:
            for i, badge in enumerate(badges):
                badge_frame = tk.Frame(badges_frame, bg='white', relief=tk.RAISED, bd=2)
                badge_frame.pack(fill=tk.X, pady=5, padx=20)
                
                badge_text = f"{badge['name']} - {badge['earned_at'][:10]}"
                badge_label = tk.Label(
                    badge_frame,
                    text=badge_text,
                    font=self.normal_font,
                    bg='white',
                    fg=self.colors['success']
                )
                badge_label.pack(pady=10)
        else:
            no_badges_label = tk.Label(
                badges_frame,
                text="لا توجد شارات بعد. استمر في التعلم!",
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text']
            )
            no_badges_label.pack(pady=20)
        
        # الإنجازات
        achievements_title = tk.Label(
            parent_frame,
            text="🎯 إنجازاتي",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        achievements_title.pack(pady=(30, 20))
        
        achievements_frame = tk.Frame(parent_frame, bg=self.colors['background'])
        achievements_frame.pack(pady=10)
        
        achievements = self.progress.get('achievements', [])
        if achievements:
            for achievement in achievements:
                achievement_frame = tk.Frame(achievements_frame, bg='white', relief=tk.RAISED, bd=2)
                achievement_frame.pack(fill=tk.X, pady=5, padx=20)
                
                achievement_text = f"{achievement['name']} - {achievement['earned_at'][:10]}"
                achievement_label = tk.Label(
                    achievement_frame,
                    text=achievement_text,
                    font=self.normal_font,
                    bg='white',
                    fg=self.colors['accent']
                )
                achievement_label.pack(pady=10)
        else:
            no_achievements_label = tk.Label(
                achievements_frame,
                text="لا توجد إنجازات بعد. واصل التقدم!",
                font=self.normal_font,
                bg=self.colors['background'],
                fg=self.colors['text']
            )
            no_achievements_label.pack(pady=20)
    
    def show_recommendations(self, parent_frame):
        """عرض التوصيات"""
        # عنوان القسم
        recommendations_title = tk.Label(
            parent_frame,
            text="💡 توصياتي لك",
            font=self.header_font,
            bg=self.colors['background'],
            fg=self.colors['primary']
        )
        recommendations_title.pack(pady=(30, 20))
        
        # إطار التوصيات
        recommendations_frame = tk.Frame(parent_frame, bg='white', relief=tk.RAISED, bd=2)
        recommendations_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # التوصيات بناءً على التقدم
        recommendations = self.get_recommendations()
        
        for i, recommendation in enumerate(recommendations, 1):
            rec_label = tk.Label(
                recommendations_frame,
                text=f"{i}. {recommendation}",
                font=self.normal_font,
                bg='white',
                fg=self.colors['text'],
                anchor=tk.W
            )
            rec_label.pack(anchor=tk.W, padx=20, pady=5)
    
    def get_recommendations(self):
        """الحصول على التوصيات"""
        recommendations = []
        average_score = self.stats['average_score']
        total_quizzes = self.stats['total_quizzes']
        lessons_completed = self.stats['lessons_completed']
        
        if total_quizzes == 0:
            recommendations.extend([
                "ابدأ بأول اختبار لترى تقدمك!",
                "تعلم أساسيات التشفير أولاً",
                "جرب إنشاء محفظة بيتكوين"
            ])
        elif average_score < 60:
            recommendations.extend([
                "راجع المفاهيم الأساسية للتشفير",
                "مارس إنشاء المحافظ أكثر",
                "خذ وقتك في فهم كل مفهوم"
            ])
        elif average_score < 80:
            recommendations.extend([
                "تعمق في فهم البلوكتشين",
                "جرب الأسئلة الصعبة",
                "ساعد الآخرين في التعلم"
            ])
        else:
            recommendations.extend([
                "أنت جاهز للمفاهيم المتقدمة!",
                "ساعد الآخرين في التعلم",
                "استكشف تطبيقات البلوكتشين الأخرى"
            ])
        
        if lessons_completed < 3:
            recommendations.append("أكمل دروس التشفير لتحسين فهمك")
        
        if self.stats['wallets_created'] == 0:
            recommendations.append("جرب إنشاء محفظة بيتكوين")
        
        return recommendations[:5]  # أقصى 5 توصيات
    
    def create_buttons(self):
        """إنشاء الأزرار الإضافية"""
        # إطار الأزرار
        buttons_frame = tk.Frame(self.buttons_frame, bg=self.colors['background'])
        buttons_frame.pack()
        
        # زر تحديث
        refresh_button = tk.Button(
            buttons_frame,
            text="🔄 تحديث",
            command=self.refresh_data,
            font=self.button_font,
            bg=self.colors['accent'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        refresh_button.pack(side=tk.LEFT, padx=10)
        
        # زر تصدير
        export_button = tk.Button(
            buttons_frame,
            text="📤 تصدير التقدم",
            command=self.export_progress,
            font=self.button_font,
            bg=self.colors['secondary'],
            fg='white',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        export_button.pack(side=tk.LEFT, padx=10)
        
        # زر إعادة تعيين
        reset_button = tk.Button(
            buttons_frame,
            text="🔄 إعادة تعيين",
            command=self.reset_progress,
            font=self.button_font,
            bg=self.colors['warning'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        reset_button.pack(side=tk.LEFT, padx=10)
        
        # زر الإغلاق
        close_button = tk.Button(
            buttons_frame,
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
    
    def refresh_data(self):
        """تحديث البيانات"""
        self.load_progress_data()
        self.show_progress()
        messagebox.showinfo("تحديث", "تم تحديث البيانات بنجاح!")
    
    def export_progress(self):
        """تصدير التقدم"""
        if self.progress_manager.export_progress():
            messagebox.showinfo("تصدير", "تم تصدير التقدم بنجاح!")
        else:
            messagebox.showerror("خطأ", "فشل في تصدير التقدم!")
    
    def reset_progress(self):
        """إعادة تعيين التقدم"""
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من إعادة تعيين التقدم؟ هذا الإجراء لا يمكن التراجع عنه!"):
            self.progress_manager.reset_progress()
            self.load_progress_data()
            self.show_progress()
            messagebox.showinfo("إعادة تعيين", "تم إعادة تعيين التقدم بنجاح!")
    
    def close_window(self):
        """إغلاق النافذة"""
        self.window.destroy() 