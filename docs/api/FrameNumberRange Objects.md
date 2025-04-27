## FrameNumberRange Objects

```python
class FrameNumberRange(StructBase)
```

A contiguous set of frame numbers described by lower and upper bound values.
note: This is a mirror of TRange<FFrameNumber>, defined in Range.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lower_bound`` (FrameNumberRangeBound):  [Read-Write]
- ``upper_bound`` (FrameNumberRangeBound):  [Read-Write]

<a id="unreal.FrameNumberRange.__init__"></a>

#### __init__

```python
def __init__(
    lower_bound: FrameNumberRangeBound = [RangeBoundTypes.EXCLUSIVE, [0]],
    upper_bound: FrameNumberRangeBound = [RangeBoundTypes.EXCLUSIVE,
                                          [0]]) -> None
```

<a id="unreal.FrameNumberRange.lower_bound"></a>

#### lower_bound

```python
@property
def lower_bound() -> FrameNumberRangeBound
```

(FrameNumberRangeBound):  [Read-Write]

<a id="unreal.FrameNumberRange.lower_bound"></a>

#### lower_bound

```python
@lower_bound.setter
def lower_bound(value: FrameNumberRangeBound) -> None
```

<a id="unreal.FrameNumberRange.upper_bound"></a>

#### upper_bound

```python
@property
def upper_bound() -> FrameNumberRangeBound
```

(FrameNumberRangeBound):  [Read-Write]

<a id="unreal.FrameNumberRange.upper_bound"></a>

#### upper_bound

```python
@upper_bound.setter
def upper_bound(value: FrameNumberRangeBound) -> None
```

<a id="unreal.FrameNumberRangeBound"></a>