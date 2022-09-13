from tkinter.messagebox import YES


print('Hello And Welcome To My Quiz')

playing = input('Do You Want to Play? ')

if playing.lower() != 'yes' :
    quit()
    
print('Okay! Lets play')
score = 0

answer = input('What does CPU stands for? ')
if answer.lower() == 'central processing unit':
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does GPU stands for? ').lower()
if answer == 'graphic processing unit':
    print('Correct')
    score = score + 1
else:
    print('Incorrect!')
    
answer = input('What does RAM stands for? ').lower()
if answer == 'random access memory':
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does PAS stands for? ')
if answer.lower() == 'power supply unit':
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    
print('You got ' +str(score) + ' questions correct!')

print('You got ' +str((score/4) * 100) + '%.')


        
