## CesiumPropertyArrayBlueprintLibrary Objects

```python
class CesiumPropertyArrayBlueprintLibrary(BlueprintFunctionLibrary)
```

Blueprint library functions for acting on an array property in
EXT_structural_metadata.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyArrayBlueprintLibrary.h

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_value"></a>

#### get\_value

```python
@classmethod
def get_value(cls, array: CesiumPropertyArray,
              index: int) -> CesiumMetadataValue
```

X.get_value(array, index) -> CesiumMetadataValue
Retrieves an element from the array as a FCesiumMetadataValue. The value
can then be retrieved as a specific Blueprints type.

If the index is out-of-bounds, this returns a bogus FCesiumMetadataValue of
an unknown type.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.

Returns:
    CesiumMetadataValue: The element as a FCesiumMetadataValue.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_true_component_type"></a>

#### get\_true\_component\_type

```python
@classmethod
def get_true_component_type(
        cls, array: CesiumPropertyArray) -> CesiumMetadataTrueType_DEPRECATED
```

X.get_true_component_type(array) -> CesiumMetadataTrueType_DEPRECATED
Gets true type of the elements in the array. Many of these types are not
accessible from Blueprints, but can be converted to a Blueprint-accessible
type.
deprecated: CesiumMetadataTrueType is deprecated. Use GetElementValueType instead.

Args:
    array (CesiumPropertyArray): 

Returns:
    CesiumMetadataTrueType_DEPRECATED:

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_string"></a>

#### get\_string

```python
@classmethod
def get_string(cls,
               array: CesiumPropertyArray,
               index: int,
               default_value: str = "") -> str
```

X.get_string(array, index, default_value="") -> str
Retrieves an element from the array and attempts to convert it to a string
value.

Numeric elements are converted to a string with `FString::Format`, which
uses the current locale.

Boolean elements are converted to "true" or "false".

String elements are returned directly.
deprecated: GetString is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (str): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    str: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_size"></a>

#### get\_size

```python
@classmethod
def get_size(cls, array: CesiumPropertyArray) -> int
```

X.get_size(array) -> int64
Gets the number of elements in the array. Returns 0 if the elements have
an unknown type.
deprecated: Use GetArraySize instead.

Args:
    array (CesiumPropertyArray): 

Returns:
    int64: The number of elements in the array.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_integer64"></a>

#### get\_integer64

```python
@classmethod
def get_integer64(cls,
                  array: CesiumPropertyArray,
                  index: int,
                  default_value: int = 0) -> int
```

X.get_integer64(array, index, default_value=0) -> int64
This function is deprecated. Use Cesium > Metadata > Property Array >
GetValue instead.

Retrieves an element from the array and attempts to convert it to a signed
64-bit integer value.

If the element is an integer and between -2^63-1 and 2^63-1, it is returned
directly.

If the element is a floating-point number, it is truncated (rounded
toward zero).

If the element is a boolean, 0 is returned for false and 1 for true.

If the element is a string and the entire string can be parsed as an
integer in the valid range, the parsed value is returned. If it can be
parsed as a floating-point number, the parsed value is truncated (rounded
toward zero). In either case, the string is parsed in a locale-independent
way and does not support use of a comma or other character to group digits.

Otherwise, the default value is returned.
deprecated: GetInteger64 is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (int64): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    int64: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_integer"></a>

#### get\_integer

```python
@classmethod
def get_integer(cls,
                array: CesiumPropertyArray,
                index: int,
                default_value: int = 0) -> int
```

X.get_integer(array, index, default_value=0) -> int32
Retrieves an element from the array and attempts to convert it to a signed
32-bit integer value.

If the element is an integer and between -2,147,483,647 and 2,147,483,647,
it is returned directly.

If the element is a floating-point number, it is truncated (rounded
toward zero).

If the element is a boolean, 0 is returned for false and 1 for true.

If the element is a string and the entire string can be parsed as an
integer in the valid range, the parsed value is returned. If it can be
parsed as a floating-point number, the parsed value is truncated (rounded
toward zero). In either case, the string is parsed in a locale-independent
way and does not support use of a comma or other character to group digits.

Otherwise, the default value is returned.
deprecated: GetInteger is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (int32): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    int32: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_float64"></a>

#### get\_float64

```python
@classmethod
def get_float64(cls, array: CesiumPropertyArray, index: int,
                default_value: float) -> float
```

X.get_float64(array, index, default_value) -> double
Retrieves an element from the array and attempts to convert it to a 64-bit
floating-point value.

If the element is a single- or double-precision floating-point number, is
is returned.

If the element is an integer, it is converted to the closest representable
double-precision floating-point number.

If the element is a boolean, 0.0 is returned for false and 1.0 for true.

