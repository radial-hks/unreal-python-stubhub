## RCVirtualPropertyBase Objects

```python
class RCVirtualPropertyBase(Object)
```

Base class for dynamic virtual properties
Remote Control Virtual Properties using Property Bag and FInstancedPropertyBag to serialize FProperties values and UStruct

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RCVirtualProperty.h

<a id="unreal.RCVirtualPropertyBase.set_value_vector2d"></a>

#### set_value_vector2d

```python
def set_value_vector2d(vector2d: Vector2D) -> bool
```

x.set_value_vector2d(vector2d) -> bool
Set Vector2D value from Virtual Property

Args:
    vector2d (Vector2D): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_vector"></a>

#### set_value_vector

```python
def set_value_vector(vector: Vector) -> bool
```

x.set_value_vector(vector) -> bool
Set Vector value from Virtual Property

Args:
    vector (Vector): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_text"></a>

#### set_value_text

```python
def set_value_text(text_value: Text) -> bool
```

x.set_value_text(text_value) -> bool
Set Text value from Virtual Property

Args:
    text_value (Text): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_string"></a>

#### set_value_string

```python
def set_value_string(string_value: str) -> bool
```

x.set_value_string(string_value) -> bool
Set String value from Virtual Property

Args:
    string_value (str): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_rotator"></a>

#### set_value_rotator

```python
def set_value_rotator(rotator: Rotator) -> bool
```

x.set_value_rotator(rotator) -> bool
Set Rotator value from Virtual Property

Args:
    rotator (Rotator): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_numeric_integer"></a>

#### set_value_numeric_integer

```python
def set_value_numeric_integer(int64_value: int) -> bool
```

x.set_value_numeric_integer(int64_value) -> bool
Set Numeric value from Virtual Property

Args:
    int64_value (int64): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_name"></a>

#### set_value_name

```python
def set_value_name(name_value: Name) -> bool
```

x.set_value_name(name_value) -> bool
Set Name value from Virtual Property

Args:
    name_value (Name): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_linear_color"></a>

#### set_value_linear_color

```python
def set_value_linear_color(linear_color: LinearColor) -> bool
```

x.set_value_linear_color(linear_color) -> bool
Set LinearColor value from Virtual Property

Args:
    linear_color (LinearColor): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_int64"></a>

#### set_value_int64

```python
def set_value_int64(int64: int) -> bool
```

x.set_value_int64(int64) -> bool
Set Int64 value from Virtual Property

Args:
    int64 (int64): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_int32"></a>

#### set_value_int32

```python
def set_value_int32(int32: int) -> bool
```

x.set_value_int32(int32) -> bool
Set Int32 value from Virtual Property

Args:
    int32 (int32): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_float"></a>

#### set_value_float

```python
def set_value_float(float: float) -> bool
```

x.set_value_float(float) -> bool
Set Float value from Virtual Property

Args:
    float (float): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_double"></a>

#### set_value_double

```python
def set_value_double(double: float) -> bool
```

x.set_value_double(double) -> bool
Set Double value from Virtual Property

Args:
    double (double): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_color"></a>

#### set_value_color

```python
def set_value_color(color: Color) -> bool
```

x.set_value_color(color) -> bool
Set Color value from Virtual Property

Args:
    color (Color): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_byte"></a>

#### set_value_byte

```python
def set_value_byte(byte: int) -> bool
```

x.set_value_byte(byte) -> bool
Set Byte value from Virtual Property

Args:
    byte (uint8): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.set_value_bool"></a>

#### set_value_bool

```python
def set_value_bool(bool_value: bool) -> bool
```

x.set_value_bool(bool_value) -> bool
Set Bool value from Virtual Property

Args:
    bool_value (bool): 

Returns:
    bool:

<a id="unreal.RCVirtualPropertyBase.get_value_vector2d"></a>

#### get_value_vector2d

```python
def get_value_vector2d() -> Optional[Vector2D]
```

x.get_value_vector2d() -> Vector2D or None
Get Vector2D value from Virtual Property

Returns:
    Vector2D or None: 

    out_vector2d (Vector2D):

<a id="unreal.RCVirtualPropertyBase.get_value_vector"></a>

#### get_value_vector

```python
def get_value_vector() -> Optional[Vector]
```

x.get_value_vector() -> Vector or None
Get Vector value from Virtual Property

Returns:
    Vector or None: 

    out_vector (Vector):

<a id="unreal.RCVirtualPropertyBase.get_value_text"></a>

#### get_value_text

```python
def get_value_text() -> Optional[Text]
```

x.get_value_text() -> Text or None
Get Text value from Virtual Property

