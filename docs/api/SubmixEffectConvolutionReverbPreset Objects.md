## SubmixEffectConvolutionReverbPreset Objects

```python
class SubmixEffectConvolutionReverbPreset(SoundEffectSubmixPreset)
```

Submix Effect Convolution Reverb Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectConvolutionReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``block_size`` (SubmixEffectConvolutionReverbBlockSize):  [Read-Write] Set the internal block size. This can effect latency and performance. Higher values will result in
  lower CPU costs while lower values will result higher CPU costs. Latency may be affected depending
  on the interplay between audio engines buffer sizes and this effects block size. Generally, higher
  values result in higher latency, and lower values result in lower latency.
- ``enable_hardware_acceleration`` (bool):  [Read-Write] Opt into hardware acceleration of the convolution reverb (if available)
- ``impulse_response`` (AudioImpulseResponse):  [Read-Write] The impulse response used for convolution.
- ``settings`` (SubmixEffectConvolutionReverbSettings):  [Read-Write] ConvolutionReverbPreset Preset Settings.

<a id="unreal.SubmixEffectConvolutionReverbPreset.impulse_response"></a>

#### impulse_response

```python
@property
def impulse_response() -> AudioImpulseResponse
```

(AudioImpulseResponse):  [Read-Write] The impulse response used for convolution.

<a id="unreal.SubmixEffectConvolutionReverbPreset.impulse_response"></a>

#### impulse_response

```python
@impulse_response.setter
def impulse_response(value: AudioImpulseResponse) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectConvolutionReverbSettings
```

(SubmixEffectConvolutionReverbSettings):  [Read-Write] ConvolutionReverbPreset Preset Settings.

<a id="unreal.SubmixEffectConvolutionReverbPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectConvolutionReverbSettings) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbPreset.block_size"></a>

#### block_size

```python
@property
def block_size() -> SubmixEffectConvolutionReverbBlockSize
```

(SubmixEffectConvolutionReverbBlockSize):  [Read-Only] Set the internal block size. This can effect latency and performance. Higher values will result in
lower CPU costs while lower values will result higher CPU costs. Latency may be affected depending
on the interplay between audio engines buffer sizes and this effects block size. Generally, higher
values result in higher latency, and lower values result in lower latency.

<a id="unreal.SubmixEffectConvolutionReverbPreset.enable_hardware_acceleration"></a>

#### enable_hardware_acceleration

```python
@property
def enable_hardware_acceleration() -> bool
```

(bool):  [Read-Only] Opt into hardware acceleration of the convolution reverb (if available)

<a id="unreal.SubmixEffectConvolutionReverbPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectConvolutionReverbSettings) -> None
```

x.set_settings(settings) -> None
Set the convolution reverb settings

Args:
    settings (SubmixEffectConvolutionReverbSettings):

<a id="unreal.ConvolutionReverbPreset"></a>