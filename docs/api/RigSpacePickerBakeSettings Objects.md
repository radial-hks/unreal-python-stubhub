## RigSpacePickerBakeSettings Objects

```python
class RigSpacePickerBakeSettings(StructBase)
```

Rig Space Picker Bake Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: RigSpacePickerBakeSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_frame`` (FrameNumber):  [Read-Write] DEPRECATED 5.3
  deprecated: Use Settings.EndFrame instead
- ``reduce_keys`` (bool):  [Read-Write] DEPRECATED 5.3
  deprecated: Use Settings.bReduceKeys instead
- ``settings`` (BakingAnimationKeySettings):  [Read-Write]
- ``start_frame`` (FrameNumber):  [Read-Write] DEPRECATED 5.3
  deprecated: Use Settings.StartFrame instead
- ``target_space`` (RigElementKey):  [Read-Write]
- ``tolerance`` (float):  [Read-Write] DEPRECATED 5.3
  deprecated: Use Settings.Tolerance instead

<a id="unreal.RigSpacePickerBakeSettings.__init__"></a>

#### __init__

```python
def __init__(
    target_space: RigElementKey = [RigElementType.NONE, "None"],
    settings: BakingAnimationKeySettings = [[0], [100],
                                            BakingKeySettings.KEYS_ONLY, 1,
                                            False, 0.001000]
) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.target_space"></a>

#### target_space

```python
@property
def target_space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigSpacePickerBakeSettings.target_space"></a>

#### target_space

```python
@target_space.setter
def target_space(value: RigElementKey) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.settings"></a>

#### settings

```python
@property
def settings() -> BakingAnimationKeySettings
```

(BakingAnimationKeySettings):  [Read-Write]

<a id="unreal.RigSpacePickerBakeSettings.settings"></a>

#### settings

```python
@settings.setter
def settings(value: BakingAnimationKeySettings) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.start_frame"></a>

#### start_frame

```python
@property
def start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] DEPRECATED 5.3
deprecated: Use Settings.StartFrame instead

<a id="unreal.RigSpacePickerBakeSettings.start_frame"></a>

#### start_frame

```python
@start_frame.setter
def start_frame(value: FrameNumber) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.end_frame"></a>

#### end_frame

```python
@property
def end_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] DEPRECATED 5.3
deprecated: Use Settings.EndFrame instead

<a id="unreal.RigSpacePickerBakeSettings.end_frame"></a>

#### end_frame

```python
@end_frame.setter
def end_frame(value: FrameNumber) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.reduce_keys"></a>

#### reduce_keys

```python
@property
def reduce_keys() -> bool
```

(bool):  [Read-Write] DEPRECATED 5.3
deprecated: Use Settings.bReduceKeys instead

<a id="unreal.RigSpacePickerBakeSettings.reduce_keys"></a>

#### reduce_keys

```python
@reduce_keys.setter
def reduce_keys(value: bool) -> None
```

<a id="unreal.RigSpacePickerBakeSettings.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write] DEPRECATED 5.3
deprecated: Use Settings.Tolerance instead

<a id="unreal.RigSpacePickerBakeSettings.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.ControlRigSequencerBindingProxy"></a>