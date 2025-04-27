## LandmassTerrainCarvingSettings Objects

```python
class LandmassTerrainCarvingSettings(StructBase)
```

Landmass Terrain Carving Settings

**C++ Source:**

- **Plugin**: Landmass
- **Module**: Landmass
- **File**: TerrainCarvingSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_mode`` (BrushBlendType):  [Read-Write]
- ``effects`` (LandmassBrushEffectsList):  [Read-Write]
- ``falloff_settings`` (LandmassFalloffSettings):  [Read-Write]
- ``invert_shape`` (bool):  [Read-Write]
- ``priority`` (int32):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.__init__"></a>

#### __init__

```python
def __init__(blend_mode: BrushBlendType = BrushBlendType.ALPHA_BLEND,
             invert_shape: bool = False,
             falloff_settings: LandmassFalloffSettings = [
                 BrushFalloffMode.ANGLE, 45.000000, 1024.000000, 0.000000,
                 0.000000
             ],
             effects: LandmassBrushEffectsList = [
                 [True, 2], [0.000000, 0.000000, 16.000000, 3.000000],
                 [
                     0.000000, 0.000000, None, -128.000000,
                     [0.000000, 0.000000, 0.000000, 1.000000], 0.000000
                 ], [0.010000, 0.010000],
                 [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]
             ],
             priority: int = 0) -> None
```

<a id="unreal.LandmassTerrainCarvingSettings.blend_mode"></a>

#### blend_mode

```python
@property
def blend_mode() -> BrushBlendType
```

(BrushBlendType):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.blend_mode"></a>

#### blend_mode

```python
@blend_mode.setter
def blend_mode(value: BrushBlendType) -> None
```

<a id="unreal.LandmassTerrainCarvingSettings.invert_shape"></a>

#### invert_shape

```python
@property
def invert_shape() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.invert_shape"></a>

#### invert_shape

```python
@invert_shape.setter
def invert_shape(value: bool) -> None
```

<a id="unreal.LandmassTerrainCarvingSettings.falloff_settings"></a>

#### falloff_settings

```python
@property
def falloff_settings() -> LandmassFalloffSettings
```

(LandmassFalloffSettings):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.falloff_settings"></a>

#### falloff_settings

```python
@falloff_settings.setter
def falloff_settings(value: LandmassFalloffSettings) -> None
```

<a id="unreal.LandmassTerrainCarvingSettings.effects"></a>

#### effects

```python
@property
def effects() -> LandmassBrushEffectsList
```

(LandmassBrushEffectsList):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.effects"></a>

#### effects

```python
@effects.setter
def effects(value: LandmassBrushEffectsList) -> None
```

<a id="unreal.LandmassTerrainCarvingSettings.priority"></a>

#### priority

```python
@property
def priority() -> int
```

(int32):  [Read-Write]

<a id="unreal.LandmassTerrainCarvingSettings.priority"></a>

#### priority

```python
@priority.setter
def priority(value: int) -> None
```

<a id="unreal.ShallowWaterSimulationGrid"></a>