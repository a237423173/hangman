#六次錯誤機會猜單字

import random
from words import words
import string

print("歡迎來到hangman猜字遊戲，請在六次機會內猜中指定單字\n猜對不扣次數，英文單字範圍在基礎1000字內")

def get_valid_words(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  #轉換成大寫單字

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  #將隨機選中的單字用集合儲存所有字母
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #儲存已猜過的字母
    lives = 6
    
    
    while len(word_letters) > 0 and lives > 0:
        #還有幾次機會
        print('你還有', lives, '次機會，請加油!')
        
        #目前猜過哪些
        print('已猜過字母', ' '.join(used_letters))
        
        #目前猜到的字母有哪些
        word_list = [letter if letter in used_letters else '_' for letter in word ]
        print('字母已經猜到', ' '.join(word_list))
        
        user_letter = input('請猜一個字母').upper()                
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                
        elif user_letter in used_letters:
            print("這字母已經猜過了喔!請再試一次")
            
        else:
            print("輸入錯誤，請再試一次")
    if lives ==0:
        print('真可惜，你已經沒機會了!\n正確答案是', word)
    else:
        print('恭喜你答對了!\n正確答案就是', word)

hangman()            
