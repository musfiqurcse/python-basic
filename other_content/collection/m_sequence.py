from collections.abc import MutableSequence


class CustomModSequence(MutableSequence):

    _list:list = []

    def __repr__(self):
        return self._list.__repr__()

    def _validate(self,value):
        if value % 2 != 0:
            raise ValueError

    def insert(self,idx, val):
        self._validate(val)
        self._list.insert(idx,val)

    def __setitem__(self, idx, val):
        self._validate(val)
        self._list[idx] = val

    def __delitem__(self, idx):
        del self._list[idx]

    
    def __getitem__(self,idx):
        return self._list[idx]

    def __len__(self):
        return len(self._list)
    
