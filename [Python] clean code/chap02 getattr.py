class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __getattr__(self, attr):
        if attr.startswith('fallback_'):
            name = attr.replace('fallback_', '')
            return f'[fallback resolved] {name}'
        raise AttributeError(f'{self.__class__.__name__}에는 {attr} 속성이 없음')

dyn = DynamicAttributes('value')
print(dyn.attribute) # value
print(dyn.fallback_test) # [fallback resolved] test
print(getattr(dyn, 'something', 'default')) # default
print(getattr(dyn, 'attribute', 'default')) # value
print(dyn.no_attr) # 에러발생