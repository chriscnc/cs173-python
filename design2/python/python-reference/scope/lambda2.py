f2 = lambda x: (lambda : lambda y: x + y)()
inc = f2(1)
plus10 = f2(10)
___assertEqual(inc(1), 2)
___assertEqual(plus10(5), 15)
