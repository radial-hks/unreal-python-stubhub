## CesiumModelMetadataBlueprintLibrary Objects

```python
class CesiumModelMetadataBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Model Metadata Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumModelMetadata.h

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_textures_at_indices"></a>

#### get\_property\_textures\_at\_indices

```python
@classmethod
def get_property_textures_at_indices(
        cls, model_metadata: CesiumModelMetadata,
        indices: Array[int]) -> Array[CesiumPropertyTexture]
```

X.get_property_textures_at_indices(model_metadata, indices) -> Array[CesiumPropertyTexture]
Gets an array of the property textures at the specified indices for this
model metadata.

Args:
    model_metadata (CesiumModelMetadata): 
    indices (Array[int64]): 

Returns:
    Array[CesiumPropertyTexture]:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_textures"></a>

#### get\_property\_textures

```python
@classmethod
def get_property_textures(
        cls,
        model_metadata: CesiumModelMetadata) -> Array[CesiumPropertyTexture]
```

X.get_property_textures(model_metadata) -> Array[CesiumPropertyTexture]
Gets an array of all the property textures for this model metadata.

Args:
    model_metadata (CesiumModelMetadata): 

Returns:
    Array[CesiumPropertyTexture]:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_texture"></a>

#### get\_property\_texture

```python
@classmethod
def get_property_texture(cls, model_metadata: CesiumModelMetadata,
                         index: int) -> CesiumPropertyTexture
```

X.get_property_texture(model_metadata, index) -> CesiumPropertyTexture
Gets the property table at the specified index for this model metadata. If
the index is out-of-bounds, this returns an invalid property table.

Args:
    model_metadata (CesiumModelMetadata): 
    index (int64): 

Returns:
    CesiumPropertyTexture:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_tables_at_indices"></a>

#### get\_property\_tables\_at\_indices

```python
@classmethod
def get_property_tables_at_indices(
        cls, model_metadata: CesiumModelMetadata,
        indices: Array[int]) -> Array[CesiumPropertyTable]
```

X.get_property_tables_at_indices(model_metadata, indices) -> Array[CesiumPropertyTable]
Gets the property table at the specified indices for this model metadata.
An invalid property table will be returned for any out-of-bounds index.

Args:
    model_metadata (CesiumModelMetadata): 
    indices (Array[int64]): 

Returns:
    Array[CesiumPropertyTable]:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_tables"></a>

#### get\_property\_tables

```python
@classmethod
def get_property_tables(
        cls,
        model_metadata: CesiumModelMetadata) -> Array[CesiumPropertyTable]
```

X.get_property_tables(model_metadata) -> Array[CesiumPropertyTable]
Gets an array of all the property tables for this model metadata.

Args:
    model_metadata (CesiumModelMetadata): 

Returns:
    Array[CesiumPropertyTable]:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_property_table"></a>

#### get\_property\_table

```python
@classmethod
def get_property_table(cls, model_metadata: CesiumModelMetadata,
                       index: int) -> CesiumPropertyTable
```

X.get_property_table(model_metadata, index) -> CesiumPropertyTable
Gets the property table at the specified index for this model metadata. If
the index is out-of-bounds, this returns an invalid property table.

Args:
    model_metadata (CesiumModelMetadata): 
    index (int64): 

Returns:
    CesiumPropertyTable:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_model_metadata"></a>

#### get\_model\_metadata

```python
@classmethod
def get_model_metadata(cls,
                       component: PrimitiveComponent) -> CesiumModelMetadata
```

X.get_model_metadata(component) -> CesiumModelMetadata
Gets the model metadata of a glTF primitive component. If component is
not a Cesium glTF primitive component, the returned metadata is empty.

Args:
    component (PrimitiveComponent): 

Returns:
    CesiumModelMetadata:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_feature_textures"></a>

#### get\_feature\_textures

```python
@classmethod
def get_feature_textures(
        cls, model_metadata: CesiumModelMetadata
) -> Map[str, CesiumPropertyTexture]
```

X.get_feature_textures(model_metadata) -> Map[str, CesiumPropertyTexture]

deprecated: Use GetPropertyTextures to get an array of property textures instead.
brief: Get all the feature textures for this model metadata.

Args:
    model_metadata (CesiumModelMetadata): 

Returns:
    Map[str, CesiumPropertyTexture]:

<a id="unreal.CesiumModelMetadataBlueprintLibrary.get_feature_tables"></a>

#### get\_feature\_tables

```python
@classmethod
def get_feature_tables(
        cls,
        model_metadata: CesiumModelMetadata) -> Map[str, CesiumPropertyTable]
```

X.get_feature_tables(model_metadata) -> Map[str, CesiumPropertyTable]

deprecated: Use GetPropertyTables to get an array of property tables instead.
brief: Get all the feature tables for this model metadata.

Args:
    model_metadata (CesiumModelMetadata): 

Returns:
    Map[str, CesiumPropertyTable]:

<a id="unreal.CesiumMetadataModelBlueprintLibrary"></a>