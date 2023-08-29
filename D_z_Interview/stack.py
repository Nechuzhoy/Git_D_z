class Stack:

    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1


    def push(self, val): # Функция добавления элемента val в stack
        if self.isFull():# проверка переполнения стека
            print('Упссс! Стек переполннен')
            exit(-1)# Стоп
        #print(f'Добавлен в стек - {val}')
        self.top = self.top + 1
        self.arr[self.top] = val



    def pop(self): # Функция для извлечения верхнего элемента из stack
        if self.isEmpty():# проверка пустой, не пустой stack
            print('Упссс! А в стеке, то пусто')
            exit(-1)

        #print(f'Удалили вершину стека - {self.peek()}')
        top = self.arr[self.top]  # уменьшает размер stack на 1 возвращает извлеченный элемент
        self.top = self.top - 1
        return top

    def peek(self):# Функция для возврата верхнего элемента stack
        if self.isEmpty(): # проверка пустой, не пустой stack
            exit(-1)
        return self.arr[self.top]


    def size(self): # Функция возврата размера stack
        return self.top + 1


    def isEmpty(self):     # Функция для проверки, пуст stack или нет
        return self.size() == 0


    def isFull(self):    # Функция проверки заполнения stack.
        return self.size() == self.capacity


if __name__ == '__main__':

    stack = Stack(5)
    for i in range(5):
        stack.push(i)

    for i in range(5):
        stack.pop()


    for i in range(3):
        stack.push(i)

    print('Вершина стека', stack.peek())
    print('Размер стека', stack.size())



