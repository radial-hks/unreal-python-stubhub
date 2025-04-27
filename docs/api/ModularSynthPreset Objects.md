## ModularSynthPreset Objects

```python
class ModularSynthPreset(TableRowBase)
```

Modular Synth Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EpicSynth1Component.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attack_time`` (float):  [Read-Write] The amplitude envelope attack time (in ms) [0.0, 10000]
- ``chorus_depth`` (float):  [Read-Write] The depth of the chorus effect [0.0, 1.0]
- ``chorus_enabled`` (bool):  [Read-Write] Whether or not the chorus effect is enabled
- ``chorus_feedback`` (float):  [Read-Write] The amount of feedback in the chorus effect [0.0, 1.0]
- ``chorus_frequency`` (float):  [Read-Write] The chorus LFO frequency [0.0, 20.0]
- ``decay_time`` (float):  [Read-Write] The amplitude envelope decay time (in ms)[0.0, 10000]
- ``enable_oscillator_sync`` (bool):  [Read-Write] Whether or not oscillator sync is enabled. Oscillator sync forces oscillator 2's phase to align with oscillator 1's phase.
- ``enable_polyphony`` (bool):  [Read-Write] Whether or not to allow multiple synth voices.
- ``enable_unison`` (bool):  [Read-Write] Enables forcing the oscillators to have no stereo spread.
- ``filter_algorithm`` (SynthFilterAlgorithm):  [Read-Write] The output filter circuit/algorithm type (one-pole ladder, ladder, state-variable)
- ``filter_frequency`` (float):  [Read-Write] The output filter cutoff frequency (hz) [0.0, 20000.0]
- ``filter_q`` (float):  [Read-Write] The output filter resonance (Q) [0.5, 10]
- ``filter_type`` (SynthFilterType):  [Read-Write] The output filter type (lowpass, highpass, bandpass, bandstop)
- ``gain_db`` (float):  [Read-Write] The overall gain to use for the synthesizer in dB [-90.0, 20.0]
- ``invert_modulation_envelope`` (bool):  [Read-Write] Whether or not to invert the modulation envelope
- ``invert_modulation_envelope_bias`` (bool):  [Read-Write] Whether or not to invert the modulation envelope bias output
- ``legato`` (bool):  [Read-Write] Whether or not to use legato mode.
- ``lfo1_frequency`` (float):  [Read-Write] The frequency to use for LFO 1 (in hz) [0.0, 50.0]
- ``lfo1_gain`` (float):  [Read-Write] The linear gain to use for LFO 1 [0.0, 1.0]
- ``lfo1_mode`` (SynthLFOMode):  [Read-Write] The mode to use for LFO 1
- ``lfo1_patch_type`` (SynthLFOPatchType):  [Read-Write] The built-in patch type to use for LFO 1 (you can route this to any patchable parameter using the Patches parameter)
- ``lfo1_type`` (SynthLFOType):  [Read-Write] The type of LFO to use for LFO 1
- ``lfo2_frequency`` (float):  [Read-Write] The frequency to use for LFO 2 (in hz) [0.0, 50.0]
- ``lfo2_gain`` (float):  [Read-Write] The linear gain to use for LFO 2 [0.0, 1.0]
- ``lfo2_mode`` (SynthLFOMode):  [Read-Write] The mode to use for LFO 2
- ``lfo2_patch_type`` (SynthLFOPatchType):  [Read-Write] The built-in patch type to use for LFO 2 (you can route this to any patchable parameter using the Patches parameter)
- ``lfo2_type`` (SynthLFOType):  [Read-Write] The type of LFO to use for LFO 2
- ``mod_env_bias_patch_type`` (SynthModEnvBiasPatch):  [Read-Write] The built-in patch type for the envelope modulator bias output. Bias is when the envelope output is offset by the sustain gain.
- ``mod_env_patch_type`` (SynthModEnvPatch):  [Read-Write] The built-in patch type for the envelope modulator
- ``modulation_envelope_attack_time`` (float):  [Read-Write] The modulation envelope attack time (in ms) [0.0, 10000]
- ``modulation_envelope_decay_time`` (float):  [Read-Write] The modulation envelope decay time (in ms) [0.0, 10000]
- ``modulation_envelope_depth`` (float):  [Read-Write] The "depth" (i.e. how much) modulation envelope to use. This scales the modulation envelope output. [0.0, 1.0]
- ``modulation_envelope_release_time`` (float):  [Read-Write] The modulation envelope release time (in ms) [0.0, 10000]
- ``modulation_envelope_sustain_gain`` (float):  [Read-Write] The modulation envelope sustain gain (linear gain) [0.0, 1.0]
- ``osc1_cents`` (float):  [Read-Write] The cents (hundreds of a semitone) of oscillator 1. [-100.0, 100.0]
- ``osc1_gain`` (float):  [Read-Write] The linear gain of oscillator 1 [0.0, 1.0]
- ``osc1_octave`` (float):  [Read-Write] The octave of oscillator 1. [-8.0, 8.0]
- ``osc1_pulse_width`` (float):  [Read-Write] The pulsewidth of oscillator 1 (when using a square wave type oscillator). [0.0, 1.0]
- ``osc1_semitones`` (float):  [Read-Write] The semi-tones of oscillator 1. [-12.0, 12.0]
- ``osc1_type`` (Synth1OscType):  [Read-Write] What type of oscillator to use for oscillator 1
- ``osc2_cents`` (float):  [Read-Write] The cents (hundreds of a semitone) of oscillator 2. [-100.0, 100.0]
- ``osc2_gain`` (float):  [Read-Write] The linear gain of oscillator 2 [0.0, 1.0]
- ``osc2_octave`` (float):  [Read-Write] The octave of oscillator 2. [-8.0, 8.0]
- ``osc2_pulse_width`` (float):  [Read-Write] The pulsewidth of oscillator 2 (when using a square wave type oscillator). [0.0, 1.0]
- ``osc2_semitones`` (float):  [Read-Write] The semi-tones of oscillator 2. [-12.0, 12.0]
- ``osc2_type`` (Synth1OscType):  [Read-Write] What type of oscillator to use for oscillator 2
- ``pan`` (float):  [Read-Write] The stereo pan to use. 0.0 is center. -1.0 is left, 1.0 is right.
- ``patches`` (Array[EpicSynth1Patch]):  [Read-Write] The modular synth patch cords to use for the synth. Allows routing the LFO1/LFO2 and Modulation Envelope to any patchable destination.
- ``portamento`` (float):  [Read-Write] The amount of portamento to use, which is the amount of pitch sliding from current note to next [0.0, 1.0]
- ``release_time`` (float):  [Read-Write] The amplitude envelope release time (in ms) [0.0, 10000]
- ``retrigger`` (bool):  [Read-Write] Whether or not to use retrigger mode.
- ``spread`` (float):  [Read-Write] The amount of stereo spread to use between oscillator 1 and oscillator 2 [0.0, 1.0]
- ``stereo_delay_enabled`` (bool):  [Read-Write] Whether or not stereo delay is enabled on the synth
- ``stereo_delay_feedback`` (float):  [Read-Write] The amount of feedback in the stereo delay line [0.0, 1.0]
- ``stereo_delay_mode`` (SynthStereoDelayMode):  [Read-Write] The stereo delay mode of the synth
- ``stereo_delay_ratio`` (float):  [Read-Write] The ratio between left and right stereo delay lines (wider value is more separation) [0.0, 1.0]
- ``stereo_delay_time`` (float):  [Read-Write] The stereo delay time (in ms) [0.0, 2000.0]
- ``stereo_delay_wetlevel`` (float):  [Read-Write] The output wet level to use for the stereo delay time [0.0, 1.0]
- ``sustain_gain`` (float):  [Read-Write] The amplitude envelope sustain amount (linear gain) [0.0, 1.0]

