## WaveTableTransform Objects

```python
class WaveTableTransform(StructBase)
```

Wave Table Transform

**C++ Source:**

- **Plugin**: WaveTable
- **Module**: WaveTable
- **File**: WaveTableTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (WaveTableCurve):  [Read-Write] The curve to apply when transforming the output.
- ``curve_shared`` (CurveFloat):  [Read-Write] Asset curve reference to apply if output curve type is set to 'Shared.'
- ``duration`` (float):  [Read-Write] Duration of curve or file.  Only valid if parent SampleRate is set and SamplingMode is set to 'FixedSampleRate'
  (If set to 'FixedResolution', duration is variable depending on the resolution (number of samples in the table data)
  and device's sample rate.
- ``scalar`` (float):  [Read-Write] When curve set to log, exponential or exponential inverse, value is factor 'b' in following equations with output 'y' and input 'x':
  Exponential: y = x * 10^-b(1-x)
  Exponential (Inverse): y = ((x - 1) * 10^(-bx)) + 1
  Logarithmic: y = b * log(x) + 1
- ``wave_table_settings`` (WaveTableSettings):  [Read-Write]

<a id="unreal.WaveTableTransform.__init__"></a>

#### __init__

```python
def __init__(curve: WaveTableCurve = WaveTableCurve.LINEAR,
             scalar: float = 0.000000,
             curve_shared: CurveFloat = None) -> None
```

<a id="unreal.WaveTableTransform.curve"></a>

#### curve

```python
@property
def curve() -> WaveTableCurve
```

(WaveTableCurve):  [Read-Write] The curve to apply when transforming the output.

<a id="unreal.WaveTableTransform.curve"></a>

#### curve

```python
@curve.setter
def curve(value: WaveTableCurve) -> None
```

<a id="unreal.WaveTableTransform.scalar"></a>

#### scalar

```python
@property
def scalar() -> float
```

(float):  [Read-Write] When curve set to log, exponential or exponential inverse, value is factor 'b' in following equations with output 'y' and input 'x':
Exponential: y = x * 10^-b(1-x)
Exponential (Inverse): y = ((x - 1) * 10^(-bx)) + 1
Logarithmic: y = b * log(x) + 1

<a id="unreal.WaveTableTransform.scalar"></a>

#### scalar

```python
@scalar.setter
def scalar(value: float) -> None
```

<a id="unreal.WaveTableTransform.curve_shared"></a>

#### curve_shared

```python
@property
def curve_shared() -> CurveFloat
```

(CurveFloat):  [Read-Write] Asset curve reference to apply if output curve type is set to 'Shared.'

<a id="unreal.WaveTableTransform.curve_shared"></a>

#### curve_shared

```python
@curve_shared.setter
def curve_shared(value: CurveFloat) -> None
```

<a id="unreal.MetaSoundAssetDirectory"></a>