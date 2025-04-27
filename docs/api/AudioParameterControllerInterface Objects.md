## AudioParameterControllerInterface Objects

```python
class AudioParameterControllerInterface(Interface)
```

Audio Parameter Controller Interface

**C++ Source:**

- **Module**: AudioExtensions
- **File**: AudioParameterControllerInterface.h

<a id="unreal.AudioParameterControllerInterface.set_trigger_parameter"></a>

#### set_trigger_parameter

```python
def set_trigger_parameter(name: Name) -> None
```

x.set_trigger_parameter(name) -> None
Executes a named trigger.  Does *not* cache trigger value, so only executes if the sound
is already playing.  If the intent is for the trigger to execute immediately (if playing)
and be called on initialization for all future instances, call 'SetBoolParameter' with the
intended initial trigger behavior (true if trigger desired on initialization, false if not).

Args:
    name (Name):

<a id="unreal.AudioParameterControllerInterface.set_string_parameter"></a>

#### set_string_parameter

```python
def set_string_parameter(name: Name, value: str) -> None
```

x.set_string_parameter(name, value) -> None
Sets a named String

Args:
    name (Name): 
    value (str):

<a id="unreal.AudioParameterControllerInterface.set_string_array_parameter"></a>

#### set_string_array_parameter

```python
def set_string_array_parameter(name: Name, value: Array[str]) -> None
```

x.set_string_array_parameter(name, value) -> None
Sets a named String Array

Args:
    name (Name): 
    value (Array[str]):

<a id="unreal.AudioParameterControllerInterface.set_parameters_blueprint"></a>

#### set_parameters_blueprint

```python
def set_parameters_blueprint(parameters: Array[AudioParameter]) -> None
```

x.set_parameters_blueprint(parameters) -> None
Sets an array of parameters as a batch

Args:
    parameters (Array[AudioParameter]):

<a id="unreal.AudioParameterControllerInterface.set_object_parameter"></a>

#### set_object_parameter

```python
def set_object_parameter(name: Name, value: Object) -> None
```

x.set_object_parameter(name, value) -> None
Sets a named UObject

Args:
    name (Name): 
    value (Object):

<a id="unreal.AudioParameterControllerInterface.set_object_array_parameter"></a>

#### set_object_array_parameter

```python
def set_object_array_parameter(name: Name, value: Array[Object]) -> None
```

x.set_object_array_parameter(name, value) -> None
Sets a named UObject Array

Args:
    name (Name): 
    value (Array[Object]):

<a id="unreal.AudioParameterControllerInterface.set_int_parameter"></a>

#### set_int_parameter

```python
def set_int_parameter(name: Name, int: int) -> None
```

x.set_int_parameter(name, int) -> None
Sets a named Int32

Args:
    name (Name): 
    int (int32):

<a id="unreal.AudioParameterControllerInterface.set_int_array_parameter"></a>

#### set_int_array_parameter

```python
def set_int_array_parameter(name: Name, value: Array[int]) -> None
```

x.set_int_array_parameter(name, value) -> None
Sets a named Int32 Array

Args:
    name (Name): 
    value (Array[int32]):

<a id="unreal.AudioParameterControllerInterface.set_float_parameter"></a>

#### set_float_parameter

```python
def set_float_parameter(name: Name, float: float) -> None
```

x.set_float_parameter(name, float) -> None
Sets a named Float

Args:
    name (Name): 
    float (float):

<a id="unreal.AudioParameterControllerInterface.set_float_array_parameter"></a>

#### set_float_array_parameter

```python
def set_float_array_parameter(name: Name, value: Array[float]) -> None
```

x.set_float_array_parameter(name, value) -> None
Sets a named Float Array

Args:
    name (Name): 
    value (Array[float]):

<a id="unreal.AudioParameterControllerInterface.set_bool_parameter"></a>

#### set_bool_parameter

```python
def set_bool_parameter(name: Name, bool: bool) -> None
```

x.set_bool_parameter(name, bool) -> None
Sets a named Boolean

Args:
    name (Name): 
    bool (bool):

<a id="unreal.AudioParameterControllerInterface.set_bool_array_parameter"></a>

#### set_bool_array_parameter

```python
def set_bool_array_parameter(name: Name, value: Array[bool]) -> None
```

x.set_bool_array_parameter(name, value) -> None
Sets a named Boolean Array

Args:
    name (Name): 
    value (Array[bool]):

<a id="unreal.AudioParameterControllerInterface.reset_parameters"></a>

#### reset_parameters

```python
def reset_parameters() -> None
```

x.reset_parameters() -> None
Resets all parameters to their original values.

<a id="unreal.AudioParameterInterface"></a>