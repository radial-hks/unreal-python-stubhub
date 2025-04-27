## MotionMatchingBlueprintBlendSettings Objects

```python
class MotionMatchingBlueprintBlendSettings(StructBase)
```

Motion Matching Blueprint Blend Settings

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: MotionMatchingAnimNodeLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_option`` (AlphaBlendOption):  [Read-Write]
- ``blend_profile`` (BlendProfile):  [Read-Write]
- ``blend_time`` (float):  [Read-Write]
- ``use_inertial_blend`` (bool):  [Read-Write]

<a id="unreal.MotionMatchingBlueprintBlendSettings.__init__"></a>

#### __init__

```python
def __init__(blend_time: float = 0.000000,
             blend_profile: BlendProfile = None,
             blend_option: AlphaBlendOption = AlphaBlendOption.LINEAR,
             use_inertial_blend: bool = False) -> None
```

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_time"></a>

#### blend_time

```python
@property
def blend_time() -> float
```

(float):  [Read-Write]

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_time"></a>

#### blend_time

```python
@blend_time.setter
def blend_time(value: float) -> None
```

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_profile"></a>

#### blend_profile

```python
@property
def blend_profile() -> BlendProfile
```

(BlendProfile):  [Read-Write]

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_profile"></a>

#### blend_profile

```python
@blend_profile.setter
def blend_profile(value: BlendProfile) -> None
```

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_option"></a>

#### blend_option

```python
@property
def blend_option() -> AlphaBlendOption
```

(AlphaBlendOption):  [Read-Write]

<a id="unreal.MotionMatchingBlueprintBlendSettings.blend_option"></a>

#### blend_option

```python
@blend_option.setter
def blend_option(value: AlphaBlendOption) -> None
```

<a id="unreal.MotionMatchingBlueprintBlendSettings.use_inertial_blend"></a>

#### use_inertial_blend

```python
@property
def use_inertial_blend() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MotionMatchingBlueprintBlendSettings.use_inertial_blend"></a>

#### use_inertial_blend

```python
@use_inertial_blend.setter
def use_inertial_blend(value: bool) -> None
```

<a id="unreal.MotionMatchingAnimNodeReference"></a>