## LowEntryByteDataReader Objects

```python
class LowEntryByteDataReader(Object)
```

Low Entry Byte Data Reader

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryByteDataReader.h

<a id="unreal.LowEntryByteDataReader.set_position"></a>

#### set\_position

```python
def set_position(position: int) -> None
```

x.set_position(position) -> None
Sets the current position.

Args:
    position (int32):

<a id="unreal.LowEntryByteDataReader.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Sets the current position to 0.

<a id="unreal.LowEntryByteDataReader.remaining"></a>

#### remaining

```python
def remaining() -> int
```

x.remaining() -> int32
Returns the amount of bytes left.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_string_utf8_array"></a>

#### get\_string\_utf8\_array

```python
def get_string_utf8_array() -> Array[str]
```

x.get_string_utf8_array() -> Array[str]
Gets a String (UTF-8) array.

Returns:
    Array[str]:

<a id="unreal.LowEntryByteDataReader.get_string_utf8"></a>

#### get\_string\_utf8

```python
def get_string_utf8() -> str
```

x.get_string_utf8() -> str
Gets a String (UTF-8).

Returns:
    str:

<a id="unreal.LowEntryByteDataReader.get_positive_integer3_array"></a>

#### get\_positive\_integer3\_array

```python
def get_positive_integer3_array() -> Array[int]
```

x.get_positive_integer3_array() -> Array[int32]
Gets a positive integer array.

Returns:
    Array[int32]:

<a id="unreal.LowEntryByteDataReader.get_positive_integer3"></a>

#### get\_positive\_integer3

```python
def get_positive_integer3() -> int
```

x.get_positive_integer3() -> int32
Gets a positive integer.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_positive_integer2_array"></a>

#### get\_positive\_integer2\_array

```python
def get_positive_integer2_array() -> Array[int]
```

x.get_positive_integer2_array() -> Array[int32]
Gets a positive integer array.

Returns:
    Array[int32]:

<a id="unreal.LowEntryByteDataReader.get_positive_integer2"></a>

#### get\_positive\_integer2

```python
def get_positive_integer2() -> int
```

x.get_positive_integer2() -> int32
Gets a positive integer.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_positive_integer1_array"></a>

#### get\_positive\_integer1\_array

```python
def get_positive_integer1_array() -> Array[int]
```

x.get_positive_integer1_array() -> Array[int32]
Gets a positive integer array.

Returns:
    Array[int32]:

<a id="unreal.LowEntryByteDataReader.get_positive_integer1"></a>

#### get\_positive\_integer1

```python
def get_positive_integer1() -> int
```

x.get_positive_integer1() -> int32
Gets a positive integer.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_position"></a>

#### get\_position

```python
def get_position() -> int
```

x.get_position() -> int32
Returns the current position.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_long_bytes_array"></a>

#### get\_long\_bytes\_array

```python
def get_long_bytes_array() -> Array[LowEntryLong]
```

x.get_long_bytes_array() -> Array[LowEntryLong]
Gets a long (bytes) array.

Returns:
    Array[LowEntryLong]:

<a id="unreal.LowEntryByteDataReader.get_long_bytes"></a>

#### get\_long\_bytes

```python
def get_long_bytes() -> LowEntryLong
```

x.get_long_bytes() -> LowEntryLong
Gets a long (bytes).

Returns:
    LowEntryLong:

<a id="unreal.LowEntryByteDataReader.get_long_array"></a>

#### get\_long\_array

```python
def get_long_array() -> Array[int]
```

x.get_long_array() -> Array[int64]
Gets a long (int64) array.

Returns:
    Array[int64]:

<a id="unreal.LowEntryByteDataReader.get_long"></a>

#### get\_long

```python
def get_long() -> int
```

x.get_long() -> int64
Gets a long (int64).

Returns:
    int64:

<a id="unreal.LowEntryByteDataReader.get_integer_array"></a>

#### get\_integer\_array

```python
def get_integer_array() -> Array[int]
```

x.get_integer_array() -> Array[int32]
Gets an integer array.

Returns:
    Array[int32]:

<a id="unreal.LowEntryByteDataReader.get_integer"></a>

#### get\_integer

```python
def get_integer() -> int
```

x.get_integer() -> int32
Gets an integer.

Returns:
    int32:

<a id="unreal.LowEntryByteDataReader.get_float_array"></a>

#### get\_float\_array

```python
def get_float_array() -> Array[float]
```

x.get_float_array() -> Array[float]
Gets a float array.

Returns:
    Array[float]:

<a id="unreal.LowEntryByteDataReader.get_float"></a>

#### get\_float

```python
def get_float() -> float
```

x.get_float() -> float
Gets a float.

Returns:
    float:

<a id="unreal.LowEntryByteDataReader.get_double_bytes_array"></a>

#### get\_double\_bytes\_array

```python
def get_double_bytes_array() -> Array[LowEntryDouble]
```

x.get_double_bytes_array() -> Array[LowEntryDouble]
Gets a double (byte) array.

Returns:
    Array[LowEntryDouble]:

<a id="unreal.LowEntryByteDataReader.get_double_bytes"></a>

#### get\_double\_bytes

```python
def get_double_bytes() -> LowEntryDouble
```

x.get_double_bytes() -> LowEntryDouble
Gets a double (bytes).

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryByteDataReader.get_double_array"></a>

#### get\_double\_array

```python
def get_double_array() -> Array[float]
```

x.get_double_array() -> Array[double]
Gets a double array.

Returns:
    Array[double]:

<a id="unreal.LowEntryByteDataReader.get_double"></a>

#### get\_double

```python
def get_double() -> float
```

x.get_double() -> double
Gets a double.

Returns:
    double:

<a id="unreal.LowEntryByteDataReader.get_clone"></a>

#### get\_clone

```python
def get_clone() -> LowEntryByteDataReader
```

x.get_clone() -> LowEntryByteDataReader
Clones the clone of this ByteDataReader.

Allows you to easily read and revert the position (by cloning, reading data with the clone, and then throwing the clone away).

Returns:
    LowEntryByteDataReader:

<a id="unreal.LowEntryByteDataReader.get_byte_array"></a>

#### get\_byte\_array

```python
def get_byte_array() -> Array[int]
```

x.get_byte_array() -> Array[uint8]
Gets a byte array.

Returns:
    Array[uint8]:

<a id="unreal.LowEntryByteDataReader.get_byte"></a>

#### get\_byte

```python
def get_byte() -> int
```

x.get_byte() -> uint8
Gets a byte.

Returns:
    uint8:

<a id="unreal.LowEntryByteDataReader.get_boolean_array"></a>

#### get\_boolean\_array

```python
def get_boolean_array() -> Array[bool]
```

x.get_boolean_array() -> Array[bool]
Gets a boolean array.

Returns:
    Array[bool]:

<a id="unreal.LowEntryByteDataReader.get_boolean"></a>

#### get\_boolean

```python
def get_boolean() -> bool
```

x.get_boolean() -> bool
Gets a boolean.

Returns:
    bool:

<a id="unreal.LowEntryByteDataReader.empty"></a>

#### empty

```python
def empty() -> None
```

x.empty() -> None
Causes Remaining to return 0.

<a id="unreal.LowEntryByteDataWriter"></a>