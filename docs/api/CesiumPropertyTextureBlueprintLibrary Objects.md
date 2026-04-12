## CesiumPropertyTextureBlueprintLibrary Objects

```python
class CesiumPropertyTextureBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Property Texture Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTexture.h

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_property_texture_status"></a>

#### get\_property\_texture\_status

```python
@classmethod
def get_property_texture_status(
        cls, property_texture: CesiumPropertyTexture
) -> CesiumPropertyTextureStatus
```

X.get_property_texture_status(property_texture) -> CesiumPropertyTextureStatus
Gets the status of the property texture. If the property texture is invalid
in any way, this briefly indicates why.

Args:
    property_texture (CesiumPropertyTexture): 

Returns:
    CesiumPropertyTextureStatus:

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_property_texture_name"></a>

#### get\_property\_texture\_name

```python
@classmethod
def get_property_texture_name(cls,
                              property_texture: CesiumPropertyTexture) -> str
```

X.get_property_texture_name(property_texture) -> str
Gets the name of the property texture.

Args:
    property_texture (CesiumPropertyTexture): 

Returns:
    str:

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_property_names"></a>

#### get\_property\_names

```python
@classmethod
def get_property_names(cls,
                       property_texture: CesiumPropertyTexture) -> Array[str]
```

X.get_property_names(property_texture) -> Array[str]
Gets the names of the properties in this property texture. If the property
texture is invalid, this returns an empty array.

Args:
    property_texture (CesiumPropertyTexture): 

Returns:
    Array[str]:

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_properties"></a>

#### get\_properties

```python
@classmethod
def get_properties(
    cls, property_texture: CesiumPropertyTexture
) -> Map[str, CesiumPropertyTextureProperty]
```

X.get_properties(property_texture) -> Map[str, CesiumPropertyTextureProperty]
Gets all the properties of the property texture, mapped by property name.

Args:
    property_texture (CesiumPropertyTexture): 

Returns:
    Map[str, CesiumPropertyTextureProperty]:

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_metadata_values_from_hit"></a>

#### get\_metadata\_values\_from\_hit

```python
@classmethod
def get_metadata_values_from_hit(
        cls, property_texture: CesiumPropertyTexture,
        hit: HitResult) -> Map[str, CesiumMetadataValue]
```

X.get_metadata_values_from_hit(property_texture, hit) -> Map[str, CesiumMetadataValue]
Given a trace hit result, gets all of the property values from property
texture on the hit component, mapped by property name. This will only
include values from valid property texture properties.

In EXT_structural_metadata, individual properties can specify different
texture coordinate sets to be sampled from. This method uses the
corresponding texture coordinate sets to sample each property.

Args:
    property_texture (CesiumPropertyTexture): 
    hit (HitResult): The trace hit result

Returns:
    Map[str, CesiumMetadataValue]: The property values mapped by property name.

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.get_metadata_values_for_uv"></a>

#### get\_metadata\_values\_for\_uv

```python
@classmethod
def get_metadata_values_for_uv(cls, property_texture: CesiumPropertyTexture,
                               uv: Vector2D) -> Map[str, CesiumMetadataValue]
```

X.get_metadata_values_for_uv(property_texture, uv) -> Map[str, CesiumMetadataValue]
Gets all of the property values at the given texture coordinates, mapped by
property name. This will only include values from valid property texture
properties.

In EXT_structural_metadata, individual properties can specify different
texture coordinate sets to be sampled from. This method uses the same
coordinates to sample each property, regardless of its intended texture
coordinate set. Use GetMetadataValuesForHit instead to sample the property
texture's properties with their respective texture coordinate sets.

Args:
    property_texture (CesiumPropertyTexture): 
    uv (Vector2D): The texture coordinates.

Returns:
    Map[str, CesiumMetadataValue]: The property values mapped by property name.

<a id="unreal.CesiumPropertyTextureBlueprintLibrary.find_property"></a>

#### find\_property

```python
@classmethod
def find_property(cls, property_texture: CesiumPropertyTexture,
                  property_name: str) -> CesiumPropertyTextureProperty
```

X.find_property(property_texture, property_name) -> CesiumPropertyTextureProperty
Retrieve a FCesiumPropertyTextureProperty by name. If the property texture
does not contain a property with that name, this returns an invalid
FCesiumPropertyTextureProperty.

Args:
    property_texture (CesiumPropertyTexture): 
    property_name (str): 

Returns:
    CesiumPropertyTextureProperty:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary"></a>