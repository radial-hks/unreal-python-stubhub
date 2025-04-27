## FloatRangeBound Objects

```python
class FloatRangeBound(StructBase)
```

Defines a single bound for a range of values.
note: This is a mirror of TRangeBound<float>, defined in RangeBound.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (RangeBoundTypes):  [Read-Write] Holds the type of the bound.
- ``value`` (float):  [Read-Write] Holds the bound's value.

<a id="unreal.FloatRangeBound.__init__"></a>

#### __init__

```python
def __init__(type: RangeBoundTypes = RangeBoundTypes.EXCLUSIVE,
             value: float = 0.000000) -> None
```

<a id="unreal.FloatRangeBound.type"></a>

#### type

```python
@property
def type() -> RangeBoundTypes
```

(RangeBoundTypes):  [Read-Write] Holds the type of the bound.

<a id="unreal.FloatRangeBound.type"></a>

#### type

```python
@type.setter
def type(value: RangeBoundTypes) -> None
```

<a id="unreal.FloatRangeBound.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Holds the bound's value.

<a id="unreal.FloatRangeBound.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.FrameNumber"></a>