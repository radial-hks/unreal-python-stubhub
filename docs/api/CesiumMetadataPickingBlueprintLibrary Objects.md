## CesiumMetadataPickingBlueprintLibrary Objects

```python
class CesiumMetadataPickingBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Metadata Picking Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataPickingBlueprintLibrary.h

<a id="unreal.CesiumMetadataPickingBlueprintLibrary.get_property_texture_values_from_hit"></a>

#### get\_property\_texture\_values\_from\_hit

```python
@classmethod
def get_property_texture_values_from_hit(
    cls,
    hit: HitResult,
    primitive_property_texture_index: int = 0
) -> Map[str, CesiumMetadataValue]
```

X.get_property_texture_values_from_hit(hit, primitive_property_texture_index=0) -> Map[str, CesiumMetadataValue]
Gets the property texture values from a given line trace hit, assuming it
has hit a glTF primitive component.

A primitive may use multiple property textures, as indicated by its indices
in CesiumPrimitiveMetadata. This function allows for selection of which
property texture to use from those available in CesiumPrimitiveMetadata.

In other words, the "Primitive Property Texture Index" should index into
the array property texture indices in the CesiumPrimitiveMetadata. The
primitive metadata will not necessarily contain all of the available
property textures in the CesiumModelMetadata, nor will it necessarily be
listed in the same order.

The returned result may be empty for several reasons:
- if the component is not a Cesium glTF primitive component
- if the given primitive property texture index is out-of-bounds
- if the property texture index derived from CesiumPrimitiveMetadata
is out-of-bounds

Additionally, if any of the property texture's properties are invalid, they
will not be included in the result.

Args:
    hit (HitResult): 
    primitive_property_texture_index (int64): 

Returns:
    Map[str, CesiumMetadataValue]:

<a id="unreal.CesiumMetadataPickingBlueprintLibrary.get_property_table_values_from_hit"></a>

#### get\_property\_table\_values\_from\_hit

```python
@classmethod
def get_property_table_values_from_hit(
        cls,
        hit: HitResult,
        feature_id_set_index: int = 0) -> Map[str, CesiumMetadataValue]
```

X.get_property_table_values_from_hit(hit, feature_id_set_index=0) -> Map[str, CesiumMetadataValue]
Gets the property table values from a given line trace hit, assuming
that it has hit a feature of a glTF primitive component.

A primitive may have multiple feature ID sets, so this allows a feature ID
set to be specified by index. This value should index into the array of
CesiumFeatureIdSets in the component's CesiumPrimitiveFeatures. If the
feature ID set is associated with a property table, it will return that
property table's data.

For feature ID textures and implicit feature IDs, the feature ID can vary
across the face of a primitive. If the specified CesiumFeatureIdSet is one
of those types, the feature ID of the first vertex on the face will be
used.

The returned result may be empty for several reasons:
- if the component is not a Cesium glTF primitive component
- if the hit's face index is somehow out-of-bounds
- if the specified feature ID set does not exist on the primitive
- if the specified feature ID set is not associated with a valid property
table

Additionally, if any of the property table's properties are invalid, they
will not be included in the result.

Args:
    hit (HitResult): 
    feature_id_set_index (int64): 

Returns:
    Map[str, CesiumMetadataValue]:

<a id="unreal.CesiumMetadataPickingBlueprintLibrary.get_metadata_values_for_face_as_strings"></a>

#### get\_metadata\_values\_for\_face\_as\_strings

```python
@classmethod
def get_metadata_values_for_face_as_strings(
        cls,
        component: PrimitiveComponent,
        face_index: int,
        feature_id_set_index: int = 0) -> Map[str, str]
```

X.get_metadata_values_for_face_as_strings(component, face_index, feature_id_set_index=0) -> Map[str, str]
Gets the metadata values for a face on a glTF primitive component, as
strings.

A primitive may have multiple feature ID sets, so this allows a feature ID
set to be specified by index. This value should index into the array of
CesiumFeatureIdSets in the component's CesiumPrimitiveFeatures. If the
feature ID set is associated with a property table, it will return that
property table's data.

For feature ID textures and implicit feature IDs, the feature ID can vary
across the face of a primitive. If the specified CesiumFeatureIdSet is one
of those types, the feature ID of the first vertex on the face will be
used.

The returned result may be empty for several reasons:
- if the component is not a Cesium glTF primitive component
- if the given face index is out-of-bounds
- if the specified feature ID set does not exist on the primitive
- if the specified feature ID set is not associated with a valid property
table

Additionally, if any of the property table's properties are invalid, they
will not be included in the result. Array properties will return empty
strings.
deprecated: Use GetValuesAsStrings to convert the output of GetPropertyTableValuesFromHit instead.

Args:
    component (PrimitiveComponent): 
    face_index (int64): 
    feature_id_set_index (int64): 

Returns:
    Map[str, str]:

<a id="unreal.CesiumMetadataPickingBlueprintLibrary.get_metadata_values_for_face"></a>

#### get\_metadata\_values\_for\_face

```python
@classmethod
def get_metadata_values_for_face(
        cls,
        component: PrimitiveComponent,
        face_index: int,
        feature_id_set_index: int = 0) -> Map[str, CesiumMetadataValue]
```

X.get_metadata_values_for_face(component, face_index, feature_id_set_index=0) -> Map[str, CesiumMetadataValue]
Gets the metadata values for a face on a glTF primitive component.

A primitive may have multiple feature ID sets, so this allows a feature ID
set to be specified by index. This value should index into the array of
CesiumFeatureIdSets in the component's CesiumPrimitiveFeatures. If the
feature ID set is associated with a property table, it will return that
property table's data.

For feature ID textures and implicit feature IDs, the feature ID can vary
across the face of a primitive. If the specified CesiumFeatureIdSet is one
of those types, the feature ID of the first vertex on the face will be
used.

The returned result may be empty for several reasons:
- if the component is not a Cesium glTF primitive component
- if the given face index is out-of-bounds
- if the specified feature ID set does not exist on the primitive
- if the specified feature ID set is not associated with a valid property
table

Additionally, if any of the property table's properties are invalid, they
will not be included in the result.
deprecated: Use GetPropertyTableValuesFromHit instead.

Args:
    component (PrimitiveComponent): 
    face_index (int64): 
    feature_id_set_index (int64): 

Returns:
    Map[str, CesiumMetadataValue]:

<a id="unreal.CesiumMetadataPickingBlueprintLibrary.find_uv_from_hit"></a>

#### find\_uv\_from\_hit

```python
@classmethod
def find_uv_from_hit(cls, hit: HitResult,
                     gltf_tex_coord_set_index: int) -> Optional[Vector2D]
```

X.find_uv_from_hit(hit, gltf_tex_coord_set_index) -> Vector2D or None
Compute the UV coordinates from the given line trace hit, assuming it has
hit a glTF primitive component that contains the specified texture
coordinate set. The texture coordinate set is specified relative to the
glTF itself, where the set index N resolves to the "TEXCOORD_N" attribute
in the glTF primitive.

This function can be used to sample feature ID textures or property
textures in the primitive. This works similarly to the FindCollisionUV
Blueprint, except it does not require the texture coordinate sets to be
present in the model's physics mesh.

Returns false if the given texture coordinate set index does not exist for
the primitive, or if its accessor is invalid.

Args:
    hit (HitResult): 
    gltf_tex_coord_set_index (int64): 

Returns:
    Vector2D or None: 

    uv (Vector2D):

<a id="unreal.CesiumMetadataPrimitiveBlueprintLibrary"></a>