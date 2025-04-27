## MaterialExpressionSparseVolumeTextureBase Objects

```python
class MaterialExpressionSparseVolumeTextureBase(MaterialExpression)
```

Material Expression Sparse Volume Texture Base

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSparseVolumeTextureBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``sparse_volume_texture`` (SparseVolumeTexture):  [Read-Write] The Sparse Volume Texture to sample.

<a id="unreal.MaterialExpressionSparseVolumeTextureBase.sparse_volume_texture"></a>

#### sparse_volume_texture

```python
@property
def sparse_volume_texture() -> SparseVolumeTexture
```

(SparseVolumeTexture):  [Read-Write] The Sparse Volume Texture to sample.

<a id="unreal.MaterialExpressionSparseVolumeTextureBase.sparse_volume_texture"></a>

#### sparse_volume_texture

```python
@sparse_volume_texture.setter
def sparse_volume_texture(value: SparseVolumeTexture) -> None
```

<a id="unreal.MaterialExpressionSparseVolumeTextureObject"></a>