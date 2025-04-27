## AudioComponentParam Objects

```python
class AudioComponentParam(AudioParameter)
```

Legacy struct used for storing named parameter for a given AudioComponent.

**C++ Source:**

- **Module**: Engine
- **File**: AudioComponent.h

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
- ``sound_wave_param`` (SoundWave):  [Read-Write] DEPRECATED
- ``string_param`` (str):  [Read-Write] String value of parameter

<a id="unreal.AudioComponentParam.__init__"></a>

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
             param_type: AudioParameterType = AudioParameterType.NONE,
             sound_wave_param: SoundWave = None) -> None
```

<a id="unreal.AudioComponentParam.sound_wave_param"></a>

#### sound_wave_param

```python
@property
def sound_wave_param() -> SoundWave
```

(SoundWave):  [Read-Write] DEPRECATED

<a id="unreal.AudioComponentParam.sound_wave_param"></a>

#### sound_wave_param

```python
@sound_wave_param.setter
def sound_wave_param(value: SoundWave) -> None
```

<a id="unreal.LODMappingData"></a>