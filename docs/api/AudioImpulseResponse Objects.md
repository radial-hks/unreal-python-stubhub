## AudioImpulseResponse Objects

```python
class AudioImpulseResponse(Object)
```

UAudioImpulseResponse
UAsset used to represent Imported Impulse Responses

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EffectConvolutionReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ir_data`` (Array[float]):  [Read-Write]
  deprecated: Property 'IRData' is deprecated.
- ``normalization_volume_db`` (float):  [Read-Write] Used to account for energy added by convolution with "loud" Impulse Responses.
- ``true_stereo`` (bool):  [Read-Write] If true, impulse response channels are interpreted as true stereo which allows channel crosstalk. If false, impulse response channels are interpreted as independent channel impulses.

<a id="unreal.AudioImpulseResponse.normalization_volume_db"></a>

#### normalization_volume_db

```python
@property
def normalization_volume_db() -> float
```

(float):  [Read-Only] Used to account for energy added by convolution with "loud" Impulse Responses.

<a id="unreal.AudioImpulseResponse.true_stereo"></a>

#### true_stereo

```python
@property
def true_stereo() -> bool
```

(bool):  [Read-Only] If true, impulse response channels are interpreted as true stereo which allows channel crosstalk. If false, impulse response channels are interpreted as independent channel impulses.

<a id="unreal.AudioImpulseResponse.ir_data"></a>

#### ir_data

```python
@property
def ir_data() -> Array[float]
```

(Array[float]):  [Read-Write]
deprecated: Property 'IRData' is deprecated.

<a id="unreal.AudioImpulseResponse.ir_data"></a>

#### ir_data

```python
@ir_data.setter
def ir_data(value: Array[float]) -> None
```

<a id="unreal.ImpulseResponse"></a>