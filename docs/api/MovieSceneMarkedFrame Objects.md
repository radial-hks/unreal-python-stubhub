## MovieSceneMarkedFrame Objects

```python
class MovieSceneMarkedFrame(StructBase)
```

Movie Scene Marked Frame

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneMarkedFrame.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``comment`` (str):  [Read-Write]
- ``custom_color`` (LinearColor):  [Read-Write]
- ``frame_number`` (FrameNumber):  [Read-Write]
- ``is_determinism_fence`` (bool):  [Read-Write] When checked, treat this mark as a fence for evaluation purposes. Fences cannot be crossed in a single evaluation, and force the evaluation to be split into 2 separate parts.
- ``is_inclusive_time`` (bool):  [Read-Write] Defines how this determinism fence determines the previous and next range: when true, the range will be dissected as (X, Y] -> (Y, Z], when false it will be (X, Y) -> [Y, Z].
- ``label`` (str):  [Read-Write]
- ``use_custom_color`` (bool):  [Read-Write]

<a id="unreal.MovieSceneMarkedFrame.__init__"></a>

#### __init__

```python
def __init__(frame_number: FrameNumber = [0],
             label: str = "",
             is_determinism_fence: bool = False,
             is_inclusive_time: bool = False) -> None
```

<a id="unreal.MovieSceneMarkedFrame.frame_number"></a>

#### frame_number

```python
@property
def frame_number() -> FrameNumber
```

(FrameNumber):  [Read-Write]

<a id="unreal.MovieSceneMarkedFrame.frame_number"></a>

#### frame_number

```python
@frame_number.setter
def frame_number(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneMarkedFrame.label"></a>

#### label

```python
@property
def label() -> str
```

(str):  [Read-Write]

<a id="unreal.MovieSceneMarkedFrame.label"></a>

#### label

```python
@label.setter
def label(value: str) -> None
```

<a id="unreal.MovieSceneMarkedFrame.is_determinism_fence"></a>

#### is_determinism_fence

```python
@property
def is_determinism_fence() -> bool
```

(bool):  [Read-Write] When checked, treat this mark as a fence for evaluation purposes. Fences cannot be crossed in a single evaluation, and force the evaluation to be split into 2 separate parts.

<a id="unreal.MovieSceneMarkedFrame.is_determinism_fence"></a>

#### is_determinism_fence

```python
@is_determinism_fence.setter
def is_determinism_fence(value: bool) -> None
```

<a id="unreal.MovieSceneMarkedFrame.is_inclusive_time"></a>

#### is_inclusive_time

```python
@property
def is_inclusive_time() -> bool
```

(bool):  [Read-Write] Defines how this determinism fence determines the previous and next range: when true, the range will be dissected as (X, Y] -> (Y, Z], when false it will be (X, Y) -> [Y, Z].

<a id="unreal.MovieSceneMarkedFrame.is_inclusive_time"></a>

#### is_inclusive_time

```python
@is_inclusive_time.setter
def is_inclusive_time(value: bool) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveParams"></a>