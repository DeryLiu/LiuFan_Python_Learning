# 8.set
'''
set是一种用于保存不重复元素的数据结构。常被用作测试归属性，故其查找的性能十分重要。

Set是python自带的基本数据结构， 有多种初始化方式。
Python的set跟dict的Implementation方式类似， 可以认为set是只有key的dict.

'''
s = set()
s1 = {1, 2, 3}
s.add('shaunwei')
is_exist = 'shaun' in s  # return true
s.remove('shaunwei')


class set(object):

    """
    set() -> new empty set object
    set(iterable) -> new set object

    Build an unordered collection of unique elements.
    """
    def add(self, *args, **kwargs): # real signature unknown
        """ 添加 """
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from this set. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs): # real signature unknown
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs): # real signature unknown
        """ 删除当前set中的所有包含在 new set 里的元素 """
        """ Remove all elements of another set from this set. """
        pass

    def discard(self, *args, **kwargs): # real signature unknown
        """ 移除元素 """
        """
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        pass

    def intersection(self, *args, **kwargs): # real signature unknown
        """ 取交集，新创建一个set """
        """
        Return the intersection of two or more sets as a new set.

        (i.e. elements that are common to all of the sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs): # real signature unknown
        """ 取交集，修改原来set """
        """ Update a set with the intersection of itself and another. """
        pass

    def isdisjoint(self, *args, **kwargs): # real signature unknown
        """ 如果没有交集，返回true  """
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs): # real signature unknown
        """ 是否是子集 """
        """ Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs): # real signature unknown
        """ 是否是父集 """
        """ Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ 移除 """
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ 移除 """
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        pass

    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        """ 差集，创建新对象"""
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        """ 差集，改变原来 """
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs): # real signature unknown
        """ 并集 """
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ 更新 """
        """ Update a set with the union of itself and others. """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x. """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __iand__(self, y): # real signature unknown; restored from __doc__
        """ x.__iand__(y) <==> x&=y """
        pass

    def __init__(self, seq=()): # known special case of set.__init__
        """
        set() -> new empty set object
        set(iterable) -> new set object

        Build an unordered collection of unique elements.
        # (copied from class doc)
        """
        pass

    def __ior__(self, y): # real signature unknown; restored from __doc__
        """ x.__ior__(y) <==> x|=y """
        pass

    def __isub__(self, y): # real signature unknown; restored from __doc__
        """ x.__isub__(y) <==> x-=y """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __ixor__(self, y): # real signature unknown; restored from __doc__
        """ x.__ixor__(y) <==> x^=y """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    __hash__ = None