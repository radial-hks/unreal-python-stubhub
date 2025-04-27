## RuntimeVirtualTexture Objects

```python
class RuntimeVirtualTexture(Object)
```

Runtime virtual texture UObject

**C++ Source:**

- **Module**: Engine
- **File**: RuntimeVirtualTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adaptive`` (bool):  [Read-Write] Enable sparse adaptive page tables. This supports larger tile counts but adds an indirection cost when sampling the virtual texture. It is recommended only when very large virtual resolutions are necessary.
- ``clear_textures`` (bool):  [Read-Write] Enable clear before rendering a page of the virtual texture. Disabling this can be an optimization if you know that the texture will always be fully covered by rendering.
- ``compress_textures`` (bool):  [Read-Write] Enable storing the virtual texture in GPU supported compression formats. Using uncompressed is only recommended for debugging and quality comparisons.
- ``continuous_update`` (bool):  [Read-Write] Enable continuous update of the virtual texture pages. This round-robin updates already mapped pages and can help fix pages that are mapped before dependent textures are fully streamed in.
- ``lod_group`` (TextureGroup):  [Read-Write] Texture group this texture belongs to
- ``material_type`` (RuntimeVirtualTextureMaterialType):  [Read-Write] Contents of virtual texture.
- ``private_space`` (bool):  [Read-Write] Enable private page table allocation. This can reduce total page table memory allocation but can also reduce the total number of virtual textures supported.
- ``remove_low_mips`` (int32):  [Read-Write] Number of low mips to cut from the virtual texture. This can reduce peak virtual texture update cost but will also increase the probability of mip shimmering.
- ``single_physical_space`` (bool):  [Read-Write] Enable page table channel packing. This reduces page table memory and update cost but can reduce the ability to share physical memory with other virtual textures.
- ``tile_border_size`` (int32):  [Read-Write] Page tile border size divided by 2 (Actual values increase in multiples of 2). Higher values trigger a higher anisotropic sampling level.
- ``tile_count`` (int32):  [Read-Write] Size of virtual texture in tiles. (Actual values increase in powers of 2).
  This is applied to the largest axis in world space and the size for any shorter axis is chosen to maintain aspect ratio.
- ``tile_size`` (int32):  [Read-Write] Page tile size. (Actual values increase in powers of 2)
- ``use_low_quality_compression`` (bool):  [Read-Write] Use low quality textures (RGB565/RGB555A1) to replace runtime compression

<a id="unreal.RuntimeVirtualTexture.tile_count"></a>

#### tile_count

```python
@property
def tile_count() -> int
```

(int32):  [Read-Only] Size of virtual texture in tiles. (Actual values increase in powers of 2).
This is applied to the largest axis in world space and the size for any shorter axis is chosen to maintain aspect ratio.

<a id="unreal.RuntimeVirtualTexture.tile_size"></a>

#### tile_size

```python
@property
def tile_size() -> int
```

(int32):  [Read-Only] Page tile size. (Actual values increase in powers of 2)

<a id="unreal.RuntimeVirtualTexture.tile_border_size"></a>

#### tile_border_size

```python
@property
def tile_border_size() -> int
```

(int32):  [Read-Only] Page tile border size divided by 2 (Actual values increase in multiples of 2). Higher values trigger a higher anisotropic sampling level.

<a id="unreal.RuntimeVirtualTexture.material_type"></a>

#### material_type

```python
@property
def material_type() -> RuntimeVirtualTextureMaterialType
```

(RuntimeVirtualTextureMaterialType):  [Read-Only] Contents of virtual texture.

<a id="unreal.RuntimeVirtualTexture.compress_textures"></a>

#### compress_textures

```python
@property
def compress_textures() -> bool
```

(bool):  [Read-Only] Enable storing the virtual texture in GPU supported compression formats. Using uncompressed is only recommended for debugging and quality comparisons.

<a id="unreal.RuntimeVirtualTexture.use_low_quality_compression"></a>

#### use_low_quality_compression

```python
@property
def use_low_quality_compression() -> bool
```

(bool):  [Read-Only] Use low quality textures (RGB565/RGB555A1) to replace runtime compression

<a id="unreal.RuntimeVirtualTexture.lod_group"></a>

#### lod_group

```python
@property
def lod_group() -> TextureGroup
```

(TextureGroup):  [Read-Write] Texture group this texture belongs to

<a id="unreal.RuntimeVirtualTexture.lod_group"></a>

#### lod_group

```python
@lod_group.setter
def lod_group(value: TextureGroup) -> None
```

<a id="unreal.RuntimeVirtualTexture.get_size"></a>

#### get_size

```python
def get_size() -> int
```

x.get_size() -> int32
Public getter for virtual texture size. This is derived from the TileCount and TileSize.

Returns:
    int32:

<a id="unreal.RuntimeVirtualTexture.get_page_table_size"></a>

#### get_page_table_size

```python
def get_page_table_size() -> int
```

x.get_page_table_size() -> int32
Public getter for virtual texture page table size. This is only different from GetTileCount() when using an adaptive page table.

Returns:
    int32:

<a id="unreal.RuntimeVirtualTextureVolume"></a>