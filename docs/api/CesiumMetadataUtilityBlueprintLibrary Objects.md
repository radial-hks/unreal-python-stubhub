## CesiumMetadataUtilityBlueprintLibrary Objects

```python
class CesiumMetadataUtilityBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Metadata Utility Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataUtilityBlueprintLibrary.h

<a id="unreal.CesiumMetadataUtilityBlueprintLibrary.get_primitive_metadata"></a>

#### get\_primitive\_metadata

```python
@classmethod
def get_primitive_metadata(
        cls, component: PrimitiveComponent) -> CesiumMetadataPrimitive
```

X.get_primitive_metadata(component) -> CesiumMetadataPrimitive
Gets the primitive metadata of a glTF primitive component. If component is
not a Cesium glTF primitive component, the returned metadata is empty
deprecated: CesiumMetadataPrimitive is deprecated. Use CesiumPrimitiveFeatures and CesiumPrimitiveMetadata instead.

Args:
    component (PrimitiveComponent): 

Returns:
    CesiumMetadataPrimitive:

<a id="unreal.CesiumMetadataUtilityBlueprintLibrary.get_metadata_values_for_face"></a>

#### get\_metadata\_values\_for\_face

```python
@classmethod
def get_metadata_values_for_face(
        cls, component: PrimitiveComponent,
        face_id: int) -> Map[str, CesiumMetadataValue]
```

X.get_metadata_values_for_face(component, face_id) -> Map[str, CesiumMetadataValue]
Gets the metadata of a face of a glTF primitive component. If the component
is not a Cesium glTF primitive component, the returned metadata is empty.
If the primitive has multiple feature tables, the metadata in the first
table is returned.
deprecated: The CesiumMetadataUtility blueprint library is deprecated. Use GetMetadataValuesForFace in the CesiumMetadataPicking blueprint library instead.

Args:
    component (PrimitiveComponent): 
    face_id (int64): 

Returns:
    Map[str, CesiumMetadataValue]:

<a id="unreal.CesiumMetadataUtilityBlueprintLibrary.get_metadata_values_as_string_for_face"></a>

#### get\_metadata\_values\_as\_string\_for\_face

```python
@classmethod
def get_metadata_values_as_string_for_face(cls, component: PrimitiveComponent,
                                           face_id: int) -> Map[str, str]
```

X.get_metadata_values_as_string_for_face(component, face_id) -> Map[str, str]
Gets the metadata as string of a face of a glTF primitive component. If the
component is not a Cesium glTF primitive component, the returned metadata
is empty. If the primitive has multiple feature tables, the metadata in the
first table is returned.
deprecated: The CesiumMetadataUtility blueprint library is deprecated. Use GetMetadataValuesForFaceAsStrings in the CesiumMetadataPicking blueprint library instead.

Args:
    component (PrimitiveComponent): 
    face_id (int64): 

Returns:
    Map[str, str]:

<a id="unreal.CesiumMetadataUtilityBlueprintLibrary.get_feature_id_from_face_id"></a>

#### get\_feature\_id\_from\_face\_id

```python
@classmethod
def get_feature_id_from_face_id(cls, primitive: CesiumMetadataPrimitive,
                                feature_id_attribute: CesiumFeatureIdAttribute,
                                face_id: int) -> int
```

X.get_feature_id_from_face_id(primitive, feature_id_attribute, face_id) -> int64
Gets the feature ID associated with a given face for a feature id
attribute.
deprecated: Use GetFeatureIDFromFace with CesiumPrimitiveFeatures instead.

Args:
    primitive (CesiumMetadataPrimitive): 
    feature_id_attribute (CesiumFeatureIdAttribute): 
    face_id (int64): 

Returns:
    int64:

<a id="unreal.CesiumMetadataValueBlueprintLibrary"></a>