class American(object):
    '''An american class'''
    pass

class NewYorker(American):
    '''A NewYorker class subclass of American class'''
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(American.__doc__)
print(NewYorker.__doc__)
print(anAmerican)
print(aNewYorker)
