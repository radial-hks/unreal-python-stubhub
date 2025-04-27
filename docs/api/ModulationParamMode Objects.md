## ModulationParamMode Objects

```python
class ModulationParamMode(EnumBase)
```

Modulation Param Mode

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeModulatorContinuous.h

<a id="unreal.ModulationParamMode.MPM_NORMAL"></a>

#### MPM_NORMAL

0: Clamps input value to the range (MinInput, MaxInput) then maps to the range (MinOutput, MaxOutput)

<a id="unreal.ModulationParamMode.MPM_ABS"></a>

#### MPM_ABS

1: Same as Normal except that the input value is treated as an absolute value

<a id="unreal.ModulationParamMode.MPM_DIRECT"></a>

#### MPM_DIRECT

2: Use the input value directly without scaling or reference to Min or Max input or output values

<a id="unreal.VolumeLightingMethod"></a>