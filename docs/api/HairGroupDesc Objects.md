## HairGroupDesc Objects

```python
class HairGroupDesc(StructBase)
```

Note: If a new field is added to this struct, think to update GroomComponentDestailsCustomization.cpp to handle override flags

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomDesc.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hair_length_scale`` (float):  [Read-Write] When enabled, Length Scale allow to scale the length of the hair.
- ``hair_length_scale_override`` (bool):  [Read-Write]
- ``hair_raytracing_radius_scale`` (float):  [Read-Write] Scale the hair geometry radius for ray tracing effects (e.g. shadow)
- ``hair_raytracing_radius_scale_override`` (bool):  [Read-Write]
- ``hair_root_scale`` (float):  [Read-Write] Scale the hair width at the root
- ``hair_root_scale_override`` (bool):  [Read-Write]
- ``hair_shadow_density`` (float):  [Read-Write] Override the hair shadow density factor (unit less).
- ``hair_shadow_density_override`` (bool):  [Read-Write]
- ``hair_tip_scale`` (float):  [Read-Write] Scale the hair width at the tip
- ``hair_tip_scale_override`` (bool):  [Read-Write]
- ``hair_width`` (float):  [Read-Write] Hair width (in centimeters)
- ``hair_width_override`` (bool):  [Read-Write]
- ``lod_bias`` (float):  [Read-Write] Bias the selected LOD. A value >0 will progressively select lower detailed lods. Used when r.HairStrands.Cluster.Culling = 1.
- ``scatter_scene_lighting`` (bool):  [Read-Write] Light hair with the scene color. This is used for vellus/short hair to bring light from the surrounding surface, like skin.
- ``scatter_scene_lighting_override`` (bool):  [Read-Write]
- ``use_hair_raytracing_geometry`` (bool):  [Read-Write] Enable hair strands geomtry for raytracing
- ``use_hair_raytracing_geometry_override`` (bool):  [Read-Write]
- ``use_stable_rasterization`` (bool):  [Read-Write] Insure the hair does not alias. When enable, group of hairs might appear thicker. Isolated hair should remain thin.
- ``use_stable_rasterization_override`` (bool):  [Read-Write]

<a id="unreal.HairGroupDesc.__init__"></a>

#### __init__

```python
def __init__(hair_width: float = 0.000000,
             hair_width_override: bool = False,
             hair_root_scale: float = 0.000000,
             hair_root_scale_override: bool = False,
             hair_tip_scale: float = 0.000000,
             hair_tip_scale_override: bool = False,
             hair_shadow_density: float = 0.000000,
             hair_shadow_density_override: bool = False,
             hair_raytracing_radius_scale: float = 0.000000,
             hair_raytracing_radius_scale_override: bool = False,
             use_hair_raytracing_geometry: bool = False,
             use_hair_raytracing_geometry_override: bool = False,
             lod_bias: float = 0.000000,
             use_stable_rasterization: bool = False,
             use_stable_rasterization_override: bool = False,
             scatter_scene_lighting: bool = False,
             scatter_scene_lighting_override: bool = False,
             hair_length_scale: float = 0.000000,
             hair_length_scale_override: bool = False) -> None
```

<a id="unreal.HairGroupDesc.hair_width"></a>

#### hair_width

```python
@property
def hair_width() -> float
```

(float):  [Read-Write] Hair width (in centimeters)

<a id="unreal.HairGroupDesc.hair_width"></a>

#### hair_width

```python
@hair_width.setter
def hair_width(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_width_override"></a>

#### hair_width_override

```python
@property
def hair_width_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_width_override"></a>

#### hair_width_override

