## PCGRenderTargetData Objects

```python
class PCGRenderTargetData(PCGBaseTextureData)
```

TODO: It's possible that caching the result in this class is not as efficient as it could be
 if we expect to sample in different ways (e.g. channel) in the same render target

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGRenderTargetData.h

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
- ``render_target`` (TextureRenderTarget2D):  [Read-Only]
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

<a id="unreal.PCGRenderTargetData.render_target"></a>

#### render_target

```python
@property
def render_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.PCGRenderTargetData.initialize"></a>

#### initialize

```python
def initialize(render_target: TextureRenderTarget2D,
               transform: Transform) -> None
```

x.initialize(render_target, transform) -> None
Initialize

Args:
    render_target (TextureRenderTarget2D): 
    transform (Transform):

<a id="unreal.PCGSplineData"></a>