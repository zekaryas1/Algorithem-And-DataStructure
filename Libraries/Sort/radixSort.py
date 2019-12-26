from Libraries.Stack_Queue_Linkedlist.Stack_And_Queue_With_Node.Queue import Queue


def radixSort(Array):
    numdigit = len(numDigit(Array))

    holder = []
    for i in range(10):
        holder.append(Queue())
    column = 1

    for i in range(numdigit):
        for key in Array:
            place = (key // column) % 10
            holder[place].enQueue(key)

        i = 0
        for bin in holder:
            while not bin.isEmpty():
                Array[i] = bin.deQueue()
                i += 1

        column *= 10
    print(Array)


def numDigit(Array):
    return str(max(Array))


if __name__ == '__main__':
    radixSort([10, 23, 51, 18, 4, 31, 5, 13])
