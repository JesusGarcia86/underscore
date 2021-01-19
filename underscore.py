class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        return iterable

_ = Underscore()
print(_.map([1,2,3], lambda x: x*2))

# output [2,4,6]
    
class Underscore:
    def find(self, iterable, callback):
        for val in iterable:
            if callback(val):
                return val

_ = Underscore()
print(_.find([1,2,3,4,5,6], lambda x: x > 4))

# output 5
    
class Underscore:
    def filter(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if callback(val):
                new_arr.append(val)
        return new_arr

_ = Underscore()
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) 

# output [2,4,6]
    
class Underscore:
    def reject(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if not callback(val):
                new_arr.append(val)
        return new_arr

_ = Underscore()
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) 

# output [1,3,5]