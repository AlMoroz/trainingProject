# функция - это обьект
'''def shout(word='yes!'):
    return word.capitalize()+"!"

print(shout())

scream = shout
print(scream())
'''

# определение ф-и внутри ф-и
'''def talk():
    def whisper(word = 'yes'):
        return word.lower()+'...'
    print(whisper())
talk()'''

'''
# ф-я возвращает ф-ю
def getTalk(type='shout'):
    def shout(word='yes'):
        return word.capitalize()

    def whisper(word='yes'):
        return word.lower()
    if type == 'shout':
        return shout
    else:
        return whisper

talk = getTalk()
print(talk())
'''

#декоратор своими руками
def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        a_function_to_decorate()
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function



#красивая запись
@my_shiny_new_decorator
def another_stand_alone_function():
    print("отвали")

another_stand_alone_function()