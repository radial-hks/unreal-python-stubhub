## UnderwaterPostProcessSettings Objects

```python
class UnderwaterPostProcessSettings(StructBase)
```

Underwater Post Process Settings

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBodyComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_radius`` (float):  [Read-Write] World space radius around the volume that is used for blending (only if not unbound).
- ``blend_weight`` (float):  [Read-Write] 0:no effect, 1:full effect
- ``enabled`` (bool):  [Read-Write]
- ``post_process_settings`` (PostProcessSettings):  [Read-Write] List of all post-process settings to use when underwater : note : use UnderwaterPostProcessMaterial for setting the actual post process material.
- ``priority`` (float):  [Read-Write]

<a id="unreal.UnderwaterPostProcessSettings.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             priority: float = 0.000000,
             blend_radius: float = 0.000000,
             blend_weight: float = 0.000000,
             post_process_settings: PostProcessSettings = []) -> None
```

<a id="unreal.UnderwaterPostProcessSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.UnderwaterPostProcessSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.UnderwaterPostProcessSettings.priority"></a>

#### priority

```python
@property
def priority() -> float
```

(float):  [Read-Write]

<a id="unreal.UnderwaterPostProcessSettings.priority"></a>

#### priority

```python
@priority.setter
def priority(value: float) -> None
```

<a id="unreal.UnderwaterPostProcessSettings.blend_radius"></a>

#### blend_radius

```python
@property
def blend_radius() -> float
```

(float):  [Read-Write] World space radius around the volume that is used for blending (only if not unbound).

<a id="unreal.UnderwaterPostProcessSettings.blend_radius"></a>

#### blend_radius

```python
@blend_radius.setter
def blend_radius(value: float) -> None
```

<a id="unreal.UnderwaterPostProcessSettings.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] 0:no effect, 1:full effect

<a id="unreal.UnderwaterPostProcessSettings.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.UnderwaterPostProcessSettings.post_process_settings"></a>

#### post_process_settings

```python
@property
def post_process_settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write] List of all post-process settings to use when underwater : note : use UnderwaterPostProcessMaterial for setting the actual post process material.

<a id="unreal.UnderwaterPostProcessSettings.post_process_settings"></a>

#### post_process_settings

```python
@post_process_settings.setter
def post_process_settings(value: PostProcessSettings) -> None
```

<a id="unreal.WaterBodyHeightmapSettings"></a>