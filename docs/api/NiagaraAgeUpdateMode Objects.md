## NiagaraAgeUpdateMode Objects

```python
class NiagaraAgeUpdateMode(EnumBase)
```

Defines modes for updating the component's age.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraAgeUpdateMode.TICK_DELTA_TIME"></a>

#### TICK_DELTA_TIME

0: Update the age using the delta time supplied to the component tick function.

<a id="unreal.NiagaraAgeUpdateMode.DESIRED_AGE"></a>

#### DESIRED_AGE

1: Update the age by seeking to the DesiredAge. To prevent major perf loss, we clamp to MaxClampTime

<a id="unreal.NiagaraAgeUpdateMode.DESIRED_AGE_NO_SEEK"></a>

#### DESIRED_AGE_NO_SEEK

2: Update the age by tracking changes to the desired age, but when the desired age goes backwards in time,
      or jumps forwards in time by more than a few steps, the system is reset and simulated forward by a single step.
      This mode is useful for continuous effects controlled by sequencer.

<a id="unreal.NiagaraTickBehavior"></a>