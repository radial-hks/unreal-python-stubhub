## CesiumFeatureIdSetBlueprintLibrary Objects

```python
class CesiumFeatureIdSetBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Feature Id Set Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeatureIdSet.h

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_property_table_index"></a>

#### get\_property\_table\_index

```python
@classmethod
def get_property_table_index(cls, feature_id_set: CesiumFeatureIdSet) -> int
```

X.get_property_table_index(feature_id_set) -> int64
Get the index of the property table corresponding to this feature
ID set. The index can be used to fetch the appropriate
FCesiumPropertyTable from the FCesiumModelMetadata. If the
feature ID set does not specify a property table, this returns -1.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_null_feature_id"></a>

#### get\_null\_feature\_id

```python
@classmethod
def get_null_feature_id(cls, feature_id_set: CesiumFeatureIdSet) -> int
```

X.get_null_feature_id(feature_id_set) -> int64
Gets the null feature ID, i.e., the value that indicates no feature is
associated with the owner. In other words, if a vertex or texel returns
this value, then it is not associated with any feature.

If this value was not defined in the glTF feature ID set, this defaults to
-1.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_label"></a>

#### get\_label

```python
@classmethod
def get_label(cls, feature_id_set: CesiumFeatureIdSet) -> str
```

X.get_label(feature_id_set) -> str
Gets the label assigned to this feature ID set. If no label was present in
the glTF feature ID set, this returns an empty string.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    str:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_feature_id_set_type"></a>

#### get\_feature\_id\_set\_type

```python
@classmethod
def get_feature_id_set_type(
        cls, feature_id_set: CesiumFeatureIdSet) -> CesiumFeatureIdSetType
```

X.get_feature_id_set_type(feature_id_set) -> CesiumFeatureIdSetType
Gets the type of this feature ID set.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    CesiumFeatureIdSetType:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_feature_id_from_hit"></a>

#### get\_feature\_id\_from\_hit

```python
@classmethod
def get_feature_id_from_hit(cls, feature_id_set: CesiumFeatureIdSet,
                            hit: HitResult) -> int
```

X.get_feature_id_from_hit(feature_id_set, hit) -> int64
Given a trace hit result, gets the feature ID from the feature ID set on
the hit component. This returns a more accurate value for feature ID
textures, since they define feature IDs per-texel instead of per-vertex.
The feature ID can be used with a FCesiumPropertyTable to retrieve the
corresponding metadata.

This can still retrieve the feature IDs for non-texture feature ID sets.
For attribute or implicit feature IDs, the first feature ID associated
with the first vertex of the intersected face is returned.

This returns -1 if the feature ID set is invalid (e.g., it contains an
invalid feature ID texture).

Args:
    feature_id_set (CesiumFeatureIdSet): 
    hit (HitResult): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_feature_id_for_vertex"></a>

#### get\_feature\_id\_for\_vertex

```python
@classmethod
def get_feature_id_for_vertex(cls, feature_id_set: CesiumFeatureIdSet,
                              vertex_index: int) -> int
```

X.get_feature_id_for_vertex(feature_id_set, vertex_index) -> int64
Gets the feature ID associated with a given vertex. The feature ID can be
used with a FCesiumPropertyTable to retrieve the corresponding metadata.

This returns -1 if the given vertex is out-of-bounds, or if the feature ID
set is invalid (e.g., it contains an invalid feature ID texture).

Args:
    feature_id_set (CesiumFeatureIdSet): 
    vertex_index (int64): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_feature_count"></a>

#### get\_feature\_count

```python
@classmethod
def get_feature_count(cls, feature_id_set: CesiumFeatureIdSet) -> int
```

X.get_feature_count(feature_id_set) -> int64
Get the number of features this primitive has.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_as_feature_id_texture"></a>

#### get\_as\_feature\_id\_texture

```python
@classmethod
def get_as_feature_id_texture(
        cls, feature_id_set: CesiumFeatureIdSet) -> CesiumFeatureIdTexture
```

X.get_as_feature_id_texture(feature_id_set) -> CesiumFeatureIdTexture
Gets this feature ID set as a feature ID texture. This can be used for more
fine-grained interaction with the texture itself. If this feature ID is
not defined as a texture, then the returned texture will be invalid.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    CesiumFeatureIdTexture:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary.get_as_feature_id_attribute"></a>

#### get\_as\_feature\_id\_attribute

```python
@classmethod
def get_as_feature_id_attribute(
        cls, feature_id_set: CesiumFeatureIdSet) -> CesiumFeatureIdAttribute
```

X.get_as_feature_id_attribute(feature_id_set) -> CesiumFeatureIdAttribute
Gets this feature ID set as a feature ID attribute. This can be used for
more fine-grained interaction with the attribute itself. If this feature ID
is not defined as an attribute, then the returned attribute will be
invalid.

Args:
    feature_id_set (CesiumFeatureIdSet): 

Returns:
    CesiumFeatureIdAttribute:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary"></a>