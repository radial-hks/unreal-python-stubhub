## ReverbEffect Objects

```python
class ReverbEffect(Object)
```

Reverb Effect

**C++ Source:**

- **Module**: Engine
- **File**: ReverbEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air_absorption_gain_hf`` (float):  [Read-Write] Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption
- ``bypass_early_reflections`` (bool):  [Read-Write] Bypasses early reflections
- ``bypass_late_reflections`` (bool):  [Read-Write] Bypasses late reflections.
- ``decay_hf_ratio`` (float):  [Read-Write] Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much quicker or slower the high frequencies decay relative to the lower frequencies.
- ``decay_time`` (float):  [Read-Write] Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb
- ``density`` (float):  [Read-Write] Density - 0.0 < 1.0 < 1.0 - Coloration of the late reverb - lower value is more grainy
- ``diffusion`` (float):  [Read-Write] Diffusion - 0.0 < 1.0 < 1.0 - Echo density in the reverberation decay - lower is more grainy
- ``gain`` (float):  [Read-Write] Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control
- ``gain_hf`` (float):  [Read-Write] Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound
- ``late_delay`` (float):  [Read-Write] Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections
- ``late_gain`` (float):  [Read-Write] Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb
- ``reflections_delay`` (float):  [Read-Write] Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection
- ``reflections_gain`` (float):  [Read-Write] Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections

<a id="unreal.ReverbEffect.bypass_early_reflections"></a>

#### bypass_early_reflections

```python
@property
def bypass_early_reflections() -> bool
```

(bool):  [Read-Write] Bypasses early reflections

<a id="unreal.ReverbEffect.bypass_early_reflections"></a>

#### bypass_early_reflections

```python
@bypass_early_reflections.setter
def bypass_early_reflections(value: bool) -> None
```

<a id="unreal.ReverbEffect.bypass_late_reflections"></a>

#### bypass_late_reflections

```python
@property
def bypass_late_reflections() -> bool
```

(bool):  [Read-Write] Bypasses late reflections.

<a id="unreal.ReverbEffect.bypass_late_reflections"></a>

#### bypass_late_reflections

```python
@bypass_late_reflections.setter
def bypass_late_reflections(value: bool) -> None
```

<a id="unreal.RuntimeOptionsBase"></a>