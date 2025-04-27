## FloatRange Objects

```python
class FloatRange(StructBase)
```

A contiguous set of floats described by lower and upper bound values.
note: This is a mirror of TRange<float>, defined in Range.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lower_bound`` (FloatRangeBound):  [Read-Write] Holds the range's lower bound.
- ``upper_bound`` (FloatRangeBound):  [Read-Write] Holds the range's upper bound.

<a id="unreal.FloatRange.__init__"></a>

#### __init__

```python
def __init__(
    lower_bound: FloatRangeBound = [RangeBoundTypes.EXCLUSIVE, 0.000000],
    upper_bound: FloatRangeBound = [RangeBoundTypes.EXCLUSIVE,
                                    0.000000]) -> None
```

<a id="unreal.FloatRange.lower_bound"></a>

#### lower_bound

```python
@property
def lower_bound() -> FloatRangeBound
```

(FloatRangeBound):  [Read-Write] Holds the range's lower bound.

<a id="unreal.FloatRange.lower_bound"></a>

#### lower_bound

```python
@lower_bound.setter
def lower_bound(value: FloatRangeBound) -> None
```

<a id="unreal.FloatRange.upper_bound"></a>

#### upper_bound

```python
@property
def upper_bound() -> FloatRangeBound
```

(FloatRangeBound):  [Read-Write] Holds the range's upper bound.

<a id="unreal.FloatRange.upper_bound"></a>

#### upper_bound

```python
@upper_bound.setter
def upper_bound(value: FloatRangeBound) -> None
```

<a id="unreal.FloatRangeBound"></a>