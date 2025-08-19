try:
    print(int(10/0))
except ZeroDivisionError as e:
    print(isinstance(e, Exception))
    print(e)


try:
    print(10/0)
except:
    print("Some error occurred")  # Не рекомендуется так прописывать except,
                                  # так как нет информации об ошибке


