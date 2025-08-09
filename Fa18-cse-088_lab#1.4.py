
questions = list(['what is your name?',
'how can I get admisson in cse?',
'is there any test or exam necessary to get admission in MUST university?'
,'are there any other field in must related to computer science ?'
,'Can I get a fee concession?','where is admin office?','thank you'])
answers = list(['I am a chatbot',
'Visit the MUST website and click on admission you will get information',
'Yes, If you are intrested in Engineering faculty you must be passed the MUST entry test first.',
'Yes,There are BSc Software Engineering,IT,And BSc computer science where you can get admission. ',
'Go to the admin,ask them!!','Go to administration and take right you will get the office',
'You are wellcome'])

while 1:
 
    question = input('> ')
    question = question.lower()
    if question == questions[0]:
        print(answers[0])
    elif question == questions[1]:
        print(answers[1])
    elif question == questions[2]:
        print(answers[2])
    elif question == questions[3]:
        print(answers[3])
    elif question == questions[4]:
        print(answers[4])
    elif question == questions[5]:
        print(answers[5])
    elif question == questions[6]:
        print(answers[6])
   
        exit(0)
    else:
        print('Soryy irrelevant question')


    

