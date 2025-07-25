#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
شرح مفاهيم التشفير للأطفال
"""

import hashlib
import secrets
import json
from typing import Dict, List, Tuple

class CryptoExplainer:
    """شرح مفاهيم التشفير للأطفال"""
    
    def __init__(self):
        self.colors = {
            'primary': '#FF6B6B',
            'secondary': '#4ECDC4',
            'accent': '#45B7D1',
            'success': '#96CEB4',
            'warning': '#FFEAA7'
        }
    
    def explain_what_is_crypto(self) -> Dict:
        """شرح ما هو التشفير للأطفال"""
        explanation = {
            "title": "🔐 ما هو التشفير؟",
            "description": "التشفير هو مثل لعبة الشفرات السرية!",
            "examples": [
                {
                    "title": "📝 الرسائل السرية",
                    "description": "مثل عندما تكتب رسالة سرية لصديقك",
                    "example": "مرحبا → م ر ح ب ا (كل حرف له رمز)"
                },
                {
                    "title": "🔑 الأقفال والمفاتيح",
                    "description": "مثل قفل البيت، لا يمكن فتحه إلا بالمفتاح الصحيح",
                    "example": "المفتاح الخاص = مفتاح البيت، العنوان = رقم البيت"
                },
                {
                    "title": "🎭 الأقنعة",
                    "description": "مثل ارتداء قناع لإخفاء هويتك",
                    "example": "المفتاح العام = القناع، المفتاح الخاص = وجهك الحقيقي"
                }
            ],
            "fun_fact": "التشفير موجود منذ آلاف السنين! المصريون القدماء استخدموه!"
        }
        return explanation
    
    def explain_private_vs_public_key(self) -> Dict:
        """شرح الفرق بين المفتاح الخاص والعام"""
        explanation = {
            "title": "🔑 المفتاح الخاص vs المفتاح العام",
            "private_key": {
                "title": "🔐 المفتاح الخاص",
                "description": "مثل مفتاح بيتك - لا تشاركه مع أحد!",
                "characteristics": [
                    "سري جداً",
                    "لا تشاركه مع أحد",
                    "مثل كلمة المرور",
                    "يجب حفظه في مكان آمن"
                ],
                "example": "مثل مفتاح غرفتك الخاصة"
            },
            "public_key": {
                "title": "🔓 المفتاح العام",
                "description": "مثل عنوان بيتك - يمكن للجميع معرفته",
                "characteristics": [
                    "يمكن مشاركته",
                    "مثل رقم الهاتف",
                    "آمن للمشاركة",
                    "يستخدم للاستقبال"
                ],
                "example": "مثل عنوان البريد الإلكتروني"
            },
            "analogy": {
                "title": "🏠 تشبيه البيت",
                "description": "المفتاح الخاص = مفتاح البيت، المفتاح العام = عنوان البيت"
            }
        }
        return explanation
    
    def explain_hash_functions(self) -> Dict:
        """شرح دوال التشفير (Hash Functions)"""
        explanation = {
            "title": "🔢 دوال التشفير (Hash Functions)",
            "description": "مثل آلة تحول أي شيء إلى رمز ثابت!",
            "examples": [
                {
                    "input": "مرحبا",
                    "output": "A1B2C3D4",
                    "description": "نفس الكلمة تعطي نفس النتيجة دائماً"
                },
                {
                    "input": "أهلاً وسهلاً",
                    "output": "E5F6G7H8",
                    "description": "كلمات مختلفة تعطي نتائج مختلفة"
                }
            ],
            "characteristics": [
                "نفس المدخل يعطي نفس المخرج دائماً",
                "لا يمكن العودة من المخرج إلى المدخل",
                "أي تغيير صغير يغير النتيجة كلياً",
                "مثل تحويل اسمك إلى رقم خاص بك"
            ],
            "fun_example": "مثل تحويل اسمك إلى رقم خاص بك في المدرسة!"
        }
        return explanation
    
    def demonstrate_hash_function(self, text: str) -> str:
        """إظهار كيف تعمل دالة التشفير"""
        # استخدام SHA-256 ولكن عرض النتيجة بطريقة مبسطة
        hash_result = hashlib.sha256(text.encode('utf-8')).hexdigest()
        # أخذ أول 8 أحرف للتبسيط
        return hash_result[:8].upper()
    
    def explain_blockchain_simple(self) -> Dict:
        """شرح البلوكتشين بطريقة مبسطة"""
        explanation = {
            "title": "⛓️ ما هو البلوكتشين؟",
            "description": "مثل دفتر ملاحظات مشترك بين الجميع!",
            "blocks": [
                {
                    "title": "📦 الكتلة (Block)",
                    "description": "مثل صفحة في الدفتر تحتوي على معلومات",
                    "content": ["المعاملات", "التاريخ", "الرقم التسلسلي"]
                },
                {
                    "title": "🔗 السلسلة (Chain)",
                    "description": "كل كتلة مرتبطة بالكتلة السابقة",
                    "content": ["مثل حلقة في سلسلة", "لا يمكن تغييرها"]
                }
            ],
            "characteristics": [
                "جميع الناس يرون نفس المعلومات",
                "لا يمكن تغيير المعلومات السابقة",
                "آمن جداً",
                "شفاف للجميع"
            ],
            "analogy": "مثل دفتر ملاحظات مدرسي مشترك - الجميع يرى ما يكتبه الجميع!"
        }
        return explanation
    
    def explain_bitcoin_simple(self) -> Dict:
        """شرح البيتكوين بطريقة مبسطة"""
        explanation = {
            "title": "₿ ما هو البيتكوين؟",
            "description": "نقود رقمية مثل النقود العادية ولكن على الإنترنت!",
            "features": [
                {
                    "title": "💻 رقمية",
                    "description": "لا توجد أوراق أو عملات معدنية"
                },
                {
                    "title": "🌍 عالمية",
                    "description": "يمكن استخدامها في أي مكان في العالم"
                },
                {
                    "title": "🔒 آمنة",
                    "description": "مشفرة ومحمية بالتكنولوجيا"
                },
                {
                    "title": "👥 لامركزية",
                    "description": "لا توجد بنك أو حكومة تتحكم بها"
                }
            ],
            "how_it_works": [
                "1. تحويل النقود العادية إلى بيتكوين",
                "2. إرسال البيتكوين عبر الإنترنت",
                "3. استقبال البيتكوين في محفظة رقمية",
                "4. تحويل البيتكوين إلى نقود عادية عند الحاجة"
            ],
            "fun_fact": "أول بيتكوين تم شراؤه كان مقابل بيتزا! 🍕"
        }
        return explanation
    
    def create_interactive_demo(self) -> Dict:
        """إنشاء عرض تفاعلي للتشفير"""
        demo = {
            "title": "🎮 عرض تفاعلي للتشفير",
            "steps": [
                {
                    "step": 1,
                    "title": "اكتب اسمك",
                    "description": "سنحوله إلى رمز مشفر",
                    "action": "input_text"
                },
                {
                    "step": 2,
                    "title": "شاهد التحويل",
                    "description": "كيف تحول اسمك إلى رمز",
                    "action": "show_hash"
                },
                {
                    "step": 3,
                    "title": "جرب تغيير حرف واحد",
                    "description": "شاهد كيف يتغير الرمز كلياً",
                    "action": "modify_text"
                }
            ],
            "examples": {
                "أحمد": "A1B2C3D4",
                "أحمدا": "E5F6G7H8",
                "أحمدي": "I9J0K1L2"
            }
        }
        return demo
    
    def get_crypto_quiz_questions(self) -> List[Dict]:
        """أسئلة اختبارية عن التشفير"""
        questions = [
            {
                "question": "ما هو المفتاح الذي يجب أن تبقيه سرياً؟",
                "options": ["المفتاح العام", "المفتاح الخاص", "العنوان", "الجميع"],
                "correct": 1,
                "explanation": "المفتاح الخاص مثل مفتاح بيتك - لا تشاركه مع أحد!"
            },
            {
                "question": "ما الذي يحدث إذا غيرت حرفاً واحداً في النص المشفر؟",
                "options": ["لا يتغير شيء", "يتغير الرمز قليلاً", "يتغير الرمز كلياً", "يختفي الرمز"],
                "correct": 2,
                "explanation": "أي تغيير صغير يغير النتيجة كلياً - مثل تغيير اسمك!"
            },
            {
                "question": "ما هو البلوكتشين؟",
                "options": ["نوع من النقود", "دفتر ملاحظات مشترك", "جهاز كمبيوتر", "برنامج"],
                "correct": 1,
                "explanation": "البلوكتشين مثل دفتر ملاحظات مشترك بين الجميع!"
            },
            {
                "question": "ما هو البيتكوين؟",
                "options": ["نقود رقمية", "لعبة فيديو", "برنامج", "جهاز"],
                "correct": 0,
                "explanation": "البيتكوين نقود رقمية مثل النقود العادية ولكن على الإنترنت!"
            }
        ]
        return questions

# دالة مساعدة للاختبار
def test_crypto_explainer():
    """اختبار شرح التشفير"""
    explainer = CryptoExplainer()
    
    print("🧪 اختبار شرح التشفير...")
    
    # شرح التشفير
    crypto_explanation = explainer.explain_what_is_crypto()
    print(f"\n{crypto_explanation['title']}")
    print(crypto_explanation['description'])
    
    # شرح المفاتيح
    keys_explanation = explainer.explain_private_vs_public_key()
    print(f"\n{keys_explanation['title']}")
    print(f"المفتاح الخاص: {keys_explanation['private_key']['description']}")
    print(f"المفتاح العام: {keys_explanation['public_key']['description']}")
    
    # عرض دالة التشفير
    print("\n🔢 عرض دالة التشفير:")
    test_text = "مرحبا"
    hash_result = explainer.demonstrate_hash_function(test_text)
    print(f"'{test_text}' → {hash_result}")

if __name__ == "__main__":
    test_crypto_explainer() 