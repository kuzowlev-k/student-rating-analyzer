data = list(map(int, input().split()))

if len(data) != 7:
    print('Во введённых данных ошибка')
    exit()

N = data[0]  # Число учеников в курсе (N)
M = data[1]  # Количество занятий в курсе (M)

if M < 1:
    print('Во введённых данных ошибка')
    exit()

Q = data[2]  # Максимальный рейтинг (Q)

if Q <= 0:
    print('Во введённых данных ошибка')
    exit()

cw = data[3]  # Коэффициент для активности на занятии (cw)
sw = data[4]  # Коэффициент для практики (sw)
hw = data[5]  # Коэффициент для домашней работы (hw)
tw = data[6]  # Коэффициент для контрольной работы (tw)

# Проверка коэффициентов > 0
if cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
    print('Во введённых данных ошибка')
    exit()

surname = input()

total_raiting = 0

for j in range(M):
    raitings = list(map(int, input().split(',')))
    for k in range(len(raitings)):
        if raitings[k] < 0:
            print('Во введённых данных ошибка')
            exit()
        else:
            if k == 0:
                total_raiting += raitings[k] * cw
            if k == 1:
                total_raiting += raitings[k] * sw
            if k == 2:
                total_raiting += raitings[k] * hw
            if k == 3:
                total_raiting += raitings[k] * tw

total_rate = round((100 * total_raiting) / Q)

if total_raiting  > Q:
    print('Во введённых данных ошибка')
    exit()

print(f'{surname} {total_rate}%')

