#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مدير التقدم - حفظ وتحميل بيانات المستخدم
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class ProgressManager:
    """مدير التقدم لحفظ وتحميل بيانات المستخدم"""
    
    def __init__(self, data_file: str = "data/user_progress.json"):
        self.data_file = data_file
        self.progress_data = self.load_progress()
        
        # التأكد من وجود المجلد
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
    
    def load_progress(self) -> Dict:
        """تحميل بيانات التقدم من الملف"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return self.validate_progress_data(data)
            else:
                return self.get_default_progress()
        except Exception as e:
            print(f"خطأ في تحميل التقدم: {e}")
            return self.get_default_progress()
    
    def save_progress(self) -> bool:
        """حفظ بيانات التقدم إلى الملف"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress_data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطأ في حفظ التقدم: {e}")
            return False
    
    def get_default_progress(self) -> Dict:
        """الحصول على بيانات التقدم الافتراضية"""
        return {
            "user_info": {
                "name": "",
                "age": "",
                "created_at": datetime.now().isoformat(),
                "last_login": datetime.now().isoformat()
            },
            "wallet_creation": {
                "completed": False,
                "wallets_created": 0,
                "last_wallet": None,
                "steps_completed": []
            },
            "crypto_learning": {
                "completed": False,
                "lessons_completed": [],
                "current_lesson": 0,
                "hash_demos_tried": 0
            },
            "quizzes": {
                "total_quizzes": 0,
                "total_points": 0,
                "average_score": 0.0,
                "quiz_history": [],
                "categories_completed": []
            },
            "badges": [],
            "achievements": [],
            "settings": {
                "sound_enabled": True,
                "animations_enabled": True,
                "difficulty_level": "easy"
            }
        }
    
    def validate_progress_data(self, data: Dict) -> Dict:
        """التحقق من صحة بيانات التقدم"""
        default_data = self.get_default_progress()
        
        # التأكد من وجود جميع الأقسام المطلوبة
        for section, default_value in default_data.items():
            if section not in data:
                data[section] = default_value
            elif isinstance(default_value, dict):
                # التحقق من الأقسام الفرعية
                for subsection, subdefault in default_value.items():
                    if subsection not in data[section]:
                        data[section][subsection] = subdefault
        
        return data
    
    def get_progress(self) -> Dict:
        """الحصول على بيانات التقدم الحالية"""
        return self.progress_data
    
    def update_user_info(self, name: str = "", age: str = ""):
        """تحديث معلومات المستخدم"""
        if name:
            self.progress_data["user_info"]["name"] = name
        if age:
            self.progress_data["user_info"]["age"] = age
        
        self.progress_data["user_info"]["last_login"] = datetime.now().isoformat()
        self.save_progress()
    
    def complete_wallet_creation(self, wallet_data: Dict = None):
        """تسجيل إكمال إنشاء المحفظة"""
        self.progress_data["wallet_creation"]["completed"] = True
        self.progress_data["wallet_creation"]["wallets_created"] += 1
        
        if wallet_data:
            self.progress_data["wallet_creation"]["last_wallet"] = wallet_data
        
        # إضافة شارة
        self.add_badge("wallet_creator", "💼 منشئ المحافظ")
        
        self.save_progress()
    
    def complete_crypto_lesson(self, lesson_name: str):
        """تسجيل إكمال درس في التشفير"""
        if lesson_name not in self.progress_data["crypto_learning"]["lessons_completed"]:
            self.progress_data["crypto_learning"]["lessons_completed"].append(lesson_name)
        
        self.progress_data["crypto_learning"]["current_lesson"] += 1
        
        # التحقق من إكمال جميع الدروس
        if len(self.progress_data["crypto_learning"]["lessons_completed"]) >= 4:
            self.progress_data["crypto_learning"]["completed"] = True
            self.add_badge("crypto_expert", "🔐 خبير التشفير")
        
        self.save_progress()
    
    def add_quiz_result(self, quiz_data: Dict):
        """إضافة نتيجة اختبار"""
        self.progress_data["quizzes"]["total_quizzes"] += 1
        self.progress_data["quizzes"]["total_points"] += quiz_data.get("points", 0)
        
        # حساب متوسط النتيجة
        total_quizzes = self.progress_data["quizzes"]["total_quizzes"]
        total_points = self.progress_data["quizzes"]["total_points"]
        
        if total_quizzes > 0:
            self.progress_data["quizzes"]["average_score"] = (total_points / total_quizzes) * 10
        
        # إضافة إلى التاريخ
        quiz_record = {
            "date": datetime.now().isoformat(),
            "category": quiz_data.get("category", "general"),
            "score": quiz_data.get("score", 0),
            "points": quiz_data.get("points", 0)
        }
        self.progress_data["quizzes"]["quiz_history"].append(quiz_record)
        
        # التحقق من الشارات
        self.check_quiz_badges(quiz_data)
        
        self.save_progress()
    
    def check_quiz_badges(self, quiz_data: Dict):
        """التحقق من الشارات الجديدة"""
        total_quizzes = self.progress_data["quizzes"]["total_quizzes"]
        average_score = self.progress_data["quizzes"]["average_score"]
        
        # شارة أول اختبار
        if total_quizzes == 1:
            self.add_badge("first_quiz", "🥇 أول اختبار")
        
        # شارة نتيجة مثالية
        if quiz_data.get("score", 0) >= 90:
            self.add_badge("perfect_score", "⭐ نتيجة مثالية")
        
        # شارة متعلم سريع
        if total_quizzes >= 5 and average_score >= 80:
            self.add_badge("quick_learner", "⚡ متعلم سريع")
        
        # شارة مثابر
        if total_quizzes >= 10:
            self.add_badge("persistent", "💪 مثابر")
    
    def add_badge(self, badge_id: str, badge_name: str):
        """إضافة شارة جديدة"""
        badge = {
            "id": badge_id,
            "name": badge_name,
            "earned_at": datetime.now().isoformat()
        }
        
        # التحقق من عدم وجود الشارة مسبقاً
        existing_badges = [b["id"] for b in self.progress_data["badges"]]
        if badge_id not in existing_badges:
            self.progress_data["badges"].append(badge)
    
    def add_achievement(self, achievement_id: str, achievement_name: str, description: str = ""):
        """إضافة إنجاز جديد"""
        achievement = {
            "id": achievement_id,
            "name": achievement_name,
            "description": description,
            "earned_at": datetime.now().isoformat()
        }
        
        # التحقق من عدم وجود الإنجاز مسبقاً
        existing_achievements = [a["id"] for a in self.progress_data["achievements"]]
        if achievement_id not in existing_achievements:
            self.progress_data["achievements"].append(achievement)
    
    def get_statistics(self) -> Dict:
        """الحصول على إحصائيات التقدم"""
        stats = {
            "total_quizzes": self.progress_data["quizzes"]["total_quizzes"],
            "total_points": self.progress_data["quizzes"]["total_points"],
            "average_score": self.progress_data["quizzes"]["average_score"],
            "badges_earned": len(self.progress_data["badges"]),
            "achievements_earned": len(self.progress_data["achievements"]),
            "wallets_created": self.progress_data["wallet_creation"]["wallets_created"],
            "lessons_completed": len(self.progress_data["crypto_learning"]["lessons_completed"]),
            "days_active": self.calculate_days_active()
        }
        
        return stats
    
    def calculate_days_active(self) -> int:
        """حساب عدد أيام النشاط"""
        try:
            created_at = datetime.fromisoformat(self.progress_data["user_info"]["created_at"])
            days_active = (datetime.now() - created_at).days
            return max(1, days_active)
        except:
            return 1
    
    def reset_progress(self):
        """إعادة تعيين التقدم"""
        self.progress_data = self.get_default_progress()
        self.save_progress()
    
    def export_progress(self, filename: str = None) -> bool:
        """تصدير بيانات التقدم"""
        if not filename:
            filename = f"cryptokidz_progress_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.progress_data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطأ في تصدير التقدم: {e}")
            return False
    
    def import_progress(self, filename: str) -> bool:
        """استيراد بيانات التقدم"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                imported_data = json.load(f)
            
            # التحقق من صحة البيانات المستوردة
            validated_data = self.validate_progress_data(imported_data)
            self.progress_data = validated_data
            self.save_progress()
            return True
        except Exception as e:
            print(f"خطأ في استيراد التقدم: {e}")
            return False

# دالة مساعدة للاختبار
def test_progress_manager():
    """اختبار مدير التقدم"""
    manager = ProgressManager("test_progress.json")
    
    print("🧪 اختبار مدير التقدم...")
    
    # تحديث معلومات المستخدم
    manager.update_user_info("أحمد", "10")
    print("✅ تم تحديث معلومات المستخدم")
    
    # إكمال إنشاء محفظة
    manager.complete_wallet_creation({"address": "test123"})
    print("✅ تم تسجيل إنشاء المحفظة")
    
    # إكمال درس في التشفير
    manager.complete_crypto_lesson("hash_functions")
    print("✅ تم تسجيل درس التشفير")
    
    # إضافة نتيجة اختبار
    quiz_result = {
        "category": "wallet_creation",
        "score": 85,
        "points": 25
    }
    manager.add_quiz_result(quiz_result)
    print("✅ تم إضافة نتيجة الاختبار")
    
    # عرض الإحصائيات
    stats = manager.get_statistics()
    print(f"\n📊 الإحصائيات:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # تنظيف ملف الاختبار
    try:
        os.remove("test_progress.json")
    except:
        pass

if __name__ == "__main__":
    test_progress_manager() 