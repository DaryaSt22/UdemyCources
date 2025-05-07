button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey',  # Допускается в последней строке ставить запятую, а можно не ставить.
                      # Ошибки не возникнет
}

red_button = {  # Порядок следования строк здесь важен!
    **button,
    'color': 'red',
}


print(red_button)
print(button)

button_info = {
    'text': 'Buy'
}

button_style = {
    'width': 200,
    'text': 'Buy',
    'color': 'wine'
}

button_new = {
    'hug': 'happy',
    'love': 'man'
}

# button_common = {
#      **button_info,
#      **button_style,
#     **button_new
#  }

button_common = button_info | button_style | button_new  # Один и тот же результат на строках 27-30 и на 32 строке

print(button_common)