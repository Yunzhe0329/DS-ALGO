from typing import overload, Union, List

@overload
def shout(text: str) -> str: ...
@overload
def shout(text: List[str]) -> List[str]: ...

def shout(text: Union[str, List[str]]) -> Union[str, List[str]]:
    if isinstance(text, str):
        return text.upper()
    elif isinstance(text, list):
        return [t.upper() for t in text]
    else:
        raise TypeError("Invalid input type")
print(shout("hello"))           # 'HELLO'
print(shout(["hi", "there"]))   # ['HI', 'THERE']

