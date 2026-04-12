## CesiumPropertyTexturePropertyBlueprintLibrary Objects

```python
class CesiumPropertyTexturePropertyBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Property Texture Property Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTextureProperty.h

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.is_normalized"></a>

#### is\_normalized

```python
@classmethod
def is_normalized(cls, property_: CesiumPropertyTextureProperty) -> bool
```

X.is_normalized(property_) -> bool
Whether this property is normalized. Only applicable when this property
has an integer component type.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    bool: Whether this property is normalized.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector4"></a>

#### get\_vector4

```python
@classmethod
def get_vector4(cls, property_: CesiumPropertyTextureProperty, uv: Vector2D,
                default_value: Vector4) -> Vector4
```

X.get_vector4(property_, uv, default_value) -> Vector4
Attempts to retrieve the value at the given texture coordinates as a
FVector4.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a 4-dimensional vector, its components will be converted
to double-precision floating-point numbers.

- If the value is a 3-dimensional vector, it will become the XYZ-components
of the FVector4. The W-component will be set to zero.

- If the value is a 2-dimensional vector, it will become the XY-components
of the FVector4. The Z- and W-components will be set to zero.

- If the value is a scalar, then the resulting FVector4 will have this
value as a double-precision floating-point number in all of its components.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (Vector4): The default value to fall back on.

Returns:
    Vector4: The property value as a FVector4.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector2d"></a>

#### get\_vector2d

```python
@classmethod
def get_vector2d(cls, property_: CesiumPropertyTextureProperty, uv: Vector2D,
                 default_value: Vector2D) -> Vector2D
```

X.get_vector2d(property_, uv, default_value) -> Vector2D
Attempts to retrieve the value at the given texture coordinates as a
FVector2D.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a 2-dimensional vector, its components will be converted
to double-precision floating-point numbers.

- If the value is a 3- or 4-dimensional vector, it will use the first two
components to construct the FVector2D.

- If the value is a scalar that can be converted to a 32-bit signed
integer, the resulting FVector2D will have this value in both of its
components.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (Vector2D): The default value to fall back on.

Returns:
    Vector2D: The property value as a FVector2D.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector"></a>

#### get\_vector

```python
@classmethod
def get_vector(cls, property_: CesiumPropertyTextureProperty, uv: Vector2D,
               default_value: Vector) -> Vector
```

X.get_vector(property_, uv, default_value) -> Vector
Attempts to retrieve the value at the given texture coordinates as a
FVector.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a 3-dimensional vector, its components will be converted
to double-precision floating-point numbers.

- If the value is a 4-dimensional vector, a FVector containing the first
three components will be returned.

- If the value is a 2-dimensional vector, it will become the XY-components
of the FVector. The Z-component will be set to zero.

- If the value is a scalar, then the resulting FVector will have this value
as a double-precision floating-point number in all of its components.

In all other cases, the user-defined default value is returned. In all
vector cases, if any of the relevant components cannot be represented as a
single-precision float, the default value is returned.

If the property texture property is somehow invalid, the user-defined
default value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (Vector): The default value to fall back on.

Returns:
    Vector: The property value as a FVector.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_value_type"></a>

#### get\_value\_type

```python
@classmethod
def get_value_type(
        cls,
        property_: CesiumPropertyTextureProperty) -> CesiumMetadataValueType
```

X.get_value_type(property_) -> CesiumMetadataValueType
Gets the type of the metadata value as defined in the
EXT_structural_metadata extension. Many of these types are not accessible
from Blueprints, but can be converted to a Blueprint-accessible type.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValueType:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_value"></a>

#### get\_value

```python
@classmethod
def get_value(cls, property_: CesiumPropertyTextureProperty,
              uv: Vector2D) -> CesiumMetadataValue
```

X.get_value(property_, uv) -> CesiumMetadataValue
Retrieves the value of the property for the given texture coordinates. This
allows the value to be acted on more generically; its true value can be
retrieved later as a specific Blueprints type.

For numeric properties, the raw value for a given feature will be
transformed by the property's normalization, scale, and offset before it is
returned. If the raw value is equal to the property's "no data" value, an
empty value will be returned. However, if the property itself specifies a
default value, then the property-defined default value will be returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.

Returns:
    CesiumMetadataValue: The property value.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_unreal_uv_channel"></a>

#### get\_unreal\_uv\_channel

```python
@classmethod
def get_unreal_uv_channel(cls, component: PrimitiveComponent,
                          property_: CesiumPropertyTextureProperty) -> int
