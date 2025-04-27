## PCGTextureSamplerSettings Objects

```python
class PCGTextureSamplerSettings(PCGSettings)
```

PCGTexture Sampler Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGTextureSampler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``center_offset`` (Vector2D):  [Read-Write]
- ``color_channel`` (PCGTextureColorChannel):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``density_function`` (PCGTextureDensityFunction):  [Read-Write]
  deprecated: Property 'DensityFunction' is deprecated.
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``filter`` (PCGTextureFilter):  [Read-Write] Method used to determine the value for a sample based on the value of nearby texels.
- ``force_editor_only_cpu_sampling`` (bool):  [Read-Write] Even if the texture is not set to CPU-available, it can still be accessed from CPU memory under certain conditions (sRGB disabled, no mipmaps, and non-compressed format).
  Reading from CPU memory will be faster and more accurate than reading from GPU memory, since the texture will not be subject to compression or resolution clamping. Enable
  this flag to force a duplicate of the texture with the correct settings for CPU memory access. This is editor-only.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``rotation`` (float):  [Read-Write] Rotation to apply when sampling texture.
- ``seed`` (int32):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write] By default, texture loading is asynchronous, can force it synchronous if needed.
- ``texel_size`` (float):  [Read-Write] The size of one texel in cm, used when calling ToPointData.
- ``texture`` (Texture):  [Read-Write] Texture specific parameters
- ``texture_array_index`` (int32):  [Read-Write] Index of texture array slice. Only used when built with editor and if the type of Texture is UTexture2DArray.
- ``tile_bounds_max`` (Vector2D):  [Read-Write]
- ``tile_bounds_min`` (Vector2D):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]
- ``transform`` (Transform):  [Read-Write] Surface transform
- ``use_absolute_transform`` (bool):  [Read-Write]
- ``use_advanced_tiling`` (bool):  [Read-Write] Whether to tile the source or to stretch it to fit target area.
- ``use_density_source_channel`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_tile_bounds`` (bool):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] Surface transform

<a id="unreal.PCGTextureSamplerSettings.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.PCGTextureSamplerSettings.use_absolute_transform"></a>

#### use_absolute_transform

```python
@property
def use_absolute_transform() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.use_absolute_transform"></a>

#### use_absolute_transform

```python
@use_absolute_transform.setter
def use_absolute_transform(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.texture_array_index"></a>

#### texture_array_index

```python
@property
def texture_array_index() -> int
```

(int32):  [Read-Write] Index of texture array slice. Only used when built with editor and if the type of Texture is UTexture2DArray.

<a id="unreal.PCGTextureSamplerSettings.texture_array_index"></a>

#### texture_array_index

```python
@texture_array_index.setter
def texture_array_index(value: int) -> None
```

<a id="unreal.PCGTextureSamplerSettings.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGTextureDensityFunction
```

(PCGTextureDensityFunction):  [Read-Write]
deprecated: Property 'DensityFunction' is deprecated.

<a id="unreal.PCGTextureSamplerSettings.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGTextureDensityFunction) -> None
```

<a id="unreal.PCGTextureSamplerSettings.use_density_source_channel"></a>

#### use_density_source_channel

```python
@property
def use_density_source_channel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.use_density_source_channel"></a>

#### use_density_source_channel

```python
@use_density_source_channel.setter
def use_density_source_channel(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.color_channel"></a>

#### color_channel

```python
@property
def color_channel() -> PCGTextureColorChannel
```

(PCGTextureColorChannel):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.color_channel"></a>

#### color_channel

```python
@color_channel.setter
def color_channel(value: PCGTextureColorChannel) -> None
```

<a id="unreal.PCGTextureSamplerSettings.filter"></a>

#### filter

```python
@property
def filter() -> PCGTextureFilter
```

(PCGTextureFilter):  [Read-Write] Method used to determine the value for a sample based on the value of nearby texels.

<a id="unreal.PCGTextureSamplerSettings.filter"></a>

#### filter

```python
@filter.setter
def filter(value: PCGTextureFilter) -> None
```

<a id="unreal.PCGTextureSamplerSettings.texel_size"></a>

#### texel_size

```python
@property
def texel_size() -> float
```

(float):  [Read-Write] The size of one texel in cm, used when calling ToPointData.

<a id="unreal.PCGTextureSamplerSettings.texel_size"></a>

#### texel_size

```python
@texel_size.setter
def texel_size(value: float) -> None
```

<a id="unreal.PCGTextureSamplerSettings.use_advanced_tiling"></a>

#### use_advanced_tiling

```python
@property
def use_advanced_tiling() -> bool
```

(bool):  [Read-Write] Whether to tile the source or to stretch it to fit target area.

<a id="unreal.PCGTextureSamplerSettings.use_advanced_tiling"></a>

#### use_advanced_tiling

```python
@use_advanced_tiling.setter
def use_advanced_tiling(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.tiling"></a>

#### tiling

```python
@property
def tiling() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: Vector2D) -> None
```

<a id="unreal.PCGTextureSamplerSettings.center_offset"></a>

#### center_offset

```python
@property
def center_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.center_offset"></a>

#### center_offset

```python
@center_offset.setter
def center_offset(value: Vector2D) -> None
```

<a id="unreal.PCGTextureSamplerSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write] Rotation to apply when sampling texture.

<a id="unreal.PCGTextureSamplerSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.PCGTextureSamplerSettings.use_tile_bounds"></a>

#### use_tile_bounds

```python
@property
def use_tile_bounds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.use_tile_bounds"></a>

#### use_tile_bounds

```python
@use_tile_bounds.setter
def use_tile_bounds(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.tile_bounds_min"></a>

#### tile_bounds_min

```python
@property
def tile_bounds_min() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.tile_bounds_min"></a>

#### tile_bounds_min

```python
@tile_bounds_min.setter
def tile_bounds_min(value: Vector2D) -> None
```

<a id="unreal.PCGTextureSamplerSettings.tile_bounds_max"></a>

#### tile_bounds_max

```python
@property
def tile_bounds_max() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PCGTextureSamplerSettings.tile_bounds_max"></a>

#### tile_bounds_max

```python
@tile_bounds_max.setter
def tile_bounds_max(value: Vector2D) -> None
```

<a id="unreal.PCGTextureSamplerSettings.force_editor_only_cpu_sampling"></a>

#### force_editor_only_cpu_sampling

```python
@property
def force_editor_only_cpu_sampling() -> bool
```

(bool):  [Read-Write] Even if the texture is not set to CPU-available, it can still be accessed from CPU memory under certain conditions (sRGB disabled, no mipmaps, and non-compressed format).
Reading from CPU memory will be faster and more accurate than reading from GPU memory, since the texture will not be subject to compression or resolution clamping. Enable
this flag to force a duplicate of the texture with the correct settings for CPU memory access. This is editor-only.

<a id="unreal.PCGTextureSamplerSettings.force_editor_only_cpu_sampling"></a>

#### force_editor_only_cpu_sampling

```python
@force_editor_only_cpu_sampling.setter
def force_editor_only_cpu_sampling(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, texture loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGTextureSamplerSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write] Texture specific parameters

<a id="unreal.PCGTextureSamplerSettings.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.PCGTransformPointsSettings"></a>