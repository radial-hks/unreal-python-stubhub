## PCGTextureData Objects

```python
class PCGTextureData(PCGBaseTextureData)
```

PCGTexture Data

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
- ``readback_from_gpu_initiated`` (bool):  [Read-Only]
- ``rotation`` (float):  [Read-Write] Rotation to apply when sampling texture.
- ``successfully_initialized`` (bool):  [Read-Only]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``texel_size`` (float):  [Read-Write] The size of one texel in cm, used when calling ToPointData.
- ``texture`` (Texture):  [Read-Only]
- ``texture_index`` (int32):  [Read-Only]
- ``tile_bounds`` (Box2D):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]
- ``transform`` (Transform):  [Read-Only]
- ``use_advanced_tiling`` (bool):  [Read-Write] Whether to tile the source or to stretch it to fit target area.
- ``use_density_source_channel`` (bool):  [Read-Write]
- ``use_tile_bounds`` (bool):  [Read-Write]
- ``width`` (int32):  [Read-Only]

<a id="unreal.PCGTextureData.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Only]

<a id="unreal.PCGTextureData.texture_index"></a>

#### texture_index

```python
@property
def texture_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.PCGTextureData.successfully_initialized"></a>

#### successfully_initialized

```python
@property
def successfully_initialized() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PCGTextureData.readback_from_gpu_initiated"></a>

#### readback_from_gpu_initiated

```python
@property
def readback_from_gpu_initiated() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PCGUnionData"></a>