## QualifiedTime Objects

```python
class QualifiedTime(StructBase)
```

A frame time qualified by a frame rate context.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\QualifiedFrameTime.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rate`` (FrameRate):  [Read-Write] The rate that this frame time is in
- ``time`` (FrameTime):  [Read-Write] The frame time

<a id="unreal.QualifiedTime.__init__"></a>

#### __init__

```python
def __init__(frame: FrameNumber = [0],
             frame_rate: FrameRate = [60000, 1],
             sub_frame: float = 0.000000) -> None
```

<a id="unreal.QualifiedTime.time"></a>

#### time

```python
@property
def time() -> FrameTime
```

(FrameTime):  [Read-Write] The frame time

<a id="unreal.QualifiedTime.time"></a>

#### time

```python
@time.setter
def time(value: FrameTime) -> None
```

<a id="unreal.QualifiedTime.rate"></a>

#### rate

```python
@property
def rate() -> FrameRate
```

(FrameRate):  [Read-Write] The rate that this frame time is in

<a id="unreal.QualifiedTime.rate"></a>

#### rate

```python
@rate.setter
def rate(value: FrameRate) -> None
```

<a id="unreal.Quat4f"></a>