<a id="unreal.ModularSynthPreset.__init__"></a>

#### __init__

```python
def __init__(
        enable_polyphony: bool = False,
        osc1_type: Synth1OscType = Synth1OscType.SINE,
        osc1_gain: float = 0.000000,
        osc1_octave: float = 0.000000,
        osc1_semitones: float = 0.000000,
        osc1_cents: float = 0.000000,
        osc1_pulse_width: float = 0.000000,
        osc2_type: Synth1OscType = Synth1OscType.SINE,
        osc2_gain: float = 0.000000,
        osc2_octave: float = 0.000000,
        osc2_semitones: float = 0.000000,
        osc2_cents: float = 0.000000,
        osc2_pulse_width: float = 0.000000,
        portamento: float = 0.000000,
        enable_unison: bool = False,
        enable_oscillator_sync: bool = False,
        spread: float = 0.000000,
        pan: float = 0.000000,
        lfo1_frequency: float = 0.000000,
        lfo1_gain: float = 0.000000,
        lfo1_type: SynthLFOType = SynthLFOType.SINE,
        lfo1_mode: SynthLFOMode = SynthLFOMode.SYNC,
        lfo1_patch_type: SynthLFOPatchType = SynthLFOPatchType.PATCH_TO_NONE,
        lfo2_frequency: float = 0.000000,
        lfo2_gain: float = 0.000000,
        lfo2_type: SynthLFOType = SynthLFOType.SINE,
        lfo2_mode: SynthLFOMode = SynthLFOMode.SYNC,
        lfo2_patch_type: SynthLFOPatchType = SynthLFOPatchType.PATCH_TO_NONE,
        gain_db: float = 0.000000,
        attack_time: float = 0.000000,
        decay_time: float = 0.000000,
        sustain_gain: float = 0.000000,
        release_time: float = 0.000000,
        mod_env_patch_type: SynthModEnvPatch = SynthModEnvPatch.PATCH_TO_NONE,
        mod_env_bias_patch_type: SynthModEnvBiasPatch = SynthModEnvBiasPatch.
    PATCH_TO_NONE,
        invert_modulation_envelope: bool = False,
        invert_modulation_envelope_bias: bool = False,
        modulation_envelope_depth: float = 0.000000,
        modulation_envelope_attack_time: float = 0.000000,
        modulation_envelope_decay_time: float = 0.000000,
        modulation_envelope_sustain_gain: float = 0.000000,
        modulation_envelope_release_time: float = 0.000000,
        legato: bool = False,
        retrigger: bool = False,
        filter_frequency: float = 0.000000,
        filter_q: float = 0.000000,
        filter_type: SynthFilterType = SynthFilterType.LOW_PASS,
        filter_algorithm: SynthFilterAlgorithm = SynthFilterAlgorithm.ONE_POLE,
        stereo_delay_enabled: bool = False,
        stereo_delay_mode: SynthStereoDelayMode = SynthStereoDelayMode.NORMAL,
        stereo_delay_time: float = 0.000000,
        stereo_delay_feedback: float = 0.000000,
        stereo_delay_wetlevel: float = 0.000000,
        stereo_delay_ratio: float = 0.000000,
        chorus_enabled: bool = False,
        chorus_depth: float = 0.000000,
        chorus_feedback: float = 0.000000,
        chorus_frequency: float = 0.000000,
        patches: Array[EpicSynth1Patch] = []) -> None
```

