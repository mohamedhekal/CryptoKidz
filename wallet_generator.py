#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد محافظ البيتكوين المبسط للأطفال
"""

import hashlib
import secrets
import base58
import json
from typing import Dict, List, Tuple

class SimpleWalletGenerator:
    """مولد محفظة مبسط للأطفال"""
    
    def __init__(self):
        self.colors = {
            'primary': '#FF6B6B',      # أحمر فاتح
            'secondary': '#4ECDC4',    # أزرق مخضر
            'accent': '#45B7D1',       # أزرق فاتح
            'success': '#96CEB4',      # أخضر فاتح
            'warning': '#FFEAA7'       # أصفر فاتح
        }
    
    def generate_simple_seed(self) -> str:
        """توليد seed phrase مبسط للأطفال"""
        # كلمات بسيطة ومفهومة للأطفال
        simple_words = [
            "قط", "كلب", "أسد", "نمر", "فيل", "زرافة", "حصان", "بقرة",
            "خروف", "دجاجة", "بط", "بطة", "سمكة", "سلحفاة", "أرنب",
            "قرد", "باندا", "كوالا", "كنغر", "دب", "ذئب", "ثعلب"
        ]
        
        # توليد 4 كلمات عشوائية
        seed_words = []
        for _ in range(4):
            word = secrets.choice(simple_words)
            seed_words.append(word)
        
        return " ".join(seed_words)
    
    def create_simple_hash(self, text: str) -> str:
        """إنشاء hash مبسط للأطفال"""
        # استخدام SHA-256 ولكن عرض النتيجة بطريقة مبسطة
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        # أخذ أول 8 أحرف فقط للتبسيط
        return hash_result[:8].upper()
    
    def generate_public_key(self, private_key: str) -> str:
        """توليد مفتاح عام مبسط"""
        # محاكاة بسيطة لتوليد المفتاح العام
        hash_result = hashlib.sha256(private_key.encode()).hexdigest()
        return f"BTC{hash_result[:10].upper()}"
    
    def generate_address(self, public_key: str) -> str:
        """توليد عنوان البيتكوين المبسط"""
        # محاكاة بسيطة لتوليد العنوان
        address_hash = hashlib.sha256(public_key.encode()).hexdigest()
        return f"1{address_hash[:10].upper()}"
    
    def create_wallet(self) -> Dict:
        """إنشاء محفظة كاملة مبسطة"""
        # توليد الكلمات السرية
        seed_phrase = self.generate_simple_seed()
        
        # إنشاء المفتاح الخاص
        private_key = self.create_simple_hash(seed_phrase)
        
        # إنشاء المفتاح العام
        public_key = self.generate_public_key(private_key)
        
        # إنشاء العنوان
        address = self.generate_address(public_key)
        
        wallet = {
            "seed_phrase": seed_phrase,
            "private_key": private_key,
            "public_key": public_key,
            "address": address,
            "balance": "0.00 BTC",
            "created_at": "اليوم"
        }
        
        return wallet
    
    def explain_wallet_creation(self) -> List[Dict]:
        """شرح خطوات إنشاء المحفظة للأطفال"""
        steps = [
            {
                "step": 1,
                "title": "🎲 توليد الكلمات السرية",
                "description": "نقوم باختيار 4 كلمات عشوائية مثل: قط كلب أسد نمر",
                "code": "seed = generate_random_words()",
                "color": self.colors['primary']
            },
            {
                "step": 2,
                "title": "🔐 إنشاء المفتاح الخاص",
                "description": "نحول الكلمات إلى مفتاح سري باستخدام دالة التشفير",
                "code": "private_key = hash(seed_phrase)",
                "color": self.colors['secondary']
            },
            {
                "step": 3,
                "title": "🔑 إنشاء المفتاح العام",
                "description": "من المفتاح الخاص نولد مفتاح عام يمكن مشاركته",
                "code": "public_key = generate_from(private_key)",
                "color": self.colors['accent']
            },
            {
                "step": 4,
                "title": "📍 إنشاء العنوان",
                "description": "نحول المفتاح العام إلى عنوان قصير وسهل التذكر",
                "code": "address = convert_to_address(public_key)",
                "color": self.colors['success']
            }
        ]
        return steps
    
    def validate_wallet(self, wallet: Dict) -> bool:
        """التحقق من صحة المحفظة"""
        required_fields = ['seed_phrase', 'private_key', 'public_key', 'address']
        return all(field in wallet for field in required_fields)
    
    def get_wallet_info(self, wallet: Dict) -> str:
        """الحصول على معلومات المحفظة بصيغة نصية"""
        info = f"""
🐱 محفظة CryptoKidz الجديدة:

📝 الكلمات السرية:
{wallet['seed_phrase']}

🔐 المفتاح الخاص:
{wallet['private_key']}

🔑 المفتاح العام:
{wallet['public_key']}

📍 العنوان:
{wallet['address']}

💰 الرصيد: {wallet['balance']}
        """
        return info.strip()

# دالة مساعدة للاختبار
def test_wallet_generator():
    """اختبار مولد المحفظة"""
    generator = SimpleWalletGenerator()
    
    print("🧪 اختبار مولد المحفظة...")
    
    # إنشاء محفظة
    wallet = generator.create_wallet()
    print("\n✅ تم إنشاء المحفظة بنجاح!")
    print(generator.get_wallet_info(wallet))
    
    # عرض خطوات الإنشاء
    print("\n📚 خطوات إنشاء المحفظة:")
    steps = generator.explain_wallet_creation()
    for step in steps:
        print(f"\n{step['step']}. {step['title']}")
        print(f"   {step['description']}")

if __name__ == "__main__":
    test_wallet_generator() 