## LiveLinkLightFrameData Objects

```python
class LiveLinkLightFrameData(LiveLinkTransformFrameData)
```

Dynamic data for light.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkLightTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attenuation_radius`` (float):  [Read-Write] Light visible influence. Works for Pointlight and Spotlight.
- ``inner_cone_angle`` (float):  [Read-Write] Inner cone angle in degrees for a Spotlight.
- ``intensity`` (float):  [Read-Write] Total energy that the light emits in lux.
- ``light_color`` (Color):  [Read-Write] Filter color of the light.
- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``outer_cone_angle`` (float):  [Read-Write] Outer cone angle in degrees for a Spotlight.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``soft_source_radius`` (float):  [Read-Write] Soft radius of light source shape. Works for Pointlight and Spotlight.
- ``source_length`` (float):  [Read-Write] Length of light source shape. Works for Pointlight and Spotlight.
- ``source_radius`` (float):  [Read-Write] Radius of light source shape. Works for Pointlight and Spotlight.
- ``temperature`` (float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant
- ``transform`` (Transform):  [Read-Write] Transform of the frame
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkLightFrameData.__init__"></a>

#### __init__

```python
def __init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
             property_values: Array[float] = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             temperature: float = 0.000000,
             intensity: float = 0.000000,
             light_color: Color = [0, 0, 0, 0],
             inner_cone_angle: float = 0.000000,
             outer_cone_angle: float = 0.000000,
             attenuation_radius: float = 0.000000,
             source_radius: float = 0.000000,
             soft_source_radius: float = 0.000000,
             source_length: float = 0.000000) -> None
```

<a id="unreal.LiveLinkLightFrameData.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant

<a id="unreal.LiveLinkLightFrameData.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Total energy that the light emits in lux.

<a id="unreal.LiveLinkLightFrameData.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.light_color"></a>

#### light_color

```python
@property
def light_color() -> Color
```

(Color):  [Read-Write] Filter color of the light.

<a id="unreal.LiveLinkLightFrameData.light_color"></a>

#### light_color

```python
@light_color.setter
def light_color(value: Color) -> None
```

<a id="unreal.LiveLinkLightFrameData.inner_cone_angle"></a>

#### inner_cone_angle

```python
@property
def inner_cone_angle() -> float
```

(float):  [Read-Write] Inner cone angle in degrees for a Spotlight.

<a id="unreal.LiveLinkLightFrameData.inner_cone_angle"></a>

#### inner_cone_angle

```python
@inner_cone_angle.setter
def inner_cone_angle(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.outer_cone_angle"></a>

#### outer_cone_angle

```python
@property
def outer_cone_angle() -> float
```

(float):  [Read-Write] Outer cone angle in degrees for a Spotlight.

<a id="unreal.LiveLinkLightFrameData.outer_cone_angle"></a>

#### outer_cone_angle

```python
@outer_cone_angle.setter
def outer_cone_angle(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.attenuation_radius"></a>

#### attenuation_radius

```python
@property
def attenuation_radius() -> float
```

(float):  [Read-Write] Light visible influence. Works for Pointlight and Spotlight.

<a id="unreal.LiveLinkLightFrameData.attenuation_radius"></a>

#### attenuation_radius

```python
@attenuation_radius.setter
def attenuation_radius(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.source_radius"></a>

#### source_radius

```python
@property
def source_radius() -> float
```

(float):  [Read-Write] Radius of light source shape. Works for Pointlight and Spotlight.

<a id="unreal.LiveLinkLightFrameData.source_radius"></a>

#### source_radius

```python
@source_radius.setter
def source_radius(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.soft_source_radius"></a>

#### soft_source_radius

```python
@property
def soft_source_radius() -> float
```

(float):  [Read-Write] Soft radius of light source shape. Works for Pointlight and Spotlight.

<a id="unreal.LiveLinkLightFrameData.soft_source_radius"></a>

#### soft_source_radius

```python
@soft_source_radius.setter
def soft_source_radius(value: float) -> None
```

<a id="unreal.LiveLinkLightFrameData.source_length"></a>

#### source_length

```python
@property
def source_length() -> float
```

(float):  [Read-Write] Length of light source shape. Works for Pointlight and Spotlight.

<a id="unreal.LiveLinkLightFrameData.source_length"></a>

#### source_length

```python
@source_length.setter
def source_length(value: float) -> None
```

<a id="unreal.LiveLinkLightBlueprintData"></a>