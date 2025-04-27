## DisplacementFadeRange Objects

```python
class DisplacementFadeRange(StructBase)
```

Displacement Fade Range

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_size_pixels`` (float):  [Read-Write] How large the max displacement should be, in on-screen pixels, when fading out should complete, and displacement
  should be disabled.
  NOTE: This should be a SMALLER number than Start Fade Size.
- ``start_size_pixels`` (float):  [Read-Write] How large the max displacement should be, in on-screen pixels, when beginning to fade out displacement.
  NOTE: This should be a LARGER number than End Fade Size.

<a id="unreal.DisplacementFadeRange.__init__"></a>

#### __init__

```python
def __init__(start_size_pixels: float = 0.000000,
             end_size_pixels: float = 0.000000) -> None
```

<a id="unreal.DisplacementFadeRange.start_size_pixels"></a>

#### start_size_pixels

```python
@property
def start_size_pixels() -> float
```

(float):  [Read-Write] How large the max displacement should be, in on-screen pixels, when beginning to fade out displacement.
NOTE: This should be a LARGER number than End Fade Size.

<a id="unreal.DisplacementFadeRange.start_size_pixels"></a>

#### start_size_pixels

```python
@start_size_pixels.setter
def start_size_pixels(value: float) -> None
```

<a id="unreal.DisplacementFadeRange.end_size_pixels"></a>

#### end_size_pixels

```python
@property
def end_size_pixels() -> float
```

(float):  [Read-Write] How large the max displacement should be, in on-screen pixels, when fading out should complete, and displacement
should be disabled.
NOTE: This should be a SMALLER number than Start Fade Size.

<a id="unreal.DisplacementFadeRange.end_size_pixels"></a>

#### end_size_pixels

```python
@end_size_pixels.setter
def end_size_pixels(value: float) -> None
```

<a id="unreal.CollectionReference"></a>