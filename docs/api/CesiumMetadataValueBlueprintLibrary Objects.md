## CesiumMetadataValueBlueprintLibrary Objects

```python
class CesiumMetadataValueBlueprintLibrary(BlueprintFunctionLibrary)
```

Cesium Metadata Value Blueprint Library

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataValue.h

<a id="unreal.CesiumMetadataValueBlueprintLibrary.is_empty"></a>

#### is\_empty

```python
@classmethod
def is_empty(cls, value: CesiumMetadataValue) -> bool
```

X.is_empty(value) -> bool
Whether the value is empty, i.e., whether it does not actually represent
any data. An empty value functions as a null value, and can be compared to
a std::nullopt in C++. For example, when the raw value of a property
matches the property's specified "no data" value, it will return an empty
FCesiumMetadataValue.

Args:
    value (CesiumMetadataValue): 

Returns:
    bool: Whether the value is empty.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_vector4"></a>

#### get\_vector4

```python
@classmethod
def get_vector4(cls, value: CesiumMetadataValue,
                default_value: Vector4) -> Vector4
```

X.get_vector4(value, default_value) -> Vector4
Attempts to retrieve the value as a FVector4.

If the value is a 4-dimensional vector, its components will be converted to
double-precision floating-point numbers.

If the value is a 3-dimensional vector, it will become the XYZ-components
of the FVector4. The W-component will be set to zero.

If the value is a 2-dimensional vector, it will become the XY-components of
the FVector4. The Z- and W-components will be set to zero.

If the value is a scalar, then the resulting FVector4 will have this value
as a double-precision floating-point number in all of its components.

If the value is a boolean, (1.0, 1.0, 1.0, 1.0) is returned for true, while
(0.0, 0.0, 0.0, 0.0) is returned for false.

If the value is a string that can be parsed as a FVector4, the parsed
value is returned. This follows the rules of FVector4::InitFromString. The
string must be formatted as "X=... Y=... Z=... W=...". The W-component is
optional; if absent, it will be set to 1.0.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (Vector4): The default value to use if the given value cannot be converted to a FVector4.

Returns:
    Vector4: The value as a FVector4.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_vector3f"></a>

#### get\_vector3f

```python
@classmethod
def get_vector3f(cls, value: CesiumMetadataValue,
                 default_value: Vector3f) -> Vector3f
```

X.get_vector3f(value, default_value) -> Vector3f
Attempts to retrieve the value as a FVector3f.

If the value is a 3-dimensional vector, its components will be converted to
the closest representable single-precision floats, if possible.

If the value is a 4-dimensional vector, a FVector3f containing the first
three components will be returned.

If the value is a 2-dimensional vector, it will become the XY-components of
the FVector3f. The Z-component will be set to zero.

If the value is a scalar that can be converted to a single-precision
floating-point number, then the resulting FVector3f will have this value in
all of its components.

If the value is a boolean, (1.0f, 1.0f, 1.0f) is returned for true, while
(0.0f, 0.0f, 0.0f) is returned for false.

If the value is a string that can be parsed as a FVector3f, the parsed
value is returned. The string must be formatted as "X=... Y=... Z=".

In all other cases, the default value is returned. In all vector cases, if
any of the relevant components cannot be represented as a single-precision
float, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (Vector3f): The default value to use if the given value cannot be converted to a FVector3f.

Returns:
    Vector3f: The value as a FVector3f.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_vector2d"></a>

#### get\_vector2d

```python
@classmethod
def get_vector2d(cls, value: CesiumMetadataValue,
                 default_value: Vector2D) -> Vector2D
```

X.get_vector2d(value, default_value) -> Vector2D
Attempts to retrieve the value as a FVector2D.

If the value is a 2-dimensional vector, its components will be converted to
double-precision floating-point numbers.

If the value is a 3- or 4-dimensional vector, it will use the first two
components to construct the FVector2D.

If the value is a scalar, the resulting FVector2D will have this value in
both of its components.

If the value is a boolean, (1.0, 1.0) is returned for true, while (0.0,
0.0) is returned for false.

If the value is a string that can be parsed as a FVector2D, the parsed
value is returned. The string must be formatted as "X=... Y=...".

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (Vector2D): The default value to use if the given value cannot be converted to a FIntPoint.

Returns:
    Vector2D: The value as a FIntPoint.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_vector"></a>

#### get\_vector

```python
@classmethod
def get_vector(cls, value: CesiumMetadataValue,
               default_value: Vector) -> Vector
```

X.get_vector(value, default_value) -> Vector
Attempts to retrieve the value as a FVector.

If the value is a 3-dimensional vector, its components will be converted to
double-precision floating-point numbers.

