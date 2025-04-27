## MetasoundOutputBlueprintAccess Objects

```python
class MetasoundOutputBlueprintAccess(BlueprintFunctionLibrary)
```

Blueprint support for core types. If you want to support more core types, add them here.
If you want to support types introduced in other plugins, create a blueprint library in that plugin.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundOutput.h

<a id="unreal.MetasoundOutputBlueprintAccess.is_time"></a>

#### is_time

```python
@classmethod
def is_time(cls, output: MetaSoundOutput) -> bool
```

X.is_time(output) -> bool
Is Time

Args:
    output (MetaSoundOutput): 

Returns:
    bool:

<a id="unreal.MetasoundOutputBlueprintAccess.is_string"></a>

#### is_string

```python
@classmethod
def is_string(cls, output: MetaSoundOutput) -> bool
```

X.is_string(output) -> bool
Is String

Args:
    output (MetaSoundOutput): 

Returns:
    bool:

<a id="unreal.MetasoundOutputBlueprintAccess.is_int32"></a>

#### is_int32

```python
@classmethod
def is_int32(cls, output: MetaSoundOutput) -> bool
```

X.is_int32(output) -> bool
Is Int 32

Args:
    output (MetaSoundOutput): 

Returns:
    bool:

<a id="unreal.MetasoundOutputBlueprintAccess.is_float"></a>

#### is_float

```python
@classmethod
def is_float(cls, output: MetaSoundOutput) -> bool
```

X.is_float(output) -> bool
Is Float

Args:
    output (MetaSoundOutput): 

Returns:
    bool:

<a id="unreal.MetasoundOutputBlueprintAccess.is_bool"></a>

#### is_bool

```python
@classmethod
def is_bool(cls, output: MetaSoundOutput) -> bool
```

X.is_bool(output) -> bool
Is Bool

Args:
    output (MetaSoundOutput): 

Returns:
    bool:

<a id="unreal.MetasoundOutputBlueprintAccess.get_time_seconds"></a>

#### get_time_seconds

```python
@classmethod
def get_time_seconds(cls, output: MetaSoundOutput) -> Tuple[float, bool]
```

X.get_time_seconds(output) -> (double, success=bool)
Get Time Seconds

Args:
    output (MetaSoundOutput): 

Returns:
    bool: 

    success (bool):

<a id="unreal.MetasoundOutputBlueprintAccess.get_string"></a>

#### get_string

```python
@classmethod
def get_string(cls, output: MetaSoundOutput) -> Tuple[str, bool]
```

X.get_string(output) -> (str, success=bool)
Get String

Args:
    output (MetaSoundOutput): 

Returns:
    bool: 

    success (bool):

<a id="unreal.MetasoundOutputBlueprintAccess.get_int32"></a>

#### get_int32

```python
@classmethod
def get_int32(cls, output: MetaSoundOutput) -> Tuple[int, bool]
```

X.get_int32(output) -> (int32, success=bool)
Get Int 32

Args:
    output (MetaSoundOutput): 

Returns:
    bool: 

    success (bool):

<a id="unreal.MetasoundOutputBlueprintAccess.get_float"></a>

#### get_float

```python
@classmethod
def get_float(cls, output: MetaSoundOutput) -> Tuple[float, bool]
```

X.get_float(output) -> (float, success=bool)
Get Float

Args:
    output (MetaSoundOutput): 

Returns:
    bool: 

    success (bool):

<a id="unreal.MetasoundOutputBlueprintAccess.get_bool"></a>

#### get_bool

```python
@classmethod
def get_bool(cls, output: MetaSoundOutput) -> Optional[bool]
```

X.get_bool(output) -> bool or None
Get Bool

Args:
    output (MetaSoundOutput): 

Returns:
    bool or None: 

    success (bool):

<a id="unreal.MetaSoundOutputSubsystem"></a>