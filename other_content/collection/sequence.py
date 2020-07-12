from collections.abc import Sequence

def use_sequence(seq: Sequence):
    print(f'the type of this sequence is {type(seq)}')
    assert(issubclass(type(seq),Sequence))
    print(f'it\'s length is {len(seq)}' )
    print(f'here it\' repr{repr(seq)}')
    for it in seq:
        print(it)
        
    