If the value is a 4-dimensional vector, a FVector containing the first
three components will be returned.

If the value is a 2-dimensional vector, it will become the XY-components of
the FVector. The Z-component will be set to zero.

If the value is a scalar, then the resulting FVector will have this value
as a double-precision floating-point number in all of its components.

If the value is a boolean, (1.0, 1.0, 1.0) is returned for true, while
(0.0, 0.0, 0.0) is returned for false.

If the value is a string that can be parsed as a FVector, the parsed
value is returned. The string must be formatted as "X=... Y=... Z=".

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (Vector): The default value to use if the given value cannot be converted to a FVector.

Returns:
    Vector: The value as a FVector.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_value_type"></a>

#### get\_value\_type

```python
@classmethod
def get_value_type(cls, value: CesiumMetadataValue) -> CesiumMetadataValueType
```

X.get_value_type(value) -> CesiumMetadataValueType
Gets the type of the metadata value as defined in the
EXT_structural_metadata extension. Many of these types are not accessible
from Blueprints, but can be converted to a Blueprint-accessible type.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumMetadataValueType:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_values_as_strings"></a>

#### get\_values\_as\_strings

```python
@classmethod
def get_values_as_strings(
        cls, values: Map[str, CesiumMetadataValue]) -> Map[str, str]
```

X.get_values_as_strings(values) -> Map[str, str]
Gets the given map of metadata values as a new map of strings, mapped by
name. This is useful for displaying the values from a property table or
property texture as strings in a user interface.

Array properties cannot be converted to strings, so empty strings
will be returned for their values.

Args:
    values (Map[str, CesiumMetadataValue]): 

Returns:
    Map[str, str]:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_true_type"></a>

#### get\_true\_type

```python
@classmethod
def get_true_type(
        cls, value: CesiumMetadataValue) -> CesiumMetadataTrueType_DEPRECATED
```

X.get_true_type(value) -> CesiumMetadataTrueType_DEPRECATED
Gets true type of the value. Many of these types are not accessible
from Blueprints, but can be converted to a Blueprint-accessible type.
deprecated: CesiumMetadataTrueType is deprecated. Use GetValueType to get the CesiumMetadataValueType instead.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumMetadataTrueType_DEPRECATED:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_true_component_type"></a>

#### get\_true\_component\_type

```python
@classmethod
def get_true_component_type(
        cls, value: CesiumMetadataValue) -> CesiumMetadataTrueType_DEPRECATED
```

X.get_true_component_type(value) -> CesiumMetadataTrueType_DEPRECATED
Gets true type of the elements in the array. If this value is not an array,
the component type will be None. Many of these types are not accessible
from Blueprints, but can be converted to a Blueprint-accessible type.
deprecated: CesiumMetadataTrueType is deprecated. Use GetValueType to get the CesiumMetadataValueType instead.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumMetadataTrueType_DEPRECATED:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_string"></a>

#### get\_string

```python
@classmethod
def get_string(cls, value: CesiumMetadataValue, default_value: str) -> str
```

X.get_string(value, default_value) -> str
Attempts to retrieve the value as a FString.

String properties are returned as-is.

Scalar values are converted to a string with `std::to_string`.

Boolean properties are converted to "true" or "false".

Vector properties are returned as strings in the format "X=... Y=... Z=...
W=..." depending on how many components they have.

Matrix properties are returned as strings row-by-row, where each row's
values are printed between square brackets. For example, a 2-by-2 matrix
will be printed out as "[A B] [C D]".

Array properties return the default value.

Args:
    value (CesiumMetadataValue): 
    default_value (str): The default value to use if the given value cannot be converted to a FString.

Returns:
    str: The value as a FString.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_matrix"></a>

#### get\_matrix

```python
@classmethod
def get_matrix(cls, value: CesiumMetadataValue,
               default_value: Matrix) -> Matrix
```

X.get_matrix(value, default_value) -> Matrix
Attempts to retrieve the value as a FMatrix.

If the value is a 4-by-4 matrix, its components will be converted to
double-precision floating-point numbers.

If the value is a 3-by-3 matrix, it will initialize the corresponding
entries of the FMatrix, while all other entries are set to zero. In other
words, the 3-by-3 matrix is returned in an FMatrix where the fourth row and
column are filled with zeroes.

If the value is a 2-by-2 matrix, it will initialize the corresponding
entries of the FMatrix, while all other entries are set to zero. In other
words, the 2-by-2 matrix is returned in an FMatrix where the third and
fourth rows / columns are filled with zeroes.

If the value is a scalar, then the resulting FMatrix will have this value
along its diagonal, including the very last component. All other entries
will be zero.

