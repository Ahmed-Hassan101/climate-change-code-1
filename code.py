abcdefg=input("Do you wanna play this quiz?")
if abcdefg=="yes":
 print("This quiz is about climate change it is out of 10 marks")
 print("Quiz by Ahmed Hassan, Saif Samer, Abdulhadi and Rashied 9-E")
 print("Answer each question with either true or false!")
 x=input("Human activities are the primary cause of recent climate change.")
 if x=="true":
    print("Correct!")
    q=1
    print("Your score is",q)
 else:
    print("Wrong.")
    q=0
    print("Your score is",q)
 y=input("Greenhouse gases trap heat in the Earth's atmosphere.")
 if y=="true":
    print("Correct!")
    i=1
    print("Your score is",q+i)
 else:
    print("Wrong.")
    i=0
    print("Your score is",q+i)
 a=input("Climate change only affects temperatures, not weather patterns.")
 if a=="false":
    print("Correct!")
    batman=1
    print("Your score is",q+i+batman)
 else:
    print("Wrong.")
    batman=0
    print("Your score is",i+q+batman)
 lol=input("Sea levels are rising due to melting polar ice caps and glaciers.")
 if lol=="true":
    print("Correct!")
    sixpack=1
    print("Your score is", i+q+batman+sixpack)
 else:
    print("Wrong.")
    sixpack=0
    print("Your score is",i+q+batman+sixpack)
 spongebob=input("Climate change has no impact on human health.")
 if spongebob=="false":
    print("Correct!")
    bobby=1
    print("Your score is", i+q+batman+sixpack+bobby)
 else:
    print("Wrong.")
    bobby=0
    print("Your score is",i+q+batman+sixpack+bobby)
 poopyhead=input("Global warming and climate change mean exactly the same thing.")
 if poopyhead=="false":
    print("Correct!")
    johnwick=1
    print("Your score is", i+q+batman+sixpack+bobby+johnwick)
 else:
    print("Wrong.")
    johnwick=0
    print("Your score is",i+q+batman+sixpack+bobby+johnwick)
 ahmed=input("Renewable energy sources can help mitigate climate change.")
 if ahmed=="true":
    print("Correct!")
    hassan=1
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan)
 else:
    print("Wrong.")
    hassan=0
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan)
 rashied=input("There is no evidence of climate change affecting wildlife and ecosystems.")
 if rashied=="false":
    print("Correct!")
    jamal=1
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal)
 else:
    print("Wrong.")
    jamal=0
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal)
 r=input("Reducing carbon emissions can help slow down climate change.")
 if r=="true":
    print("Correct!")
    ryanburping=1
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping)
 else:
    print("Wrong.")
    ryanburping=0
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping)
 computer=input("The Paris Agreement aims to limit global warming to below 2 degrees Celsius.")
 if computer=="true":
    print("Correct")
    chemistry=1
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping+chemistry)
 else:
    print("Wrong.")
    chemistry=0
    print("Your score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping+chemistry)
 finalscore=i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping+chemistry
 print("Your final score is",i+q+batman+sixpack+bobby+johnwick+hassan+jamal+ryanburping+chemistry)
 if finalscore==10:
    print("You got 10/10 congratulations!")
 if finalscore<5:
    print("You failed")
 else:
    print("You passed")
 print("Thank you for playing this quiz, We hoped you enjoyed it!")
else:
    print("Give it a chance, you will enjoy it.")