<a id="unreal.ModularSynthPreset.enable_polyphony"></a>

#### enable_polyphony

```python
@property
def enable_polyphony() -> bool
```

(bool):  [Read-Write] Whether or not to allow multiple synth voices.

<a id="unreal.ModularSynthPreset.enable_polyphony"></a>

#### enable_polyphony

```python
@enable_polyphony.setter
def enable_polyphony(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.osc1_type"></a>

#### osc1_type

```python
@property
def osc1_type() -> Synth1OscType
```

(Synth1OscType):  [Read-Write] What type of oscillator to use for oscillator 1

<a id="unreal.ModularSynthPreset.osc1_type"></a>

#### osc1_type

```python
@osc1_type.setter
def osc1_type(value: Synth1OscType) -> None
```

<a id="unreal.ModularSynthPreset.osc1_gain"></a>

#### osc1_gain

```python
@property
def osc1_gain() -> float
```

(float):  [Read-Write] The linear gain of oscillator 1 [0.0, 1.0]

<a id="unreal.ModularSynthPreset.osc1_gain"></a>

#### osc1_gain

```python
@osc1_gain.setter
def osc1_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc1_octave"></a>

#### osc1_octave

```python
@property
def osc1_octave() -> float
```

(float):  [Read-Write] The octave of oscillator 1. [-8.0, 8.0]

<a id="unreal.ModularSynthPreset.osc1_octave"></a>

#### osc1_octave