If the value is a boolean, it is converted to 1.0 for true and 0.0 for
false. Then, the resulting FMatrix will have this value along its diagonal,
including the very last component. All other entries will be zero.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (Matrix): The default value to use if the given value cannot be converted to a FMatrix.

Returns:
    Matrix: The value as a FMatrix.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_int_vector"></a>

#### get\_int\_vector

```python
@classmethod
def get_int_vector(cls, value: CesiumMetadataValue,
                   default_value: IntVector) -> IntVector
```

X.get_int_vector(value, default_value) -> IntVector
Attempts to retrieve the value as a FIntVector.

If the value is a 3-dimensional vector, its components will be converted to
32-bit signed integers if possible.

If the value is a 4-dimensional vector, it will use the first three
components to construct the FIntVector.

If the value is a 2-dimensional vector, it will become the XY-components of
the FIntVector. The Z component will be set to zero.

If the value is a scalar that can be converted to a 32-bit signed integer,
the resulting FIntVector will have this value in all of its components.

If the value is a boolean, (1, 1, 1) is returned for true, while (0, 0, 0)
is returned for false.

If the value is a string that can be parsed as a FIntVector, the parsed
value is returned. The string must be formatted as "X=... Y=... Z=".

In all other cases, the default value is returned. In all vector cases, if
any of the relevant components cannot be represented as a 32-bit signed
integer, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (IntVector): The default value to use if the given value cannot be converted to a FIntVector.

Returns:
    IntVector: The value as a FIntVector.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_int_point"></a>

#### get\_int\_point

```python
@classmethod
def get_int_point(cls, value: CesiumMetadataValue,
                  default_value: IntPoint) -> IntPoint
```

X.get_int_point(value, default_value) -> IntPoint
Attempts to retrieve the value as a FIntPoint.

If the value is a 2-dimensional vector, its components will be converted to
32-bit signed integers if possible.

If the value is a 3- or 4-dimensional vector, it will use the first two
components to construct the FIntPoint.

If the value is a scalar that can be converted to a 32-bit signed integer,
the resulting FIntPoint will have this value in both of its components.

If the value is a boolean, (1, 1) is returned for true, while (0, 0) is
returned for false.

If the value is a string that can be parsed as a FIntPoint, the parsed
value is returned. The string must be formatted as "X=... Y=...".

In all other cases, the default value is returned. In all vector cases, if
any of the relevant components cannot be represented as a 32-bit signed,
the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (IntPoint): The default value to use if the given value cannot be converted to a FIntPoint.

Returns:
    IntPoint: The value as a FIntPoint.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_integer64"></a>

#### get\_integer64

```python
@classmethod
def get_integer64(cls, value: CesiumMetadataValue, default_value: int) -> int
```

X.get_integer64(value, default_value) -> int64
Attempts to retrieve the value as a signed 64-bit integer.

If the value is an integer and between -2^63 and (2^63 - 1),
it is returned as-is.

If the value is a floating-point number in the aforementioned range, it
is truncated (rounded toward zero) and returned;

If the value is a boolean, 1 is returned for true and 0 for false.

If the value is a string and the entire string can be parsed as an
integer in the valid range, the parsed value is returned. If it can be
parsed as a floating-point number, the parsed value is truncated (rounded
toward zero). In either case, the string is parsed in a locale-independent
way and does not support the use of commas or other delimiters to group
digits together.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (int64): The default value to use if the given value cannot be converted to an Integer64.

Returns:
    int64: The value as an Integer64.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_integer"></a>

#### get\_integer

```python
@classmethod
def get_integer(cls, value: CesiumMetadataValue, default_value: int) -> int
```

X.get_integer(value, default_value) -> int32
Attempts to retrieve the value as a signed 32-bit integer.

If the value is an integer between -2,147,483,648 and 2,147,483,647,
it is returned as-is.

If the value is a floating-point number in the aforementioned range, it is
truncated (rounded toward zero) and returned;

If the value is a boolean, 1 is returned for true and 0 for false.

If the value is a string and the entire string can be parsed as an
integer in the valid range, the parsed value is returned. If it can be
parsed as a floating-point number, the parsed value is truncated (rounded
toward zero). In either case, the string is parsed in a locale-independent
way and does not support the use of commas or other delimiters to group
digits together.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (int32): The default value to use if the given value cannot be converted to an Integer.

Returns:
    int32: The value as an Integer.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_float64"></a>

#### get\_float64

```python
@classmethod
def get_float64(cls, value: CesiumMetadataValue,
                default_value: float) -> float
```

X.get_float64(value, default_value) -> double
Attempts to retrieve the value as a double-precision floating-point number.

If the value is a single- or double-precision floating-point number, it is
returned as-is.

