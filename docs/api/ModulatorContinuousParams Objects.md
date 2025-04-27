## ModulatorContinuousParams Objects

```python
class ModulatorContinuousParams(StructBase)
```

Modulator Continuous Params

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeModulatorContinuous.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default`` (float):  [Read-Write] The default value to be used if the parameter is not found.
- ``max_input`` (float):  [Read-Write] The maximum input value. Values will be clamped to the [MinInput, MaxInput] range.
- ``max_output`` (float):  [Read-Write] The maximum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput]
- ``min_input`` (float):  [Read-Write] The minimum input value. Values will be clamped to the [MinInput, MaxInput] range.
- ``min_output`` (float):  [Read-Write] The minimum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput]
- ``param_mode`` (ModulationParamMode):  [Read-Write] The mode with which to treat the input value
- ``parameter_name`` (Name):  [Read-Write] The name of the sound instance parameter that specifies the current value.

<a id="unreal.ModulatorContinuousParams.__init__"></a>

#### __init__

```python
def __init__(parameter_name: Name = "None") -> None
```

<a id="unreal.ModulatorContinuousParams.parameter_name"></a>

#### parameter_name

```python
@property
def parameter_name() -> Name
```

(Name):  [Read-Only] The name of the sound instance parameter that specifies the current value.

<a id="unreal.SoundSourceBusSendInfo"></a>