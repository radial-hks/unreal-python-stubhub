## CesiumFeatureIdTextureBlueprintLibrary Objects

```python
class CesiumFeatureIdTextureBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Feature Id Texture Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeatureIdTexture.h

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_unreal_uv_channel"></a>

#### get\_unreal\_uv\_channel

```python
@classmethod
def get_unreal_uv_channel(cls, component: PrimitiveComponent,
                          feature_id_texture: CesiumFeatureIdTexture) -> int
```

X.get_unreal_uv_channel(component, feature_id_texture) -> int64
Gets the UV channel containing the texture coordinate set that is used by
the feature ID texture on the given component. This refers to the UV
channel it uses on the primitive's static mesh, which is not necessarily
equal to value of GetGltfTextureCoordinateSetIndex.

This function may be used with FindCollisionUV to get the feature ID from a
line trace hit. However, in order for this function to work, the feature ID
texture should be listed under the CesiumFeaturesMetadataComponent of the
owner Cesium3DTileset. Otherwise, its texture coordinate set may not be
included in the Unreal mesh data. To avoid using
CesiumFeaturesMetadataComponent, use GetFeatureIDFromHit instead.

This returns -1 if the feature ID texture is invalid, or if the specified
texture coordinate set is not present in the component's mesh data.

Args:
    component (PrimitiveComponent): 
    feature_id_texture (CesiumFeatureIdTexture): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_texture_coordinate_index"></a>

#### get\_texture\_coordinate\_index

```python
@classmethod
def get_texture_coordinate_index(
        cls, component: PrimitiveComponent,
        feature_id_texture: CesiumFeatureIdTexture) -> int
```

deprecated: 'get_texture_coordinate_index' was renamed to 'get_unreal_uv_channel'.

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_gltf_texture_coordinate_set_index"></a>

#### get\_gltf\_texture\_coordinate\_set\_index

```python
@classmethod
def get_gltf_texture_coordinate_set_index(
        cls, feature_id_texture: CesiumFeatureIdTexture) -> int
```

X.get_gltf_texture_coordinate_set_index(feature_id_texture) -> int64
Gets the glTF texture coordinate set index used by the feature ID texture.
This is the index N corresponding to the "TEXCOORD_N" attribute on the glTF
primitive that samples this texture.

If the texture contains the `KHR_texture_transform` extension, the original
texture coordinate set index can be overridden by the one provided by the
extension.

If the feature ID texture is invalid, this returns -1.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_table_name"></a>

#### get\_feature\_table\_name

```python
@classmethod
def get_feature_table_name(cls,
                           feature_id_texture: CesiumFeatureIdTexture) -> str
```

X.get_feature_table_name(feature_id_texture) -> str
Gets the name of the feature table corresponding to this feature ID
texture. The name can be used to fetch the appropriate
FCesiumFeatureTable from the FCesiumMetadataModel.
deprecated: Use GetPropertyTableIndex on a CesiumFeatureIdSet instead.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 

Returns:
    str:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_texture_status"></a>

#### get\_feature\_id\_texture\_status

```python
@classmethod
def get_feature_id_texture_status(
    cls, feature_id_texture: CesiumFeatureIdTexture
) -> CesiumFeatureIdTextureStatus
```

X.get_feature_id_texture_status(feature_id_texture) -> CesiumFeatureIdTextureStatus
Gets the status of the feature ID texture. If this texture is
invalid in any way, this will briefly indicate why.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 

Returns:
    CesiumFeatureIdTextureStatus:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_from_hit"></a>

#### get\_feature\_id\_from\_hit

```python
@classmethod
def get_feature_id_from_hit(cls, feature_id_texture: CesiumFeatureIdTexture,
                            hit: HitResult) -> int
```

X.get_feature_id_from_hit(feature_id_texture, hit) -> int64
Gets the feature ID from a given line trace hit on the primitive containing
this feature ID texture. The feature ID can be used with a
FCesiumPropertyTable to retrieve the corresponding metadata.

If the feature ID texture is invalid, this returns -1.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 
    hit (HitResult): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_vertex"></a>

#### get\_feature\_id\_for\_vertex

```python
@classmethod
def get_feature_id_for_vertex(cls, feature_id_texture: CesiumFeatureIdTexture,
                              vertex_index: int) -> int
```

X.get_feature_id_for_vertex(feature_id_texture, vertex_index) -> int64
Gets the feature ID associated with the given vertex. The
feature ID can be used with a FCesiumPropertyTable to retrieve the
per-vertex metadata.

This works if the vertex contains texture coordinates for the relevant
texture coordinate set as indicated by GetGltfTextureCoordinateSetIndex. If
the vertex has no such coordinates, or if the feature ID texture itself is
invalid, this returns -1.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 
    vertex_index (int64): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_uv"></a>

#### get\_feature\_id\_for\_uv

```python
@classmethod
def get_feature_id_for_uv(cls, feature_id_texture: CesiumFeatureIdTexture,
                          uv: Vector2D) -> int
```

X.get_feature_id_for_uv(feature_id_texture, uv) -> int64
Gets the feature ID corresponding to the pixel specified by the UV texture
coordinates. The feature ID can be used with a FCesiumPropertyTable to
retrieve the per-pixel metadata.

If the feature ID texture is invalid, this returns -1.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 
    uv (Vector2D): 

Returns:
    int64:

<a id="unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_texture_coordinates"></a>

#### get\_feature\_id\_for\_texture\_coordinates

```python
@classmethod
def get_feature_id_for_texture_coordinates(
        cls, feature_id_texture: CesiumFeatureIdTexture, u: float,
        v: float) -> int
```

X.get_feature_id_for_texture_coordinates(feature_id_texture, u, v) -> int64
Gets the feature ID corresponding to the pixel specified by the texture
coordinates. The feature ID can be used with a FCesiumPropertyTable to
retrieve the per-pixel metadata.

This assumes the given texture coordinates are from the appropriate
texture coordinate set as indicated by GetTextureCoordinateSetIndex. If the
feature ID texture is invalid, this returns -1.

Args:
    feature_id_texture (CesiumFeatureIdTexture): 
    u (float): 
    v (float): 

Returns:
    int64:

<a id="unreal.CesiumFeaturesMetadataComponent"></a>