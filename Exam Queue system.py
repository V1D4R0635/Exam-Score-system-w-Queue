from collections import deque


def read_scores_to_queue():
    score_queue = deque()
    print("Enter exam scores (type 'done' to finish):")

    while True:
        score = input("Enter score: ")
        if score.lower() == 'done':
            break
        try:
            score_queue.append(int(score))
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")

    return score_queue


def filter_scores(score_queue):
    filtered_queue = deque()
    while score_queue:
        score = score_queue.popleft()
        if score != 100:
            filtered_queue.append(score)
    return filtered_queue


def print_scores_from_queue(score_queue):
    print("Exam scores (excluding scores of 100) in the order they were entered:")
    while score_queue:
        print(score_queue.popleft())


def main():
    scores = read_scores_to_queue()
    filtered_scores = filter_scores(scores)
    print_scores_from_queue(filtered_scores)


if __name__ == "__main__":
    main()
