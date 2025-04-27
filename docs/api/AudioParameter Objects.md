## AudioParameter Objects

```python
class AudioParameter(StructBase)
```

Audio Parameter

**C++ Source:**

- **Module**: AudioExtensions
- **File**: AudioParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``array_bool_param`` (Array[bool]):  [Read-Write] Boolean value of parameter
- ``array_float_param`` (Array[float]):  [Read-Write] Array Float value of parameter
- ``array_int_param`` (Array[int32]):  [Read-Write] Integer value of parameter
- ``array_object_param`` (Array[Object]):  [Read-Write] Object value of parameter
- ``array_string_param`` (Array[str]):  [Read-Write] String value of parameter
- ``bool_param`` (bool):  [Read-Write] Boolean value of parameter
- ``float_param`` (float):  [Read-Write] Float value of parameter
- ``int_param`` (int32):  [Read-Write] Integer value of parameter. If set to 'Default Construct', value is number of array items to construct.
- ``object_param`` (Object):  [Read-Write] Object value of parameter
- ``param_name`` (Name):  [Read-Write] Name of the parameter
- ``param_type`` (AudioParameterType):  [Read-Write]
- ``string_param`` (str):  [Read-Write] String value of parameter

<a id="unreal.AudioParameter.__init__"></a>

#### __init__

```python
def __init__(param_name: Name = "None",
             float_param: float = 0.000000,
             bool_param: bool = False,
             int_param: int = 0,
             object_param: Object = None,
             string_param: str = "",
             array_float_param: Array[float] = [],
             array_bool_param: Array[bool] = [],
             array_int_param: Array[int] = [],
             array_object_param: Array[Object] = [],
             array_string_param: Array[str] = [],
             param_type: AudioParameterType = AudioParameterType.NONE) -> None
```

<a id="unreal.AudioParameter.param_name"></a>

#### param_name

```python
@property
def param_name() -> Name
```

(Name):  [Read-Write] Name of the parameter

<a id="unreal.AudioParameter.param_name"></a>

#### param_name

```python
@param_name.setter
def param_name(value: Name) -> None
```

<a id="unreal.AudioParameter.float_param"></a>

#### float_param

```python
@property
def float_param() -> float
```

(float):  [Read-Write] Float value of parameter

<a id="unreal.AudioParameter.float_param"></a>

#### float_param

```python
@float_param.setter
def float_param(value: float) -> None
```

<a id="unreal.AudioParameter.bool_param"></a>

#### bool_param

```python
@property
def bool_param() -> bool
```

(bool):  [Read-Write] Boolean value of parameter

<a id="unreal.AudioParameter.bool_param"></a>

#### bool_param

```python
@bool_param.setter
def bool_param(value: bool) -> None
```

<a id="unreal.AudioParameter.int_param"></a>

#### int_param

```python
@property
def int_param() -> int
```

(int32):  [Read-Write] Integer value of parameter. If set to 'Default Construct', value is number of array items to construct.

<a id="unreal.AudioParameter.int_param"></a>

#### int_param

```python
@int_param.setter
def int_param(value: int) -> None
```

<a id="unreal.AudioParameter.object_param"></a>

#### object_param

```python
@property
def object_param() -> Object
```

(Object):  [Read-Write] Object value of parameter

<a id="unreal.AudioParameter.object_param"></a>

#### object_param

```python
@object_param.setter
def object_param(value: Object) -> None
```

<a id="unreal.AudioParameter.sound_wave_param"></a>

#### sound_wave_param

```python
@property
def sound_wave_param() -> Object
```

deprecated: 'sound_wave_param' was renamed to 'object_param'.

<a id="unreal.AudioParameter.sound_wave_param"></a>

#### sound_wave_param

```python
@sound_wave_param.setter
def sound_wave_param(value: Object) -> None
```

<a id="unreal.AudioParameter.string_param"></a>

#### string_param

```python
@property
def string_param() -> str
```

(str):  [Read-Write] String value of parameter

<a id="unreal.AudioParameter.string_param"></a>

#### string_param

```python
@string_param.setter
def string_param(value: str) -> None
```

<a id="unreal.AudioParameter.array_float_param"></a>

#### array_float_param

```python
@property
def array_float_param() -> Array[float]
```

(Array[float]):  [Read-Write] Array Float value of parameter

<a id="unreal.AudioParameter.array_float_param"></a>

#### array_float_param

```python
@array_float_param.setter
def array_float_param(value: Array[float]) -> None
```

<a id="unreal.AudioParameter.array_bool_param"></a>

#### array_bool_param

```python
@property
def array_bool_param() -> Array[bool]
```

(Array[bool]):  [Read-Write] Boolean value of parameter

<a id="unreal.AudioParameter.array_bool_param"></a>

#### array_bool_param

```python
@array_bool_param.setter
def array_bool_param(value: Array[bool]) -> None
```

<a id="unreal.AudioParameter.array_int_param"></a>

#### array_int_param

```python
@property
def array_int_param() -> Array[int]
```

(Array[int32]):  [Read-Write] Integer value of parameter

<a id="unreal.AudioParameter.array_int_param"></a>

#### array_int_param

```python
@array_int_param.setter
def array_int_param(value: Array[int]) -> None
```

<a id="unreal.AudioParameter.array_object_param"></a>

#### array_object_param

```python
@property
def array_object_param() -> Array[Object]
```

(Array[Object]):  [Read-Write] Object value of parameter

<a id="unreal.AudioParameter.array_object_param"></a>

#### array_object_param

```python
@array_object_param.setter
def array_object_param(value: Array[Object]) -> None
```

<a id="unreal.AudioParameter.array_string_param"></a>

#### array_string_param

```python
@property
def array_string_param() -> Array[str]
```

(Array[str]):  [Read-Write] String value of parameter

<a id="unreal.AudioParameter.array_string_param"></a>

#### array_string_param

```python
@array_string_param.setter
def array_string_param(value: Array[str]) -> None
```

<a id="unreal.AudioParameter.param_type"></a>

#### param_type

```python
@property
def param_type() -> AudioParameterType
```

(AudioParameterType):  [Read-Write]

<a id="unreal.AudioParameter.param_type"></a>

#### param_type

```python
@param_type.setter
def param_type(value: AudioParameterType) -> None
```

<a id="unreal.ToolDynamicUIAction"></a>