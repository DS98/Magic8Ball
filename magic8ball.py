import random
Question = input('What would you like to know?: ')
possible_answers = ["Yes - definitely!",
"It is decidedly so!",
"Without a doubt!",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

random_index = random.randint(0, len(possible_answers) -1)

answer = possible_answers[random_index]

print(answer)
