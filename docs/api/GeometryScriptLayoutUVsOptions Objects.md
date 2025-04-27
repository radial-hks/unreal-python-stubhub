## GeometryScriptLayoutUVsOptions Objects

```python
class GeometryScriptLayoutUVsOptions(StructBase)
```

Geometry Script Layout UVs Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_flips`` (bool):  [Read-Write] Allow the Repack layout type to flip the orientation when rotating UV islands to save space. Note that this may cause problems for downstream operations, and therefore is disabled by default.
- ``enable_udim_layout`` (bool):  [Read-Write] Enable UDIM aware layout and keep islands within their originating UDIM tiles when laying out.
- ``layout_type`` (GeometryScriptUVLayoutType):  [Read-Write] Type of layout applied to input UVs
- ``preserve_rotation`` (bool):  [Read-Write] Force the Repack layout type to preserve existing rotation of UV islands. Note, this might lead to the packing not being as space efficient as possible, and therefore is disabled by default.
- ``preserve_scale`` (bool):  [Read-Write] Force the Repack layout type to preserve existing scaling of UV islands. Note, this might lead to the packing not fitting within a unit square, and therefore is disabled by default.
- ``scale`` (float):  [Read-Write] Uniform scale applied to UVs after packing
- ``texture_resolution`` (int32):  [Read-Write] Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts
- ``translation`` (Vector2D):  [Read-Write] Translation applied to UVs after packing, and after scaling
- ``udim_resolutions`` (Map[int32, int32]):  [Read-Write]

<a id="unreal.GeometryScriptLayoutUVsOptions.__init__"></a>

#### __init__

```python
def __init__(
        layout_type: GeometryScriptUVLayoutType = GeometryScriptUVLayoutType.
    TRANSFORM,
        texture_resolution: int = 0,
        scale: float = 0.000000,
        translation: Vector2D = [0.000000, 0.000000],
        preserve_scale: bool = False,
        preserve_rotation: bool = False,
        allow_flips: bool = False,
        enable_udim_layout: bool = False,
        udim_resolutions: Map[int, int] = {}) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.layout_type"></a>

#### layout_type

```python
@property
def layout_type() -> GeometryScriptUVLayoutType
```

(GeometryScriptUVLayoutType):  [Read-Write] Type of layout applied to input UVs

<a id="unreal.GeometryScriptLayoutUVsOptions.layout_type"></a>

#### layout_type

```python
@layout_type.setter
def layout_type(value: GeometryScriptUVLayoutType) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.texture_resolution"></a>

#### texture_resolution

```python
@property
def texture_resolution() -> int
```

(int32):  [Read-Write] Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts

<a id="unreal.GeometryScriptLayoutUVsOptions.texture_resolution"></a>

#### texture_resolution

```python
@texture_resolution.setter
def texture_resolution(value: int) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] Uniform scale applied to UVs after packing

<a id="unreal.GeometryScriptLayoutUVsOptions.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.translation"></a>

#### translation

```python
@property
def translation() -> Vector2D
```

(Vector2D):  [Read-Write] Translation applied to UVs after packing, and after scaling

<a id="unreal.GeometryScriptLayoutUVsOptions.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector2D) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.preserve_scale"></a>

#### preserve_scale

```python
@property
def preserve_scale() -> bool
```

(bool):  [Read-Write] Force the Repack layout type to preserve existing scaling of UV islands. Note, this might lead to the packing not fitting within a unit square, and therefore is disabled by default.

<a id="unreal.GeometryScriptLayoutUVsOptions.preserve_scale"></a>

#### preserve_scale

```python
@preserve_scale.setter
def preserve_scale(value: bool) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.preserve_rotation"></a>

#### preserve_rotation

```python
@property
def preserve_rotation() -> bool
```

(bool):  [Read-Write] Force the Repack layout type to preserve existing rotation of UV islands. Note, this might lead to the packing not being as space efficient as possible, and therefore is disabled by default.

<a id="unreal.GeometryScriptLayoutUVsOptions.preserve_rotation"></a>

#### preserve_rotation

```python
@preserve_rotation.setter
def preserve_rotation(value: bool) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.allow_flips"></a>

#### allow_flips

```python
@property
def allow_flips() -> bool
```

(bool):  [Read-Write] Allow the Repack layout type to flip the orientation when rotating UV islands to save space. Note that this may cause problems for downstream operations, and therefore is disabled by default.

<a id="unreal.GeometryScriptLayoutUVsOptions.allow_flips"></a>

#### allow_flips

```python
@allow_flips.setter
def allow_flips(value: bool) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.enable_udim_layout"></a>

#### enable_udim_layout

```python
@property
def enable_udim_layout() -> bool
```

(bool):  [Read-Write] Enable UDIM aware layout and keep islands within their originating UDIM tiles when laying out.

<a id="unreal.GeometryScriptLayoutUVsOptions.enable_udim_layout"></a>

#### enable_udim_layout

```python
@enable_udim_layout.setter
def enable_udim_layout(value: bool) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions.udim_resolutions"></a>

#### udim_resolutions

```python
@property
def udim_resolutions() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write]

<a id="unreal.GeometryScriptLayoutUVsOptions.udim_resolutions"></a>

#### udim_resolutions

```python
@udim_resolutions.setter
def udim_resolutions(value: Map[int, int]) -> None
```

<a id="unreal.GeometryScriptExpMapUVOptions"></a>