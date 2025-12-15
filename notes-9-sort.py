# Intro to Sort
# Author: connor ter stege
# 4 December

import csv

from helper_spotify import songs_by_artist, string_to_num

def selection_sort(l: list[int], ascending=True) -> list[int]:
    num_items = len(l)
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i
        for j in range(i+1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
        l[i], l[candidate_index] = l[candidate_index], l[i]
    return l

def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    values = [string_to_num(row[col]) for row in songs]
    sorted_values = selection_sort(values.copy(), ascending=ascending)
    sorted_list = []
    used = set()
    for v in sorted_values:
        for i, row in enumerate(songs):
            if i not in used and string_to_num(row[col]) == v:
                sorted_list.append(row)
                used.add(i)
                break
    return sorted_list

if __name__ == "__main__":
    file_path = "spotify2024.csv"

    print("Task 1")
    ed_songs = songs_by_artist(file_path, "Ed Sheeran")
    for row in ed_songs:
        print(row[0], string_to_num(row[11]))

    print("\nTask 2")
    sorted_by_yt = sort_songs(ed_songs, col=11, ascending=True)
    for row in sorted_by_yt:
        print(row[0], string_to_num(row[11]))

    print("\nTask 3")
    sorted_by_tt = sort_songs(ed_songs, col=15, ascending=False)
    for row in sorted_by_tt:
        print(row[0], string_to_num(row[15]))







