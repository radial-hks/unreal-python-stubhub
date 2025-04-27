## GeometryScriptBakeTextureOptions Objects

```python
class GeometryScriptBakeTextureOptions(StructBase)
```

Geometry Script Bake Texture Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bit_depth`` (GeometryScriptBakeBitDepth):  [Read-Write] The bit depth for each channel of the generated textures
- ``filtering_type`` (GeometryScriptBakeFilteringType):  [Read-Write] Filtering Type to perform on samples
- ``projection_distance`` (float):  [Read-Write] Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
  This is only relevant if a separate source mesh is provided.
- ``projection_in_world_space`` (bool):  [Read-Write] If true, uses the world space positions for the projection from target mesh to source mesh, otherwise it uses their object space positions.
  This is only relevant if a separate source mesh is provided.
- ``resolution`` (GeometryScriptBakeResolution):  [Read-Write] The pixel resolution of the generated textures
- ``sample_filter_mask`` (Texture2D):  [Read-Write] Mask texture for filtering out samples/pixels from the output texture
- ``samples_per_pixel`` (GeometryScriptBakeSamplesPerPixel):  [Read-Write] Number of samples per pixel

<a id="unreal.GeometryScriptBakeTextureOptions.__init__"></a>

#### __init__

```python
def __init__(
        resolution: GeometryScriptBakeResolution = GeometryScriptBakeResolution
    .RESOLUTION16,
        bit_depth: GeometryScriptBakeBitDepth = GeometryScriptBakeBitDepth.
    CHANNEL_BITS8,
        samples_per_pixel:
    GeometryScriptBakeSamplesPerPixel = GeometryScriptBakeSamplesPerPixel.
    SAMPLE1,
        sample_filter_mask: Texture2D = None,
        filtering_type:
    GeometryScriptBakeFilteringType = GeometryScriptBakeFilteringType.B_SPLINE,
        projection_distance: float = 0.000000,
        projection_in_world_space: bool = False) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.resolution"></a>

#### resolution

```python
@property
def resolution() -> GeometryScriptBakeResolution
```

(GeometryScriptBakeResolution):  [Read-Write] The pixel resolution of the generated textures

<a id="unreal.GeometryScriptBakeTextureOptions.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: GeometryScriptBakeResolution) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.bit_depth"></a>

#### bit_depth

```python
@property
def bit_depth() -> GeometryScriptBakeBitDepth
```

(GeometryScriptBakeBitDepth):  [Read-Write] The bit depth for each channel of the generated textures

<a id="unreal.GeometryScriptBakeTextureOptions.bit_depth"></a>

#### bit_depth

```python
@bit_depth.setter
def bit_depth(value: GeometryScriptBakeBitDepth) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.samples_per_pixel"></a>

#### samples_per_pixel

```python
@property
def samples_per_pixel() -> GeometryScriptBakeSamplesPerPixel
```

(GeometryScriptBakeSamplesPerPixel):  [Read-Write] Number of samples per pixel

<a id="unreal.GeometryScriptBakeTextureOptions.samples_per_pixel"></a>

#### samples_per_pixel

```python
@samples_per_pixel.setter
def samples_per_pixel(value: GeometryScriptBakeSamplesPerPixel) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.sample_filter_mask"></a>

#### sample_filter_mask

```python
@property
def sample_filter_mask() -> Texture2D
```

(Texture2D):  [Read-Write] Mask texture for filtering out samples/pixels from the output texture

<a id="unreal.GeometryScriptBakeTextureOptions.sample_filter_mask"></a>

#### sample_filter_mask

```python
@sample_filter_mask.setter
def sample_filter_mask(value: Texture2D) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.filtering_type"></a>

#### filtering_type

```python
@property
def filtering_type() -> GeometryScriptBakeFilteringType
```

(GeometryScriptBakeFilteringType):  [Read-Write] Filtering Type to perform on samples

<a id="unreal.GeometryScriptBakeTextureOptions.filtering_type"></a>

#### filtering_type

```python
@filtering_type.setter
def filtering_type(value: GeometryScriptBakeFilteringType) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.projection_distance"></a>

#### projection_distance

```python
@property
def projection_distance() -> float
```

(float):  [Read-Write] Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
This is only relevant if a separate source mesh is provided.

<a id="unreal.GeometryScriptBakeTextureOptions.projection_distance"></a>

#### projection_distance

```python
@projection_distance.setter
def projection_distance(value: float) -> None
```

<a id="unreal.GeometryScriptBakeTextureOptions.projection_in_world_space"></a>

#### projection_in_world_space

```python
@property
def projection_in_world_space() -> bool
```

(bool):  [Read-Write] If true, uses the world space positions for the projection from target mesh to source mesh, otherwise it uses their object space positions.
This is only relevant if a separate source mesh is provided.

<a id="unreal.GeometryScriptBakeTextureOptions.projection_in_world_space"></a>

#### projection_in_world_space

```python
@projection_in_world_space.setter
def projection_in_world_space(value: bool) -> None
```

<a id="unreal.GeometryScriptBakeVertexOptions"></a>