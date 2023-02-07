# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их
# отгадать. Для этого Петя делает две подсказки. Он
# называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные
# Петей числа.

s = int(input())
p = int(input())
answer = "I didn't guess"

d = s * s - 4 * p

if d >= 0:
    x = (s + d ** 0.5) //2
    y = (s - d ** 0.5) // 2
    if x * y == p:
        answer = f"{x}, {y}"

print(answer)