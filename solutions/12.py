from util import list_factors

# python generator, keep infinitly procuding new values on demand
def triangle_gen():
    t, i = 0, 1
    while True:
        t += i
        i += 1
        yield t


for t in triangle_gen():
    if len(list_factors(t)) > 500:
        print(t)
        break