If the element is a string and the entire string can be parsed as a
number, the parsed value is returned. The string is parsed in a
locale-independent way and does not support use of a comma or other
character to group digits.

Otherwise, the default value is returned.
deprecated: GetFloat64 is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (double): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    double: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_float"></a>

#### get\_float

```python
@classmethod
def get_float(cls,
              array: CesiumPropertyArray,
              index: int,
              default_value: float = 0.000000) -> float
```

X.get_float(array, index, default_value=0.000000) -> float
Retrieves an element from the array and attempts to convert it to a 32-bit
floating-point value.

If the element is a single-precision floating-point number, is is returned.

If the element is an integer or double-precision floating-point number,
it is converted to the closest representable single-precision
floating-point number.

If the element is a boolean, 0.0 is returned for false and 1.0 for true.

If the element is a string and the entire string can be parsed as a
number, the parsed value is returned. The string is parsed in a
locale-independent way and does not support use of a comma or other
character to group digits.

Otherwise, the default value is returned.
deprecated: GetFloat is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (float): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    float: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_element_value_type"></a>

#### get\_element\_value\_type

```python
@classmethod
def get_element_value_type(
        cls, array: CesiumPropertyArray) -> CesiumMetadataValueType
```

X.get_element_value_type(array) -> CesiumMetadataValueType
Gets the true value type of the elements in the array. Many of these types
are not accessible from Blueprints, but can be converted to a
Blueprint-accessible type.

Args:
    array (CesiumPropertyArray): 

Returns:
    CesiumMetadataValueType:

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_element_blueprint_type"></a>

#### get\_element\_blueprint\_type

```python
@classmethod
def get_element_blueprint_type(
        cls, array: CesiumPropertyArray) -> CesiumMetadataBlueprintType
```

X.get_element_blueprint_type(array) -> CesiumMetadataBlueprintType
Gets the best-fitting Blueprints type for the elements of this array.

Args:
    array (CesiumPropertyArray): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_byte"></a>

#### get\_byte

```python
@classmethod
def get_byte(cls,
             array: CesiumPropertyArray,
             index: int,
             default_value: int = 0) -> int
```

X.get_byte(array, index, default_value=0) -> uint8
Retrieves an element from the array and attempts to convert it to an
unsigned 8-bit integer value.

If the element is an integer and between 0 and 255, it is returned
directly.

If the element is a floating-point number, it is truncated (rounded
toward zero).

If the element is a boolean, 0 is returned for false and 1 for true.

If the element is a string and the entire string can be parsed as an
integer between 0 and 255, the parsed value is returned. The string is
parsed in a locale-independent way and does not support use of a comma or
other character to group digits.

Otherwise, the default value is returned.
deprecated: GetByte is deprecated on arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (uint8): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    uint8: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_boolean"></a>

#### get\_boolean

```python
@classmethod
def get_boolean(cls,
                array: CesiumPropertyArray,
                index: int,
                default_value: bool = False) -> bool
```

X.get_boolean(array, index, default_value=False) -> bool
Retrieves an element from the array and attempts to convert it to a Boolean
value.

If the element is boolean, it is returned directly.

If the element is numeric, zero is converted to false, while any other
value is converted to true.

If the element is a string, "0", "false", and "no" (case-insensitive) are
converted to false, while "1", "true", and "yes" are converted to true.
All other strings, including strings that can be converted to numbers,
will return the default value.

Other types of elements will return the default value.
deprecated: GetBoolean is deprecated for metadata arrays. Use GetValue instead.

Args:
    array (CesiumPropertyArray): 
    index (int64): The index of the array element to retrieve.
    default_value (bool): The default value to use if the index is invalid or the element's value cannot be converted.

Returns:
    bool: The element value.

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_blueprint_component_type"></a>

#### get\_blueprint\_component\_type

```python
@classmethod
def get_blueprint_component_type(
        cls, array: CesiumPropertyArray) -> CesiumMetadataBlueprintType
```

X.get_blueprint_component_type(array) -> CesiumMetadataBlueprintType
Gets the best-fitting Blueprints type for the elements of this array.
deprecated: Use GetElementBlueprintType instead.

Args:
    array (CesiumPropertyArray): 

Returns:
    CesiumMetadataBlueprintType:

<a id="unreal.CesiumPropertyArrayBlueprintLibrary.get_array_size"></a>

#### get\_array\_size

```python
@classmethod
def get_array_size(cls, array: CesiumPropertyArray) -> int
```

X.get_array_size(array) -> int64
Gets the number of elements in the array. Returns 0 if the elements have
an unknown type.

Args:
    array (CesiumPropertyArray): 

Returns:
    int64: The number of elements in the array.

<a id="unreal.CesiumMetadataArrayBlueprintLibrary"></a>