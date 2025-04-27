## SubsurfaceProfileStruct Objects

```python
class SubsurfaceProfileStruct(StructBase)
```

struct with all the settings we want in USubsurfaceProfile, separate to make it easer to pass this data around in the engine.

**C++ Source:**

- **Module**: Engine
- **File**: SubsurfaceProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``boundary_color_bleed`` (LinearColor):  [Read-Write]
- ``enable_burley`` (bool):  [Read-Write] Effective only when Burley subsurface scattering is enabled in cmd.
- ``enable_mean_free_path`` (bool):  [Read-Write] Switch to use Mean Free Path, otherwise use diffuse mean free path.
- ``extinction_scale`` (float):  [Read-Write]
- ``falloff_color`` (LinearColor):  [Read-Write] defines the per-channel falloff of the gradients
  produced by the subsurface scattering events, can be used to fine tune the color of the gradients
  (called "falloff" in SeparableSSS, default there: 1, 0.37, 0.3)
  deprecated: Property 'FalloffColor' is deprecated.
- ``ior`` (float):  [Read-Write]
- ``lobe_mix`` (float):  [Read-Write]
- ``mean_free_path_color`` (LinearColor):  [Read-Write] Controls how far light goes into the subsurface in the Red, Green and Blue channel. It is scaled by Mean Free path distance.
- ``mean_free_path_distance`` (float):  [Read-Write] Subsurface mean free path distance in world/unreal units (cm)
- ``normal_scale`` (float):  [Read-Write]
- ``roughness0`` (float):  [Read-Write]
- ``roughness1`` (float):  [Read-Write]
- ``scatter_radius`` (float):  [Read-Write] in world/unreal units (cm)
  deprecated: Property 'ScatterRadius' is deprecated.
- ``scattering_distribution`` (float):  [Read-Write]
- ``subsurface_color`` (LinearColor):  [Read-Write] Specifies the how much of the diffuse light gets into the material,
  can be seen as a per-channel mix factor between the original image,
  and the SSS-filtered image (called "strength" in SeparableSSS, default there: 0.48, 0.41, 0.28)
  deprecated: Property 'SubsurfaceColor' is deprecated.
- ``surface_albedo`` (LinearColor):  [Read-Write] It should match The base color of the corresponding material as much as possible.
- ``tint`` (LinearColor):  [Read-Write] Specifies the how much of the diffuse light gets into the material,
  can be seen as a per-channel mix factor between the original image,
  and the SSS-filtered image. It introduces Non-PBR looks.
- ``transmission_tint_color`` (LinearColor):  [Read-Write] Transmission tint control. It is multiplied on the transmission results. Works only when Burley is enabled.
- ``world_unit_scale`` (float):  [Read-Write] Control the scale of world/unreal units (cm)

<a id="unreal.SubsurfaceProfileStruct.__init__"></a>

#### __init__

```python
def __init__(
    surface_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    mean_free_path_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    mean_free_path_distance: float = 0.000000,
    world_unit_scale: float = 0.000000,
    enable_burley: bool = False,
    enable_mean_free_path: bool = False,
    tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    boundary_color_bleed: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    extinction_scale: float = 0.000000,
    normal_scale: float = 0.000000,
    scattering_distribution: float = 0.000000,
    ior: float = 0.000000,
    roughness0: float = 0.000000,
    roughness1: float = 0.000000,
    lobe_mix: float = 0.000000,
    transmission_tint_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.SubsurfaceProfileStruct.surface_albedo"></a>

#### surface_albedo

```python
@property
def surface_albedo() -> LinearColor
```

(LinearColor):  [Read-Only] It should match The base color of the corresponding material as much as possible.

<a id="unreal.SubsurfaceProfileStruct.mean_free_path_color"></a>

#### mean_free_path_color

```python
@property
def mean_free_path_color() -> LinearColor
```

(LinearColor):  [Read-Only] Controls how far light goes into the subsurface in the Red, Green and Blue channel. It is scaled by Mean Free path distance.

<a id="unreal.SubsurfaceProfileStruct.mean_free_path_distance"></a>

#### mean_free_path_distance

```python
@property
def mean_free_path_distance() -> float
```

(float):  [Read-Only] Subsurface mean free path distance in world/unreal units (cm)

<a id="unreal.SubsurfaceProfileStruct.world_unit_scale"></a>

#### world_unit_scale

```python
@property
def world_unit_scale() -> float
```

(float):  [Read-Only] Control the scale of world/unreal units (cm)

<a id="unreal.SubsurfaceProfileStruct.enable_burley"></a>

#### enable_burley

```python
@property
def enable_burley() -> bool
```

(bool):  [Read-Only] Effective only when Burley subsurface scattering is enabled in cmd.

<a id="unreal.SubsurfaceProfileStruct.enable_mean_free_path"></a>

#### enable_mean_free_path

```python
@property
def enable_mean_free_path() -> bool
```

(bool):  [Read-Only] Switch to use Mean Free Path, otherwise use diffuse mean free path.

<a id="unreal.SubsurfaceProfileStruct.tint"></a>

#### tint

```python
@property
def tint() -> LinearColor
```

(LinearColor):  [Read-Only] Specifies the how much of the diffuse light gets into the material,
can be seen as a per-channel mix factor between the original image,
and the SSS-filtered image. It introduces Non-PBR looks.

<a id="unreal.SubsurfaceProfileStruct.scatter_radius"></a>

#### scatter_radius

```python
@property
def scatter_radius() -> float
```

(float):  [Read-Only] in world/unreal units (cm)
deprecated: Property 'ScatterRadius' is deprecated.

<a id="unreal.SubsurfaceProfileStruct.subsurface_color"></a>

#### subsurface_color

```python
@property
def subsurface_color() -> LinearColor
```

(LinearColor):  [Read-Only] Specifies the how much of the diffuse light gets into the material,
can be seen as a per-channel mix factor between the original image,
and the SSS-filtered image (called "strength" in SeparableSSS, default there: 0.48, 0.41, 0.28)
deprecated: Property 'SubsurfaceColor' is deprecated.

<a id="unreal.SubsurfaceProfileStruct.falloff_color"></a>

#### falloff_color

```python
@property
def falloff_color() -> LinearColor
```

(LinearColor):  [Read-Only] defines the per-channel falloff of the gradients
produced by the subsurface scattering events, can be used to fine tune the color of the gradients
(called "falloff" in SeparableSSS, default there: 1, 0.37, 0.3)
deprecated: Property 'FalloffColor' is deprecated.

<a id="unreal.SubsurfaceProfileStruct.boundary_color_bleed"></a>

#### boundary_color_bleed

```python
@property
def boundary_color_bleed() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.extinction_scale"></a>

#### extinction_scale

```python
@property
def extinction_scale() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.normal_scale"></a>

#### normal_scale

```python
@property
def normal_scale() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.scattering_distribution"></a>

#### scattering_distribution

```python
@property
def scattering_distribution() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.ior"></a>

#### ior

```python
@property
def ior() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.roughness0"></a>

#### roughness0

```python
@property
def roughness0() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.roughness1"></a>

#### roughness1

```python
@property
def roughness1() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.lobe_mix"></a>

#### lobe_mix

```python
@property
def lobe_mix() -> float
```

(float):  [Read-Only]

<a id="unreal.SubsurfaceProfileStruct.transmission_tint_color"></a>

#### transmission_tint_color

```python
@property
def transmission_tint_color() -> LinearColor
```

(LinearColor):  [Read-Only] Transmission tint control. It is multiplied on the transmission results. Works only when Burley is enabled.

<a id="unreal.SingleAnimationPlayData"></a>