def dist(a, b):
    """ Расстояние Левенштейна (редакционное расстояние, дистанция редактирования) —
    метрика, измеряющая разность между двумя последовательностями символов.
    """

    def rec(i, j):
        if i == 0 or j == 0:
            return (max(i, j))
        elif a[i - 1] == b[j - 1]:
            return rec(i - 1, j - 1)
        else:
            return 1 + min(
                rec(i, j - 1),
                rec(i - 1, j),
                rec(i - 1, j - 1)
            )

    return rec(len(a), len(b))


str1 = 'Hello'
str2 = 'Hel'

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = round(((bigger - lev) / bigger) * 100, 1)

print('Расстояние Левенштейна: ' + str(lev))

enter_str1 = 'Строка #1: {str1}'.format(str1=str1)
enter_str2 = 'Строка #2: {str2}'.format(str2=str2)


def delimiter(s1, s2):
    dell_i = 0
    dell = ''

    longest = s1 if len(s1) > len(s2) else s2

    while dell_i != len(longest):
        dell_i += 1
        dell += '='
    return dell


print(delimiter(enter_str1, enter_str2) + '\n' + enter_str1 + '\n' + enter_str2, '\n' +
      delimiter(enter_str1, enter_str2) + '\nСхожесть: {pct}%'
      .format(pct=pct), end='')
