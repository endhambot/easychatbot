
ques_ans = {
    'what is your name': 'endham',
    'how old are you': '16 years old',
    'what is your School': 'ananda college colombo 10 ',
    'who created you': 'I was created by thulina ',
    'what is your purpose': 'I was created for bits 2020 chat box task ',
    'who is your best friend': 'you are my best freind ',
    'whats up': 'I am doing good',
    'can we be friends': 'as you wish ',
    'do you need me': 'i made for you ',
    'Who is the greatest that you have ever met': 'YOU!',
    'are you an ai': 'no im a simple chat bot  '
}
print("")
print("please ask correct questions without a mistake ")
print("")
print('questions to ask ')
print('')
for i, ques in enumerate(ques_ans):
    print(f'{i + 1}. {ques}')
print('\ntype EXIT to exit the program\n\n')
while True:
    inp_ques = input('Q: ')
    if inp_ques == 'EXIT':
        break
    print('A:', ques_ans.get(inp_ques) or 'Question not found???', '\n')
