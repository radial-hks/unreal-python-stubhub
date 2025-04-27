## FrameTime Objects

```python
class FrameTime(StructBase)
```

Represents a time by a context-free frame number, plus a sub frame value in the range [0:1).
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\FrameTime.h
note: The 'SubFrame' field is private to match its C++ class declaration in the header above.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_number`` (FrameNumber):  [Read-Write] Count of frames from start of timing
- ``sub_frame`` (float):  [Read-Write] Time within a frame, always between >= 0 and < 1

<a id="unreal.FrameTime.__init__"></a>

#### __init__

```python
def __init__(frame_number: FrameNumber = [0],
             sub_frame: float = 0.000000) -> None
```

<a id="unreal.FrameTime.frame_number"></a>

#### frame_number

```python
@property
def frame_number() -> FrameNumber
```

(FrameNumber):  [Read-Write] Count of frames from start of timing

<a id="unreal.FrameTime.frame_number"></a>

#### frame_number

```python
@frame_number.setter
def frame_number(value: FrameNumber) -> None
```

<a id="unreal.FrameTime.sub_frame"></a>

#### sub_frame

```python
@property
def sub_frame() -> float
```

(float):  [Read-Write] Time within a frame, always between >= 0 and < 1

<a id="unreal.FrameTime.sub_frame"></a>

#### sub_frame

```python
@sub_frame.setter
def sub_frame(value: float) -> None
```

<a id="unreal.InputDeviceId"></a>