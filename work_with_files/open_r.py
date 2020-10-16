file = open('data_r.txt', 'r', encoding='UTF-8')
body = file.read()
file.close()


file = open('data_r.txt', 'r', encoding='UTF-8')
body2 = file.readlines()
file.close()

for i in range(len(body2)):
    body2[i] = body2[i].replace('\n', '')

print(body)
print(body2)
