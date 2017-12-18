class Queue(list):
    def pop(self):  # переопределяем метод pop
        return super(Queue, self).pop(0)


if __name__ == '__main__':
    print('Первый экземпляр')
    queue_1 = Queue([2, 3, 5])  # создаём экземплял класса Queue
    print(queue_1)
    queue_1.append(1)  # добавлям новый элемент в конец очереди
    print(queue_1)
    print(queue_1.pop())  # выводим первый элемент очереди и удаляем его
    print(queue_1)
    # аналогично с остальными 2 экземплярами
    print('Второй экземпляр')
    queue_2 = Queue()
    queue_2.append(2)
    print(queue_2)
    queue_2.append('b')
    print(queue_2)
    print(queue_2.pop())
    print(queue_2)
    print('Третий экземпляр')
    queue_3 = Queue([i*i for i in range(4)])
    print(queue_3)
    queue_3.append(10)
    print(queue_3)
    print(queue_3.pop())
    print(queue_3)
