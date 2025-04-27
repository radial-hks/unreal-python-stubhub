## CameraExposureSettings Objects

```python
class CameraExposureSettings(StructBase)
```

Camera Exposure Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_physical_camera_exposure`` (bool):  [Read-Write] Enables physical camera exposure using ShutterSpeed/ISO/Aperture.
- ``bias`` (float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``bias_curve`` (CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
  Used to calibrate the final exposure differently depending on the average scene luminance.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``calibration_constant`` (float):  [Read-Write] Calibration constant for 18% albedo.
- ``high_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 80 .. 95
- ``histogram_log_max`` (float):  [Read-Write] temporary exposed until we found good values 4: 16, 8: 256
- ``histogram_log_min`` (float):  [Read-Write] temporary exposed until we found good values, -8: 1/256, -10: 1/1024
- ``low_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 70 .. 80
- ``max_brightness`` (float):  [Read-Write] A good value should be positive (2 is a good value). This is the maximum brightness the auto exposure can adapt to.
  It should be tweaked in a bright lighting situation (too small: image appears too bright, too large: image appears too dark).
  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global
  effect and defined the HDR range - you don't want to change that late in the project development.
  Eye Adaptation is disabled if MinBrightness = MaxBrightness
- ``meter_mask`` (Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
  and dark spots will have low influence.
- ``method`` (AutoExposureMethod):  [Read-Write] Luminance computation method
- ``min_brightness`` (float):  [Read-Write] A good value should be positive near 0. This is the minimum brightness the auto exposure can adapt to.
  It should be tweaked in a dark lighting situation (too small: image appears too bright, too large: image appears too dark).
  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global
  effect and defined the HDR range - you don't want to change that late in the project development.
  Eye Adaptation is disabled if MinBrightness = MaxBrightness
- ``speed_down`` (float):  [Read-Write] In F-stops per second, should be >0
- ``speed_up`` (float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.CameraExposureSettings.__init__"></a>

#### __init__

```python
def __init__(method: AutoExposureMethod = AutoExposureMethod.AEM_HISTOGRAM,
             low_percent: float = 0.000000,
             high_percent: float = 0.000000,
             min_brightness: float = 0.000000,
             max_brightness: float = 0.000000,
             speed_up: float = 0.000000,
             speed_down: float = 0.000000,
             bias: float = 0.000000,
             bias_curve: CurveFloat = None,
             meter_mask: Texture = None,
             histogram_log_min: float = 0.000000,
             histogram_log_max: float = 0.000000,
             calibration_constant: float = 0.000000,
             apply_physical_camera_exposure: bool = False) -> None
```

<a id="unreal.CameraExposureSettings.method"></a>

#### method

```python
@property
def method() -> AutoExposureMethod
```

(AutoExposureMethod):  [Read-Write] Luminance computation method

<a id="unreal.CameraExposureSettings.method"></a>

#### method

```python
@method.setter
def method(value: AutoExposureMethod) -> None
```

<a id="unreal.CameraExposureSettings.low_percent"></a>

#### low_percent

```python
@property
def low_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 70 .. 80

<a id="unreal.CameraExposureSettings.low_percent"></a>

#### low_percent

```python
@low_percent.setter
def low_percent(value: float) -> None
```

<a id="unreal.CameraExposureSettings.high_percent"></a>

#### high_percent

```python
@property
def high_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 80 .. 95

<a id="unreal.CameraExposureSettings.high_percent"></a>

#### high_percent

```python
@high_percent.setter
def high_percent(value: float) -> None
```

<a id="unreal.CameraExposureSettings.min_brightness"></a>

#### min_brightness

```python
@property
def min_brightness() -> float
```

(float):  [Read-Write] A good value should be positive near 0. This is the minimum brightness the auto exposure can adapt to.
It should be tweaked in a dark lighting situation (too small: image appears too bright, too large: image appears too dark).
Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global
effect and defined the HDR range - you don't want to change that late in the project development.
Eye Adaptation is disabled if MinBrightness = MaxBrightness

<a id="unreal.CameraExposureSettings.min_brightness"></a>

#### min_brightness

```python
@min_brightness.setter
def min_brightness(value: float) -> None
```

<a id="unreal.CameraExposureSettings.max_brightness"></a>

#### max_brightness

```python
@property
def max_brightness() -> float
```

(float):  [Read-Write] A good value should be positive (2 is a good value). This is the maximum brightness the auto exposure can adapt to.
It should be tweaked in a bright lighting situation (too small: image appears too bright, too large: image appears too dark).
Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global
effect and defined the HDR range - you don't want to change that late in the project development.
Eye Adaptation is disabled if MinBrightness = MaxBrightness

<a id="unreal.CameraExposureSettings.max_brightness"></a>

#### max_brightness

```python
@max_brightness.setter
def max_brightness(value: float) -> None
```

<a id="unreal.CameraExposureSettings.speed_up"></a>

#### speed_up

```python
@property
def speed_up() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.CameraExposureSettings.speed_up"></a>

#### speed_up

```python
@speed_up.setter
def speed_up(value: float) -> None
```

<a id="unreal.CameraExposureSettings.speed_down"></a>

#### speed_down

```python
@property
def speed_down() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.CameraExposureSettings.speed_down"></a>

#### speed_down

```python
@speed_down.setter
def speed_down(value: float) -> None
```

<a id="unreal.CameraExposureSettings.bias"></a>

#### bias

```python
@property
def bias() -> float
```

(float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.CameraExposureSettings.bias"></a>

#### bias

```python
@bias.setter
def bias(value: float) -> None
```

<a id="unreal.CameraExposureSettings.bias_curve"></a>

#### bias_curve

```python
@property
def bias_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
Used to calibrate the final exposure differently depending on the average scene luminance.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.CameraExposureSettings.bias_curve"></a>

#### bias_curve

```python
@bias_curve.setter
def bias_curve(value: CurveFloat) -> None
```

<a id="unreal.CameraExposureSettings.meter_mask"></a>

#### meter_mask

```python
@property
def meter_mask() -> Texture
```

(Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
and dark spots will have low influence.

<a id="unreal.CameraExposureSettings.meter_mask"></a>

#### meter_mask

```python
@meter_mask.setter
def meter_mask(value: Texture) -> None
```

<a id="unreal.CameraExposureSettings.histogram_log_min"></a>

#### histogram_log_min

```python
@property
def histogram_log_min() -> float
```

(float):  [Read-Write] temporary exposed until we found good values, -8: 1/256, -10: 1/1024

<a id="unreal.CameraExposureSettings.histogram_log_min"></a>

#### histogram_log_min

```python
@histogram_log_min.setter
def histogram_log_min(value: float) -> None
```

<a id="unreal.CameraExposureSettings.histogram_log_max"></a>

#### histogram_log_max

```python
@property
def histogram_log_max() -> float
```

(float):  [Read-Write] temporary exposed until we found good values 4: 16, 8: 256

<a id="unreal.CameraExposureSettings.histogram_log_max"></a>

#### histogram_log_max

```python
@histogram_log_max.setter
def histogram_log_max(value: float) -> None
```

<a id="unreal.CameraExposureSettings.calibration_constant"></a>

#### calibration_constant

```python
@property
def calibration_constant() -> float
```

(float):  [Read-Write] Calibration constant for 18% albedo.

<a id="unreal.CameraExposureSettings.calibration_constant"></a>

#### calibration_constant

```python
@calibration_constant.setter
def calibration_constant(value: float) -> None
```

<a id="unreal.CameraExposureSettings.apply_physical_camera_exposure"></a>

#### apply_physical_camera_exposure

```python
@property
def apply_physical_camera_exposure() -> bool
```

(bool):  [Read-Write] Enables physical camera exposure using ShutterSpeed/ISO/Aperture.

<a id="unreal.CameraExposureSettings.apply_physical_camera_exposure"></a>

#### apply_physical_camera_exposure

```python
@apply_physical_camera_exposure.setter
def apply_physical_camera_exposure(value: bool) -> None
```

<a id="unreal.SceneViewExtensionIsActiveFunctor"></a>