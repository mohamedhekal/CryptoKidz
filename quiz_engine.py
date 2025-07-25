#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
محرك الأسئلة التفاعلية للأطفال
"""

import json
import random
from typing import Dict, List, Tuple
from datetime import datetime

class QuizEngine:
    """محرك الأسئلة التفاعلية"""
    
    def __init__(self):
        self.colors = {
            'primary': '#FF6B6B',
            'secondary': '#4ECDC4',
            'accent': '#45B7D1',
            'success': '#96CEB4',
            'warning': '#FFEAA7',
            'error': '#FF8A80'
        }
        
        # تحميل الأسئلة
        self.questions = self.load_questions()
        
        # نظام المكافآت
        self.rewards = {
            'crypto_expert': '🏆 خبير التشفير',
            'wallet_master': '💼 سيد المحافظ',
            'blockchain_guru': '⛓️ حكيم البلوكتشين',
            'bitcoin_ninja': '₿ نينجا البيتكوين',
            'security_guard': '🛡️ حارس الأمان'
        }
        
        # الشارات
        self.badges = {
            'first_quiz': '🥇 أول اختبار',
            'perfect_score': '⭐ نتيجة مثالية',
            'quick_learner': '⚡ متعلم سريع',
            'persistent': '💪 مثابر',
            'crypto_friend': '🐱 صديق Crypto'
        }
    
    def load_questions(self) -> Dict:
        """تحميل الأسئلة من ملف JSON"""
        questions = {
            "wallet_creation": [
                {
                    "id": "wc_1",
                    "question": "ما هي الكلمات السرية في المحفظة؟",
                    "options": [
                        "كلمات عادية نختارها",
                        "كلمات سحرية تولدها المحفظة",
                        "أرقام عشوائية فقط",
                        "رموز خاصة"
                    ],
                    "correct": 1,
                    "explanation": "الكلمات السرية مثل كلمة سر سحرية تفتح خزنتك!",
                    "difficulty": "easy",
                    "points": 10
                },
                {
                    "id": "wc_2",
                    "question": "كم عدد الكلمات السرية في محفظة CryptoKidz؟",
                    "options": ["2 كلمات", "4 كلمات", "6 كلمات", "8 كلمات"],
                    "correct": 1,
                    "explanation": "نستخدم 4 كلمات بسيطة ومفهومة للأطفال!",
                    "difficulty": "easy",
                    "points": 10
                },
                {
                    "id": "wc_3",
                    "question": "ما هو المفتاح الخاص؟",
                    "options": [
                        "مفتاح يمكن مشاركته مع الجميع",
                        "مفتاح سري مثل مفتاح بيتك",
                        "عنوان المحفظة",
                        "كلمة المرور"
                    ],
                    "correct": 1,
                    "explanation": "المفتاح الخاص مثل مفتاح بيتك - لا تشاركه مع أحد!",
                    "difficulty": "medium",
                    "points": 15
                }
            ],
            "cryptography": [
                {
                    "id": "cr_1",
                    "question": "ما هو التشفير؟",
                    "options": [
                        "نوع من النقود",
                        "لعبة الشفرات السرية",
                        "برنامج كمبيوتر",
                        "جهاز إلكتروني"
                    ],
                    "correct": 1,
                    "explanation": "التشفير مثل لعبة الشفرات - تحول الرسائل إلى رموز سرية!",
                    "difficulty": "easy",
                    "points": 10
                },
                {
                    "id": "cr_2",
                    "question": "ما الذي يحدث إذا غيرت حرفاً واحداً في النص المشفر؟",
                    "options": [
                        "لا يتغير شيء",
                        "يتغير الرمز قليلاً",
                        "يتغير الرمز كلياً",
                        "يختفي الرمز"
                    ],
                    "correct": 2,
                    "explanation": "أي تغيير صغير يغير النتيجة كلياً - مثل تغيير اسمك!",
                    "difficulty": "medium",
                    "points": 15
                },
                {
                    "id": "cr_3",
                    "question": "ما هو الفرق بين المفتاح الخاص والعام؟",
                    "options": [
                        "لا يوجد فرق",
                        "الخاص سري والعام يمكن مشاركته",
                        "الخاص طويل والعام قصير",
                        "الخاص أحمر والعام أزرق"
                    ],
                    "correct": 1,
                    "explanation": "المفتاح الخاص سري مثل مفتاح بيتك، والعام مثل عنوان بيتك!",
                    "difficulty": "medium",
                    "points": 15
                }
            ],
            "blockchain": [
                {
                    "id": "bc_1",
                    "question": "ما هو البلوكتشين؟",
                    "options": [
                        "نوع من النقود",
                        "دفتر ملاحظات مشترك",
                        "جهاز كمبيوتر",
                        "برنامج"
                    ],
                    "correct": 1,
                    "explanation": "البلوكتشين مثل دفتر ملاحظات مشترك بين الجميع!",
                    "difficulty": "easy",
                    "points": 10
                },
                {
                    "id": "bc_2",
                    "question": "لماذا البلوكتشين آمن؟",
                    "options": [
                        "لأنه كبير",
                        "لأنه مشفر ومتوزع",
                        "لأنه سريع",
                        "لأنه مجاني"
                    ],
                    "correct": 1,
                    "explanation": "البلوكتشين آمن لأنه مشفر ومتوزع بين الجميع!",
                    "difficulty": "medium",
                    "points": 15
                }
            ],
            "bitcoin": [
                {
                    "id": "bt_1",
                    "question": "ما هو البيتكوين؟",
                    "options": [
                        "نقود رقمية",
                        "لعبة فيديو",
                        "برنامج",
                        "جهاز"
                    ],
                    "correct": 0,
                    "explanation": "البيتكوين نقود رقمية مثل النقود العادية ولكن على الإنترنت!",
                    "difficulty": "easy",
                    "points": 10
                },
                {
                    "id": "bt_2",
                    "question": "أين يمكن استخدام البيتكوين؟",
                    "options": [
                        "في بلد واحد فقط",
                        "في أي مكان في العالم",
                        "في الإنترنت فقط",
                        "في البنوك فقط"
                    ],
                    "correct": 1,
                    "explanation": "البيتكوين يمكن استخدامه في أي مكان في العالم!",
                    "difficulty": "easy",
                    "points": 10
                }
            ]
        }
        return questions
    
    def get_quiz_by_category(self, category: str, num_questions: int = 3) -> List[Dict]:
        """الحصول على أسئلة من فئة معينة"""
        if category not in self.questions:
            return []
        
        available_questions = self.questions[category]
        if num_questions >= len(available_questions):
            return available_questions
        
        return random.sample(available_questions, num_questions)
    
    def get_random_quiz(self, num_questions: int = 5) -> List[Dict]:
        """الحصول على أسئلة عشوائية من جميع الفئات"""
        all_questions = []
        for category in self.questions.values():
            all_questions.extend(category)
        
        if num_questions >= len(all_questions):
            return all_questions
        
        return random.sample(all_questions, num_questions)
    
    def check_answer(self, question: Dict, selected_answer: int) -> Dict:
        """فحص الإجابة وإرجاع النتيجة"""
        is_correct = selected_answer == question['correct']
        points = question['points'] if is_correct else 0
        
        result = {
            "correct": is_correct,
            "points": points,
            "explanation": question['explanation'],
            "correct_answer": question['options'][question['correct']],
            "selected_answer": question['options'][selected_answer]
        }
        
        return result
    
    def calculate_score(self, answers: List[Dict]) -> Dict:
        """حساب النتيجة النهائية"""
        total_points = sum(answer['points'] for answer in answers)
        correct_answers = sum(1 for answer in answers if answer['correct'])
        total_questions = len(answers)
        percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        
        # تحديد المستوى
        if percentage >= 90:
            level = "ممتاز"
            reward = "🏆 خبير التشفير"
        elif percentage >= 80:
            level = "جيد جداً"
            reward = "⭐ متعلم ممتاز"
        elif percentage >= 70:
            level = "جيد"
            reward = "👍 متعلم جيد"
        elif percentage >= 60:
            level = "مقبول"
            reward = "👏 متقدم"
        else:
            level = "يحتاج ممارسة"
            reward = "💪 استمر في التعلم"
        
        return {
            "total_points": total_points,
            "correct_answers": correct_answers,
            "total_questions": total_questions,
            "percentage": percentage,
            "level": level,
            "reward": reward
        }
    
    def get_encouragement_message(self, score: Dict) -> str:
        """الحصول على رسالة تشجيعية بناءً على النتيجة"""
        percentage = score['percentage']
        
        if percentage >= 90:
            return "🎉 رائع! أنت خبير حقيقي في عالم التشفير!"
        elif percentage >= 80:
            return "🌟 ممتاز! أنت تتعلم بسرعة كبيرة!"
        elif percentage >= 70:
            return "👍 جيد جداً! استمر في التعلم!"
        elif percentage >= 60:
            return "👏 جيد! أنت على الطريق الصحيح!"
        else:
            return "💪 لا تستسلم! الممارسة تجعل الكمال!"
    
    def get_hint(self, question: Dict) -> str:
        """الحصول على تلميح للسؤال"""
        hints = {
            "wc_1": "فكر في كلمة سر سحرية تفتح خزنتك!",
            "wc_2": "نستخدم عدد بسيط ومفهوم للأطفال!",
            "wc_3": "أي مفتاح لا تريد أن يشاركه أحد؟",
            "cr_1": "فكر في الرسائل السرية!",
            "cr_2": "ماذا يحدث إذا غيرت حرفاً واحداً في اسمك؟",
            "cr_3": "أي مفتاح تشاركه مع الجميع؟",
            "bc_1": "فكر في دفتر ملاحظات مشترك!",
            "bc_2": "لماذا لا يمكن تغيير المعلومات السابقة؟",
            "bt_1": "فكر في النقود ولكن رقمية!",
            "bt_2": "هل يمكن استخدام الإنترنت في أي مكان؟"
        }
        
        return hints.get(question['id'], "فكر بعناية في الإجابة!")
    
    def create_progress_report(self, user_progress: Dict) -> Dict:
        """إنشاء تقرير التقدم"""
        total_quizzes = user_progress.get('total_quizzes', 0)
        total_points = user_progress.get('total_points', 0)
        average_score = user_progress.get('average_score', 0)
        badges_earned = user_progress.get('badges', [])
        
        report = {
            "title": "📊 تقرير التقدم",
            "stats": {
                "total_quizzes": total_quizzes,
                "total_points": total_points,
                "average_score": f"{average_score:.1f}%",
                "badges_earned": len(badges_earned)
            },
            "badges": badges_earned,
            "recommendations": self.get_recommendations(user_progress)
        }
        
        return report
    
    def get_recommendations(self, user_progress: Dict) -> List[str]:
        """الحصول على توصيات بناءً على التقدم"""
        recommendations = []
        average_score = user_progress.get('average_score', 0)
        
        if average_score < 60:
            recommendations.append("راجع المفاهيم الأساسية للتشفير")
            recommendations.append("مارس إنشاء المحافظ أكثر")
        elif average_score < 80:
            recommendations.append("تعمق في فهم البلوكتشين")
            recommendations.append("جرب الأسئلة الصعبة")
        else:
            recommendations.append("أنت جاهز للمفاهيم المتقدمة!")
            recommendations.append("ساعد الآخرين في التعلم")
        
        return recommendations

# دالة مساعدة للاختبار
def test_quiz_engine():
    """اختبار محرك الأسئلة"""
    quiz_engine = QuizEngine()
    
    print("🧪 اختبار محرك الأسئلة...")
    
    # الحصول على أسئلة عشوائية
    questions = quiz_engine.get_random_quiz(3)
    print(f"\n📝 تم تحميل {len(questions)} أسئلة")
    
    # محاكاة الإجابات
    answers = []
    for i, question in enumerate(questions):
        print(f"\nالسؤال {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"  {j+1}. {option}")
        
        # محاكاة إجابة صحيحة
        result = quiz_engine.check_answer(question, question['correct'])
        answers.append(result)
        print(f"✅ الإجابة صحيحة! +{result['points']} نقاط")
    
    # حساب النتيجة النهائية
    final_score = quiz_engine.calculate_score(answers)
    print(f"\n🏆 النتيجة النهائية:")
    print(f"النقاط: {final_score['total_points']}")
    print(f"النسبة المئوية: {final_score['percentage']:.1f}%")
    print(f"المستوى: {final_score['level']}")
    print(f"المكافأة: {final_score['reward']}")

if __name__ == "__main__":
    test_quiz_engine() 