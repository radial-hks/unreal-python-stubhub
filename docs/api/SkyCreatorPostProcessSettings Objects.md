## SkyCreatorPostProcessSettings Objects

```python
class SkyCreatorPostProcessSettings(StructBase)
```

Sky Creator Post Process Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bloom_intensity`` (float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter
- ``bloom_threshold`` (float):  [Read-Write] minimum brightness the bloom starts having effect
  -1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter
- ``exposure_compensation`` (float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.SkyCreatorPostProcessSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(bloom_intensity: float = 0.000000,
             bloom_threshold: float = 0.000000,
             exposure_compensation: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorPostProcessSettings.bloom_intensity"></a>

#### bloom\_intensity

```python
@property
def bloom_intensity() -> float
```

(float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter

<a id="unreal.SkyCreatorPostProcessSettings.bloom_intensity"></a>

#### bloom\_intensity

```python
@bloom_intensity.setter
def bloom_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorPostProcessSettings.bloom_threshold"></a>

#### bloom\_threshold

```python
@property
def bloom_threshold() -> float
```

(float):  [Read-Write] minimum brightness the bloom starts having effect
-1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter

<a id="unreal.SkyCreatorPostProcessSettings.bloom_threshold"></a>

#### bloom\_threshold

```python
@bloom_threshold.setter
def bloom_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorPostProcessSettings.exposure_compensation"></a>

#### exposure\_compensation

```python
@property
def exposure_compensation() -> float
```

(float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.SkyCreatorPostProcessSettings.exposure_compensation"></a>

#### exposure\_compensation

```python
@exposure_compensation.setter
def exposure_compensation(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherSettings"></a>