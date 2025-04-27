## WaterBodyHeightmapSettings Objects

```python
class WaterBodyHeightmapSettings(StructBase)
```

Water Body Heightmap Settings

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBodyHeightmapSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_mode`` (WaterBrushBlendType):  [Read-Write]
- ``effects`` (WaterBrushEffects):  [Read-Write]
- ``falloff_settings`` (WaterFalloffSettings):  [Read-Write]
- ``invert_shape`` (bool):  [Read-Write]

<a id="unreal.WaterBodyHeightmapSettings.__init__"></a>

#### __init__

```python
def __init__(
    blend_mode: WaterBrushBlendType = WaterBrushBlendType.ALPHA_BLEND,
    invert_shape: bool = False,
    falloff_settings: WaterFalloffSettings = [
        WaterBrushFalloffMode.ANGLE, 45.000000, 1024.000000, 0.000000, 0.000000
    ],
    effects: WaterBrushEffects = [
        [True, 2], [0.000000, 0.000000, 16.000000, 3.000000],
        [
            0.000000, 0.000000, None, -128.000000,
            [0.000000, 0.000000, 0.000000, 1.000000], 0.000000
        ], [0.010000, 0.010000],
        [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.WaterBodyHeightmapSettings.blend_mode"></a>

#### blend_mode

```python
@property
def blend_mode() -> WaterBrushBlendType
```

(WaterBrushBlendType):  [Read-Write]

<a id="unreal.WaterBodyHeightmapSettings.blend_mode"></a>

#### blend_mode

```python
@blend_mode.setter
def blend_mode(value: WaterBrushBlendType) -> None
```

<a id="unreal.WaterBodyHeightmapSettings.invert_shape"></a>

#### invert_shape

```python
@property
def invert_shape() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBodyHeightmapSettings.invert_shape"></a>

#### invert_shape

```python
@invert_shape.setter
def invert_shape(value: bool) -> None
```

<a id="unreal.WaterBodyHeightmapSettings.falloff_settings"></a>

#### falloff_settings

```python
@property
def falloff_settings() -> WaterFalloffSettings
```

(WaterFalloffSettings):  [Read-Write]

<a id="unreal.WaterBodyHeightmapSettings.falloff_settings"></a>

#### falloff_settings

```python
@falloff_settings.setter
def falloff_settings(value: WaterFalloffSettings) -> None
```

<a id="unreal.WaterBodyHeightmapSettings.effects"></a>

#### effects

```python
@property
def effects() -> WaterBrushEffects
```

(WaterBrushEffects):  [Read-Write]

<a id="unreal.WaterBodyHeightmapSettings.effects"></a>

#### effects

```python
@effects.setter
def effects(value: WaterBrushEffects) -> None
```

<a id="unreal.WaterBrushEffects"></a>