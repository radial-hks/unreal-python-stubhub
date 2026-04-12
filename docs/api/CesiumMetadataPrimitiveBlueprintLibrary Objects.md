## CesiumMetadataPrimitiveBlueprintLibrary Objects

```python
class CesiumMetadataPrimitiveBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Metadata Primitive Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataPrimitive.h

<a id="unreal.CesiumMetadataPrimitiveBlueprintLibrary.get_first_vertex_id_from_face_id"></a>

#### get\_first\_vertex\_id\_from\_face\_id

```python
@classmethod
def get_first_vertex_id_from_face_id(
        cls, metadata_primitive: CesiumMetadataPrimitive, face_id: int) -> int
```

X.get_first_vertex_id_from_face_id(metadata_primitive, face_id) -> int64
Gets the ID of the first vertex that makes up a given face of this
primitive.
deprecated: CesiumMetadataPrimitive is deprecated. Use GetFirstVertexFromFace with CesiumPrimitiveFeatures instead.

Args:
    metadata_primitive (CesiumMetadataPrimitive): 
    face_id (int64): The ID of the face.

Returns:
    int64:

<a id="unreal.CesiumMetadataPrimitiveBlueprintLibrary.get_feature_texture_names"></a>

#### get\_feature\_texture\_names

```python
@classmethod
def get_feature_texture_names(
        cls, metadata_primitive: CesiumMetadataPrimitive) -> Array[str]
```

X.get_feature_texture_names(metadata_primitive) -> Array[str]

deprecated: CesiumMetadataPrimitive is deprecated. Get the associated property texture indices from CesiumPrimitiveMetadata instead.
brief: Get all the feature textures that are associated with the primitive.

Args:
    metadata_primitive (CesiumMetadataPrimitive): 

Returns:
    Array[str]:

<a id="unreal.CesiumMetadataPrimitiveBlueprintLibrary.get_feature_id_textures"></a>

#### get\_feature\_id\_textures

```python
@classmethod
def get_feature_id_textures(
    cls, metadata_primitive: CesiumMetadataPrimitive
) -> Array[CesiumFeatureIdTexture]
```

X.get_feature_id_textures(metadata_primitive) -> Array[CesiumFeatureIdTexture]
Get all the feature ID textures that are associated with the
primitive.
deprecated: CesiumMetadataPrimitive is deprecated. Get feature IDs from CesiumPrimitiveFeatures instead.

Args:
    metadata_primitive (CesiumMetadataPrimitive): 

Returns:
    Array[CesiumFeatureIdTexture]:

<a id="unreal.CesiumMetadataPrimitiveBlueprintLibrary.get_feature_id_attributes"></a>

#### get\_feature\_id\_attributes

```python
@classmethod
def get_feature_id_attributes(
    cls, metadata_primitive: CesiumMetadataPrimitive
) -> Array[CesiumFeatureIdAttribute]
```

X.get_feature_id_attributes(metadata_primitive) -> Array[CesiumFeatureIdAttribute]
Get all the feature ID attributes that are associated with the
primitive.
deprecated: CesiumMetadataPrimitive is deprecated. Get feature IDs from CesiumPrimitiveFeatures instead.

Args:
    metadata_primitive (CesiumMetadataPrimitive): 

Returns:
    Array[CesiumFeatureIdAttribute]:

<a id="unreal.CesiumMetadataUtilityBlueprintLibrary"></a>