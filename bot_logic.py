import random
from praise_data import basic_praise, mood_praise, special_praise

class PraiseBot:
    def __init__(self):
        self.praise_count = 0
        self.name = "ほめほめちゃん"
    
    def get_random_praise(self):
        """基本的な褒め言葉をランダムに返す"""
        self.praise_count += 1
        
        # 10回に1回は特別な褒め言葉
        if random.randint(1, 10) == 1:
            return f"🌟特別メッセージ🌟\n{random.choice(special_praise)}"
        
        return random.choice(basic_praise)
    
    def get_mood_praise(self, mood):
        """気分に応じた褒め言葉を返す"""
        self.praise_count += 1
        
        if mood in mood_praise:
            return random.choice(mood_praise[mood])
        else:
            return self.get_random_praise()
    
    def get_greeting(self):
        """挨拶メッセージ"""
        if self.praise_count == 0:
            return f"こんにちは！{self.name}だよ！\n今日も君を褒めさせて！✨"
        else:
            return f"おかえり！また君に会えて嬉しい！\n（これまで{self.praise_count}回褒めたよ♪）"
    
    def farewell(self):
        """お別れメッセージ"""
        return f"またいつでも来てね！\n君は本当に素晴らしいよ！👋✨"