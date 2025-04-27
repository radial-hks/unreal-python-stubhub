## GuidLibrary Objects

```python
class GuidLibrary(BlueprintFunctionLibrary)
```

Kismet Guid Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetGuidLibrary.h

<a id="unreal.GuidLibrary.parse_string_to_guid"></a>

#### parse_string_to_guid

```python
@classmethod
def parse_string_to_guid(cls, guid_string: str) -> Tuple[Guid, bool]
```

X.parse_string_to_guid(guid_string) -> (out_guid=Guid, success=bool)
Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

Args:
    guid_string (str): 

Returns:
    tuple: 

    out_guid (Guid): 

    success (bool):

<a id="unreal.GuidLibrary.not_equal_guid_guid"></a>

#### not_equal_guid_guid

```python
@classmethod
def not_equal_guid_guid(cls, a: Guid, b: Guid) -> bool
```

X.not_equal_guid_guid(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (Guid): 
    b (Guid): 

Returns:
    bool:

<a id="unreal.GuidLibrary.new_guid"></a>

#### new_guid

```python
@classmethod
def new_guid(cls) -> Guid
```

X.new_guid() -> Guid
Returns a new unique GUID

Returns:
    Guid:

<a id="unreal.GuidLibrary.is_valid_guid"></a>

#### is_valid_guid

```python
@classmethod
def is_valid_guid(cls, guid: Guid) -> bool
```

X.is_valid_guid(guid) -> bool
Checks whether the given GUID is valid

Args:
    guid (Guid): 

Returns:
    bool:

<a id="unreal.GuidLibrary.invalidate_guid"></a>

#### invalidate_guid

```python
@classmethod
def invalidate_guid(cls, guid: Guid) -> Guid
```

X.invalidate_guid(guid) -> Guid
Invalidates the given GUID

Args:
    guid (Guid): 

Returns:
    Guid: 

    guid (Guid):

<a id="unreal.GuidLibrary.equal_equal_guid_guid"></a>

#### equal_equal_guid_guid

```python
@classmethod
def equal_equal_guid_guid(cls, a: Guid, b: Guid) -> bool
```

X.equal_equal_guid_guid(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (Guid): 
    b (Guid): 

Returns:
    bool:

<a id="unreal.GuidLibrary.conv_guid_to_string"></a>

#### conv_guid_to_string

```python
@classmethod
def conv_guid_to_string(cls, guid: Guid) -> str
```

X.conv_guid_to_string(guid) -> str
Converts a GUID value to a string, in the form 'A-B-C-D'

Args:
    guid (Guid): 

Returns:
    str:

<a id="unreal.InputLibrary"></a>