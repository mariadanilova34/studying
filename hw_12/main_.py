import random
import string
import operator


'''Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains name of the file and number in that file:
A.txt: 67
B.txt: 12
...
Z.txt: 98
'''


def task_1():

    summary_file_task_1 = open('task1_summary_file.txt', 'w')

    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        file_task_1 = open(file_name, "w")
        random_number = random.randint(1, 100)
        file_task_1.write(f"{random_number}")
        summary_file_task_1.write(f"{letter}: {random_number}\n")
        file_task_1.close()

    summary_file_task_1.close()
    return


task_1()

'''

Create file with some content. As example you can take this one
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,
Create second file and copy content of the first file to the second file in upper case.
'''


def task_2():

    with open('task2_file_with_some_content.txt', "w+") as file_with_some_content_task_2:
        file_with_some_content_task_2.write("Тому що ніколи тебе не вирвеш\n"
                                            "ніколи не забереш,\n"
                                            "тому що вся твоя свобода\n"
                                            "складається з меж,\n"
                                            "тому що в тебе немає\n"
                                            "жодного вантажу,\n"
                                            "тому що ти ніколи не слухаєш,\n"
                                            "оскільки знаєш і так,\n"
                                            "що я скажу")

    with open('task2_file_with_some_content.txt', "r") as file_with_some_content_task_2:
        some_content_in_upper_case = file_with_some_content_task_2.read().upper()

    with open("task2_second_file.txt", 'w') as second_file_task_2:
        second_file_task_2.write(some_content_in_upper_case)

    return


task_2()

'''
Write a program that will simulate user score in a game. Create a list with 5 player's names. After that simulate 100 
games for each player. As a result of the game create a list with player's name and his score (0-1000 range). 
And save it to a CSV file. File should looks like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
'''


def task_3():

    name_list2, players_book = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary'], []

    for players in range(0, 100):
        for name in name_list2:
            players_book.append(f"{name}, {random.randint(0, 1000)}")

    with open('task3_result.csv', 'w') as result_task_3:
        result_task_3.write("Player name, Score")
        for p in players_book:
            result_task_3.write(f'\n{p}')
    return


task_3()


'''
Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv where each row 
contains the player name and their highest score. Final score should sorted by descending of highest score

The output CSV file should look like this:

Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345

high_scores.csv
'''


def task_4():

    name_list, highest_score_book = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary'], {}
    josh, luke, kate, mark, mary = [], [], [], [], []
    with open('task3_result.csv', 'r') as previous_file:
        data = previous_file.read()

    data_list = data.split("\n")

    for i in data_list:
        if i.startswith('Josh'):
            josh.append(int(i[i.find(" ")+1:]))
        elif i.startswith('Luke'):
            luke.append(int(i[i.find(" ")+1:]))
        elif i.startswith('Kate'):
            kate.append(int(i[i.find(" ")+1:]))
        elif i.startswith('Mark'):
            mark.append(int(i[i.find(" ")+1:]))
        elif i.startswith('Mary'):
            mary.append(int(i[i.find(" ")+1:]))

    highest_score_book['Josh'] = max(josh)
    highest_score_book['Luke'] = max(luke)
    highest_score_book['Kate'] = max(kate)
    highest_score_book['Mark'] = max(mark)
    highest_score_book['Mary'] = max(mary)

    sorted_values = sorted(highest_score_book.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = {k: v for k, v in sorted_values}

    with open('task4_high_scores.csv', 'w') as high_scores_file:
        high_scores_file.write("Player name, Highest score")
        for player in sorted_dict:
            high_scores_file.write(f"\n{player}, {sorted_dict[player]}")

    return


task_4()