# course = 'Python for beginners'
# another = course[1:-1]
#
# len(course)
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find('P'))
# print(course.replace('o', 'O'))
# print('...' in course)
#
# print(10 // 3)  # to get integer
# print(10 % 3)  # modulus
# print(10 ** 3)  # exponent
# print(10 += 3)   # augmented assignment operator
#
#
# price = 1000000
# is_good_credit = true
#
# if is_good_credit:
#     down_payment = 0.1 * price
# else
#     down_payment = 0.2 *price
# print(f"Down Payment : ${down_payment}")

# Day2
# weight = input('Weight:')
# unit = input('(L)lbs or (K)g: ')
#
# if unit.upper() == "L":
#     converted = int(weight)
#     print(converted * 0.45)
# elif unit.upper() == "K":
#     converted = int(weight)
#     print(converted / 0.45)
#
# secrete_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input('Guess : '))
#     guess_count +=1
#     if guess == secrete_number:
#         print('You Won!')
#         break
# else: print('Sorry you failed!')

command = ""
started = False
while True:
    command = input("> ").lower()
    if command.lower() == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Car started')
    elif command.lower() == 'stop':
        if started:
            print('Car stopped')
        else:
            started: False
            print('Car is already stopped')
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

