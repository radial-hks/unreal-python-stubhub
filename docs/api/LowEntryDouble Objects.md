## LowEntryDouble Objects

```python
class LowEntryDouble(Object)
```

Low Entry Double

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryDouble.h

<a id="unreal.LowEntryDouble.set_double"></a>

#### set\_double

```python
def set_double(value: float) -> None
```

x.set_double(value) -> None
Sets the value.

Args:
    value (double):

<a id="unreal.LowEntryDouble.set_bytes"></a>

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

<a id="unreal.LowEntryDouble.long_bytes_less_than"></a>

#### long\_bytes\_less\_than

```python
def long_bytes_less_than(value: LowEntryLong) -> bool
```

x.long_bytes_less_than(value) -> bool
Returns true if the double is less than the given long.

Args:
    value (LowEntryLong): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.long_bytes_greater_than"></a>

#### long\_bytes\_greater\_than

```python
def long_bytes_greater_than(value: LowEntryLong) -> bool
```

x.long_bytes_greater_than(value) -> bool
Returns true if the double is greater than the given long.

Args:
    value (LowEntryLong): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.integer_less_than"></a>

#### integer\_less\_than

```python
def integer_less_than(value: int) -> bool
```

x.integer_less_than(value) -> bool
Returns true if the double is less than the given integer.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.integer_greater_than"></a>

#### integer\_greater\_than

```python
def integer_greater_than(value: int) -> bool
```

x.integer_greater_than(value) -> bool
Returns true if the double is greater than the given integer.

Args:
    value (int32): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.get_double"></a>

#### get\_double

```python
def get_double() -> float
```

x.get_double() -> double
Returns the value.

Returns:
    double:

<a id="unreal.LowEntryDouble.get_bytes"></a>

#### get\_bytes

```python
def get_bytes() -> Array[int]
```

x.get_bytes() -> Array[uint8]
Returns the bytes (always 8 bytes).

Returns:
    Array[uint8]:

<a id="unreal.LowEntryDouble.float_subtract"></a>

#### float\_subtract

```python
def float_subtract(value: float) -> None
```

x.float_subtract(value) -> None
Subtracts a float from this double.

Args:
    value (double):

<a id="unreal.LowEntryDouble.float_less_than"></a>

#### float\_less\_than

```python
def float_less_than(value: float) -> bool
```

x.float_less_than(value) -> bool
Returns true if the double is less than the given float.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.float_greater_than"></a>

#### float\_greater\_than

```python
def float_greater_than(value: float) -> bool
```

x.float_greater_than(value) -> bool
Returns true if the double is greater than the given float.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.float_equals"></a>

#### float\_equals

```python
def float_equals(value: float) -> bool
```

x.float_equals(value) -> bool
Returns true if the double is equal to the given integer.

Args:
    value (double): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.float_add"></a>

#### float\_add

```python
def float_add(value: float) -> None
```

x.float_add(value) -> None
Add a float to this double.

Args:
    value (double):

<a id="unreal.LowEntryDouble.double_bytes_subtract"></a>

#### double\_bytes\_subtract

```python
def double_bytes_subtract(value: LowEntryDouble) -> None
```

x.double_bytes_subtract(value) -> None
Subtracts a float from this double.

Args:
    value (LowEntryDouble):

<a id="unreal.LowEntryDouble.double_bytes_less_than"></a>

#### double\_bytes\_less\_than

```python
def double_bytes_less_than(value: LowEntryDouble) -> bool
```

x.double_bytes_less_than(value) -> bool
Returns true if the double is less than the given float.

Args:
    value (LowEntryDouble): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.double_bytes_greater_than"></a>

#### double\_bytes\_greater\_than

```python
def double_bytes_greater_than(value: LowEntryDouble) -> bool
```

x.double_bytes_greater_than(value) -> bool
Returns true if the double is greater than the given float.

Args:
    value (LowEntryDouble): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.double_bytes_equals"></a>

#### double\_bytes\_equals

```python
def double_bytes_equals(value: LowEntryDouble) -> bool
```

x.double_bytes_equals(value) -> bool
Returns true if the double is equal to the given integer.

Args:
    value (LowEntryDouble): 

Returns:
    bool:

<a id="unreal.LowEntryDouble.double_bytes_add"></a>

#### double\_bytes\_add

```python
def double_bytes_add(value: LowEntryDouble) -> None
```

x.double_bytes_add(value) -> None
Add a float to this double.

Args:
    value (LowEntryDouble):

<a id="unreal.LowEntryDouble.create_clone"></a>

#### create\_clone

```python
def create_clone() -> LowEntryDouble
```

x.create_clone() -> LowEntryDouble
Casts the long to a double.

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryDouble.cast_to_string"></a>

#### cast\_to\_string

```python
def cast_to_string(min_fractional_digits: int = 1) -> str
```

x.cast_to_string(min_fractional_digits=1) -> str
Casts the double to a string.

Args:
    min_fractional_digits (int32): 

Returns:
    str:

<a id="unreal.LowEntryDouble.cast_to_long_bytes"></a>

#### cast\_to\_long\_bytes

```python
def cast_to_long_bytes() -> LowEntryLong
```

x.cast_to_long_bytes() -> LowEntryLong
Casts the double to a long.

Returns:
    LowEntryLong:

<a id="unreal.LowEntryExecutionQueue"></a>