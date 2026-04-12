## LowEntryByteDataWriter Objects

```python
class LowEntryByteDataWriter(Object)
```

Low Entry Byte Data Writer

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryByteDataWriter.h

<a id="unreal.LowEntryByteDataWriter.add_string_utf8_array"></a>

#### add\_string\_utf8\_array

```python
def add_string_utf8_array(value: Array[str]) -> None
```

x.add_string_utf8_array(value) -> None
Adds a String (UTF-8) array.

Args:
    value (Array[str]):

<a id="unreal.LowEntryByteDataWriter.add_string_utf8"></a>

#### add\_string\_utf8

```python
def add_string_utf8(value: str) -> None
```

x.add_string_utf8(value) -> None
Adds a String (UTF-8).

Args:
    value (str):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer3_array"></a>

#### add\_positive\_integer3\_array

```python
def add_positive_integer3_array(value: Array[int]) -> None
```

x.add_positive_integer3_array(value) -> None
Adds a positive integer array.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer3"></a>

#### add\_positive\_integer3

```python
def add_positive_integer3(value: int) -> None
```

x.add_positive_integer3(value) -> None
Adds a positive integer.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer2_array"></a>

#### add\_positive\_integer2\_array

```python
def add_positive_integer2_array(value: Array[int]) -> None
```

x.add_positive_integer2_array(value) -> None
Adds a positive integer array.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer2"></a>

#### add\_positive\_integer2

```python
def add_positive_integer2(value: int) -> None
```

x.add_positive_integer2(value) -> None
Adds a positive integer.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer1_array"></a>

#### add\_positive\_integer1\_array

```python
def add_positive_integer1_array(value: Array[int]) -> None
```

x.add_positive_integer1_array(value) -> None
Adds a positive integer array.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]):

<a id="unreal.LowEntryByteDataWriter.add_positive_integer1"></a>

#### add\_positive\_integer1

```python
def add_positive_integer1(value: int) -> None
```

x.add_positive_integer1(value) -> None
Adds a positive integer.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32):

<a id="unreal.LowEntryByteDataWriter.add_long_bytes_array"></a>

#### add\_long\_bytes\_array

```python
def add_long_bytes_array(value: Array[LowEntryLong]) -> None
```

x.add_long_bytes_array(value) -> None
Adds a long (bytes) array.

Args:
    value (Array[LowEntryLong]):

<a id="unreal.LowEntryByteDataWriter.add_long_bytes"></a>

#### add\_long\_bytes

```python
def add_long_bytes(value: LowEntryLong) -> None
```

x.add_long_bytes(value) -> None
Adds a long (bytes).

Args:
    value (LowEntryLong):

<a id="unreal.LowEntryByteDataWriter.add_long_array"></a>

#### add\_long\_array

```python
def add_long_array(value: Array[int]) -> None
```

x.add_long_array(value) -> None
Adds a long (int64) array.

Args:
    value (Array[int64]):

<a id="unreal.LowEntryByteDataWriter.add_long"></a>

#### add\_long

```python
def add_long(value: int) -> None
```

x.add_long(value) -> None
Adds a long (int64).

Args:
    value (int64):

<a id="unreal.LowEntryByteDataWriter.add_integer_array"></a>

#### add\_integer\_array

```python
def add_integer_array(value: Array[int]) -> None
```

x.add_integer_array(value) -> None
Adds an integer array.

Args:
    value (Array[int32]):

<a id="unreal.LowEntryByteDataWriter.add_integer"></a>

#### add\_integer

```python
def add_integer(value: int) -> None
```

x.add_integer(value) -> None
Adds an integer.

Args:
    value (int32):

<a id="unreal.LowEntryByteDataWriter.add_float_array"></a>

#### add\_float\_array

```python
def add_float_array(value: Array[float]) -> None
```

x.add_float_array(value) -> None
Adds a float array.

Args:
    value (Array[float]):

<a id="unreal.LowEntryByteDataWriter.add_float"></a>

#### add\_float

```python
def add_float(value: float) -> None
```

x.add_float(value) -> None
Adds a float.

Args:
    value (float):

<a id="unreal.LowEntryByteDataWriter.add_double_bytes_array"></a>

#### add\_double\_bytes\_array

```python
def add_double_bytes_array(value: Array[LowEntryDouble]) -> None
```

x.add_double_bytes_array(value) -> None
Adds a double (bytes) array.

Args:
    value (Array[LowEntryDouble]):

<a id="unreal.LowEntryByteDataWriter.add_double_bytes"></a>

#### add\_double\_bytes

```python
def add_double_bytes(value: LowEntryDouble) -> None
```

x.add_double_bytes(value) -> None
Adds a double (bytes).

Args:
    value (LowEntryDouble):

<a id="unreal.LowEntryByteDataWriter.add_double_array"></a>

#### add\_double\_array

```python
def add_double_array(value: Array[float]) -> None
```

x.add_double_array(value) -> None
Adds a double array.

Args:
    value (Array[double]):

<a id="unreal.LowEntryByteDataWriter.add_double"></a>

#### add\_double

```python
def add_double(value: float) -> None
```

x.add_double(value) -> None
Adds a double.

Args:
    value (double):

<a id="unreal.LowEntryByteDataWriter.add_byte_array"></a>

#### add\_byte\_array

```python
def add_byte_array(value: Array[int]) -> None
```

x.add_byte_array(value) -> None
Adds a byte array.

Args:
    value (Array[uint8]):

<a id="unreal.LowEntryByteDataWriter.add_byte"></a>

#### add\_byte

```python
def add_byte(value: int) -> None
```

x.add_byte(value) -> None
Adds a byte.

Args:
    value (uint8):

<a id="unreal.LowEntryByteDataWriter.add_boolean_array"></a>

#### add\_boolean\_array

```python
def add_boolean_array(value: Array[bool]) -> None
```

x.add_boolean_array(value) -> None
Adds a boolean array.

Args:
    value (Array[bool]):

<a id="unreal.LowEntryByteDataWriter.add_boolean"></a>

#### add\_boolean

```python
def add_boolean(value: bool) -> None
```

x.add_boolean(value) -> None
Adds a boolean.

Args:
    value (bool):

<a id="unreal.LowEntryDouble"></a>