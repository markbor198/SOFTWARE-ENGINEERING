class my_islice_iterator() :
    def __init__(self, iterable, start = 0, stop = 0):
        self.iterable = iterable
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        bucket = list(self.iterable)
        if len(bucket) == 0:
            raise StopIteration

        if self.start < self.stop:
            new = self.start
            self.start +=1
            return bucket[new]
        else:
            raise StopIteration

def test_my_isslice () :
    #print("isslice generator")    
    
    #assert list(my_islice_generator('', 2, 5))             == [] 
    #assert list(my_islice_generator('ABCDEFG', 2, 5))      == ['C', 'D', 'E'] 
    #assert list(my_islice_generator('ABCDEFG', 2, 7))      == ['C', 'D', 'E', 'F', 'G'] 
    
    print("isslice iterator")   
 
    p = my_islice_iterator('', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p

    assert list(p) == []
    
    p = my_islice_iterator('ABCDEFG', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E'] 

    p = my_islice_iterator('ABCDEFG', 2, 7)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E', 'F', 'G']
    print('passed')
def main():
    test_my_isslice()


main()
