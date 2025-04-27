## GaussianSumBloomSettings Objects

```python
class GaussianSumBloomSettings(StructBase)
```

Gaussian Sum Bloom Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter1_size`` (float):  [Read-Write] Diameter size for the Bloom1 in percent of the screen width
  (is done in 1/2 resolution, larger values cost more performance, good for high frequency details)
  >=0: can be clamped because of shader limitations
- ``filter1_tint`` (LinearColor):  [Read-Write] Bloom1 tint color
- ``filter2_size`` (float):  [Read-Write] Diameter size for Bloom2 in percent of the screen width
  (is done in 1/4 resolution, larger values cost more performance)
  >=0: can be clamped because of shader limitations
- ``filter2_tint`` (LinearColor):  [Read-Write] Bloom2 tint color
- ``filter3_size`` (float):  [Read-Write] Diameter size for Bloom3 in percent of the screen width
  (is done in 1/8 resolution, larger values cost more performance)
  >=0: can be clamped because of shader limitations
- ``filter3_tint`` (LinearColor):  [Read-Write] Bloom3 tint color
- ``filter4_size`` (float):  [Read-Write] Diameter size for Bloom4 in percent of the screen width
  (is done in 1/16 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``filter4_tint`` (LinearColor):  [Read-Write] Bloom4 tint color
- ``filter5_size`` (float):  [Read-Write] Diameter size for Bloom5 in percent of the screen width
  (is done in 1/32 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``filter5_tint`` (LinearColor):  [Read-Write] Bloom5 tint color
- ``filter6_size`` (float):  [Read-Write] Diameter size for Bloom6 in percent of the screen width
  (is done in 1/64 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``filter6_tint`` (LinearColor):  [Read-Write] Bloom6 tint color
- ``intensity`` (float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter
- ``size_scale`` (float):  [Read-Write] Scale for all bloom sizes
- ``threshold`` (float):  [Read-Write] minimum brightness the bloom starts having effect
  -1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter

<a id="unreal.GaussianSumBloomSettings.__init__"></a>

#### __init__

```python
def __init__(
    intensity: float = 0.000000,
    threshold: float = 0.000000,
    size_scale: float = 0.000000,
    filter1_size: float = 0.000000,
    filter2_size: float = 0.000000,
    filter3_size: float = 0.000000,
    filter4_size: float = 0.000000,
    filter5_size: float = 0.000000,
    filter6_size: float = 0.000000,
    filter1_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    filter2_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    filter3_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    filter4_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    filter5_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    filter6_tint: LinearColor = [0.000000, 0.000000, 0.000000,
                                 0.000000]) -> None
```

<a id="unreal.GaussianSumBloomSettings.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter

<a id="unreal.GaussianSumBloomSettings.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.threshold"></a>

#### threshold

```python
@property
def threshold() -> float
```

(float):  [Read-Write] minimum brightness the bloom starts having effect
-1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter

<a id="unreal.GaussianSumBloomSettings.threshold"></a>

#### threshold

```python
@threshold.setter
def threshold(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.size_scale"></a>

#### size_scale

```python
@property
def size_scale() -> float
```

(float):  [Read-Write] Scale for all bloom sizes

<a id="unreal.GaussianSumBloomSettings.size_scale"></a>

#### size_scale

```python
@size_scale.setter
def size_scale(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter1_size"></a>

#### filter1_size

```python
@property
def filter1_size() -> float
```

(float):  [Read-Write] Diameter size for the Bloom1 in percent of the screen width
(is done in 1/2 resolution, larger values cost more performance, good for high frequency details)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter1_size"></a>

#### filter1_size

```python
@filter1_size.setter
def filter1_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter2_size"></a>

#### filter2_size

```python
@property
def filter2_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom2 in percent of the screen width
(is done in 1/4 resolution, larger values cost more performance)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter2_size"></a>

#### filter2_size

```python
@filter2_size.setter
def filter2_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter3_size"></a>

#### filter3_size

```python
@property
def filter3_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom3 in percent of the screen width
(is done in 1/8 resolution, larger values cost more performance)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter3_size"></a>

#### filter3_size

```python
@filter3_size.setter
def filter3_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter4_size"></a>

#### filter4_size

```python
@property
def filter4_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom4 in percent of the screen width
(is done in 1/16 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter4_size"></a>

#### filter4_size

```python
@filter4_size.setter
def filter4_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter5_size"></a>

#### filter5_size

```python
@property
def filter5_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom5 in percent of the screen width
(is done in 1/32 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter5_size"></a>

#### filter5_size

```python
@filter5_size.setter
def filter5_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter6_size"></a>

#### filter6_size

```python
@property
def filter6_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom6 in percent of the screen width
(is done in 1/64 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.GaussianSumBloomSettings.filter6_size"></a>

#### filter6_size

```python
@filter6_size.setter
def filter6_size(value: float) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter1_tint"></a>

#### filter1_tint

```python
@property
def filter1_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom1 tint color

<a id="unreal.GaussianSumBloomSettings.filter1_tint"></a>

#### filter1_tint

```python
@filter1_tint.setter
def filter1_tint(value: LinearColor) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter2_tint"></a>

#### filter2_tint

```python
@property
def filter2_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom2 tint color

<a id="unreal.GaussianSumBloomSettings.filter2_tint"></a>

#### filter2_tint

```python
@filter2_tint.setter
def filter2_tint(value: LinearColor) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter3_tint"></a>

#### filter3_tint

```python
@property
def filter3_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom3 tint color

<a id="unreal.GaussianSumBloomSettings.filter3_tint"></a>

#### filter3_tint

```python
@filter3_tint.setter
def filter3_tint(value: LinearColor) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter4_tint"></a>

#### filter4_tint

```python
@property
def filter4_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom4 tint color

<a id="unreal.GaussianSumBloomSettings.filter4_tint"></a>

#### filter4_tint

```python
@filter4_tint.setter
def filter4_tint(value: LinearColor) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter5_tint"></a>

#### filter5_tint

```python
@property
def filter5_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom5 tint color

<a id="unreal.GaussianSumBloomSettings.filter5_tint"></a>

#### filter5_tint

```python
@filter5_tint.setter
def filter5_tint(value: LinearColor) -> None
```

<a id="unreal.GaussianSumBloomSettings.filter6_tint"></a>

#### filter6_tint

```python
@property
def filter6_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom6 tint color

<a id="unreal.GaussianSumBloomSettings.filter6_tint"></a>

#### filter6_tint

```python
@filter6_tint.setter
def filter6_tint(value: LinearColor) -> None
```

<a id="unreal.ConvolutionBloomSettings"></a>