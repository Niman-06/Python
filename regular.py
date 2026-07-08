# regular experssion  
import re 
# exp="[6-9]{1}\d{9}"
# str1="1 2 4 6 2 7 NUMBER 9078842146 and mail id is nimanpreetkaur04@gmail.com and other id is usergmail.com and INSTA@gmail.com"
# print(re.findall(exp,str1))
# print(re.sub(exp,repl='_',string=str1))


password_exp="[?=a-zA-Z0-9]+[@,_]\d{2,3}"
str1="gurleen_54 and Manvir@67 and insta"
print(re.findall(password_exp,str1))

