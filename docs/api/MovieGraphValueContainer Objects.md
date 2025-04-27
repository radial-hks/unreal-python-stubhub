## MovieGraphValueContainer Objects

```python
class MovieGraphValueContainer(Object)
```

Holds a generic value, with an API for getting/setting the value, as well as getting/setting its type
and container (eg, array).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphValueContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (InstancedPropertyBag):  [Read-Write] The value held by this object.

<a id="unreal.MovieGraphValueContainer.set_value_type_object"></a>

#### set_value_type_object

```python
def set_value_type_object(value_type_object: Object) -> None
```

x.set_value_type_object(value_type_object) -> None
Sets the object that defines the enum, struct, or class.

Args:
    value_type_object (Object):

<a id="unreal.MovieGraphValueContainer.set_value_type"></a>

#### set_value_type

```python
def set_value_type(value_type: MovieGraphValueType,
                   value_type_object: Object = None) -> None
```

x.set_value_type(value_type, value_type_object=None) -> None
Sets the type of the stored data. Enums, structs, and classes must specify a value type object.

Args:
    value_type (MovieGraphValueType): 
    value_type_object (Object):

<a id="unreal.MovieGraphValueContainer.set_value_text"></a>

#### set_value_text

```python
def set_value_text(value: Text) -> bool
```

x.set_value_text(value) -> bool
Sets the FText value of the held data. Returns true on success, else false.

Args:
    value (Text): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_string"></a>

#### set_value_string

```python
def set_value_string(value: str) -> bool
```

x.set_value_string(value) -> bool
Sets the FString value of the held data. Returns true on success, else false.

Args:
    value (str): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_serialized_string"></a>

#### set_value_serialized_string

```python
def set_value_serialized_string(new_value: str) -> bool
```

x.set_value_serialized_string(new_value) -> bool
Sets the serialized value of the held data. The string should be the serialized representation of the value. Returns true on success, else false.

Args:
    new_value (str): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_object"></a>

#### set_value_object

```python
def set_value_object(value: Object) -> bool
```

x.set_value_object(value) -> bool
Sets the object value of the held data. Returns true on success, else false.

Args:
    value (Object): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_name"></a>

#### set_value_name

```python
def set_value_name(value: Name) -> bool
```

x.set_value_name(value) -> bool
Sets the FName value of the held data. Returns true on success, else false.