```

X.get_unreal_uv_channel(component, property_) -> int64
Gets the UV channel containing the texture coordinate set that is used by
the property texture property on the given component. This refers to the UV
channel it uses on the primitive's static mesh, which is not necessarily
equal to value of GetGltfTextureCoordinateSetIndex.

This function may be used with FindCollisionUV to get the feature ID from a
line trace hit. However, in order for this function to work, the feature ID
texture should be listed under the CesiumFeaturesMetadataComponent of the
owner Cesium3DTileset. Otherwise, its texture coordinate set may not be
included in the Unreal mesh data. To avoid using
CesiumFeaturesMetadataComponent, use GetFeatureIDFromHit instead.

This returns -1 if the property texture property is invalid, or if the
specified texture coordinate set is not present in the component's mesh
data.

Args:
    component (PrimitiveComponent): 
    property_ (CesiumPropertyTextureProperty): 

Returns:
    int64:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_texture_coordinate_index"></a>

#### get\_texture\_coordinate\_index

```python
@classmethod
def get_texture_coordinate_index(
        cls, component: PrimitiveComponent,
        property_: CesiumPropertyTextureProperty) -> int
```

deprecated: 'get_texture_coordinate_index' was renamed to 'get_unreal_uv_channel'.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_swizzle"></a>

#### get\_swizzle

```python
@classmethod
def get_swizzle(cls, property_: CesiumPropertyTextureProperty) -> str
```

X.get_swizzle(property_) -> str

deprecated: Swizzles are no longer hardcoded in Unreal materials. To see what channels the property uses, use GetChannels instead.
brief: Get the string representing how the metadata is encoded into a pixel color. This is useful to unpack the correct order of the metadata components from the pixel color.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    str:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_scale"></a>

#### get\_scale

```python
@classmethod
def get_scale(cls,
              property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_scale(property_) -> CesiumMetadataValue
Gets the scale of this property. This can be defined by the class property
that it implements, or overridden by the instance of the property itself.

This is only applicable to properties with floating-point or normalized
integer component types. If a scale is not defined or applicable, this
returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The scale of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_raw_value"></a>

#### get\_raw\_value

```python
@classmethod
def get_raw_value(cls, property_: CesiumPropertyTextureProperty,
                  uv: Vector2D) -> CesiumMetadataValue
```

X.get_raw_value(property_, uv) -> CesiumMetadataValue
Retrieves the raw value of the property for the given feature. This is the
value of the property without normalization, offset, or scale applied.

If this property specifies a "no data" value, and the raw value is equal to
this "no data" value, the value is returned as-is.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.

Returns:
    CesiumMetadataValue: The raw property value.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_property_texture_property_status"></a>

#### get\_property\_texture\_property\_status

```python
@classmethod
def get_property_texture_property_status(
    cls, property_: CesiumPropertyTextureProperty
) -> CesiumPropertyTexturePropertyStatus
```

X.get_property_texture_property_status(property_) -> CesiumPropertyTexturePropertyStatus
Gets the status of the property texture property. If this property texture
property is invalid in any way, this will briefly indicate why.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumPropertyTexturePropertyStatus:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_offset"></a>

#### get\_offset

```python
@classmethod
def get_offset(
        cls, property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_offset(property_) -> CesiumMetadataValue
Gets the offset of this property. This can be defined by the class property
that it implements, or overridden by the instance of the property itself.

This is only applicable to properties with floating-point or normalized
integer component types. If an offset is not defined or applicable, this
returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The offset of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_no_data_value"></a>

#### get\_no\_data\_value

```python
@classmethod
def get_no_data_value(
        cls, property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_no_data_value(property_) -> CesiumMetadataValue
Gets the "no data" value of this property, as defined by its class
property. This value functions a sentinel value, indicating missing data
wherever it appears. The value is compared against the property's raw data,
without normalization, offset, or scale applied.

This is not applicable to boolean properties. If a "no data" value is
not defined or applicable, this returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The "no data" value of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_minimum_value"></a>

#### get\_minimum\_value

```python
@classmethod
def get_minimum_value(
        cls, property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_minimum_value(property_) -> CesiumMetadataValue
Gets the minimum value of this property. This can be defined by the class
property that it implements, or overridden by the instance of the property
itself.

This is only applicable to scalar, vecN and matN properties. It represents
the component-wise minimum of all property values with normalization,
offset, and scale applied. If a minimum value is not defined or
applicable, this returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The minimum value of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_maximum_value"></a>

#### get\_maximum\_value

```python
@classmethod
def get_maximum_value(
        cls, property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_maximum_value(property_) -> CesiumMetadataValue
Gets the maximum value of this property. This can be defined by the class
property that it implements, or overridden by the instance of the property
itself.

This is only applicable to scalar, vecN and matN properties. It represents
the component-wise maximum of all property values with normalization,
offset, and scale applied. If a maximum value is not defined or applicable,
this returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The maximum value of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_int_vector"></a>

#### get\_int\_vector

```python
@classmethod
def get_int_vector(cls, property_: CesiumPropertyTextureProperty, uv: Vector2D,
                   default_value: IntVector) -> IntVector
```

X.get_int_vector(property_, uv, default_value) -> IntVector
Attempts to retrieve the value at the given texture coordinates as a
FIntVector.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a 3-dimensional vector, its components will be converted
to 32-bit signed integers if possible.

- If the value is a 4-dimensional vector, it will use the first three
components to construct the FIntVector.

- If the value is a 2-dimensional vector, it will become the XY-components
of the FIntVector. The Z component will be set to zero.

- If the value is a scalar that can be converted to a 32-bit signed
integer, the resulting FIntVector will have this value in all of its
components.

In all other cases, the user-defined default value is returned. In all
vector cases, if any of the relevant components cannot be represented as a
32-bit signed integer, the default value is returned.

If the property texture property is somehow invalid, the user-defined
default value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (IntVector): The default value to fall back on.

Returns:
    IntVector: The property value as a FIntVector.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_int_point"></a>

#### get\_int\_point

```python
@classmethod
def get_int_point(cls, property_: CesiumPropertyTextureProperty, uv: Vector2D,
                  default_value: IntPoint) -> IntPoint
```

X.get_int_point(property_, uv, default_value) -> IntPoint
Attempts to retrieve the value at the given texture coordinates as a
FIntPoint.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a 2-dimensional vector, its components will be converted
to 32-bit signed integers if possible.

- If the value is a 3- or 4-dimensional vector, it will use the first two
components to construct the FIntPoint.

- If the value is a scalar that can be converted to a 32-bit signed
integer, the resulting FIntPoint will have this value in both of its
components.

In all other cases, the user-defined default value is returned. In all
vector cases, if any of the relevant components cannot be represented as a
32-bit signed, the default value is returned.

If the property texture property is somehow invalid, the user-defined
default value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (IntPoint): The default value to fall back on.

Returns:
    IntPoint: The property value as a FIntPoint.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_integer"></a>

#### get\_integer

```python
@classmethod
def get_integer(cls,
                property_: CesiumPropertyTextureProperty,
                uv: Vector2D,
                default_value: int = 0) -> int
```

X.get_integer(property_, uv, default_value=0) -> int32
Attempts to retrieve the value at the given texture coordinates as a signed
32-bit integer.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if
possible. If the property-defined default value cannot be converted, or
does not exist, then the user-defined default value is returned.

Property values are converted as follows:

- If the value is an integer between -2,147,483,648 and 2,147,483,647, it
is returned as-is.
- If the value is a floating-point number in the aforementioned range, it
is truncated (rounded toward zero) and returned.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (int32): The default value to fall back on.

Returns:
    int32: The property value as an Integer.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_gltf_texture_coordinate_set_index"></a>

#### get\_gltf\_texture\_coordinate\_set\_index

```python
@classmethod
def get_gltf_texture_coordinate_set_index(
        cls, property_: CesiumPropertyTextureProperty) -> int
```

X.get_gltf_texture_coordinate_set_index(property_) -> int64
Gets the glTF texture coordinate set index used by the property texture
property. This is the index N corresponding to the "TEXCOORD_N" attribute
on the glTF primitive that samples this texture.

If the property texture property is invalid, this returns -1.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    int64:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_float64"></a>

#### get\_float64

```python
@classmethod
def get_float64(cls,
                property_: CesiumPropertyTextureProperty,
                uv: Vector2D,
                default_value: float = 0.000000) -> float
```

X.get_float64(property_, uv, default_value=0.000000) -> double
Attempts to retrieve the value at the given texture coordinates as a
double-precision floating-point number.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is a single- or double-precision floating-point number, it
is returned as-is.

- If the value is an integer, it is converted to the closest representable
double-precision floating-point number.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (double): The default value to fall back on.

Returns:
    double: The property value as a Float.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_float"></a>

#### get\_float

```python
@classmethod
def get_float(cls,
              property_: CesiumPropertyTextureProperty,
              uv: Vector2D,
              default_value: float = 0.000000) -> float
```

X.get_float(property_, uv, default_value=0.000000) -> float
Attempts to retrieve the value at the given texture coordinates as a
single-precision floating-point number.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is already a single-precision floating-point
number, it is returned as-is.

- If the value is a scalar of any other type within the range of values
that a single-precision float can represent, it is converted to its closest
representation as a single-precision float and returned.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (float): The default value to fall back on.

Returns:
    float: The property value as a Float.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_default_value"></a>

#### get\_default\_value

```python
@classmethod
def get_default_value(
        cls, property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
```

X.get_default_value(property_) -> CesiumMetadataValue
Gets the default value of this property, as defined by its class
property. This default value is used use when encountering a "no data"
value in the property.

If a default value is not defined, this returns an empty value.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataValue: The default value of the property.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_component_count"></a>

#### get\_component\_count

```python
@classmethod
def get_component_count(cls, property_: CesiumPropertyTextureProperty) -> int
```

X.get_component_count(property_) -> int64

deprecated: Use GetChannels to get the channels array of a property texture property instead.
brief: Get the component count of this property. Since the metadata is encoded as pixel color, this is also the number of meaningful channels it will use.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    int64:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_channels"></a>

#### get\_channels

```python
@classmethod
def get_channels(cls, property_: CesiumPropertyTextureProperty) -> Array[int]
```

X.get_channels(property_) -> Array[int64]

brief: Get the channels array of this property. This contains the indices of the meaningful texel channels that will be used when sampling the property texture.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    Array[int64]:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_byte"></a>

#### get\_byte

```python
@classmethod
def get_byte(cls,
             property_: CesiumPropertyTextureProperty,
             uv: Vector2D,
             default_value: int = 0) -> int
```

X.get_byte(property_, uv, default_value=0) -> uint8
Attempts to retrieve the value at the given texture coordinates as an
unsigned 8-bit integer.

For numeric properties, the raw value for the given coordinates will be
transformed by the property's normalization, scale, and offset before it is
further converted. If the raw value is equal to the property's "no data"
value, then the property's default value will be converted if possible. If
the property-defined default value cannot be converted, or does not exist,
then the user-defined default value is returned.

Property values are converted as follows:

- If the value is an integer between 0 and 255, it is returned as-is.
- If the value is a floating-point number in the aforementioned range, it
is truncated (rounded toward zero) and returned.

In all other cases, the user-defined default value is returned. If the
property texture property is somehow invalid, the user-defined default
value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.
    default_value (uint8): The default value to fall back on.

Returns:
    uint8: The property value as a Byte.

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_blueprint_type"></a>

#### get\_blueprint\_type

```python
@classmethod
def get_blueprint_type(
        cls, property_: CesiumPropertyTextureProperty
) -> CesiumMetadataBlueprintType
```

X.get_blueprint_type(property_) -> CesiumMetadataBlueprintType
Gets the best-fitting type for the property that is accessible from
Blueprints. For the most precise representation of the values possible in
Blueprints, you should retrieve it using this type.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array_size"></a>

#### get\_array\_size

```python
@classmethod
def get_array_size(cls, property_: CesiumPropertyTextureProperty) -> int
```

X.get_array_size(property_) -> int64
Gets the number of elements in an array of this property. Only
applicable when the property is a fixed-length array type.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    int64:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array_element_blueprint_type"></a>

#### get\_array\_element\_blueprint\_type

```python
@classmethod
def get_array_element_blueprint_type(
        cls, property_: CesiumPropertyTextureProperty
) -> CesiumMetadataBlueprintType
```

X.get_array_element_blueprint_type(property_) -> CesiumMetadataBlueprintType
Gets the best-fitting Blueprints type for the elements in this property's
array values. If the given property does not contain array values, this
returns None.

Args:
    property_ (CesiumPropertyTextureProperty): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array"></a>

#### get\_array

```python
@classmethod
def get_array(cls, property_: CesiumPropertyTextureProperty,
              uv: Vector2D) -> CesiumPropertyArray
```

X.get_array(property_, uv) -> CesiumPropertyArray
Attempts to retrieve the value for the given texture coordinates as a
FCesiumPropertyArray. If the property is not an array type, this returns an
empty array.

For numeric array properties, the raw array value for a given coordinates
will be transformed by the property's normalization, scale, and offset
before it is further converted. If the raw value is equal to the property's
"no data" value, then the property's default value will be converted if
possible. If the property-defined default value cannot be converted, or
does not exist, then the user-defined default value is returned.

Args:
    property_ (CesiumPropertyTextureProperty): 
    uv (Vector2D): The texture coordinates.

Returns:
    CesiumPropertyArray: The property value as a FCesiumPropertyArray.

<a id="unreal.CesiumSampleHeightMostDetailedAsyncAction"></a>