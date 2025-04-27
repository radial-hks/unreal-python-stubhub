## Int32RangeBound Objects

```python
class Int32RangeBound(StructBase)
```

Defines a single bound for a range of values.
note: This is a mirror of TRangeBound<int32>, defined in RangeBound.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (RangeBoundTypes):  [Read-Write] Holds the type of the bound.
- ``value`` (int32):  [Read-Write] Holds the bound's value.

<a id="unreal.Int32RangeBound.__init__"></a>

#### __init__

```python
def __init__(type: RangeBoundTypes = RangeBoundTypes.EXCLUSIVE,
             value: int = 0) -> None
```

<a id="unreal.Int32RangeBound.type"></a>

#### type

```python
@property
def type() -> RangeBoundTypes
```

(RangeBoundTypes):  [Read-Write] Holds the type of the bound.

<a id="unreal.Int32RangeBound.type"></a>

#### type

```python
@type.setter
def type(value: RangeBoundTypes) -> None
```

<a id="unreal.Int32RangeBound.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write] Holds the bound's value.

<a id="unreal.Int32RangeBound.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.InterpCurveFloat"></a>