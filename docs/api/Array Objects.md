## Array Objects

```python
class Array(_WrapperBase, MutableSequence[_ElemType])
```

Type for all Unreal exposed array instances

<a id="unreal.Array.__init__"></a>

#### __init__

```python
def __init__(type: type) -> None
```

<a id="unreal.Array.__setitem__"></a>

#### __setitem__

```python
def __setitem__(index: int, value: _ElemType) -> None
```

<a id="unreal.Array.__getitem__"></a>

#### __getitem__

```python
def __getitem__(index: int) -> _ElemType
```

<a id="unreal.Array.__class_getitem__"></a>

#### __class_getitem__

```python
@classmethod
def __class_getitem__(cls, *args)
```

__class_getitem__(cls, item: _ElemType) -- implemented for type hinting purpose only

<a id="unreal.Array.cast"></a>

#### cast

```python
@classmethod
def cast(cls, type: Type[_ElemType], obj: object) -> Array[_ElemType]
```

cast(cls, type: Type[_ElemType], obj: object) -> Array[_ElemType] -- cast the given object to this Unreal array type

<a id="unreal.Array.__copy__"></a>

#### __copy__

```python
def __copy__() -> Array[_ElemType]
```

__copy__(self) -> Array[_ElemType] -- copy this Unreal array

<a id="unreal.Array.copy"></a>

#### copy

```python
def copy() -> Array[_ElemType]
```

copy(self) -> Array[_ElemType] -- copy this Unreal array

<a id="unreal.Array.append"></a>

#### append

```python
def append(value: _ElemType) -> None
```

append(self, value: _ElemType) -> None -- append the given value to the end of this Unreal array (equivalent to TArray::Add in C++)

<a id="unreal.Array.count"></a>

#### count

```python
def count(value: _ElemType) -> int
```

count(self, value: _ElemType) -> int -- return the number of times that value appears in this this Unreal array

<a id="unreal.Array.extend"></a>

#### extend

```python
def extend(values: Iterable[_ElemType]) -> None
```

extend(self, values: Iterable[_ElemType]) -> None -- extend this Unreal array by appending elements from the given iterable (equivalent to TArray::Append in C++)

<a id="unreal.Array.index"></a>

#### index

```python
def index(value: _ElemType, start: int = 0, stop: int = -1) -> int
```

index(self, value: _ElemType, start: int = 0, stop: int = -1) -> int -- get the index of the first matching value in this Unreal array, or raise ValueError if missing (equivalent to TArray::IndexOfByKey in C++)

<a id="unreal.Array.insert"></a>

#### insert

```python
def insert(index: int, value: _ElemType) -> None
```

insert(self, index: int, value: _ElemType) -> None -- insert the given value at the given index in this Unreal array

<a id="unreal.Array.pop"></a>

#### pop

```python
def pop(index: int = -1) -> _ElemType
```

pop(self, index: int = -1) -> _ElemType -- remove and return the value at the given index in this Unreal array, or raise IndexError if the index is out-of-bounds

<a id="unreal.Array.clear"></a>

#### clear

```python
def clear() -> None
```

clear(self) -> None -- remove all values from this Unreal array

<a id="unreal.Array.remove"></a>

#### remove

```python
def remove(value: _ElemType) -> None
```

remove(self, value: _ElemType) -> None -- remove the first matching value in this Unreal array, or raise ValueError if missing

<a id="unreal.Array.reverse"></a>

#### reverse

```python
def reverse() -> None
```

reverse(self) -> None -- reverse this Unreal array in-place

<a id="unreal.Array.sort"></a>

#### sort

```python
def sort(key: Optional[Callable[[_ElemType], object]] = None,
         reverse: bool = False) -> None
```

sort(self, key: Optional[Callable[[_ElemType], object]]=None, reverse: bool=False) -> None -- stable sort this Unreal array in-place

<a id="unreal.Array.resize"></a>

#### resize

```python
def resize(len: int) -> None
```

resize(self, len: int) -> None -- resize this Unreal array to hold the given number of elements

<a id="unreal.FixedArray"></a>