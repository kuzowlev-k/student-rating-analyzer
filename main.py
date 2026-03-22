data = list(map(int, input().split()))

if len(data) != 7:
    print('Во введённых данных ошибка')
    exit()

for i in range(len(data)):
    if i == 0:
        N = data[i] # Число учеников в курсе (N)
    if i == 1:
        if data[i] < 1:
            print('Во введённых данных ошибка')
            exit()
        else:
            M = data[i] # Количество занятий в курсе (M) 
    if i == 2:
        if data[i] <= 0:
            print('Во введённых данных ошибка')
            exit()
        else:
            Q = data[i] # Максимальный рейтинг (Q)
    if i == 3:
        cw = data[i] # Коэффициент для активности на занятии (cw)
    if i == 4:
        sw = data[i] # Коэффициент для практики (sw)
    if i == 5:
        hw = data[i] # Коэффициент для домашней работы (hw)
    if i == 6:
        tw = data[i] # Коэффициент для контрольной работы (tw)

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

