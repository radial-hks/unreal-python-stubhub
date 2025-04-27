## PCGBaseTextureData Objects

```python
class PCGBaseTextureData(PCGSurfaceData)
```

PCGBase Texture Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGTextureData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box):  [Read-Only]
- ``center_offset`` (Vector2D):  [Read-Write]
- ``color_channel`` (PCGTextureColorChannel):  [Read-Write]
- ``density_function`` (PCGTextureDensityFunction):  [Read-Write]
  deprecated: Property 'DensityFunction' is deprecated.
- ``filter`` (PCGTextureFilter):  [Read-Write] Method used to determine the value for a sample based on the value of nearby texels.
- ``height`` (int32):  [Read-Only]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``local_bounds`` (Box):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``rotation`` (float):  [Read-Write] Rotation to apply when sampling texture.
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``texel_size`` (float):  [Read-Write] The size of one texel in cm, used when calling ToPointData.
- ``tile_bounds`` (Box2D):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]
- ``transform`` (Transform):  [Read-Only]
- ``use_advanced_tiling`` (bool):  [Read-Write] Whether to tile the source or to stretch it to fit target area.
- ``use_density_source_channel`` (bool):  [Read-Write]
- ``use_tile_bounds`` (bool):  [Read-Write]
- ``width`` (int32):  [Read-Only]

<a id="unreal.PCGBaseTextureData.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGTextureDensityFunction
```

(PCGTextureDensityFunction):  [Read-Write]
deprecated: Property 'DensityFunction' is deprecated.

<a id="unreal.PCGBaseTextureData.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGTextureDensityFunction) -> None
```

<a id="unreal.PCGBaseTextureData.use_density_source_channel"></a>

#### use_density_source_channel

```python
@property
def use_density_source_channel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBaseTextureData.use_density_source_channel"></a>

#### use_density_source_channel

```python
@use_density_source_channel.setter
def use_density_source_channel(value: bool) -> None
```

<a id="unreal.PCGBaseTextureData.color_channel"></a>

#### color_channel

```python
@property
def color_channel() -> PCGTextureColorChannel
```

(PCGTextureColorChannel):  [Read-Write]

<a id="unreal.PCGBaseTextureData.color_channel"></a>

#### color_channel

```python
@color_channel.setter
def color_channel(value: PCGTextureColorChannel) -> None
```

<a id="unreal.PCGBaseTextureData.filter"></a>

#### filter

```python
@property
def filter() -> PCGTextureFilter
```

(PCGTextureFilter):  [Read-Write] Method used to determine the value for a sample based on the value of nearby texels.

<a id="unreal.PCGBaseTextureData.filter"></a>

#### filter

```python
@filter.setter
def filter(value: PCGTextureFilter) -> None
```

<a id="unreal.PCGBaseTextureData.texel_size"></a>

#### texel_size

```python
@property
def texel_size() -> float
```

(float):  [Read-Write] The size of one texel in cm, used when calling ToPointData.

<a id="unreal.PCGBaseTextureData.texel_size"></a>

#### texel_size

```python
@texel_size.setter
def texel_size(value: float) -> None
```

<a id="unreal.PCGBaseTextureData.use_advanced_tiling"></a>

#### use_advanced_tiling

```python
@property
def use_advanced_tiling() -> bool
```

(bool):  [Read-Write] Whether to tile the source or to stretch it to fit target area.

<a id="unreal.PCGBaseTextureData.use_advanced_tiling"></a>

#### use_advanced_tiling

```python
@use_advanced_tiling.setter
def use_advanced_tiling(value: bool) -> None
```

<a id="unreal.PCGBaseTextureData.tiling"></a>

#### tiling

```python
@property
def tiling() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGBaseTextureData.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: Vector2D) -> None
```

<a id="unreal.PCGBaseTextureData.center_offset"></a>

#### center_offset

```python
@property
def center_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGBaseTextureData.center_offset"></a>

#### center_offset

```python
@center_offset.setter
def center_offset(value: Vector2D) -> None
```

<a id="unreal.PCGBaseTextureData.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write] Rotation to apply when sampling texture.

<a id="unreal.PCGBaseTextureData.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.PCGBaseTextureData.use_tile_bounds"></a>

#### use_tile_bounds

```python
@property
def use_tile_bounds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBaseTextureData.use_tile_bounds"></a>

#### use_tile_bounds

```python
@use_tile_bounds.setter
def use_tile_bounds(value: bool) -> None
```

<a id="unreal.PCGBaseTextureData.tile_bounds"></a>

#### tile_bounds

```python
@property
def tile_bounds() -> Box2D
```

(Box2D):  [Read-Write]

<a id="unreal.PCGBaseTextureData.tile_bounds"></a>

#### tile_bounds

```python
@tile_bounds.setter
def tile_bounds(value: Box2D) -> None
```

<a id="unreal.PCGBaseTextureData.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Only]

<a id="unreal.PCGBaseTextureData.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Only]

<a id="unreal.PCGBaseTextureData.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Only]

<a id="unreal.PCGRenderTargetData"></a>