## LowEntryBitDataWriter Objects

```python
class LowEntryBitDataWriter(Object)
```

Low Entry Bit Data Writer

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryBitDataWriter.h

<a id="unreal.LowEntryBitDataWriter.add_string_utf8_array"></a>

#### add\_string\_utf8\_array

```python
def add_string_utf8_array(value: Array[str]) -> None
```

x.add_string_utf8_array(value) -> None
Adds a String (UTF-8) array.

Args:
    value (Array[str]):

<a id="unreal.LowEntryBitDataWriter.add_string_utf8"></a>

#### add\_string\_utf8

```python
def add_string_utf8(value: str) -> None
```

x.add_string_utf8(value) -> None
Adds a String (UTF-8).

Args:
    value (str):

<a id="unreal.LowEntryBitDataWriter.add_positive_integer3_array"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_positive_integer3"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_positive_integer2_array"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_positive_integer2"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_positive_integer1_array"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_positive_integer1"></a>

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

<a id="unreal.LowEntryBitDataWriter.add_long_bytes_array"></a>

#### add\_long\_bytes\_array

```python
def add_long_bytes_array(value: Array[LowEntryLong]) -> None
```

x.add_long_bytes_array(value) -> None
Adds a long (bytes) array.

Args:
    value (Array[LowEntryLong]):

<a id="unreal.LowEntryBitDataWriter.add_long_bytes"></a>

#### add\_long\_bytes

```python
def add_long_bytes(value: LowEntryLong) -> None
```

x.add_long_bytes(value) -> None
Adds a long (bytes).

Args:
    value (LowEntryLong):

<a id="unreal.LowEntryBitDataWriter.add_long_array"></a>

#### add\_long\_array

```python
def add_long_array(value: Array[int]) -> None
```

x.add_long_array(value) -> None
Adds a long (int64) array.

Args:
    value (Array[int64]):

<a id="unreal.LowEntryBitDataWriter.add_long"></a>

#### add\_long

```python
def add_long(value: int) -> None
```

x.add_long(value) -> None
Adds a long (int64).

Args:
    value (int64):

<a id="unreal.LowEntryBitDataWriter.add_integer_most_significant_bits"></a>

#### add\_integer\_most\_significant\_bits

```python
def add_integer_most_significant_bits(value: int, bit_count: int) -> None
```

x.add_integer_most_significant_bits(value, bit_count) -> None
Adds an integer, will only add a certain amount of bits from the given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value 268435471 and bitcount 4, only the highest 4 bits will be added, meaning only 0001 will be added, which will then have a value of 268435456 when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (int32): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_integer_least_significant_bits"></a>

#### add\_integer\_least\_significant\_bits

```python
def add_integer_least_significant_bits(value: int, bit_count: int) -> None
```

x.add_integer_least_significant_bits(value, bit_count) -> None
Adds an integer, will only add a certain amount of bits from the given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value 268435471 and bitcount 4, only the lowest 4 bits will be added, meaning only 1111 will be added, which will then have a value of 15 when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (int32): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_integer_array_most_significant_bits"></a>

#### add\_integer\_array\_most\_significant\_bits

```python
def add_integer_array_most_significant_bits(value: Array[int],
                                            bit_count: int) -> None
```

x.add_integer_array_most_significant_bits(value, bit_count) -> None
Adds an integer array, will only add a certain amount of bits from every given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value [268435471, 268435471, 268435471] and bitcount 4, only the highest 4 bits of each integer will be added, meaning only 0001 0001 0001 will be added, which will then have a value of 268435456 for each integer when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (Array[int32]): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_integer_array_least_significant_bits"></a>

#### add\_integer\_array\_least\_significant\_bits

```python
def add_integer_array_least_significant_bits(value: Array[int],
                                             bit_count: int) -> None
```

x.add_integer_array_least_significant_bits(value, bit_count) -> None
Adds an integer array, will only add a certain amount of bits from every given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value [268435471, 268435471, 268435471] and bitcount 4, only the lowest 4 bits of each integer will be added, meaning only 1111 1111 1111 will be added, which will then have a value of 15 for each integer when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (Array[int32]): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_integer_array"></a>

#### add\_integer\_array

```python
def add_integer_array(value: Array[int]) -> None
```

x.add_integer_array(value) -> None
Adds an integer array.

Args:
    value (Array[int32]):

<a id="unreal.LowEntryBitDataWriter.add_integer"></a>

#### add\_integer

```python
def add_integer(value: int) -> None
```

x.add_integer(value) -> None
Adds an integer.

Args:
    value (int32):

<a id="unreal.LowEntryBitDataWriter.add_float_array"></a>

#### add\_float\_array

```python
def add_float_array(value: Array[float]) -> None
```

x.add_float_array(value) -> None
Adds a float array.

Args:
    value (Array[float]):

<a id="unreal.LowEntryBitDataWriter.add_float"></a>

