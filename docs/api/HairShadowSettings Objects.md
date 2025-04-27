## HairShadowSettings Objects

```python
class HairShadowSettings(StructBase)
```

Hair Shadow Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetRendering.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hair_raytracing_radius_scale`` (float):  [Read-Write] Scale the hair geometry radius for ray tracing effects (e.g. shadow)
- ``hair_shadow_density`` (float):  [Read-Write] Override the hair shadow density factor (unit less).
- ``use_hair_raytracing_geometry`` (bool):  [Read-Write] Enable hair strands geomtry for raytracing
- ``voxelize`` (bool):  [Read-Write] Enable stands voxelize for casting shadow and environment occlusion

<a id="unreal.HairShadowSettings.__init__"></a>

#### __init__

```python
def __init__(hair_shadow_density: float = 0.000000,
             hair_raytracing_radius_scale: float = 0.000000,
             use_hair_raytracing_geometry: bool = False,
             voxelize: bool = False) -> None
```

<a id="unreal.HairShadowSettings.hair_shadow_density"></a>

#### hair_shadow_density

```python
@property
def hair_shadow_density() -> float
```

(float):  [Read-Write] Override the hair shadow density factor (unit less).

<a id="unreal.HairShadowSettings.hair_shadow_density"></a>

#### hair_shadow_density

```python
@hair_shadow_density.setter
def hair_shadow_density(value: float) -> None
```

<a id="unreal.HairShadowSettings.hair_raytracing_radius_scale"></a>

#### hair_raytracing_radius_scale

```python
@property
def hair_raytracing_radius_scale() -> float
```

(float):  [Read-Write] Scale the hair geometry radius for ray tracing effects (e.g. shadow)

<a id="unreal.HairShadowSettings.hair_raytracing_radius_scale"></a>

#### hair_raytracing_radius_scale

```python
@hair_raytracing_radius_scale.setter
def hair_raytracing_radius_scale(value: float) -> None
```

<a id="unreal.HairShadowSettings.use_hair_raytracing_geometry"></a>

#### use_hair_raytracing_geometry

```python
@property
def use_hair_raytracing_geometry() -> bool
```

(bool):  [Read-Write] Enable hair strands geomtry for raytracing

<a id="unreal.HairShadowSettings.use_hair_raytracing_geometry"></a>

#### use_hair_raytracing_geometry

```python
@use_hair_raytracing_geometry.setter
def use_hair_raytracing_geometry(value: bool) -> None
```

<a id="unreal.HairShadowSettings.voxelize"></a>

#### voxelize

```python
@property
def voxelize() -> bool
```

(bool):  [Read-Write] Enable stands voxelize for casting shadow and environment occlusion

<a id="unreal.HairShadowSettings.voxelize"></a>

#### voxelize

```python
@voxelize.setter
def voxelize(value: bool) -> None
```

<a id="unreal.HairAdvancedRenderingSettings"></a>