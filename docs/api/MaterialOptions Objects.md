## MaterialOptions Objects

```python
class MaterialOptions(Object)
```

Options object to define what and how a material should be baked out

**C++ Source:**

- **Module**: MaterialBaking
- **File**: MaterialOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lod_indices`` (Array[int32]):  [Read-Write] LOD indices for which the materials should be baked out
- ``properties`` (Array[PropertyEntry]):  [Read-Write] Properties which are supposed to be baked out for the material(s)
- ``texture_coordinate_index`` (int32):  [Read-Write] Specific texture coordinate which should be used to while baking out material properties as the positions stream
- ``texture_size`` (IntPoint):  [Read-Write] Size of the final texture(s) containing the baked out property data
- ``use_mesh_data`` (bool):  [Read-Write] Determines whether to not allow usage of the source mesh data while baking out material properties
- ``use_specific_uv_index`` (bool):  [Read-Write] Flag whether or not the value of TextureCoordinateIndex should be used while baking out material properties

<a id="unreal.MaterialOptions.properties"></a>

#### properties

```python
@property
def properties() -> Array[PropertyEntry]
```

(Array[PropertyEntry]):  [Read-Write] Properties which are supposed to be baked out for the material(s)

<a id="unreal.MaterialOptions.properties"></a>

#### properties

```python
@properties.setter
def properties(value: Array[PropertyEntry]) -> None
```

<a id="unreal.MaterialOptions.texture_size"></a>

#### texture_size

```python
@property
def texture_size() -> IntPoint
```

(IntPoint):  [Read-Write] Size of the final texture(s) containing the baked out property data

<a id="unreal.MaterialOptions.texture_size"></a>

#### texture_size

```python
@texture_size.setter
def texture_size(value: IntPoint) -> None
```

<a id="unreal.MaterialOptions.lod_indices"></a>

#### lod_indices

```python
@property
def lod_indices() -> Array[int]
```

(Array[int32]):  [Read-Write] LOD indices for which the materials should be baked out

<a id="unreal.MaterialOptions.lod_indices"></a>

#### lod_indices

```python
@lod_indices.setter
def lod_indices(value: Array[int]) -> None
```

<a id="unreal.MaterialOptions.use_mesh_data"></a>

#### use_mesh_data

```python
@property
def use_mesh_data() -> bool
```

(bool):  [Read-Write] Determines whether to not allow usage of the source mesh data while baking out material properties

<a id="unreal.MaterialOptions.use_mesh_data"></a>

#### use_mesh_data

```python
@use_mesh_data.setter
def use_mesh_data(value: bool) -> None
```

<a id="unreal.MaterialOptions.use_specific_uv_index"></a>

#### use_specific_uv_index

```python
@property
def use_specific_uv_index() -> bool
```

(bool):  [Read-Write] Flag whether or not the value of TextureCoordinateIndex should be used while baking out material properties

<a id="unreal.MaterialOptions.use_specific_uv_index"></a>

#### use_specific_uv_index

```python
@use_specific_uv_index.setter
def use_specific_uv_index(value: bool) -> None
```

<a id="unreal.MaterialOptions.texture_coordinate_index"></a>

#### texture_coordinate_index

```python
@property
def texture_coordinate_index() -> int
```

(int32):  [Read-Write] Specific texture coordinate which should be used to while baking out material properties as the positions stream

<a id="unreal.MaterialOptions.texture_coordinate_index"></a>

#### texture_coordinate_index

```python
@texture_coordinate_index.setter
def texture_coordinate_index(value: int) -> None
```

<a id="unreal.AssetBakeOptions"></a>