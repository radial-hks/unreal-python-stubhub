## SubmixEffectReverbSettings Objects

```python
class SubmixEffectReverbSettings(StructBase)
```

Submix Effect Reverb Settings

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air_absorption_gain_hf`` (float):  [Read-Write] Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption
- ``bypass`` (bool):  [Read-Write] Bypasses reverb
- ``bypass_early_reflections`` (bool):  [Read-Write] Bypasses early reflections
- ``bypass_late_reflections`` (bool):  [Read-Write] Bypasses late reflections.
- ``decay_hf_ratio`` (float):  [Read-Write] Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much quicker or slower the high frequencies decay relative to the lower frequencies.
- ``decay_time`` (float):  [Read-Write] Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb
- ``density`` (float):  [Read-Write] Density - 0.0 < 0.85 < 1.0 - Coloration of the late reverb - lower value is more grainy
- ``diffusion`` (float):  [Read-Write] Diffusion - 0.0 < 0.85 < 1.0 - Echo density in the reverberation decay - lower is more grainy
- ``dry_level`` (float):  [Read-Write] Overall dry level of the reverb effect
- ``gain`` (float):  [Read-Write] Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control
- ``gain_hf`` (float):  [Read-Write] Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound
- ``late_delay`` (float):  [Read-Write] Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections
- ``late_gain`` (float):  [Read-Write] Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb
- ``reflections_delay`` (float):  [Read-Write] Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection
- ``reflections_gain`` (float):  [Read-Write] Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections
- ``wet_level`` (float):  [Read-Write] Overall wet level of the reverb effect

<a id="unreal.SubmixEffectReverbSettings.__init__"></a>

#### __init__

```python
def __init__(bypass_early_reflections: bool = False,
             reflections_delay: float = 0.000000,
             gain_hf: float = 0.000000,
             reflections_gain: float = 0.000000,
             bypass_late_reflections: bool = False,
             late_delay: float = 0.000000,
             decay_time: float = 0.000000,
             density: float = 0.000000,
             diffusion: float = 0.000000,
             air_absorption_gain_hf: float = 0.000000,
             decay_hf_ratio: float = 0.000000,
             late_gain: float = 0.000000,
             gain: float = 0.000000,
             wet_level: float = 0.000000,
             dry_level: float = 0.000000,
             bypass: bool = False) -> None
```

<a id="unreal.SubmixEffectReverbSettings.bypass_early_reflections"></a>

#### bypass_early_reflections

```python
@property
def bypass_early_reflections() -> bool
```

(bool):  [Read-Write] Bypasses early reflections

<a id="unreal.SubmixEffectReverbSettings.bypass_early_reflections"></a>

#### bypass_early_reflections

```python
@bypass_early_reflections.setter
def bypass_early_reflections(value: bool) -> None
```

<a id="unreal.SubmixEffectReverbSettings.reflections_delay"></a>

#### reflections_delay

```python
@property
def reflections_delay() -> float
```

(float):  [Read-Write] Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection

<a id="unreal.SubmixEffectReverbSettings.reflections_delay"></a>

#### reflections_delay

```python
@reflections_delay.setter
def reflections_delay(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.gain_hf"></a>

#### gain_hf

```python
@property
def gain_hf() -> float
```

(float):  [Read-Write] Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound

<a id="unreal.SubmixEffectReverbSettings.gain_hf"></a>

#### gain_hf

```python
@gain_hf.setter
def gain_hf(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.reflections_gain"></a>

#### reflections_gain

```python
@property
def reflections_gain() -> float
```

(float):  [Read-Write] Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections

<a id="unreal.SubmixEffectReverbSettings.reflections_gain"></a>

#### reflections_gain

```python
@reflections_gain.setter
def reflections_gain(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.bypass_late_reflections"></a>

#### bypass_late_reflections

```python
@property
def bypass_late_reflections() -> bool
```

(bool):  [Read-Write] Bypasses late reflections.

<a id="unreal.SubmixEffectReverbSettings.bypass_late_reflections"></a>

#### bypass_late_reflections

```python
@bypass_late_reflections.setter
def bypass_late_reflections(value: bool) -> None
```

<a id="unreal.SubmixEffectReverbSettings.late_delay"></a>

#### late_delay

```python
@property
def late_delay() -> float
```

(float):  [Read-Write] Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections

<a id="unreal.SubmixEffectReverbSettings.late_delay"></a>

#### late_delay

```python
@late_delay.setter
def late_delay(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.decay_time"></a>

#### decay_time

```python
@property
def decay_time() -> float
```

(float):  [Read-Write] Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb

<a id="unreal.SubmixEffectReverbSettings.decay_time"></a>

#### decay_time

```python
@decay_time.setter
def decay_time(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.density"></a>

#### density

```python
@property
def density() -> float
```

(float):  [Read-Write] Density - 0.0 < 0.85 < 1.0 - Coloration of the late reverb - lower value is more grainy

<a id="unreal.SubmixEffectReverbSettings.density"></a>

#### density

```python
@density.setter
def density(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.diffusion"></a>

#### diffusion

```python
@property
def diffusion() -> float
```

(float):  [Read-Write] Diffusion - 0.0 < 0.85 < 1.0 - Echo density in the reverberation decay - lower is more grainy

<a id="unreal.SubmixEffectReverbSettings.diffusion"></a>

#### diffusion

```python
@diffusion.setter
def diffusion(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.air_absorption_gain_hf"></a>

#### air_absorption_gain_hf

```python
@property
def air_absorption_gain_hf() -> float
```

(float):  [Read-Write] Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption

<a id="unreal.SubmixEffectReverbSettings.air_absorption_gain_hf"></a>

#### air_absorption_gain_hf

```python
@air_absorption_gain_hf.setter
def air_absorption_gain_hf(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.decay_hf_ratio"></a>

#### decay_hf_ratio

```python
@property
def decay_hf_ratio() -> float
```

(float):  [Read-Write] Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much quicker or slower the high frequencies decay relative to the lower frequencies.

<a id="unreal.SubmixEffectReverbSettings.decay_hf_ratio"></a>

#### decay_hf_ratio

```python
@decay_hf_ratio.setter
def decay_hf_ratio(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.late_gain"></a>

#### late_gain

```python
@property
def late_gain() -> float
```

(float):  [Read-Write] Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb

<a id="unreal.SubmixEffectReverbSettings.late_gain"></a>

#### late_gain

```python
@late_gain.setter
def late_gain(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.gain"></a>

#### gain

```python
@property
def gain() -> float
```

(float):  [Read-Write] Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control

<a id="unreal.SubmixEffectReverbSettings.gain"></a>

#### gain

```python
@gain.setter
def gain(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write] Overall wet level of the reverb effect

<a id="unreal.SubmixEffectReverbSettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.dry_level"></a>

#### dry_level

```python
@property
def dry_level() -> float
```

(float):  [Read-Write] Overall dry level of the reverb effect

<a id="unreal.SubmixEffectReverbSettings.dry_level"></a>

#### dry_level

```python
@dry_level.setter
def dry_level(value: float) -> None
```

<a id="unreal.SubmixEffectReverbSettings.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write] Bypasses reverb

<a id="unreal.SubmixEffectReverbSettings.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.SubmixEffectReverbFastSettings"></a>