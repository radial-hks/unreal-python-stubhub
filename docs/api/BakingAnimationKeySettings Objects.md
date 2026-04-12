## BakingAnimationKeySettings Objects

```python
class BakingAnimationKeySettings(StructBase)
```

Baking Animation Key Settings

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: BakingAnimationKeySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``baking_key_settings`` (BakingKeySettings):  [Read-Write]
- ``end_frame`` (FrameNumber):  [Read-Write]
- ``frame_increment`` (int32):  [Read-Write]
- ``reduce_keys`` (bool):  [Read-Write]
- ``start_frame`` (FrameNumber):  [Read-Write]
- ``tolerance`` (float):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        start_frame: FrameNumber = [0],
        end_frame: FrameNumber = [0],
        baking_key_settings: BakingKeySettings = BakingKeySettings.KEYS_ONLY,
        frame_increment: int = 0,
        reduce_keys: bool = False,
        tolerance: float = 0.000000) -> None
```

<a id="unreal.BakingAnimationKeySettings.start_frame"></a>

#### start\_frame

```python
@property
def start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.start_frame"></a>

#### start\_frame

```python
@start_frame.setter
def start_frame(value: FrameNumber) -> None
```

<a id="unreal.BakingAnimationKeySettings.end_frame"></a>

#### end\_frame

```python
@property
def end_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.end_frame"></a>

#### end\_frame

```python
@end_frame.setter
def end_frame(value: FrameNumber) -> None
```

<a id="unreal.BakingAnimationKeySettings.baking_key_settings"></a>

#### baking\_key\_settings

```python
@property
def baking_key_settings() -> BakingKeySettings
```

(BakingKeySettings):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.baking_key_settings"></a>

#### baking\_key\_settings

```python
@baking_key_settings.setter
def baking_key_settings(value: BakingKeySettings) -> None
```

<a id="unreal.BakingAnimationKeySettings.frame_increment"></a>

#### frame\_increment

```python
@property
def frame_increment() -> int
```

(int32):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.frame_increment"></a>

#### frame\_increment

```python
@frame_increment.setter
def frame_increment(value: int) -> None
```

<a id="unreal.BakingAnimationKeySettings.reduce_keys"></a>

#### reduce\_keys

```python
@property
def reduce_keys() -> bool
```

(bool):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.reduce_keys"></a>

#### reduce\_keys

```python
@reduce_keys.setter
def reduce_keys(value: bool) -> None
```

<a id="unreal.BakingAnimationKeySettings.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.BakingAnimationKeySettings.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.ControlToTransformMappings"></a>