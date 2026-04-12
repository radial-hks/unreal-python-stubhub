## LowEntryLong Objects

```python
class LowEntryLong(Object)
```

Low Entry Long

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLong.h

<a id="unreal.LowEntryLong.set_long"></a>

#### set\_long

```python
def set_long(value: int) -> None
```

x.set_long(value) -> None
Sets the value.

Args:
    value (int64):

<a id="unreal.LowEntryLong.set_bytes"></a>

#### set\_bytes

```python
def set_bytes(byte_array: Array[int],
              index: int = 0,
              length: int = 2147483647) -> None
```

x.set_bytes(byte_array, index=0, length=2147483647) -> None
Sets the bytes (will only add the first 8 bytes, will add 0 bytes if the given byte array was less than 8 bytes).

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32):

<a id="unreal.LowEntryLong.long_bytes_subtract"></a>

#### long\_bytes\_subtract

```python
def long_bytes_subtract(value: LowEntryLong) -> None
```

x.long_bytes_subtract(value) -> None
Subtracts an integer from this long.

Args:
    value (LowEntryLong):

<a id="unreal.LowEntryLong.long_bytes_less_than"></a>

#### long\_bytes\_less\_than

```python
def long_bytes_less_than(value: LowEntryLong) -> bool
```

x.long_bytes_less_than(value) -> bool
Returns true if the long is less than the given integer.

Args:
    value (LowEntryLong): 

Returns:
    bool:

<a id="unreal.LowEntryLong.long_bytes_greater_than"></a>

#### long\_bytes\_greater\_than

```python
def long_bytes_greater_than(value: LowEntryLong) -> bool
```

x.long_bytes_greater_than(value) -> bool
Returns true if the long is greater than the given integer.

Args:
    value (LowEntryLong): 

Returns:
    bool:

<a id="unreal.LowEntryLong.long_bytes_equals"></a>

#### long\_bytes\_equals

```python
def long_bytes_equals(value: LowEntryLong) -> bool
```

x.long_bytes_equals(value) -> bool
Returns true if the long is equal to the given integer.

Args:
    value (LowEntryLong): 

Returns:
    bool:

<a id="unreal.LowEntryLong.long_bytes_add"></a>

#### long\_bytes\_add

```python
def long_bytes_add(value: LowEntryLong) -> None
```

x.long_bytes_add(value) -> None
Add a long to this long.

Args:
    value (LowEntryLong):

<a id="unreal.LowEntryLong.integer_subtract"></a>

#### integer\_subtract

```python
def integer_subtract(value: int) -> None
```

x.integer_subtract(value) -> None
Subtracts an integer from this long.

Args:
    value (int32):

<a id="unreal.LowEntryLong.integer_less_than"></a>

#### integer\_less\_than

```python
def integer_less_than(value: int) -> bool
```

x.integer_less_than(value) -> bool
Returns true if the long is less than the given integer.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.LowEntryLong.integer_greater_than"></a>

#### integer\_greater\_than

```python
def integer_greater_than(value: int) -> bool
```

x.integer_greater_than(value) -> bool
Returns true if the long is greater than the given integer.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.LowEntryLong.integer_equals"></a>

#### integer\_equals

```python
def integer_equals(value: int) -> bool
```

x.integer_equals(value) -> bool
Returns true if the long is equal to the given integer.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.LowEntryLong.integer_add"></a>

#### integer\_add

```python
def integer_add(value: int) -> None
```

x.integer_add(value) -> None
Add an integer to this long.

Args:
    value (int32):

<a id="unreal.LowEntryLong.get_long"></a>

#### get\_long

```python
def get_long() -> int
```

x.get_long() -> int64
Returns the value.

Returns:
    int64:

<a id="unreal.LowEntryLong.get_bytes"></a>

#### get\_bytes

```python
def get_bytes() -> Array[int]
```

x.get_bytes() -> Array[uint8]
Returns the bytes (always 8 bytes).

Returns:
    Array[uint8]:

<a id="unreal.LowEntryLong.float_less_than"></a>

#### float\_less\_than

```python
def float_less_than(value: float) -> bool
```

x.float_less_than(value) -> bool
Returns true if the long is less than the given float.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.LowEntryLong.float_greater_than"></a>

#### float\_greater\_than

```python
def float_greater_than(value: float) -> bool
```

x.float_greater_than(value) -> bool
Returns true if the long is greater than the given float.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.LowEntryLong.double_bytes_less_than"></a>

#### double\_bytes\_less\_than

```python
def double_bytes_less_than(value: LowEntryDouble) -> bool
```

x.double_bytes_less_than(value) -> bool
Returns true if the long is less than the given double.

Args:
    value (LowEntryDouble): 

Returns:
    bool:

<a id="unreal.LowEntryLong.double_bytes_greater_than"></a>

#### double\_bytes\_greater\_than

```python
def double_bytes_greater_than(value: LowEntryDouble) -> bool
```

x.double_bytes_greater_than(value) -> bool
Returns true if the long is greater than the given double.

Args:
    value (LowEntryDouble): 

Returns:
    bool:

<a id="unreal.LowEntryLong.create_clone"></a>

#### create\_clone

```python
def create_clone() -> LowEntryLong
```

x.create_clone() -> LowEntryLong
Casts the long to a double.

Returns:
    LowEntryLong:

<a id="unreal.LowEntryLong.cast_to_string"></a>

#### cast\_to\_string

```python
def cast_to_string() -> str
```

x.cast_to_string() -> str
Casts the long to a string.

Returns:
    str:

<a id="unreal.LowEntryLong.cast_to_double_bytes"></a>

#### cast\_to\_double\_bytes

```python
def cast_to_double_bytes() -> LowEntryDouble
```

x.cast_to_double_bytes() -> LowEntryDouble
Casts the long to a double.

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryParsedHashcash"></a>