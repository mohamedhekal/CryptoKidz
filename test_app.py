#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار بسيط للتطبيق
"""

import sys
import os

# إضافة المجلد الحالي للمسار
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_wallet_generator():
    """اختبار مولد المحفظة"""
    print("🧪 اختبار مولد المحفظة...")
    
    try:
        from wallet_generator import SimpleWalletGenerator
        
        generator = SimpleWalletGenerator()
        wallet = generator.create_wallet()
        
        print("✅ تم إنشاء المحفظة بنجاح!")
        print(f"📝 الكلمات السرية: {wallet['seed_phrase']}")
        print(f"🔐 المفتاح الخاص: {wallet['private_key']}")
        print(f"🔑 المفتاح العام: {wallet['public_key']}")
        print(f"📍 العنوان: {wallet['address']}")
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار مولد المحفظة: {e}")
        return False

def test_crypto_explainer():
    """اختبار شرح التشفير"""
    print("\n🧪 اختبار شرح التشفير...")
    
    try:
        from crypto_explainer import CryptoExplainer
        
        explainer = CryptoExplainer()
        
        # اختبار شرح التشفير
        crypto_explanation = explainer.explain_what_is_crypto()
        print(f"✅ شرح التشفير: {crypto_explanation['title']}")
        
        # اختبار دالة التشفير
        hash_result = explainer.demonstrate_hash_function("مرحبا")
        print(f"✅ دالة التشفير: 'مرحبا' → {hash_result}")
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار شرح التشفير: {e}")
        return False

def test_quiz_engine():
    """اختبار محرك الأسئلة"""
    print("\n🧪 اختبار محرك الأسئلة...")
    
    try:
        from quiz_engine import QuizEngine
        
        quiz_engine = QuizEngine()
        
        # اختبار الحصول على أسئلة
        questions = quiz_engine.get_random_quiz(3)
        print(f"✅ تم تحميل {len(questions)} أسئلة")
        
        # اختبار فحص الإجابة
        if questions:
            question = questions[0]
            result = quiz_engine.check_answer(question, question['correct'])
            print(f"✅ فحص الإجابة: {result['correct']}")
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار محرك الأسئلة: {e}")
        return False

def test_progress_manager():
    """اختبار مدير التقدم"""
    print("\n🧪 اختبار مدير التقدم...")
    
    try:
        from data.progress_manager import ProgressManager
        
        manager = ProgressManager("test_progress.json")
        
        # اختبار تحديث معلومات المستخدم
        manager.update_user_info("أحمد", "10")
        print("✅ تم تحديث معلومات المستخدم")
        
        # اختبار إضافة نتيجة اختبار
        quiz_data = {
            'category': 'test',
            'score': 85,
            'points': 25
        }
        manager.add_quiz_result(quiz_data)
        print("✅ تم إضافة نتيجة الاختبار")
        
        # اختبار الحصول على الإحصائيات
        stats = manager.get_statistics()
        print(f"✅ الإحصائيات: {stats['total_quizzes']} اختبارات")
        
        # تنظيف ملف الاختبار
        try:
            os.remove("test_progress.json")
        except:
            pass
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار مدير التقدم: {e}")
        return False

def test_animations():
    """اختبار الرسوم المتحركة"""
    print("\n🧪 اختبار الرسوم المتحركة...")
    
    try:
        from animations import CryptoAnimations
        
        animations = CryptoAnimations()
        print("✅ تم تهيئة الرسوم المتحركة")
        
        # ملاحظة: الرسوم المتحركة تحتاج نافذة رسومية
        print("ℹ️ الرسوم المتحركة تحتاج نافذة رسومية للاختبار الكامل")
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار الرسوم المتحركة: {e}")
        return False

def main():
    """الاختبار الرئيسي"""
    print("🚀 بدء اختبار CryptoKidz...")
    print("=" * 50)
    
    tests = [
        test_wallet_generator,
        test_crypto_explainer,
        test_quiz_engine,
        test_progress_manager,
        test_animations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 نتائج الاختبار: {passed}/{total} اختبارات نجحت")
    
    if passed == total:
        print("🎉 جميع الاختبارات نجحت! التطبيق جاهز للاستخدام.")
    else:
        print("⚠️ بعض الاختبارات فشلت. يرجى مراجعة الأخطاء.")
    
    print("\n💡 لتشغيل التطبيق:")
    print("python3 main.py")
    print("أو")
    print("python3 run.py")

if __name__ == "__main__":
    main() 