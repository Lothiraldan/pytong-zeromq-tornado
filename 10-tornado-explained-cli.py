class Return(Exception):
    pass

class Task(object):
    def __init__(self, task):
        self.task = task
    def __call__(self):
        return self.task()

def some_task():
    return 42

def generator():
    raise Return((yield Task(some_task)))

gen = generator()
print generator
# <generator object get at 0x110811dc0>
# C'est un générateur, consommons-le !
task = next(gen)
print task
# <__main__.Task object at 0x110a42bd0>
# C'est une task, exécutons-la !
result = task()
print result
# 42
# Renvoyons le résultat au générateur
gen.send(result)
Return                                    Traceback (most recent call last)
<ipython-input-163-b5ca476de253> in <module>()
----> 1 gen.send(result)

<ipython-input-162-0f4b6d0ad93b> in generator()
     17
     18 def generator():
---> 19     raise Return((yield Task(some_task)))
     20
     21

Return: 42