#### add\_float

```python
def add_float(value: float) -> None
```

x.add_float(value) -> None
Adds a float.

Args:
    value (float):

<a id="unreal.LowEntryBitDataWriter.add_double_bytes_array"></a>

#### add\_double\_bytes\_array

```python
def add_double_bytes_array(value: Array[LowEntryDouble]) -> None
```

x.add_double_bytes_array(value) -> None
Adds a double (bytes) array.

Args:
    value (Array[LowEntryDouble]):

<a id="unreal.LowEntryBitDataWriter.add_double_bytes"></a>

#### add\_double\_bytes

```python
def add_double_bytes(value: LowEntryDouble) -> None
```

x.add_double_bytes(value) -> None
Adds a double (bytes).

Args:
    value (LowEntryDouble):

<a id="unreal.LowEntryBitDataWriter.add_double_array"></a>

#### add\_double\_array

```python
def add_double_array(value: Array[float]) -> None
```

x.add_double_array(value) -> None
Adds a double array.

Args:
    value (Array[double]):

<a id="unreal.LowEntryBitDataWriter.add_double"></a>

#### add\_double

```python
def add_double(value: float) -> None
```

x.add_double(value) -> None
Adds a double.

Args:
    value (double):

<a id="unreal.LowEntryBitDataWriter.add_byte_most_significant_bits"></a>

#### add\_byte\_most\_significant\_bits

```python
def add_byte_most_significant_bits(value: int, bit_count: int) -> None
```

x.add_byte_most_significant_bits(value, bit_count) -> None
Adds a byte, will only add a certain amount of bits from the given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value 63 and bitcount 4, only the highest 4 bits will be added, meaning only 0011 will be added, which will then have a value of 48 when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (uint8): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_byte_least_significant_bits"></a>

#### add\_byte\_least\_significant\_bits

```python
def add_byte_least_significant_bits(value: int, bit_count: int) -> None
```

x.add_byte_least_significant_bits(value, bit_count) -> None
Adds a byte, will only add a certain amount of bits from the given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value 63 and bitcount 4, only the lowest 4 bits will be added, meaning only 1111 will be added, which will then have a value of 15 when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (uint8): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_byte_array_most_significant_bits"></a>

#### add\_byte\_array\_most\_significant\_bits

```python
def add_byte_array_most_significant_bits(value: Array[int],
                                         bit_count: int) -> None
```

x.add_byte_array_most_significant_bits(value, bit_count) -> None
Adds a byte array, will only add a certain amount of bits from every given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value [63, 63, 63] and bitcount 4, only the highest 4 bits of each byte will be added, meaning only 0011 0011 0011 will be added, which will then have a value of 48 for each byte when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (Array[uint8]): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_byte_array_least_significant_bits"></a>

#### add\_byte\_array\_least\_significant\_bits

```python
def add_byte_array_least_significant_bits(value: Array[int],
                                          bit_count: int) -> None
```

x.add_byte_array_least_significant_bits(value, bit_count) -> None
Adds a byte array, will only add a certain amount of bits from every given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value [63, 63, 63] and bitcount 4, only the lowest 4 bits of each byte will be added, meaning only 1111 1111 1111 will be added, which will then have a value of 15 for each byte when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (Array[uint8]): 
    bit_count (int32):

<a id="unreal.LowEntryBitDataWriter.add_byte_array"></a>

#### add\_byte\_array

```python
def add_byte_array(value: Array[int]) -> None
```

x.add_byte_array(value) -> None
Adds a byte array.

Args:
    value (Array[uint8]):

<a id="unreal.LowEntryBitDataWriter.add_byte"></a>

#### add\_byte

```python
def add_byte(value: int) -> None
```

x.add_byte(value) -> None
Adds a byte.

Args:
    value (uint8):

<a id="unreal.LowEntryBitDataWriter.add_boolean_array"></a>

#### add\_boolean\_array

```python
def add_boolean_array(value: Array[bool]) -> None
```

x.add_boolean_array(value) -> None
Adds a boolean array, this does the same as adding a bit array.

Args:
    value (Array[bool]):

<a id="unreal.LowEntryBitDataWriter.add_boolean"></a>

#### add\_boolean

```python
def add_boolean(value: bool) -> None
```

x.add_boolean(value) -> None
Adds a boolean, this does the same as adding a bit.

Args:
    value (bool):

<a id="unreal.LowEntryBitDataWriter.add_bit_array"></a>

#### add\_bit\_array

```python
def add_bit_array(value: Array[bool]) -> None
```

x.add_bit_array(value) -> None
Adds a bit array.

Args:
    value (Array[bool]):

<a id="unreal.LowEntryBitDataWriter.add_bit"></a>

#### add\_bit

```python
def add_bit(value: bool) -> None
```

x.add_bit(value) -> None
Adds a bit.

Args:
    value (bool):

<a id="unreal.LowEntryByteArray"></a>