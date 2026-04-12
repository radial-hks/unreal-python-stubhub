## LowEntryParsedHashcash Objects

```python
class LowEntryParsedHashcash(Object)
```

Low Entry Parsed Hashcash

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryParsedHashcash.h

<a id="unreal.LowEntryParsedHashcash.to_string"></a>

#### to\_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts the Parsed Hashcash to a String, for debugging purposes.

Returns:
    str:

<a id="unreal.LowEntryParsedHashcash.get_resource"></a>

#### get\_resource

```python
def get_resource() -> str
```

x.get_resource() -> str
Returns the resource (basically the service ID) of this Hashcash.

Returns:
    str:

<a id="unreal.LowEntryParsedHashcash.get_date"></a>

#### get\_date

```python
def get_date() -> DateTime
```

x.get_date() -> DateTime
Returns the creation date (in UTC) of this Hashcash.

Returns:
    DateTime:

<a id="unreal.LowEntryParsedHashcash.get_bits"></a>

#### get\_bits

```python
def get_bits() -> int
```

x.get_bits() -> int32
Returns the bits (the strength, the value) of this Hashcash.

Returns:
    int32:

<a id="unreal.ActorSequence"></a>