import random
import argparse
import time

DEFAULT_LEVEL = 4
GAME_LEN = 5

def check_positive(value):
    ivalue = int(value)
    if ivalue < 0:
        parser.print_help()
        raise argparse.ArgumentTypeError("Invalid argument %s. Level must be a positive integer." % value)
    return ivalue

parser = argparse.ArgumentParser()
endless = parser.add_mutually_exclusive_group(required=True)
endless.add_argument('--game', '-g', action='store_true', help='Play game of {} questions'.format(GAME_LEN))
endless.add_argument('--training', '-t', action='store_true', help='Play endless training')
parser.add_argument('--level', '-l', nargs='?', default=DEFAULT_LEVEL, type=check_positive, help='Maximum number of bits used (max decimal = 2^level-1')
args = parser.parse_args()

if args.training:
    print("###################################")
    print("# To close the training enter 'q' #")
    print("###################################")

print("Selected Level: {} (Max decimal {})\n".format(args.level, 2**args.level-1))

game_numbers = random.sample(range(0, 2**args.level-1), GAME_LEN)
MAX_POINTS = 100
MAX_TIME = 20
correct = 0
wrong = 0
time_counter = 0
points = 0
question_counter = 1
game_completed = False
while True:
    # If game is completed
    if question_counter > GAME_LEN and args.game:
        game_completed = True
        break

    if args.game:
        number = game_numbers[question_counter-1]
    else:
        number = random.randint(0, 2**args.level-1)

    q_type = random.randint(0,2)

    question1 = str(question_counter) + ". What is binary and hex of " + str(number) + " (bin,hex): "
    question2 = str(question_counter) + ". What is decimal and hex of " + '{0:0{num_of_bits}b}'.format(number, num_of_bits=args.level) + " (dec,hex): "
    question3 = str(question_counter) + ". What is decimal and binary of " + hex(number) + " (dec,bin): "

    questions = [question1, question2, question3]
    tic = time.perf_counter()
    if q_type == 0:
        ans = input(question1).replace(" ", "").upper().split(",")
        correct_ans = ['{:b}'.format(number), hex(number)[2:].upper()]
    elif q_type == 1:
        ans = input(question2).replace(" ", "").upper().split(",")
        correct_ans = [str(number), hex(number)[2:].upper()]
    elif q_type == 2:
        ans = input(question3).replace(" ", "").upper().split(",")
        correct_ans = [str(number), '{:b}'.format(number)]

    toc = time.perf_counter()

    if ans == ["Q"]:
        break
    elif ans == correct_ans:
        correct += 1
        k = -MAX_POINTS/MAX_TIME
        points_to_add = k*(toc-tic)+MAX_POINTS
        if points_to_add < 0:
            points_to_add = 0
        points += points_to_add
        print("Correct answer! {:.2f} points earned".format(points_to_add))
    else:
        print("Wrong answer! Correct answer is ", correct_ans[0],", ", correct_ans[1], sep="")
        wrong += 1

    time_counter += toc - tic
    question_counter += 1

    if not (args.game or args.training):
        break

correct_percent = round(correct/(correct+wrong)*100)
avg_time = round(time_counter/(correct+wrong),2)
print()
# If game was completed
if args.game and game_completed:
    print("Game score:  {:.2f}".format(points))
print("Avg correct: {} %".format(correct_percent))
print("Avg time:    {} sec".format(avg_time))