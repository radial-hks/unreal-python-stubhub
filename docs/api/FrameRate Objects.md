## FrameRate Objects

```python
class FrameRate(StructBase)
```

A frame rate represented as a fraction comprising 2 integers: a numerator (number of frames), and a denominator (per second).
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\FrameRate.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``denominator`` (int32):  [Read-Write] The denominator of the framerate represented as a number of frames per second (e.g. 1 for 60 fps)
- ``numerator`` (int32):  [Read-Write] The numerator of the framerate represented as a number of frames per second (e.g. 60 for 60 fps)

<a id="unreal.FrameRate.__init__"></a>

#### __init__

```python
def __init__(numerator: int = 0, denominator: int = 1) -> None
```

<a id="unreal.FrameRate.numerator"></a>

#### numerator

```python
@property
def numerator() -> int
```

(int32):  [Read-Write] The numerator of the framerate represented as a number of frames per second (e.g. 60 for 60 fps)

<a id="unreal.FrameRate.numerator"></a>

#### numerator

```python
@numerator.setter
def numerator(value: int) -> None
```

<a id="unreal.FrameRate.denominator"></a>

#### denominator

```python
@property
def denominator() -> int
```

(int32):  [Read-Write] The denominator of the framerate represented as a number of frames per second (e.g. 1 for 60 fps)

<a id="unreal.FrameRate.denominator"></a>

#### denominator

```python
@denominator.setter
def denominator(value: int) -> None
```

<a id="unreal.FrameTime"></a>