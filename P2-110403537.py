"""
Practice 2
Name:楊薇蓉
Student Number:110403537
Course: 2022-CE1003-A
"""

#假設valid==0，代表為錯誤答案;假設valid==1，代表為正確答案,
valid=0
#確認密碼
while 1:
    #第一次執行do...while或是鍵入值不為EXIT或是答案錯誤
    if  valid == 0:
        valid=1
        print("Please enter your password:",end=" ")
        password = input()
        if password == "exit":
            break
        oneUpper=0
        oneNumber=0
        #進行前面幾項的判斷
        for word in password:
            #判斷是否為大寫字母
            word=ord(word)
            if(65<=word) and (word<=90):
                oneUpper=1
            #判斷是否數字
            if(48<=word) and (word<=57):
                oneNumber=1
        #輸出錯誤訊息
        #字串長度判斷
        if 6>len(password) or 10<len(password):
            valid=0
            print('Password should contain 6 to 10 characters, try again or type "exit" to leave.')
            continue
        #大寫字母
        elif oneUpper==0:
            valid=0
            print('Password should contain at least one upper-case alphabetical character, try again or type "exit" to leave.')
            continue
        #數字
        elif oneNumber==0:
            valid=0
            print('Password should contain at least one number, try again or type "exit" to leave.')
            continue
    else:
        if valid==1:
            print('Password is valid.')
        break