Returns:
    Text or None: 

    out_text_value (Text):

<a id="unreal.RCVirtualPropertyBase.get_value_string"></a>

#### get_value_string

```python
def get_value_string() -> Optional[str]
```

x.get_value_string() -> str or None
Get String value from Virtual Property

Returns:
    str or None: 

    out_string_value (str):

<a id="unreal.RCVirtualPropertyBase.get_value_rotator"></a>

#### get_value_rotator

```python
def get_value_rotator() -> Optional[Rotator]
```

x.get_value_rotator() -> Rotator or None
Get Rotator value from Virtual Property

Returns:
    Rotator or None: 

    out_rotator (Rotator):

<a id="unreal.RCVirtualPropertyBase.get_value_object"></a>

#### get_value_object

```python
def get_value_object() -> Object
```

x.get_value_object() -> Object
Get Object value from Virtual Property

Returns:
    Object:

<a id="unreal.RCVirtualPropertyBase.get_value_numeric_integer"></a>

#### get_value_numeric_integer

```python
def get_value_numeric_integer() -> Optional[int]
```

x.get_value_numeric_integer() -> int64 or None
Get Numeric value from Virtual Property

Returns:
    int64 or None: 

    out_int64_value (int64):

<a id="unreal.RCVirtualPropertyBase.get_value_name"></a>

#### get_value_name

```python
def get_value_name() -> Optional[Name]
```

x.get_value_name() -> Name or None
Get Name value from Virtual Property

Returns:
    Name or None: 

    out_name_value (Name):

<a id="unreal.RCVirtualPropertyBase.get_value_linear_color"></a>

#### get_value_linear_color

```python
def get_value_linear_color() -> Optional[LinearColor]
```

x.get_value_linear_color() -> LinearColor or None
Get LinearColor value from Virtual Property

Returns:
    LinearColor or None: 

    out_linear_color (LinearColor):

<a id="unreal.RCVirtualPropertyBase.get_value_int64"></a>

#### get_value_int64

```python
def get_value_int64() -> Optional[int]
```

x.get_value_int64() -> int64 or None
Get Int64 value from Virtual Property

Returns:
    int64 or None: 

    ouy_int64 (int64):

<a id="unreal.RCVirtualPropertyBase.get_value_int32"></a>

#### get_value_int32

```python
def get_value_int32() -> Optional[int]
```

x.get_value_int32() -> int32 or None
Get Int32 value from Virtual Property

Returns:
    int32 or None: 

    out_int32 (int32):

<a id="unreal.RCVirtualPropertyBase.get_value_float"></a>

#### get_value_float

```python
def get_value_float() -> Optional[float]
```

x.get_value_float() -> float or None
Get Float value from Virtual Property

Returns:
    float or None: 

    out_float (float):

<a id="unreal.RCVirtualPropertyBase.get_value_double"></a>

#### get_value_double

```python
def get_value_double() -> Optional[float]
```

x.get_value_double() -> double or None
Get Double value from Virtual Property

Returns:
    double or None: 

    out_double (double):

<a id="unreal.RCVirtualPropertyBase.get_value_color"></a>

#### get_value_color

```python
def get_value_color() -> Optional[Color]
```

x.get_value_color() -> Color or None
Get Color value from Virtual Property

Returns:
    Color or None: 

    out_color (Color):

<a id="unreal.RCVirtualPropertyBase.get_value_byte"></a>

#### get_value_byte

```python
def get_value_byte() -> Optional[int]
```

x.get_value_byte() -> uint8 or None
Get Byte value from Virtual Property

Returns:
    uint8 or None: 

    out_byte (uint8):

<a id="unreal.RCVirtualPropertyBase.get_value_bool"></a>

#### get_value_bool

```python
def get_value_bool() -> Optional[bool]
```

x.get_value_bool() -> bool or None
Get Bool value from Virtual Property

Returns:
    bool or None: 

    out_bool_value (bool):

<a id="unreal.RCVirtualPropertyBase.get_property_name"></a>

#### get_property_name

```python
def get_property_name() -> Name
```

x.get_property_name() -> Name
Get FProperty Name

Returns:
    Name:

<a id="unreal.RCVirtualPropertyBase.get_display_value_as_string"></a>

#### get_display_value_as_string

```python
def get_display_value_as_string() -> str
```

x.get_display_value_as_string() -> str
Infers correct type internally, fetches value from memory and returns the value as a string
that can be immediately used for dispaly (without needing to create a generic readonly property widget)

Returns:
    str:

<a id="unreal.RCVirtualPropertyInContainer"></a>