```python
@osc1_octave.setter
def osc1_octave(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc1_semitones"></a>

#### osc1_semitones

```python
@property
def osc1_semitones() -> float
```

(float):  [Read-Write] The semi-tones of oscillator 1. [-12.0, 12.0]

<a id="unreal.ModularSynthPreset.osc1_semitones"></a>

#### osc1_semitones

```python
@osc1_semitones.setter
def osc1_semitones(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc1_cents"></a>

#### osc1_cents

```python
@property
def osc1_cents() -> float
```

(float):  [Read-Write] The cents (hundreds of a semitone) of oscillator 1. [-100.0, 100.0]

<a id="unreal.ModularSynthPreset.osc1_cents"></a>

#### osc1_cents

```python
@osc1_cents.setter
def osc1_cents(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc1_pulse_width"></a>

#### osc1_pulse_width

```python
@property
def osc1_pulse_width() -> float
```

(float):  [Read-Write] The pulsewidth of oscillator 1 (when using a square wave type oscillator). [0.0, 1.0]

<a id="unreal.ModularSynthPreset.osc1_pulse_width"></a>

#### osc1_pulse_width

```python
@osc1_pulse_width.setter
def osc1_pulse_width(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc2_type"></a>

#### osc2_type

```python
@property
def osc2_type() -> Synth1OscType
```

(Synth1OscType):  [Read-Write] What type of oscillator to use for oscillator 2

<a id="unreal.ModularSynthPreset.osc2_type"></a>

#### osc2_type

```python
@osc2_type.setter
def osc2_type(value: Synth1OscType) -> None
```

<a id="unreal.ModularSynthPreset.osc2_gain"></a>

#### osc2_gain

```python
@property
def osc2_gain() -> float
```

(float):  [Read-Write] The linear gain of oscillator 2 [0.0, 1.0]

<a id="unreal.ModularSynthPreset.osc2_gain"></a>

#### osc2_gain

```python
@osc2_gain.setter
def osc2_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc2_octave"></a>

#### osc2_octave

```python
@property
def osc2_octave() -> float
```

(float):  [Read-Write] The octave of oscillator 2. [-8.0, 8.0]

<a id="unreal.ModularSynthPreset.osc2_octave"></a>

#### osc2_octave

```python
@osc2_octave.setter
def osc2_octave(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc2_semitones"></a>

#### osc2_semitones

```python
@property
def osc2_semitones() -> float
```

(float):  [Read-Write] The semi-tones of oscillator 2. [-12.0, 12.0]

<a id="unreal.ModularSynthPreset.osc2_semitones"></a>

#### osc2_semitones

```python
@osc2_semitones.setter
def osc2_semitones(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc2_cents"></a>

#### osc2_cents

```python
@property
def osc2_cents() -> float
```

(float):  [Read-Write] The cents (hundreds of a semitone) of oscillator 2. [-100.0, 100.0]

<a id="unreal.ModularSynthPreset.osc2_cents"></a>

#### osc2_cents

```python
@osc2_cents.setter
def osc2_cents(value: float) -> None
```

<a id="unreal.ModularSynthPreset.osc2_pulse_width"></a>

#### osc2_pulse_width

```python
@property
def osc2_pulse_width() -> float
```

(float):  [Read-Write] The pulsewidth of oscillator 2 (when using a square wave type oscillator). [0.0, 1.0]

<a id="unreal.ModularSynthPreset.osc2_pulse_width"></a>

#### osc2_pulse_width

```python
@osc2_pulse_width.setter
def osc2_pulse_width(value: float) -> None
```

<a id="unreal.ModularSynthPreset.portamento"></a>

#### portamento

```python
@property
def portamento() -> float
```

(float):  [Read-Write] The amount of portamento to use, which is the amount of pitch sliding from current note to next [0.0, 1.0]

<a id="unreal.ModularSynthPreset.portamento"></a>

#### portamento

```python
@portamento.setter
def portamento(value: float) -> None
```

<a id="unreal.ModularSynthPreset.enable_unison"></a>

#### enable_unison

```python
@property
def enable_unison() -> bool
```

(bool):  [Read-Write] Enables forcing the oscillators to have no stereo spread.

<a id="unreal.ModularSynthPreset.enable_unison"></a>

#### enable_unison

```python
@enable_unison.setter
def enable_unison(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.enable_oscillator_sync"></a>

#### enable_oscillator_sync

```python
@property
def enable_oscillator_sync() -> bool
```

(bool):  [Read-Write] Whether or not oscillator sync is enabled. Oscillator sync forces oscillator 2's phase to align with oscillator 1's phase.

<a id="unreal.ModularSynthPreset.enable_oscillator_sync"></a>

#### enable_oscillator_sync

```python
@enable_oscillator_sync.setter
def enable_oscillator_sync(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.spread"></a>

#### spread

```python
@property
def spread() -> float
```

(float):  [Read-Write] The amount of stereo spread to use between oscillator 1 and oscillator 2 [0.0, 1.0]

<a id="unreal.ModularSynthPreset.spread"></a>

#### spread

```python
@spread.setter
def spread(value: float) -> None
```

<a id="unreal.ModularSynthPreset.pan"></a>

#### pan

```python
@property
def pan() -> float
```

(float):  [Read-Write] The stereo pan to use. 0.0 is center. -1.0 is left, 1.0 is right.

<a id="unreal.ModularSynthPreset.pan"></a>

#### pan

```python
@pan.setter
def pan(value: float) -> None
```

<a id="unreal.ModularSynthPreset.lfo1_frequency"></a>

#### lfo1_frequency

```python
@property
def lfo1_frequency() -> float
```

(float):  [Read-Write] The frequency to use for LFO 1 (in hz) [0.0, 50.0]

<a id="unreal.ModularSynthPreset.lfo1_frequency"></a>

#### lfo1_frequency

```python
@lfo1_frequency.setter
def lfo1_frequency(value: float) -> None
```

<a id="unreal.ModularSynthPreset.lfo1_gain"></a>

#### lfo1_gain

```python
@property
def lfo1_gain() -> float
```

(float):  [Read-Write] The linear gain to use for LFO 1 [0.0, 1.0]

<a id="unreal.ModularSynthPreset.lfo1_gain"></a>

#### lfo1_gain

```python
@lfo1_gain.setter
def lfo1_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.lfo1_type"></a>

#### lfo1_type

```python
@property
def lfo1_type() -> SynthLFOType
```

(SynthLFOType):  [Read-Write] The type of LFO to use for LFO 1

<a id="unreal.ModularSynthPreset.lfo1_type"></a>

#### lfo1_type

```python
@lfo1_type.setter
def lfo1_type(value: SynthLFOType) -> None
```

<a id="unreal.ModularSynthPreset.lfo1_mode"></a>

#### lfo1_mode

```python
@property
def lfo1_mode() -> SynthLFOMode
```

(SynthLFOMode):  [Read-Write] The mode to use for LFO 1

<a id="unreal.ModularSynthPreset.lfo1_mode"></a>

#### lfo1_mode

```python
@lfo1_mode.setter
def lfo1_mode(value: SynthLFOMode) -> None
```

<a id="unreal.ModularSynthPreset.lfo1_patch_type"></a>

#### lfo1_patch_type

```python
@property
def lfo1_patch_type() -> SynthLFOPatchType
```

(SynthLFOPatchType):  [Read-Write] The built-in patch type to use for LFO 1 (you can route this to any patchable parameter using the Patches parameter)

<a id="unreal.ModularSynthPreset.lfo1_patch_type"></a>

#### lfo1_patch_type

```python
@lfo1_patch_type.setter
def lfo1_patch_type(value: SynthLFOPatchType) -> None
```

<a id="unreal.ModularSynthPreset.lfo2_frequency"></a>

#### lfo2_frequency

```python
@property
def lfo2_frequency() -> float
```

(float):  [Read-Write] The frequency to use for LFO 2 (in hz) [0.0, 50.0]

<a id="unreal.ModularSynthPreset.lfo2_frequency"></a>

#### lfo2_frequency

```python
@lfo2_frequency.setter
def lfo2_frequency(value: float) -> None
```

<a id="unreal.ModularSynthPreset.lfo2_gain"></a>

#### lfo2_gain

```python
@property
def lfo2_gain() -> float
```

(float):  [Read-Write] The linear gain to use for LFO 2 [0.0, 1.0]

<a id="unreal.ModularSynthPreset.lfo2_gain"></a>

#### lfo2_gain

```python
@lfo2_gain.setter
def lfo2_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.lfo2_type"></a>

#### lfo2_type

```python
@property
def lfo2_type() -> SynthLFOType
```

(SynthLFOType):  [Read-Write] The type of LFO to use for LFO 2

<a id="unreal.ModularSynthPreset.lfo2_type"></a>

#### lfo2_type

```python
@lfo2_type.setter
def lfo2_type(value: SynthLFOType) -> None
```

<a id="unreal.ModularSynthPreset.lfo2_mode"></a>

#### lfo2_mode

```python
@property
def lfo2_mode() -> SynthLFOMode
```

(SynthLFOMode):  [Read-Write] The mode to use for LFO 2

<a id="unreal.ModularSynthPreset.lfo2_mode"></a>

#### lfo2_mode

```python
@lfo2_mode.setter
def lfo2_mode(value: SynthLFOMode) -> None
```

<a id="unreal.ModularSynthPreset.lfo2_patch_type"></a>

#### lfo2_patch_type

```python
@property
def lfo2_patch_type() -> SynthLFOPatchType
```

(SynthLFOPatchType):  [Read-Write] The built-in patch type to use for LFO 2 (you can route this to any patchable parameter using the Patches parameter)

<a id="unreal.ModularSynthPreset.lfo2_patch_type"></a>

#### lfo2_patch_type

```python
@lfo2_patch_type.setter
def lfo2_patch_type(value: SynthLFOPatchType) -> None
```

<a id="unreal.ModularSynthPreset.gain_db"></a>

#### gain_db

```python
@property
def gain_db() -> float
```

(float):  [Read-Write] The overall gain to use for the synthesizer in dB [-90.0, 20.0]

<a id="unreal.ModularSynthPreset.gain_db"></a>

#### gain_db

```python
@gain_db.setter
def gain_db(value: float) -> None
```

<a id="unreal.ModularSynthPreset.attack_time"></a>

#### attack_time

```python
@property
def attack_time() -> float
```

(float):  [Read-Write] The amplitude envelope attack time (in ms) [0.0, 10000]

<a id="unreal.ModularSynthPreset.attack_time"></a>

#### attack_time

```python
@attack_time.setter
def attack_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.decay_time"></a>

#### decay_time

```python
@property
def decay_time() -> float
```

(float):  [Read-Write] The amplitude envelope decay time (in ms)[0.0, 10000]

<a id="unreal.ModularSynthPreset.decay_time"></a>

#### decay_time

```python
@decay_time.setter
def decay_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.sustain_gain"></a>

#### sustain_gain

```python
@property
def sustain_gain() -> float
```

(float):  [Read-Write] The amplitude envelope sustain amount (linear gain) [0.0, 1.0]

<a id="unreal.ModularSynthPreset.sustain_gain"></a>

#### sustain_gain

```python
@sustain_gain.setter
def sustain_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.release_time"></a>

#### release_time

```python
@property
def release_time() -> float
```

(float):  [Read-Write] The amplitude envelope release time (in ms) [0.0, 10000]

<a id="unreal.ModularSynthPreset.release_time"></a>

#### release_time

```python
@release_time.setter
def release_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.mod_env_patch_type"></a>

#### mod_env_patch_type

```python
@property
def mod_env_patch_type() -> SynthModEnvPatch
```

(SynthModEnvPatch):  [Read-Write] The built-in patch type for the envelope modulator

<a id="unreal.ModularSynthPreset.mod_env_patch_type"></a>

#### mod_env_patch_type

```python
@mod_env_patch_type.setter
def mod_env_patch_type(value: SynthModEnvPatch) -> None
```

<a id="unreal.ModularSynthPreset.mod_env_bias_patch_type"></a>

#### mod_env_bias_patch_type

```python
@property
def mod_env_bias_patch_type() -> SynthModEnvBiasPatch
```

(SynthModEnvBiasPatch):  [Read-Write] The built-in patch type for the envelope modulator bias output. Bias is when the envelope output is offset by the sustain gain.

<a id="unreal.ModularSynthPreset.mod_env_bias_patch_type"></a>

#### mod_env_bias_patch_type

```python
@mod_env_bias_patch_type.setter
def mod_env_bias_patch_type(value: SynthModEnvBiasPatch) -> None
```

<a id="unreal.ModularSynthPreset.invert_modulation_envelope"></a>

#### invert_modulation_envelope

```python
@property
def invert_modulation_envelope() -> bool
```

(bool):  [Read-Write] Whether or not to invert the modulation envelope

<a id="unreal.ModularSynthPreset.invert_modulation_envelope"></a>

#### invert_modulation_envelope

```python
@invert_modulation_envelope.setter
def invert_modulation_envelope(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.invert_modulation_envelope_bias"></a>

#### invert_modulation_envelope_bias

```python
@property
def invert_modulation_envelope_bias() -> bool
```

(bool):  [Read-Write] Whether or not to invert the modulation envelope bias output

<a id="unreal.ModularSynthPreset.invert_modulation_envelope_bias"></a>

#### invert_modulation_envelope_bias

```python
@invert_modulation_envelope_bias.setter
def invert_modulation_envelope_bias(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.modulation_envelope_depth"></a>

#### modulation_envelope_depth

```python
@property
def modulation_envelope_depth() -> float
```

(float):  [Read-Write] The "depth" (i.e. how much) modulation envelope to use. This scales the modulation envelope output. [0.0, 1.0]

<a id="unreal.ModularSynthPreset.modulation_envelope_depth"></a>

#### modulation_envelope_depth

```python
@modulation_envelope_depth.setter
def modulation_envelope_depth(value: float) -> None
```

<a id="unreal.ModularSynthPreset.modulation_envelope_attack_time"></a>

#### modulation_envelope_attack_time

```python
@property
def modulation_envelope_attack_time() -> float
```

(float):  [Read-Write] The modulation envelope attack time (in ms) [0.0, 10000]

<a id="unreal.ModularSynthPreset.modulation_envelope_attack_time"></a>

#### modulation_envelope_attack_time

```python
@modulation_envelope_attack_time.setter
def modulation_envelope_attack_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.modulation_envelope_decay_time"></a>

#### modulation_envelope_decay_time

```python
@property
def modulation_envelope_decay_time() -> float
```

(float):  [Read-Write] The modulation envelope decay time (in ms) [0.0, 10000]

<a id="unreal.ModularSynthPreset.modulation_envelope_decay_time"></a>

#### modulation_envelope_decay_time

```python
@modulation_envelope_decay_time.setter
def modulation_envelope_decay_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.modulation_envelope_sustain_gain"></a>

#### modulation_envelope_sustain_gain

```python
@property
def modulation_envelope_sustain_gain() -> float
```

(float):  [Read-Write] The modulation envelope sustain gain (linear gain) [0.0, 1.0]

<a id="unreal.ModularSynthPreset.modulation_envelope_sustain_gain"></a>

#### modulation_envelope_sustain_gain

```python
@modulation_envelope_sustain_gain.setter
def modulation_envelope_sustain_gain(value: float) -> None
```

<a id="unreal.ModularSynthPreset.modulation_envelope_release_time"></a>

#### modulation_envelope_release_time

```python
@property
def modulation_envelope_release_time() -> float
```

(float):  [Read-Write] The modulation envelope release time (in ms) [0.0, 10000]

<a id="unreal.ModularSynthPreset.modulation_envelope_release_time"></a>

#### modulation_envelope_release_time

```python
@modulation_envelope_release_time.setter
def modulation_envelope_release_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.legato"></a>

#### legato

```python
@property
def legato() -> bool
```

(bool):  [Read-Write] Whether or not to use legato mode.

<a id="unreal.ModularSynthPreset.legato"></a>

#### legato

```python
@legato.setter
def legato(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.retrigger"></a>

#### retrigger

```python
@property
def retrigger() -> bool
```

(bool):  [Read-Write] Whether or not to use retrigger mode.

<a id="unreal.ModularSynthPreset.retrigger"></a>

#### retrigger

```python
@retrigger.setter
def retrigger(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.filter_frequency"></a>

#### filter_frequency

```python
@property
def filter_frequency() -> float
```

(float):  [Read-Write] The output filter cutoff frequency (hz) [0.0, 20000.0]

<a id="unreal.ModularSynthPreset.filter_frequency"></a>

#### filter_frequency

```python
@filter_frequency.setter
def filter_frequency(value: float) -> None
```

<a id="unreal.ModularSynthPreset.filter_q"></a>

#### filter_q

```python
@property
def filter_q() -> float
```

(float):  [Read-Write] The output filter resonance (Q) [0.5, 10]

<a id="unreal.ModularSynthPreset.filter_q"></a>

#### filter_q

```python
@filter_q.setter
def filter_q(value: float) -> None
```

<a id="unreal.ModularSynthPreset.filter_type"></a>

#### filter_type

```python
@property
def filter_type() -> SynthFilterType
```

(SynthFilterType):  [Read-Write] The output filter type (lowpass, highpass, bandpass, bandstop)

<a id="unreal.ModularSynthPreset.filter_type"></a>

#### filter_type

```python
@filter_type.setter
def filter_type(value: SynthFilterType) -> None
```

<a id="unreal.ModularSynthPreset.filter_algorithm"></a>

#### filter_algorithm

```python
@property
def filter_algorithm() -> SynthFilterAlgorithm
```

(SynthFilterAlgorithm):  [Read-Write] The output filter circuit/algorithm type (one-pole ladder, ladder, state-variable)

<a id="unreal.ModularSynthPreset.filter_algorithm"></a>

#### filter_algorithm

```python
@filter_algorithm.setter
def filter_algorithm(value: SynthFilterAlgorithm) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_enabled"></a>

#### stereo_delay_enabled

```python
@property
def stereo_delay_enabled() -> bool
```

(bool):  [Read-Write] Whether or not stereo delay is enabled on the synth

<a id="unreal.ModularSynthPreset.stereo_delay_enabled"></a>

#### stereo_delay_enabled

```python
@stereo_delay_enabled.setter
def stereo_delay_enabled(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_mode"></a>

#### stereo_delay_mode

```python
@property
def stereo_delay_mode() -> SynthStereoDelayMode
```

(SynthStereoDelayMode):  [Read-Write] The stereo delay mode of the synth

<a id="unreal.ModularSynthPreset.stereo_delay_mode"></a>

#### stereo_delay_mode

```python
@stereo_delay_mode.setter
def stereo_delay_mode(value: SynthStereoDelayMode) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_time"></a>

#### stereo_delay_time

```python
@property
def stereo_delay_time() -> float
```

(float):  [Read-Write] The stereo delay time (in ms) [0.0, 2000.0]

<a id="unreal.ModularSynthPreset.stereo_delay_time"></a>

#### stereo_delay_time

```python
@stereo_delay_time.setter
def stereo_delay_time(value: float) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_feedback"></a>

#### stereo_delay_feedback

```python
@property
def stereo_delay_feedback() -> float
```

(float):  [Read-Write] The amount of feedback in the stereo delay line [0.0, 1.0]

<a id="unreal.ModularSynthPreset.stereo_delay_feedback"></a>

#### stereo_delay_feedback

```python
@stereo_delay_feedback.setter
def stereo_delay_feedback(value: float) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_wetlevel"></a>

#### stereo_delay_wetlevel

```python
@property
def stereo_delay_wetlevel() -> float
```

(float):  [Read-Write] The output wet level to use for the stereo delay time [0.0, 1.0]

<a id="unreal.ModularSynthPreset.stereo_delay_wetlevel"></a>

#### stereo_delay_wetlevel

```python
@stereo_delay_wetlevel.setter
def stereo_delay_wetlevel(value: float) -> None
```

<a id="unreal.ModularSynthPreset.stereo_delay_ratio"></a>

#### stereo_delay_ratio

```python
@property
def stereo_delay_ratio() -> float
```

(float):  [Read-Write] The ratio between left and right stereo delay lines (wider value is more separation) [0.0, 1.0]

<a id="unreal.ModularSynthPreset.stereo_delay_ratio"></a>

#### stereo_delay_ratio

```python
@stereo_delay_ratio.setter
def stereo_delay_ratio(value: float) -> None
```

<a id="unreal.ModularSynthPreset.chorus_enabled"></a>

#### chorus_enabled

```python
@property
def chorus_enabled() -> bool
```

(bool):  [Read-Write] Whether or not the chorus effect is enabled

<a id="unreal.ModularSynthPreset.chorus_enabled"></a>

#### chorus_enabled

```python
@chorus_enabled.setter
def chorus_enabled(value: bool) -> None
```

<a id="unreal.ModularSynthPreset.chorus_depth"></a>

#### chorus_depth

```python
@property
def chorus_depth() -> float
```

(float):  [Read-Write] The depth of the chorus effect [0.0, 1.0]

<a id="unreal.ModularSynthPreset.chorus_depth"></a>

#### chorus_depth

```python
@chorus_depth.setter
def chorus_depth(value: float) -> None
```

<a id="unreal.ModularSynthPreset.chorus_feedback"></a>

#### chorus_feedback

```python
@property
def chorus_feedback() -> float
```

(float):  [Read-Write] The amount of feedback in the chorus effect [0.0, 1.0]

<a id="unreal.ModularSynthPreset.chorus_feedback"></a>

#### chorus_feedback

```python
@chorus_feedback.setter
def chorus_feedback(value: float) -> None
```

<a id="unreal.ModularSynthPreset.chorus_frequency"></a>

#### chorus_frequency

```python
@property
def chorus_frequency() -> float
```

(float):  [Read-Write] The chorus LFO frequency [0.0, 20.0]

<a id="unreal.ModularSynthPreset.chorus_frequency"></a>

#### chorus_frequency

```python
@chorus_frequency.setter
def chorus_frequency(value: float) -> None
```

<a id="unreal.ModularSynthPreset.patches"></a>

#### patches

```python
@property
def patches() -> Array[EpicSynth1Patch]
```

(Array[EpicSynth1Patch]):  [Read-Write] The modular synth patch cords to use for the synth. Allows routing the LFO1/LFO2 and Modulation Envelope to any patchable destination.

<a id="unreal.ModularSynthPreset.patches"></a>

#### patches

```python
@patches.setter
def patches(value: Array[EpicSynth1Patch]) -> None
```

<a id="unreal.ModularSynthPresetBankEntry"></a>