## FrameNumberRangeBound Objects

```python
class FrameNumberRangeBound(StructBase)
```

Defines a single bound for a range of frame numbers.
note: This is a mirror of TRangeBound<FFrameNumber>, defined in RangeBound.h
note: Fields are private to match the C++ declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (RangeBoundTypes):  [Read-Write]
- ``value`` (FrameNumber):  [Read-Write]

<a id="unreal.FrameNumberRangeBound.__init__"></a>

#### __init__

```python
def __init__(type: RangeBoundTypes = RangeBoundTypes.EXCLUSIVE,
             value: FrameNumber = [0]) -> None
```

<a id="unreal.FrameNumberRangeBound.type"></a>

#### type

```python
@property
def type() -> RangeBoundTypes
```

(RangeBoundTypes):  [Read-Write]

<a id="unreal.FrameNumberRangeBound.type"></a>

#### type

```python
@type.setter
def type(value: RangeBoundTypes) -> None
```

<a id="unreal.FrameNumberRangeBound.value"></a>

#### value

```python
@property
def value() -> FrameNumber
```

(FrameNumber):  [Read-Write]

<a id="unreal.FrameNumberRangeBound.value"></a>

#### value

```python
@value.setter
def value(value: FrameNumber) -> None
```

<a id="unreal.FrameRate"></a>