```python
@hair_width_override.setter
def hair_width_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.hair_root_scale"></a>

#### hair_root_scale

```python
@property
def hair_root_scale() -> float
```

(float):  [Read-Write] Scale the hair width at the root

<a id="unreal.HairGroupDesc.hair_root_scale"></a>

#### hair_root_scale

```python
@hair_root_scale.setter
def hair_root_scale(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_root_scale_override"></a>

#### hair_root_scale_override

```python
@property
def hair_root_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_root_scale_override"></a>

#### hair_root_scale_override

```python
@hair_root_scale_override.setter
def hair_root_scale_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.hair_tip_scale"></a>

#### hair_tip_scale

```python
@property
def hair_tip_scale() -> float
```

(float):  [Read-Write] Scale the hair width at the tip

<a id="unreal.HairGroupDesc.hair_tip_scale"></a>

#### hair_tip_scale

```python
@hair_tip_scale.setter
def hair_tip_scale(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_tip_scale_override"></a>

#### hair_tip_scale_override

```python
@property
def hair_tip_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_tip_scale_override"></a>

#### hair_tip_scale_override

```python
@hair_tip_scale_override.setter
def hair_tip_scale_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.hair_shadow_density"></a>

#### hair_shadow_density

```python
@property
def hair_shadow_density() -> float
```

(float):  [Read-Write] Override the hair shadow density factor (unit less).

<a id="unreal.HairGroupDesc.hair_shadow_density"></a>

#### hair_shadow_density

```python
@hair_shadow_density.setter
def hair_shadow_density(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_shadow_density_override"></a>

#### hair_shadow_density_override

```python
@property
def hair_shadow_density_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_shadow_density_override"></a>

#### hair_shadow_density_override

```python
@hair_shadow_density_override.setter
def hair_shadow_density_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.hair_raytracing_radius_scale"></a>

#### hair_raytracing_radius_scale

```python
@property
def hair_raytracing_radius_scale() -> float
```

(float):  [Read-Write] Scale the hair geometry radius for ray tracing effects (e.g. shadow)

<a id="unreal.HairGroupDesc.hair_raytracing_radius_scale"></a>

#### hair_raytracing_radius_scale

```python
@hair_raytracing_radius_scale.setter
def hair_raytracing_radius_scale(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_raytracing_radius_scale_override"></a>

#### hair_raytracing_radius_scale_override

```python
@property
def hair_raytracing_radius_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_raytracing_radius_scale_override"></a>

#### hair_raytracing_radius_scale_override

```python
@hair_raytracing_radius_scale_override.setter
def hair_raytracing_radius_scale_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.use_hair_raytracing_geometry"></a>

#### use_hair_raytracing_geometry

```python
@property
def use_hair_raytracing_geometry() -> bool
```

(bool):  [Read-Write] Enable hair strands geomtry for raytracing

<a id="unreal.HairGroupDesc.use_hair_raytracing_geometry"></a>

#### use_hair_raytracing_geometry

```python
@use_hair_raytracing_geometry.setter
def use_hair_raytracing_geometry(value: bool) -> None
```

<a id="unreal.HairGroupDesc.use_hair_raytracing_geometry_override"></a>

#### use_hair_raytracing_geometry_override

```python
@property
def use_hair_raytracing_geometry_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.use_hair_raytracing_geometry_override"></a>

#### use_hair_raytracing_geometry_override

```python
@use_hair_raytracing_geometry_override.setter
def use_hair_raytracing_geometry_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.lod_bias"></a>

#### lod_bias

```python
@property
def lod_bias() -> float
```

(float):  [Read-Write] Bias the selected LOD. A value >0 will progressively select lower detailed lods. Used when r.HairStrands.Cluster.Culling = 1.

<a id="unreal.HairGroupDesc.lod_bias"></a>

#### lod_bias

```python
@lod_bias.setter
def lod_bias(value: float) -> None
```

<a id="unreal.HairGroupDesc.use_stable_rasterization"></a>

#### use_stable_rasterization

```python
@property
def use_stable_rasterization() -> bool
```

(bool):  [Read-Only] Insure the hair does not alias. When enable, group of hairs might appear thicker. Isolated hair should remain thin.

<a id="unreal.HairGroupDesc.use_stable_rasterization_override"></a>

#### use_stable_rasterization_override

```python
@property
def use_stable_rasterization_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.use_stable_rasterization_override"></a>

#### use_stable_rasterization_override

```python
@use_stable_rasterization_override.setter
def use_stable_rasterization_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.scatter_scene_lighting"></a>

#### scatter_scene_lighting

```python
@property
def scatter_scene_lighting() -> bool
```

(bool):  [Read-Only] Light hair with the scene color. This is used for vellus/short hair to bring light from the surrounding surface, like skin.

<a id="unreal.HairGroupDesc.scatter_scene_lighting_override"></a>

#### scatter_scene_lighting_override

```python
@property
def scatter_scene_lighting_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.scatter_scene_lighting_override"></a>

#### scatter_scene_lighting_override

```python
@scatter_scene_lighting_override.setter
def scatter_scene_lighting_override(value: bool) -> None
```

<a id="unreal.HairGroupDesc.hair_length_scale"></a>

#### hair_length_scale

```python
@property
def hair_length_scale() -> float
```

(float):  [Read-Write] When enabled, Length Scale allow to scale the length of the hair.

<a id="unreal.HairGroupDesc.hair_length_scale"></a>

#### hair_length_scale

```python
@hair_length_scale.setter
def hair_length_scale(value: float) -> None
```

<a id="unreal.HairGroupDesc.hair_length_scale_override"></a>

#### hair_length_scale_override

```python
@property
def hair_length_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGroupDesc.hair_length_scale_override"></a>

#### hair_length_scale_override

```python
@hair_length_scale_override.setter
def hair_length_scale_override(value: bool) -> None
```

<a id="unreal.HairGroupLODInfo"></a>