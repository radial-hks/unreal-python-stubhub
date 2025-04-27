## WaterBodyWeightmapSettings Objects

```python
class WaterBodyWeightmapSettings(StructBase)
```

Water Body Weightmap Settings

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBodyWeightmapSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edge_offset`` (float):  [Read-Write]
- ``falloff_width`` (float):  [Read-Write]
- ``final_opacity`` (float):  [Read-Write]
- ``midpoint`` (float):  [Read-Write]
- ``modulation_texture`` (Texture2D):  [Read-Write]
- ``texture_influence`` (float):  [Read-Write]
- ``texture_tiling`` (float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.__init__"></a>

#### __init__

```python
def __init__(falloff_width: float = 0.000000,
             edge_offset: float = 0.000000,
             modulation_texture: Texture2D = None,
             texture_tiling: float = 0.000000,
             texture_influence: float = 0.000000,
             midpoint: float = 0.000000,
             final_opacity: float = 0.000000) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.falloff_width"></a>

#### falloff_width

```python
@property
def falloff_width() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.falloff_width"></a>

#### falloff_width

```python
@falloff_width.setter
def falloff_width(value: float) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.edge_offset"></a>

#### edge_offset

```python
@property
def edge_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.edge_offset"></a>

#### edge_offset

```python
@edge_offset.setter
def edge_offset(value: float) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.modulation_texture"></a>

#### modulation_texture

```python
@property
def modulation_texture() -> Texture2D
```

(Texture2D):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.modulation_texture"></a>

#### modulation_texture

```python
@modulation_texture.setter
def modulation_texture(value: Texture2D) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.texture_tiling"></a>

#### texture_tiling

```python
@property
def texture_tiling() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.texture_tiling"></a>

#### texture_tiling

```python
@texture_tiling.setter
def texture_tiling(value: float) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.texture_influence"></a>

#### texture_influence

```python
@property
def texture_influence() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.texture_influence"></a>

#### texture_influence

```python
@texture_influence.setter
def texture_influence(value: float) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.midpoint"></a>

#### midpoint

```python
@property
def midpoint() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.midpoint"></a>

#### midpoint

```python
@midpoint.setter
def midpoint(value: float) -> None
```

<a id="unreal.WaterBodyWeightmapSettings.final_opacity"></a>

#### final_opacity

```python
@property
def final_opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBodyWeightmapSettings.final_opacity"></a>

#### final_opacity

```python
@final_opacity.setter
def final_opacity(value: float) -> None
```

<a id="unreal.WaterCurveSettings"></a>