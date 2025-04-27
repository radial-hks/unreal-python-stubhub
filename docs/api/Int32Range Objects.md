## Int32Range Objects

```python
class Int32Range(StructBase)
```

A contiguous set of floats described by lower and upper bound values.
note: This is a mirror of TRange<int32>, defined in Range.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lower_bound`` (Int32RangeBound):  [Read-Write] Holds the range's lower bound.
- ``upper_bound`` (Int32RangeBound):  [Read-Write] Holds the range's upper bound.

<a id="unreal.Int32Range.__init__"></a>

#### __init__

```python
def __init__(
        lower_bound: Int32RangeBound = [RangeBoundTypes.EXCLUSIVE, 0],
        upper_bound: Int32RangeBound = [RangeBoundTypes.EXCLUSIVE, 0]) -> None
```

<a id="unreal.Int32Range.lower_bound"></a>

#### lower_bound

```python
@property
def lower_bound() -> Int32RangeBound
```

(Int32RangeBound):  [Read-Write] Holds the range's lower bound.

<a id="unreal.Int32Range.lower_bound"></a>

#### lower_bound

```python
@lower_bound.setter
def lower_bound(value: Int32RangeBound) -> None
```

<a id="unreal.Int32Range.upper_bound"></a>

#### upper_bound

```python
@property
def upper_bound() -> Int32RangeBound
```

(Int32RangeBound):  [Read-Write] Holds the range's upper bound.

<a id="unreal.Int32Range.upper_bound"></a>

#### upper_bound

```python
@upper_bound.setter
def upper_bound(value: Int32RangeBound) -> None
```

<a id="unreal.Int32RangeBound"></a>