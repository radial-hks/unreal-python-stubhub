## FixedArray Objects

```python
class FixedArray(_WrapperBase, MutableSequence[_ElemType])
```

Type for all Unreal exposed fixed-array instances

<a id="unreal.FixedArray.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: type, len: int) -> None
```

<a id="unreal.FixedArray.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(index: int, value: _ElemType) -> None
```

<a id="unreal.FixedArray.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(index: int) -> _ElemType
```

<a id="unreal.FixedArray.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, *args)
```

__class_getitem__(cls, item: _ElemType) -- implemented for type hinting purpose only

<a id="unreal.FixedArray.cast"></a>

#### cast

```python
@classmethod
def cast(cls, type: Type[_ElemType], obj: object) -> FixedArray[_ElemType]
```

cast(cls, type: Type[_ElemType], obj: object) -> FixedArray[_ElemType] -- cast the given object to this Unreal fixed-array type

<a id="unreal.FixedArray.__copy__"></a>

#### \_\_copy\_\_

```python
def __copy__() -> FixedArray[_ElemType]
```

__copy__(self) -> FixedArray[_ElemType] -- copy this Unreal fixed-array

<a id="unreal.FixedArray.copy"></a>

#### copy

```python
def copy() -> FixedArray[_ElemType]
```

copy(self) -> FixedArray[_ElemType] -- copy this Unreal fixed-array

<a id="unreal.Set"></a>