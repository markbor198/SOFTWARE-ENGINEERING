# my_zip.py

def my_zip(*iterables):
    iterables = [iter(i) for i in iterables]
    End = object()
    while iterables:
        zip_it = tuple(next(i,End) for i in iterables)
        if End in zip_it:
            break
        yield zip_it


# tests for my_zip
def test_zip () :
   print("my_zip()")
   assert list(my_zip()) == []
   assert list(my_zip([])) == []
   assert list(my_zip((), ())) == []
   assert list(my_zip([2, 3])) == [(2,), (3,)]
   assert list(my_zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
   assert list(my_zip([2, 3, 4], [5, 6, 7])) == [(2, 5), (3, 6), (4, 7)]
   print("my_zip()")

test_zip()
#print(*my_zip([1,2,3,4],"test","abcd"))
