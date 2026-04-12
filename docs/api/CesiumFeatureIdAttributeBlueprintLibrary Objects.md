## CesiumFeatureIdAttributeBlueprintLibrary Objects

```python
class CesiumFeatureIdAttributeBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Feature Id Attribute Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeatureIdAttribute.h

<a id="unreal.CesiumFeatureIdAttributeBlueprintLibrary.get_vertex_count"></a>

#### get\_vertex\_count

```python
@classmethod
def get_vertex_count(cls,
                     feature_id_attribute: CesiumFeatureIdAttribute) -> int
```

X.get_vertex_count(feature_id_attribute) -> int64
Get the number of vertices in the primitive containing the feature
ID attribute. If the feature ID attribute is invalid, this returns 0.

Args:
    feature_id_attribute (CesiumFeatureIdAttribute): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdAttributeBlueprintLibrary.get_feature_table_name"></a>

#### get\_feature\_table\_name

```python
@classmethod
def get_feature_table_name(
        cls, feature_id_attribute: CesiumFeatureIdAttribute) -> str
```

X.get_feature_table_name(feature_id_attribute) -> str
Get the name of the feature table corresponding to this feature ID
attribute. The name can be used to fetch the appropriate
FCesiumFeatureTable from the FCesiumMetadataModel.
deprecated: Use GetPropertyTableIndex on a CesiumFeatureIdSet instead.

Args:
    feature_id_attribute (CesiumFeatureIdAttribute): 

Returns:
    str:

<a id="unreal.CesiumFeatureIdAttributeBlueprintLibrary.get_feature_id_for_vertex"></a>

#### get\_feature\_id\_for\_vertex

```python
@classmethod
def get_feature_id_for_vertex(cls,
                              feature_id_attribute: CesiumFeatureIdAttribute,
                              vertex_index: int) -> int
```

X.get_feature_id_for_vertex(feature_id_attribute, vertex_index) -> int64
Gets the feature ID associated with the given vertex. The feature ID can be
used with a FCesiumFeatureTable to retrieve the per-vertex metadata. If
the feature ID attribute is invalid, this returns -1.

Args:
    feature_id_attribute (CesiumFeatureIdAttribute): 
    vertex_index (int64): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdAttributeBlueprintLibrary.get_feature_id_attribute_status"></a>

#### get\_feature\_id\_attribute\_status

```python
@classmethod
def get_feature_id_attribute_status(
    cls, feature_id_attribute: CesiumFeatureIdAttribute
) -> CesiumFeatureIdAttributeStatus
```

X.get_feature_id_attribute_status(feature_id_attribute) -> CesiumFeatureIdAttributeStatus
Gets the status of the feature ID attribute. If this attribute is
invalid in any way, this will briefly indicate why.

Args:
    feature_id_attribute (CesiumFeatureIdAttribute): 

Returns:
    CesiumFeatureIdAttributeStatus:

<a id="unreal.CesiumFeatureIdSetBlueprintLibrary"></a>