Args:
    value (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_int64"></a>

#### set_value_int64

```python
def set_value_int64(value: int) -> bool
```

x.set_value_int64(value) -> bool
Sets the int64 value of the held data. Returns true on success, else false.

Args:
    value (int64): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_int32"></a>

#### set_value_int32

```python
def set_value_int32(value: int) -> bool
```

x.set_value_int32(value) -> bool
Sets the int32 value of the held data. Returns true on success, else false.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_float"></a>

#### set_value_float

```python
def set_value_float(value: float) -> bool
```

x.set_value_float(value) -> bool
Sets the float value of the held data. Returns true on success, else false.

Args:
    value (float): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_enum"></a>

#### set_value_enum

```python
def set_value_enum(value: int, enum: Enum) -> bool
```

x.set_value_enum(value, enum) -> bool
Sets the enum value of the held data. Returns true on success, else false.

Args:
    value (uint8): 
    enum (Enum): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_double"></a>

#### set_value_double

```python
def set_value_double(value: float) -> bool
```

x.set_value_double(value) -> bool
Sets the double value of the held data. Returns true on success, else false.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_container_type"></a>

#### set_value_container_type

```python
def set_value_container_type(container_type: MovieGraphContainerType) -> None
```

x.set_value_container_type(container_type) -> None
Sets the container type of the stored value.

Args:
    container_type (MovieGraphContainerType):

<a id="unreal.MovieGraphValueContainer.set_value_class"></a>

#### set_value_class

```python
def set_value_class(value: Class) -> bool
```

x.set_value_class(value) -> bool
Sets the class value of the held data. Returns true on success, else false.

Args:
    value (type(Class)): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_byte"></a>

#### set_value_byte

```python
def set_value_byte(value: int) -> bool
```

x.set_value_byte(value) -> bool
Sets the byte value of the held data. Returns true on success, else false.

Args:
    value (uint8): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.set_value_bool"></a>

#### set_value_bool

```python
def set_value_bool(value: bool) -> bool
```

x.set_value_bool(value) -> bool
Sets the bool value of the held data. Returns true on success, else false.

Args:
    value (bool): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.get_value_type_object"></a>

#### get_value_type_object

```python
def get_value_type_object() -> Object
```

x.get_value_type_object() -> Object
Gets the object that defines the enum, struct, or class.

Returns:
    Object:

<a id="unreal.MovieGraphValueContainer.get_value_type"></a>

#### get_value_type

```python
def get_value_type() -> MovieGraphValueType
```

x.get_value_type() -> MovieGraphValueType
Gets the type of the stored data.

Returns:
    MovieGraphValueType:

<a id="unreal.MovieGraphValueContainer.get_value_text"></a>

#### get_value_text

```python
def get_value_text() -> Optional[Text]
```

x.get_value_text() -> Text or None
Gets the FText value of the held data. Returns true on success, else false.

Returns:
    Text or None: 

    out_value (Text):

<a id="unreal.MovieGraphValueContainer.get_value_string"></a>

#### get_value_string

```python
def get_value_string() -> Optional[str]
```

x.get_value_string() -> str or None
Gets the FString value of the held data. Returns true on success, else false.

Returns:
    str or None: 

    out_value (str):

<a id="unreal.MovieGraphValueContainer.get_value_serialized_string"></a>

#### get_value_serialized_string

```python
def get_value_serialized_string() -> str
```

x.get_value_serialized_string() -> str
Gets the serialized string value of the held data.

Returns:
    str:

<a id="unreal.MovieGraphValueContainer.get_value_object"></a>

#### get_value_object

```python
def get_value_object(out_value: Object, requested_class: Class = None) -> bool
```

x.get_value_object(out_value, requested_class=None) -> bool
Gets the object value (for a specific class) of the held data. Returns true on success, else false.

Args:
    out_value (Object): 
    requested_class (type(Class)): 

Returns:
    bool:

<a id="unreal.MovieGraphValueContainer.get_value_name"></a>

#### get_value_name

```python
def get_value_name() -> Optional[Name]
```

x.get_value_name() -> Name or None
Gets the FName value of the held data. Returns true on success, else false.

Returns:
    Name or None: 

    out_value (Name):

<a id="unreal.MovieGraphValueContainer.get_value_int64"></a>

#### get_value_int64

```python
def get_value_int64() -> Optional[int]
```

x.get_value_int64() -> int64 or None
Gets the int64 value of the held data. Returns true on success, else false.

Returns:
    int64 or None: 

    out_value (int64):

<a id="unreal.MovieGraphValueContainer.get_value_int32"></a>

#### get_value_int32

```python
def get_value_int32() -> Optional[int]
```

x.get_value_int32() -> int32 or None
Gets the int32 value of the held data. Returns true on success, else false.

Returns:
    int32 or None: 

    out_value (int32):

<a id="unreal.MovieGraphValueContainer.get_value_float"></a>

#### get_value_float

```python
def get_value_float() -> Optional[float]
```

x.get_value_float() -> float or None
Gets the float value of the held data. Returns true on success, else false.

Returns:
    float or None: 

    out_value (float):

<a id="unreal.MovieGraphValueContainer.get_value_enum"></a>

#### get_value_enum

```python
def get_value_enum(requested_enum: Enum = None) -> Optional[int]
```

x.get_value_enum(requested_enum=None) -> uint8 or None
Gets the enum value (for a specific enum) of the held data. Returns true on success, else false.

Args:
    requested_enum (Enum): 

Returns:
    uint8 or None: 

    out_value (uint8):

<a id="unreal.MovieGraphValueContainer.get_value_double"></a>

#### get_value_double

```python
def get_value_double() -> Optional[float]
```

x.get_value_double() -> double or None
Gets the double value of the held data. Returns true on success, else false.

Returns:
    double or None: 

    out_value (double):

<a id="unreal.MovieGraphValueContainer.get_value_container_type"></a>

#### get_value_container_type

```python
def get_value_container_type() -> MovieGraphContainerType
```

x.get_value_container_type() -> MovieGraphContainerType
Gets the container type of the stored value.

Returns:
    MovieGraphContainerType:

<a id="unreal.MovieGraphValueContainer.get_value_class"></a>

#### get_value_class

```python
def get_value_class() -> Optional[Class]
```

x.get_value_class() -> type(Class) or None
Gets the UClass value of the held data. Returns true on success, else false.

Returns:
    type(Class) or None: 

    out_value (type(Class)):

<a id="unreal.MovieGraphValueContainer.get_value_byte"></a>

#### get_value_byte

```python
def get_value_byte() -> Optional[int]
```

x.get_value_byte() -> uint8 or None
Gets the byte value of the held data. Returns true on success, else false.

Returns:
    uint8 or None: 

    out_value (uint8):

<a id="unreal.MovieGraphValueContainer.get_value_bool"></a>

#### get_value_bool

```python
def get_value_bool() -> Optional[bool]
```

x.get_value_bool() -> bool or None
Gets the bool value of the held data. Returns true on success, else false.

Returns:
    bool or None: 

    out_value (bool):

<a id="unreal.MovieGraphMember"></a>