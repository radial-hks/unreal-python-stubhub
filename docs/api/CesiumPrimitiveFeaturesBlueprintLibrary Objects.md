## CesiumPrimitiveFeaturesBlueprintLibrary Objects

```python
class CesiumPrimitiveFeaturesBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Primitive Features Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPrimitiveFeatures.h

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_vertex_count"></a>

#### get\_vertex\_count

```python
@classmethod
def get_vertex_count(cls, primitive_features: CesiumPrimitiveFeatures) -> int
```

X.get_vertex_count(primitive_features) -> int64
Get the number of vertices in the primitive.

Args:
    primitive_features (CesiumPrimitiveFeatures): 

Returns:
    int64:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_primitive_features"></a>

#### get\_primitive\_features

```python
@classmethod
def get_primitive_features(
        cls, component: PrimitiveComponent) -> CesiumPrimitiveFeatures
```

X.get_primitive_features(component) -> CesiumPrimitiveFeatures
Gets the primitive features of a glTF primitive component. If component is
not a Cesium glTF primitive component, the returned features are empty.

Args:
    component (PrimitiveComponent): 

Returns:
    CesiumPrimitiveFeatures:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_first_vertex_from_face"></a>

#### get\_first\_vertex\_from\_face

```python
@classmethod
def get_first_vertex_from_face(cls,
                               primitive_features: CesiumPrimitiveFeatures,
                               face_index: int) -> int
```

X.get_first_vertex_from_face(primitive_features, face_index) -> int64
Gets the index of the first vertex that makes up a given face of this
primitive.

Args:
    primitive_features (CesiumPrimitiveFeatures): 
    face_index (int64): The index of the face.

Returns:
    int64:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_feature_id_sets_of_type"></a>

#### get\_feature\_id\_sets\_of\_type

```python
@classmethod
def get_feature_id_sets_of_type(
        cls, primitive_features: CesiumPrimitiveFeatures,
        type: CesiumFeatureIdSetType) -> Array[CesiumFeatureIdSet]
```

X.get_feature_id_sets_of_type(primitive_features, type) -> Array[CesiumFeatureIdSet]
Gets all the feature ID sets of the given type. If the primitive has no
sets of that type, the returned array will be empty.

Args:
    primitive_features (CesiumPrimitiveFeatures): 
    type (CesiumFeatureIdSetType): 

Returns:
    Array[CesiumFeatureIdSet]:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_feature_id_sets"></a>

#### get\_feature\_id\_sets

```python
@classmethod
def get_feature_id_sets(
        cls, primitive_features: CesiumPrimitiveFeatures
) -> Array[CesiumFeatureIdSet]
```

X.get_feature_id_sets(primitive_features) -> Array[CesiumFeatureIdSet]
Gets all the feature ID sets that are associated with the
primitive.

Args:
    primitive_features (CesiumPrimitiveFeatures): 

Returns:
    Array[CesiumFeatureIdSet]:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_feature_id_from_hit"></a>

#### get\_feature\_id\_from\_hit

```python
@classmethod
def get_feature_id_from_hit(cls,
                            primitive_features: CesiumPrimitiveFeatures,
                            hit: HitResult,
                            feature_id_set_index: int = 0) -> int
```

X.get_feature_id_from_hit(primitive_features, hit, feature_id_set_index=0) -> int64
Gets the feature ID from the given line trace hit, assuming it
has hit a glTF primitive component containing this CesiumPrimitiveFeatures.

A primitive may have multiple feature ID sets, so this allows a feature ID
set to be specified by index. This value should index into the array of
CesiumFeatureIdSets in the CesiumPrimitiveFeatures. If the specified
feature ID set index is invalid, this returns -1.

Args:
    primitive_features (CesiumPrimitiveFeatures): 
    hit (HitResult): 
    feature_id_set_index (int64): 

Returns:
    int64:

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary.get_feature_id_from_face"></a>

#### get\_feature\_id\_from\_face

```python
@classmethod
def get_feature_id_from_face(cls,
                             primitive_features: CesiumPrimitiveFeatures,
                             face_index: int,
                             feature_id_set_index: int = 0) -> int
```

X.get_feature_id_from_face(primitive_features, face_index, feature_id_set_index=0) -> int64
Gets the feature ID associated with the given face.

A primitive may have multiple feature ID sets, so this allows a feature ID
set to be specified by index. This value should index into the array of
CesiumFeatureIdSets in the CesiumPrimitiveFeatures. If the specified
feature ID set index is invalid, this returns -1.

Args:
    primitive_features (CesiumPrimitiveFeatures): 
    face_index (int64): 
    feature_id_set_index (int64): 

Returns:
    int64:

<a id="unreal.CesiumPrimitiveMetadataBlueprintLibrary"></a>