from bot_logic import PraiseBot

def show_praise(message):
    """褒め言葉を特別に表示"""
    print("\n\n\n\n")  # 前に4行改行
    print(message)
    print("\n\n\n\n")  # 後に4行改行

def wait_for_continue():
    """続けるボタンの代わり"""
    input("✨ 続けるには Enter を押してね ✨")

def main():
    # ほめほめちゃんを起動
    bot = PraiseBot()
    
    print("=" * 50)
    print(bot.get_greeting())
    print("=" * 50)
    
    while True:
        print("\n🌈 何をしようかな？")
        print("1. とにかく褒めて！")
        print("2. 疲れてる...")
        print("3. 何か達成した！")
        print("4. ちょっと落ち込んでる")
        print("5. さようなら")
        
        choice = input("\n番号を選んでね (1-5): ")
        
        if choice == "1":
            show_praise(f"💝 {bot.get_random_praise()}")
            wait_for_continue()
            
        elif choice == "2":
            show_praise(f"😴 {bot.get_mood_praise('tired')}")
            wait_for_continue()
            
        elif choice == "3":
            show_praise(f"🎉 {bot.get_mood_praise('achieved')}")
            wait_for_continue()
            
        elif choice == "4":
            show_praise(f"🤗 {bot.get_mood_praise('sad')}")
            wait_for_continue()
            
        elif choice == "5":
            print(f"\n{bot.farewell()}")
            break
            
        else:
            show_praise(f"✨ {bot.get_random_praise()}")
            print("（番号がよくわからなかったけど、とりあえず褒めとくね！）")
            wait_for_continue()

if __name__ == "__main__":
    main()