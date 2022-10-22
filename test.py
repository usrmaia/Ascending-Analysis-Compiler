from stack import Stack, Queue
from grammar import GRAMMAR

"""
q = Queue(999)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q._front) # inicio da fila
print(q.list[q.front]) # inicio da fila

q.dequeue()
print(q)

s = Stack(999)
s.put(1)
s.put(2)
s.put(3)
s.put(4)
s.put(5)
s.get()
print(s.list[s.top])
print(s)
"""
print(GRAMMAR.get("1")[1:])
print(list(reversed(GRAMMAR.get("1")[1:])))