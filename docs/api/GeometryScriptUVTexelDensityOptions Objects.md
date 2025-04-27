## GeometryScriptUVTexelDensityOptions Objects

```python
class GeometryScriptUVTexelDensityOptions(StructBase)
```

Geometry Script UVTexel Density Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_udim_layout`` (bool):  [Read-Write]
- ``target_pixel_count`` (float):  [Read-Write]
- ``target_world_units`` (float):  [Read-Write]
- ``texel_density_mode`` (GeometryScriptTexelDensityMode):  [Read-Write]
- ``texture_resolution`` (float):  [Read-Write]
- ``udim_resolutions`` (Map[int32, int32]):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.__init__"></a>

#### __init__

```python
def __init__(texel_density_mode:
             GeometryScriptTexelDensityMode = GeometryScriptTexelDensityMode.
             APPLY_TO_ISLANDS,
             target_world_units: float = 0.000000,
             target_pixel_count: float = 0.000000,
             texture_resolution: float = 0.000000,
             enable_udim_layout: bool = False,
             udim_resolutions: Map[int, int] = {}) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.texel_density_mode"></a>

#### texel_density_mode

```python
@property
def texel_density_mode() -> GeometryScriptTexelDensityMode
```

(GeometryScriptTexelDensityMode):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.texel_density_mode"></a>

#### texel_density_mode

```python
@texel_density_mode.setter
def texel_density_mode(value: GeometryScriptTexelDensityMode) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.target_world_units"></a>

#### target_world_units

```python
@property
def target_world_units() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.target_world_units"></a>

#### target_world_units

```python
@target_world_units.setter
def target_world_units(value: float) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.target_pixel_count"></a>

#### target_pixel_count

```python
@property
def target_pixel_count() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.target_pixel_count"></a>

#### target_pixel_count

```python
@target_pixel_count.setter
def target_pixel_count(value: float) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.texture_resolution"></a>

#### texture_resolution

```python
@property
def texture_resolution() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.texture_resolution"></a>

#### texture_resolution

```python
@texture_resolution.setter
def texture_resolution(value: float) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.enable_udim_layout"></a>

#### enable_udim_layout

```python
@property
def enable_udim_layout() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.enable_udim_layout"></a>

#### enable_udim_layout

```python
@enable_udim_layout.setter
def enable_udim_layout(value: bool) -> None
```

<a id="unreal.GeometryScriptUVTexelDensityOptions.udim_resolutions"></a>

#### udim_resolutions

```python
@property
def udim_resolutions() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write]

<a id="unreal.GeometryScriptUVTexelDensityOptions.udim_resolutions"></a>

#### udim_resolutions

```python
@udim_resolutions.setter
def udim_resolutions(value: Map[int, int]) -> None
```

<a id="unreal.GeometryScriptBlurMeshVertexColorsOptions"></a>