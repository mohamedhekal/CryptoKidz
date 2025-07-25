#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
الرسوم المتحركة البسيطة للأطفال
"""

import turtle
import time
import random
from typing import Tuple, List

class CryptoAnimations:
    """فئة الرسوم المتحركة للتطبيق"""
    
    def __init__(self):
        self.screen = None
        self.t = None
        self.colors = {
            'primary': '#FF6B6B',
            'secondary': '#4ECDC4',
            'accent': '#45B7D1',
            'success': '#96CEB4',
            'warning': '#FFEAA7',
            'background': '#FFE5E5'
        }
    
    def setup_screen(self, width: int = 800, height: int = 600):
        """إعداد الشاشة للرسوم المتحركة"""
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor(self.colors['background'])
        self.screen.title("CryptoKidz - الرسوم المتحركة")
        
        # إعداد السلحفاة
        self.t = turtle.Turtle()
        self.t.speed(0)  # أسرع سرعة
        self.t.hideturtle()
        
        return self.screen
    
    def draw_cat(self, x: int = 0, y: int = 0):
        """رسم القط Crypto"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # لون القط
        self.t.fillcolor('#FFB6C1')  # وردي فاتح
        self.t.begin_fill()
        
        # جسم القط (بيضاوي)
        self.t.circle(50, 90)
        self.t.circle(100, 90)
        self.t.circle(50, 90)
        self.t.circle(100, 90)
        
        self.t.end_fill()
        
        # الرأس
        self.t.penup()
        self.t.goto(x, y + 80)
        self.t.pendown()
        self.t.fillcolor('#FFB6C1')
        self.t.begin_fill()
        self.t.circle(30)
        self.t.end_fill()
        
        # العيون
        self.t.penup()
        self.t.goto(x - 15, y + 100)
        self.t.pendown()
        self.t.fillcolor('black')
        self.t.begin_fill()
        self.t.circle(5)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x + 15, y + 100)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(5)
        self.t.end_fill()
        
        # الأنف
        self.t.penup()
        self.t.goto(x, y + 90)
        self.t.pendown()
        self.t.fillcolor('pink')
        self.t.begin_fill()
        self.t.circle(3)
        self.t.end_fill()
        
        # الأذنين
        self.t.penup()
        self.t.goto(x - 20, y + 130)
        self.t.pendown()
        self.t.fillcolor('#FFB6C1')
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(20)
            self.t.left(120)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x + 20, y + 130)
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(20)
            self.t.right(120)
        self.t.end_fill()
    
    def draw_bitcoin_symbol(self, x: int = 0, y: int = 0):
        """رسم رمز البيتكوين"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # لون البيتكوين
        self.t.color('#F7931A')
        self.t.pensize(5)
        
        # رسم الحرف B
        self.t.penup()
        self.t.goto(x - 20, y + 40)
        self.t.pendown()
        
        # الخط العمودي
        self.t.goto(x - 20, y - 40)
        
        # القوس العلوي
        self.t.goto(x + 20, y + 20)
        self.t.goto(x + 20, y)
        self.t.goto(x - 20, y)
        
        # القوس السفلي
        self.t.goto(x + 20, y - 20)
        self.t.goto(x + 20, y - 40)
        
        # إضافة الخطوط العمودية
        self.t.penup()
        self.t.goto(x + 20, y + 20)
        self.t.pendown()
        self.t.goto(x + 20, y)
        
        self.t.penup()
        self.t.goto(x + 20, y - 20)
        self.t.pendown()
        self.t.goto(x + 20, y - 40)
    
    def draw_wallet(self, x: int = 0, y: int = 0):
        """رسم محفظة"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # لون المحفظة
        self.t.fillcolor('#8B4513')  # بني
        self.t.begin_fill()
        
        # شكل المحفظة
        self.t.goto(x - 40, y)
        self.t.goto(x - 40, y + 60)
        self.t.goto(x + 40, y + 60)
        self.t.goto(x + 40, y)
        self.t.goto(x, y)
        
        self.t.end_fill()
        
        # جيب المحفظة
        self.t.penup()
        self.t.goto(x - 30, y + 10)
        self.t.pendown()
        self.t.fillcolor('#654321')
        self.t.begin_fill()
        self.t.goto(x + 30, y + 10)
        self.t.goto(x + 30, y + 50)
        self.t.goto(x - 30, y + 50)
        self.t.goto(x - 30, y + 10)
        self.t.end_fill()
        
        # إضافة بعض التفاصيل
        self.t.penup()
        self.t.goto(x - 20, y + 20)
        self.t.pendown()
        self.t.color('white')
        self.t.write("₿", font=("Arial", 16, "bold"))
    
    def draw_lock(self, x: int = 0, y: int = 0, color: str = '#FF6B6B'):
        """رسم قفل"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # لون القفل
        self.t.fillcolor(color)
        self.t.begin_fill()
        
        # جسم القفل
        self.t.goto(x - 20, y)
        self.t.goto(x - 20, y + 40)
        self.t.goto(x + 20, y + 40)
        self.t.goto(x + 20, y)
        self.t.goto(x, y)
        
        self.t.end_fill()
        
        # قوس القفل
        self.t.penup()
        self.t.goto(x - 25, y + 40)
        self.t.pendown()
        self.t.circle(25, 180)
        
        # ثقب المفتاح
        self.t.penup()
        self.t.goto(x - 5, y + 20)
        self.t.pendown()
        self.t.fillcolor('black')
        self.t.begin_fill()
        self.t.circle(5)
        self.t.end_fill()
    
    def draw_key(self, x: int = 0, y: int = 0):
        """رسم مفتاح"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
        # لون المفتاح
        self.t.color('#FFD700')  # ذهبي
        self.t.pensize(3)
        
        # مقبض المفتاح
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.circle(10)
        
        # جسم المفتاح
        self.t.penup()
        self.t.goto(x, y + 10)
        self.t.pendown()
        self.t.goto(x, y + 40)
        
        # أسنان المفتاح
        self.t.goto(x - 5, y + 35)
        self.t.goto(x, y + 30)
        self.t.goto(x + 5, y + 25)
        self.t.goto(x, y + 20)
    
    def animate_wallet_creation(self):
        """رسوم متحركة لإنشاء المحفظة"""
        self.setup_screen()
        
        # رسم القط
        self.draw_cat(-200, 0)
        
        # إضافة نص
        self.t.penup()
        self.t.goto(0, 200)
        self.t.pendown()
        self.t.color('black')
        self.t.write("🐱 مرحباً! سأساعدك في إنشاء محفظتك", 
                    font=("Arial", 16, "bold"), align="center")
        
        time.sleep(2)
        
        # رسم المحفظة
        self.draw_wallet(200, 0)
        
        self.t.penup()
        self.t.goto(200, 100)
        self.t.pendown()
        self.t.write("محفظة جديدة!", font=("Arial", 14, "bold"), align="center")
        
        time.sleep(2)
        
        # رسم القفل
        self.draw_lock(0, -100)
        
        self.t.penup()
        self.t.goto(0, -150)
        self.t.pendown()
        self.t.write("مفتاح سري", font=("Arial", 14, "bold"), align="center")
        
        time.sleep(2)
        
        # رسم المفتاح
        self.draw_key(100, -100)
        
        self.t.penup()
        self.t.goto(100, -150)
        self.t.pendown()
        self.t.write("مفتاح عام", font=("Arial", 14, "bold"), align="center")
        
        time.sleep(2)
        
        # رسالة النجاح
        self.t.penup()
        self.t.goto(0, -200)
        self.t.pendown()
        self.t.color('#96CEB4')
        self.t.write("🎉 تم إنشاء المحفظة بنجاح!", 
                    font=("Arial", 18, "bold"), align="center")
        
        time.sleep(3)
        self.screen.bye()
    
    def animate_hash_function(self, text: str = "مرحبا"):
        """رسوم متحركة لدالة التشفير"""
        self.setup_screen()
        
        # عرض النص الأصلي
        self.t.penup()
        self.t.goto(-200, 100)
        self.t.pendown()
        self.t.color('black')
        self.t.write(f"النص الأصلي: {text}", font=("Arial", 16, "bold"))
        
        time.sleep(1)
        
        # رسم آلة التشفير
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.fillcolor('#4ECDC4')
        self.t.begin_fill()
        self.t.goto(-50, 0)
        self.t.goto(-50, 80)
        self.t.goto(50, 80)
        self.t.goto(50, 0)
        self.t.goto(0, 0)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(0, 40)
        self.t.pendown()
        self.t.color('white')
        self.t.write("آلة التشفير", font=("Arial", 12, "bold"), align="center")
        
        time.sleep(2)
        
        # عرض النتيجة
        hash_result = "A1B2C3D4"  # نتيجة مبسطة
        self.t.penup()
        self.t.goto(200, 100)
        self.t.pendown()
        self.t.color('#FF6B6B')
        self.t.write(f"النتيجة: {hash_result}", font=("Arial", 16, "bold"))
        
        time.sleep(2)
        
        # رسم سهم
        self.t.penup()
        self.t.goto(-100, 50)
        self.t.pendown()
        self.t.color('black')
        self.t.pensize(3)
        self.t.goto(100, 50)
        
        # رأس السهم
        self.t.penup()
        self.t.goto(100, 50)
        self.t.pendown()
        self.t.goto(90, 45)
        self.t.goto(90, 55)
        self.t.goto(100, 50)
        
        time.sleep(3)
        self.screen.bye()
    
    def animate_blockchain(self):
        """رسوم متحركة للبلوكتشين"""
        self.setup_screen()
        
        # رسم الكتل
        blocks = []
        for i in range(5):
            x = -200 + i * 100
            y = 0
            
            # رسم الكتلة
            self.t.penup()
            self.t.goto(x, y)
            self.t.pendown()
            self.t.fillcolor(self.colors['accent'])
            self.t.begin_fill()
            self.t.goto(x - 30, y)
            self.t.goto(x - 30, y + 60)
            self.t.goto(x + 30, y + 60)
            self.t.goto(x + 30, y)
            self.t.goto(x, y)
            self.t.end_fill()
            
            # رقم الكتلة
            self.t.penup()
            self.t.goto(x, y + 30)
            self.t.pendown()
            self.t.color('white')
            self.t.write(f"كتلة {i+1}", font=("Arial", 10, "bold"), align="center")
            
            blocks.append((x, y))
            
            time.sleep(0.5)
        
        # رسم الروابط
        for i in range(len(blocks) - 1):
            x1, y1 = blocks[i]
            x2, y2 = blocks[i + 1]
            
            self.t.penup()
            self.t.goto(x1 + 30, y1 + 30)
            self.t.pendown()
            self.t.color('black')
            self.t.pensize(3)
            self.t.goto(x2 - 30, y2 + 30)
            
            time.sleep(0.3)
        
        # إضافة النص
        self.t.penup()
        self.t.goto(0, 150)
        self.t.pendown()
        self.t.color('black')
        self.t.write("⛓️ البلوكتشين - سلسلة من الكتل المرتبطة", 
                    font=("Arial", 16, "bold"), align="center")
        
        time.sleep(3)
        self.screen.bye()
    
    def celebrate_achievement(self, message: str = "أحسنت!"):
        """رسوم متحركة للاحتفال بالإنجاز"""
        self.setup_screen()
        
        # رسم النجوم
        for _ in range(10):
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            
            self.t.penup()
            self.t.goto(x, y)
            self.t.pendown()
            self.t.color('#FFD700')
            self.t.begin_fill()
            
            for _ in range(5):
                self.t.forward(20)
                self.t.right(144)
            
            self.t.end_fill()
        
        # رسالة التهنئة
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.color('#FF6B6B')
        self.t.write(message, font=("Arial", 24, "bold"), align="center")
        
        time.sleep(3)
        self.screen.bye()

# دالة مساعدة للاختبار
def test_animations():
    """اختبار الرسوم المتحركة"""
    animations = CryptoAnimations()
    
    print("🧪 اختبار الرسوم المتحركة...")
    print("1. رسوم متحركة لإنشاء المحفظة")
    print("2. رسوم متحركة لدالة التشفير")
    print("3. رسوم متحركة للبلوكتشين")
    print("4. رسوم متحركة للاحتفال")
    
    choice = input("اختر رقم الرسوم المتحركة (1-4): ")
    
    if choice == "1":
        animations.animate_wallet_creation()
    elif choice == "2":
        animations.animate_hash_function()
    elif choice == "3":
        animations.animate_blockchain()
    elif choice == "4":
        animations.celebrate_achievement()
    else:
        print("اختيار غير صحيح!")

if __name__ == "__main__":
    test_animations() 