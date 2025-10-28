
class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


# Clase Node - Nodo de la lista enlazada
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_info(self):
        return self.info


# Interfaz de la Cola (definida como clase base)
class QueueInterface:
    def size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def front(self):
        raise NotImplementedError

    def enqueue(self, info):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError


# Implementación de la Cola con lista enlazada
class Queue(QueueInterface):
    def __init__(self):
        self.top = None
        self.rear = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = self.rear = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_info = self.top.get_info()
        self.top = self.top.get_next()
        self._size -= 1
        if self.is_empty():
            self.rear = None
        return removed_info

    def get_nth(self, pos):
        if pos < 1 or pos > self._size:
            return None
        current = self.top
        index = 1
        while current is not None:
            if index == pos:
                return current.get_info()
            current = current.get_next()
            index += 1
        return None

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self._size}")
        node = self.top
        index = 1
        while node is not None:
            print(f"   ** Element {index}")
            node.get_info().print()
            node = node.get_next()
            index += 1
        print("******************************")
        print()


# Clase TestQueue - Simula el comportamiento de la cola
class TestQueue:
    @staticmethod
    def main():
        queue = Queue()

        # Crear pedidos
        order1 = Order(20, "cust1")
        order2 = Order(30, "cust2")
        order3 = Order(40, "cust3")
        order4 = Order(50, "cust4")

        # Enqueue de los pedidos
        print(">> Encolando pedidos...")
        queue.enqueue(order1)
        queue.enqueue(order2)
        queue.enqueue(order3)
        queue.enqueue(order4)
        queue.print_info()

        # Ver primer elemento sin eliminar
        print(">> Primer elemento (front):")
        front_order = queue.front()
        if front_order:
            front_order.print()

        # Dequeue (eliminar primer elemento)
        print(">> Desencolando un elemento...")
        dequeued_order = queue.dequeue()
        if dequeued_order:
            print("Elemento eliminado:")
            dequeued_order.print()
        queue.print_info()

        # Obtener el 3er elemento sin eliminarlo
        print(">> Obteniendo el 3er elemento sin eliminarlo:")
        nth_order = queue.get_nth(3)
        if nth_order:
            nth_order.print()
        else:
            print("Posición no válida.")


# Ejecutar prueba
if __name__ == "__main__":
    TestQueue.main()