If the value is an integer, it is converted to the closest representable
double-precision floating-point number.

If the value is a boolean, 1.0 is returned for true and 0.0 for false.

If the value is a string and the entire string can be parsed as a
number, the parsed value is returned. The string is parsed in a
locale-independent way and does not support the use of commas or other
delimiters to group digits together.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (double): The default value to use if the given value cannot be converted to a Float64.

Returns:
    double: The value as a Float64.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_float"></a>

#### get\_float

```python
@classmethod
def get_float(cls, value: CesiumMetadataValue, default_value: float) -> float
```

X.get_float(value, default_value) -> float
Attempts to retrieve the value as a single-precision floating-point number.

If the value is already a single-precision floating-point number, it is
returned as-is.

If the value is a scalar of any other type within the range of values that
a single-precision float can represent, it is converted to its closest
representation as a single-precision float and returned.

If the value is a boolean, 1.0f is returned for true and 0.0f for false.

If the value is a string, and the entire string can be parsed as a
number, the parsed value is returned. The string is parsed in a
locale-independent way and does not support the use of a comma or other
delimiter to group digits togther.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (float): The default value to use if the given value cannot be converted to a Float.

Returns:
    float: The value as a Float.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_byte"></a>

#### get\_byte

```python
@classmethod
def get_byte(cls, value: CesiumMetadataValue, default_value: int) -> int
```

X.get_byte(value, default_value) -> uint8
Attempts to retrieve the value as an unsigned 8-bit integer.

If the value is an integer between 0 and 255, it is returned
as-is.

If the value is a floating-point number in the aforementioned range, it is
truncated (rounded toward zero) and returned.

If the value is a boolean, 1 is returned for true and 0 for false.

If the value is a string and the entire string can be parsed as an
integer between 0 and 255, the parsed value is returned. The string is
parsed in a locale-independent way and does not support the use of commas
or other delimiters to group digits together.

In all other cases, the default value is returned.

Args:
    value (CesiumMetadataValue): 
    default_value (uint8): The default value to use if the given value cannot be converted to a Byte.

Returns:
    uint8: The value as a Byte.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_boolean"></a>

#### get\_boolean

```python
@classmethod
def get_boolean(cls, value: CesiumMetadataValue, default_value: bool) -> bool
```

X.get_boolean(value, default_value) -> bool
Attempts to retrieve the value as a boolean.

If the value is a boolean, it is returned as-is.

If the value is a scalar, zero is converted to false, while any other
value is converted to true.

If the value is a string, "0", "false", and "no" (case-insensitive) are
converted to false, while "1", "true", and "yes" are converted to true.
All other strings, including strings that can be converted to numbers,
will return the default value.

All other types return the default value.

Args:
    value (CesiumMetadataValue): 
    default_value (bool): The default value to use if the given value cannot be converted to a Boolean.

Returns:
    bool: The value as a Boolean.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_blueprint_type"></a>

#### get\_blueprint\_type

```python
@classmethod
def get_blueprint_type(
        cls, value: CesiumMetadataValue) -> CesiumMetadataBlueprintType
```

X.get_blueprint_type(value) -> CesiumMetadataBlueprintType
Gets the best-fitting Blueprints type for this value. For the most precise
representation of the value possible from Blueprints, you should retrieve
it using this type.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_array_element_blueprint_type"></a>

#### get\_array\_element\_blueprint\_type

```python
@classmethod
def get_array_element_blueprint_type(
        cls, value: CesiumMetadataValue) -> CesiumMetadataBlueprintType
```

X.get_array_element_blueprint_type(value) -> CesiumMetadataBlueprintType
Gets the best-fitting Blueprints type for the elements of this array value.
If the given value is not of an array type, this returns None.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_blueprint_component_type"></a>

#### get\_blueprint\_component\_type

```python
@classmethod
def get_blueprint_component_type(
        cls, value: CesiumMetadataValue) -> CesiumMetadataBlueprintType
```

deprecated: 'get_blueprint_component_type' was renamed to 'get_array_element_blueprint_type'.

<a id="unreal.CesiumMetadataValueBlueprintLibrary.get_array"></a>

#### get\_array

```python
@classmethod
def get_array(cls, value: CesiumMetadataValue) -> CesiumPropertyArray
```

X.get_array(value) -> CesiumPropertyArray
Attempts to retrieve the value as a FCesiumPropertyArray. If the property
is not an array type, this returns an empty array.

Args:
    value (CesiumMetadataValue): 

Returns:
    CesiumPropertyArray: The value as a FCesiumPropertyArray.

<a id="unreal.CesiumMetadataGenericValueBlueprintLibrary"></a>