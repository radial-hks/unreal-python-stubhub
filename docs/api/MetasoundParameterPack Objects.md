## MetasoundParameterPack Objects

```python
class MetasoundParameterPack(Object)
```

Here is the UObject BlueprintType that can be used in c++ and blueprint code. It holds a FMetasoundParamStorage
instance and can pass it along to the audio system's SetObjectParameter function via an AudioProxy.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundParameterPack.h

<a id="unreal.MetasoundParameterPack.set_trigger"></a>

#### set_trigger

```python
def set_trigger(parameter_name: Name,
                only_if_exists: bool = True) -> SetParamResult
```

x.set_trigger(parameter_name, only_if_exists=True) -> SetParamResult
Set Trigger

Args:
    parameter_name (Name): 
    only_if_exists (bool): 

Returns:
    SetParamResult:

<a id="unreal.MetasoundParameterPack.set_string"></a>

#### set_string

```python
def set_string(parameter_name: Name,
               value: str,
               only_if_exists: bool = True) -> SetParamResult
```

x.set_string(parameter_name, value, only_if_exists=True) -> SetParamResult
Set String

Args:
    parameter_name (Name): 
    value (str): 
    only_if_exists (bool): 

Returns:
    SetParamResult:

<a id="unreal.MetasoundParameterPack.set_int"></a>

#### set_int

```python
def set_int(parameter_name: Name,
            value: int,
            only_if_exists: bool = True) -> SetParamResult
```

x.set_int(parameter_name, value, only_if_exists=True) -> SetParamResult
Set Int

Args:
    parameter_name (Name): 
    value (int32): 
    only_if_exists (bool): 

Returns:
    SetParamResult:

<a id="unreal.MetasoundParameterPack.set_float"></a>

#### set_float

```python
def set_float(parameter_name: Name,
              value: float,
              only_if_exists: bool = True) -> SetParamResult
```

x.set_float(parameter_name, value, only_if_exists=True) -> SetParamResult
Set Float

Args:
    parameter_name (Name): 
    value (float): 
    only_if_exists (bool): 

Returns:
    SetParamResult:

<a id="unreal.MetasoundParameterPack.set_bool"></a>

#### set_bool

```python
def set_bool(parameter_name: Name,
             value: bool,
             only_if_exists: bool = True) -> SetParamResult
```

x.set_bool(parameter_name, value, only_if_exists=True) -> SetParamResult
Set Bool

Args:
    parameter_name (Name): 
    value (bool): 
    only_if_exists (bool): 

Returns:
    SetParamResult:

<a id="unreal.MetasoundParameterPack.make_metasound_parameter_pack"></a>

#### make_metasound_parameter_pack

```python
@classmethod
def make_metasound_parameter_pack(cls) -> MetasoundParameterPack
```

X.make_metasound_parameter_pack() -> MetasoundParameterPack
Make Metasound Parameter Pack

Returns:
    MetasoundParameterPack:

<a id="unreal.MetasoundParameterPack.has_trigger"></a>

#### has_trigger

```python
def has_trigger(parameter_name: Name) -> bool
```

x.has_trigger(parameter_name) -> bool
Has Trigger

Args:
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MetasoundParameterPack.has_string"></a>

#### has_string

```python
def has_string(parameter_name: Name) -> bool
```

x.has_string(parameter_name) -> bool
Has String

Args:
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MetasoundParameterPack.has_int"></a>

#### has_int

```python
def has_int(parameter_name: Name) -> bool
```

x.has_int(parameter_name) -> bool
Has Int

Args:
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MetasoundParameterPack.has_float"></a>

#### has_float

```python
def has_float(parameter_name: Name) -> bool
```

x.has_float(parameter_name) -> bool
Has Float

Args:
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MetasoundParameterPack.has_bool"></a>

#### has_bool

```python
def has_bool(parameter_name: Name) -> bool
```

x.has_bool(parameter_name) -> bool
Has Bool

Args:
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MetasoundParameterPack.get_trigger"></a>

#### get_trigger

```python
def get_trigger(parameter_name: Name) -> Optional[SetParamResult]
```

x.get_trigger(parameter_name) -> SetParamResult or None
Get Trigger

Args:
    parameter_name (Name): 

Returns:
    SetParamResult or None: 

    result (SetParamResult):

<a id="unreal.MetasoundParameterPack.get_string"></a>

#### get_string

```python
def get_string(parameter_name: Name) -> Tuple[str, SetParamResult]
```

x.get_string(parameter_name) -> (str, result=SetParamResult)
Get String

Args:
    parameter_name (Name): 

Returns:
    SetParamResult: 

    result (SetParamResult):

<a id="unreal.MetasoundParameterPack.get_int"></a>

#### get_int

```python
def get_int(parameter_name: Name) -> Tuple[int, SetParamResult]
```

x.get_int(parameter_name) -> (int32, result=SetParamResult)
Get Int

Args:
    parameter_name (Name): 

Returns:
    SetParamResult: 

    result (SetParamResult):

<a id="unreal.MetasoundParameterPack.get_float"></a>

#### get_float

```python
def get_float(parameter_name: Name) -> Tuple[float, SetParamResult]
```

x.get_float(parameter_name) -> (float, result=SetParamResult)
Get Float

Args:
    parameter_name (Name): 

Returns:
    SetParamResult: 

    result (SetParamResult):

<a id="unreal.MetasoundParameterPack.get_bool"></a>

#### get_bool

```python
def get_bool(parameter_name: Name) -> Optional[SetParamResult]
```

x.get_bool(parameter_name) -> SetParamResult or None
Get Bool

Args:
    parameter_name (Name): 

Returns:
    SetParamResult or None: 

    result (SetParamResult):

<a id="unreal.WaveTableBank"></a>