# continuator
Continuations in Stackless Python or PyPy.

A continuator is a repeatable generator. Generators can be used for interrupted method processing.

We pickle the generator to make it repeatable. This is only possible in Stackless or PyPy – trying to pickle a generator in CPython will throw an error.
