def appearance(intervals):
    presence_time = 0
    previous_time = 0

    # Индексы для итерации по трём спискам
    indexes = {
        'lesson': 0,
        'pupil': 0,
        'tutor': 0
    }

    # Проверка, является ли текущий индекс в a ближайшим
    def closest(a, b, c):
        return indexes[a] < len(intervals[a]) and \
               (indexes[b] >= len(intervals[b]) or intervals[a][indexes[a]] <= intervals[b][indexes[b]]) and \
               (indexes[c] >= len(intervals[c]) or intervals[a][indexes[a]] <= intervals[c][indexes[c]])

    # Пока урок не закончился
    while indexes['lesson'] != 2:
        current = 'lesson'  # Текущий список, имеющий ближайшую по времени точку

        if closest('pupil', 'tutor', 'lesson'):
            current = 'pupil'
        elif closest('tutor', 'pupil', 'lesson'):
            current = 'tutor'

        current_time = intervals[current][indexes[current]]

        if indexes['lesson'] % 2 == 1 and indexes['pupil'] % 2 == 1 and indexes['tutor'] % 2 == 1:
            presence_time += current_time - previous_time

        indexes[current] += 1
        previous_time = current_time

    return presence_time


tests = [
    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },

    # Этот тест в списке 'pupil' содержит последовательность, которая не является возрастающей:
    #                              v
    # [1594702789, 1594704500, 1594702807, ...]

    # {'data': {'lesson': [1594702800, 1594706400],
    #           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
    #                     1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
    #                     1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
    #                     1594706524, 1594706524, 1594706579, 1594706641],
    #           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #  'answer': 3577
    #  },
    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },

    # Ещё тесты:
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [30, 50],
            'tutor': [20, 90]
        },
        'answer': 20
    },
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [0, 20, 30, 50],
            'tutor': [0, 110]
        },
        'answer': 30
    },
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [20, 70],
            'tutor': [30, 80]
        },
        'answer': 40
    },
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [20, 70],
            'tutor': [30, 60]
        },
        'answer': 30
    },
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [10, 20, 50, 55, 60, 80, 85, 100, 105, 110],
            'tutor': [10, 100]
        },
        'answer': 50
    },
    {
        'data': {
            'lesson': [10, 100],
            'pupil': [20, 110],
            'tutor': [30, 105]
        },
        'answer': 70
    }

]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

    print('tests passed')
