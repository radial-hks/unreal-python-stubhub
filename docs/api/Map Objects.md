## Map Objects

```python
class Map(_WrapperBase, MutableMapping[_KeyType, _ValueType])
```

Type for all Unreal exposed map instances

<a id="unreal.Map.__init__"></a>

#### __init__

```python
def __init__(key: type, value: type) -> None
```

<a id="unreal.Map.__setitem__"></a>

#### __setitem__

```python
def __setitem__(key: _KeyType, value: _ValueType) -> None
```

<a id="unreal.Map.__getitem__"></a>

#### __getitem__

```python
def __getitem__(key: _KeyType) -> _ValueType
```

<a id="unreal.Map.__class_getitem__"></a>

#### __class_getitem__

```python
@classmethod
def __class_getitem__(cls, *args)
```

__class_getitem__(cls, item) -- implemented for type hinting purpose only

<a id="unreal.Map.cast"></a>

#### cast

```python
@classmethod
def cast(cls, key: Type[_KeyType], value: Type[_ValueType],
         obj: object) -> Map[_KeyType, _ValueType]
```

cast(cls, key: Type[_KeyType], value: Type[_ValueType], obj: object) -> Map[_KeyType, _ValueType] -- cast the given object to this Unreal map type

<a id="unreal.Map.__copy__"></a>

#### __copy__

```python
def __copy__() -> Map[_KeyType, _ValueType]
```

__copy__(self) -> Map[_KeyType, _ValueType] -- copy this Unreal map

<a id="unreal.Map.copy"></a>

#### copy

```python
def copy() -> Map[_KeyType, _ValueType]
```

copy(self) -> Map[_KeyType, _ValueType] -- copy this Unreal map

<a id="unreal.Map.clear"></a>

#### clear

```python
def clear() -> None
```

clear(self) -> None -- remove all items from this Unreal map

<a id="unreal.Map.fromkeys"></a>

#### fromkeys

```python
@classmethod
def fromkeys(cls, sequence: Iterable[_KeyType],
             value: _ValueType) -> Map[_KeyType, _ValueType]
```

fromkeys(cls, sequence: Iterable[_KeyType], value: _ValueType) -> Map[_KeyType, _ValueType] -- returns a new Unreal map of keys from the sequence using the given value (types are inferred)

<a id="unreal.Map.get"></a>

#### get

```python
def get(key: _KeyType, default: _ValueType = ...) -> _ValueType
```

get(self, key: _KeyType, default: _ValueType=...) -> _ValueType -- x[key] if key in x, otherwise default

<a id="unreal.Map.setdefault"></a>

#### setdefault

```python
def setdefault(key: _KeyType, default: _ValueType = ...) -> _ValueType
```

setdefault(self, key: _KeyType, default: _ValueType=...) -> _ValueType -- set key to default if key not in x and return the value of key

<a id="unreal.Map.pop"></a>

#### pop

```python
def pop(key: _KeyType, default: _ValueType = ...) -> _ValueType
```

pop(self, key: _KeyType, default: _ValueType=...) -> _ValueType -- remove key and return its value, or default if key not present, or raise KeyError if no default

<a id="unreal.Map.popitem"></a>

#### popitem

```python
def popitem() -> Tuple[_KeyType, _ValueType]
```

popitem(self) -> Tuple[_KeyType, _ValueType] -- remove and return an arbitrary pair from this Unreal map, or raise KeyError if the map is empty

<a id="unreal.Map.update"></a>

#### update

```python
def update(
    pairs: Union[Mapping[_KeyType, _ValueType], Iterable[Tuple[_KeyType,
                                                               _ValueType]],
                 Iterable[List[Union[_KeyType, _ValueType]]]]
) -> None
```

update(self, pairs: Union[Mapping[_KeyType, _ValueType], Iterable[Tuple[_KeyType, _ValueType]], Iterable[List[Union[_KeyType, _ValueType]]]]) -> None -- update this Unreal map from the given mapping or sequence pairs type or key->value arguments

<a id="unreal.Map.items"></a>

#### items

```python
def items() -> ItemsView[_KeyType, _ValueType]
```

items(self) -> ItemsView[_KeyType, _ValueType] -- a set-like view of the key->value pairs of this Unreal map

<a id="unreal.Map.keys"></a>

#### keys

```python
def keys() -> KeysView[_KeyType]
```

keys(self) -> KeysView[_KeyType] -- a set-like view of the keys of this Unreal map

<a id="unreal.Map.values"></a>

#### values

```python
def values() -> ValuesView[_ValueType]
```

values(self) -> ValuesView[_ValueType] -- a view of the values of this Unreal map

<a id="unreal.FieldPath"></a>