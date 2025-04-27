## Set Objects

```python
class Set(_WrapperBase, MutableSet[_ElemType])
```

Type for all Unreal exposed set instances

<a id="unreal.Set.__init__"></a>

#### __init__

```python
def __init__(type: type) -> None
```

<a id="unreal.Set.__class_getitem__"></a>

#### __class_getitem__

```python
@classmethod
def __class_getitem__(cls, *args)
```

__class_getitem__(cls, item: _ElemType) -- implemented for type hinting purpose only

<a id="unreal.Set.cast"></a>

#### cast

```python
@classmethod
def cast(cls, type: Type[_ElemType], obj: object) -> Set[_ElemType]
```

cast(cls, type: Type[_ElemType], obj: object) -> Set[_ElemType] -- cast the given object to this Unreal set type

<a id="unreal.Set.__copy__"></a>

#### __copy__

```python
def __copy__() -> Set[_ElemType]
```

__copy__(self) -> Set[_ElemType] -- copy this Unreal set

<a id="unreal.Set.copy"></a>

#### copy

```python
def copy() -> Set[_ElemType]
```

copy(self) -> Set[_ElemType] -- copy this Unreal set

<a id="unreal.Set.add"></a>

#### add

```python
def add(value: _ElemType) -> None
```

add(self, value: _ElemType) -> None -- add the given value to this Unreal set if not already present

<a id="unreal.Set.discard"></a>

#### discard

```python
def discard(value: _ElemType) -> None
```

discard(self, value: _ElemType) -> None -- remove the given value from this Unreal set, or do nothing if not present

<a id="unreal.Set.remove"></a>

#### remove

```python
def remove(value: _ElemType) -> None
```

remove(self, value: _ElemType) -> None -- remove the given value from this Unreal set, or raise KeyError if not present

<a id="unreal.Set.pop"></a>

#### pop

```python
def pop() -> _ElemType
```

pop(self) -> _ElemType -- remove and return an arbitrary value from this Unreal set, or raise KeyError if the set is empty

<a id="unreal.Set.clear"></a>

#### clear

```python
def clear() -> None
```

clear(self) -> None -- remove all values from this Unreal set

<a id="unreal.Set.difference"></a>

#### difference

```python
def difference(*iterable: Iterable[_ElemType]) -> Set[_ElemType]
```

difference(self, *iterable: Iterable[_ElemType]) -> Set[_ElemType] -- return the difference between this Unreal set and the other iterables passed for comparison (ie, all values that are in this set but not the others)

<a id="unreal.Set.difference_update"></a>

#### difference_update

```python
def difference_update(*iterables: Iterable[_ElemType]) -> None
```

difference_update(self, *iterables: Iterable[_ElemType]) -> None -- make this set the difference between this Unreal set and the other iterables passed for comparison (ie, all values that are in this set but not the others)

<a id="unreal.Set.intersection"></a>

#### intersection

```python
def intersection(*iterables: Iterable[_ElemType]) -> Set[_ElemType]
```

intersection(self, *iterables: Iterable[_ElemType]) -> Set[_ElemType] -- return the intersection between this Unreal set and the other iterables passed for comparison (ie, values that are common to all of the sets)

<a id="unreal.Set.intersection_update"></a>

#### intersection_update

```python
def intersection_update(*iterables: Iterable[_ElemType]) -> None
```

intersection_update(self, *iterables: Iterable[_ElemType]) -> None -- make this set the intersection between this Unreal set and the other iterables passed for comparison (ie, values that are common to all of the sets)

<a id="unreal.Set.symmetric_difference"></a>

#### symmetric_difference

```python
def symmetric_difference(other: Iterable[_ElemType]) -> Set[_ElemType]
```

symmetric_difference(self, other: Iterable[_ElemType]) -> Set[_ElemType] -- return the symmetric difference between this Unreal set and another (ie, values that are in exactly one of the sets)

<a id="unreal.Set.symmetric_difference_update"></a>

#### symmetric_difference_update

```python
def symmetric_difference_update(other: Iterable[_ElemType]) -> None
```

symmetric_difference_update(self, other: Iterable[_ElemType]) -> None -- make this set the symmetric difference between this Unreal set and another (ie, values that are in exactly one of the sets)

<a id="unreal.Set.union"></a>

#### union

```python
def union(*iterables: Iterable[_ElemType]) -> Set[_ElemType]
```

union(self, *iterables: Iterable[_ElemType]) -> Set[_ElemType] -- return the union between this Unreal set and the other iterables passed for comparison (ie, values that are in any set)

<a id="unreal.Set.update"></a>

#### update

```python
def update(*iterables: Iterable[_ElemType]) -> None
```

update(self, *iterables: Iterable[_ElemType]) -> None -- make this set the union between this Unreal set and the other iterables passed for comparison (ie, values that are in any set)

<a id="unreal.Set.isdisjoint"></a>

#### isdisjoint

```python
def isdisjoint(other: Iterable[_ElemType]) -> bool
```

isdisjoint(self, other: Iterable[_ElemType]) -> bool -- return True if there is a null intersection between this Unreal set and another

<a id="unreal.Set.issubset"></a>

#### issubset

```python
def issubset(other: Iterable[_ElemType]) -> bool
```

issubset(self, other: Iterable[_ElemType]) -> bool -- return True if another set contains this Unreal set

<a id="unreal.Set.issuperset"></a>

#### issuperset

```python
def issuperset(other: Iterable[_ElemType]) -> bool
```

issuperset(self, other: Iterable[_ElemType]) -> bool -- return True if this Unreal set contains another

<a id="unreal.Map"></a>