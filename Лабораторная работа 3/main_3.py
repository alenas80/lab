# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()

    dict_letters = {}
    for letters in text:
        if letters.isalpha() and not dict_letters.get(letters, None):
            dict_letters[letters] = text.count(letters)

    return dict_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(text_letters):
    frequency_letters = {}
    letters_sum = 0
    for kol_letters in text_letters.values():
        letters_sum += kol_letters

    for key, value in text_letters.items():
        frequency_letters[key] = value / letters_sum

    return frequency_letters

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_ = calculate_frequency(count_letters(main_str))
for key, value in dict_.items():
    print(f'{key}: {value:.2f}')