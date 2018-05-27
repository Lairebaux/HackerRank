"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her
play.
She tabulates the number of times she breaks her season record for most points and
least points in a game. Points scored in the first game establish her record for the season, and
she begins counting from there.

For example, assume her scores for the season are represented in the array
score = [12, 24, 10, 24]
Scores are in the same order as the games played. She would
tabulate her results as follows:

Game    Score   Minimum Maximum Min     Max
0       12      12      12      0       0
1       24      12      24      0       1
2       10      10      24      1       1
3       24      10      24      1       1

Given Maria's array of scores for a season of games, find and print the number of times
she breaks her records for most and least points scored during the season.
"""


def breaking_records(score):
    min_score_count = max_score_count = 0
    min_score = max_score = score[0]
    for game_num in range(len(score)):
        if score[game_num] < min_score:
            min_score_count += 1
            min_score = score[game_num]
        elif score[game_num] > max_score:
            max_score_count += 1
            max_score = score[game_num]
    return max_score_count, min_score_count

