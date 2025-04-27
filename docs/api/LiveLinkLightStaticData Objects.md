## LiveLinkLightStaticData Objects

```python
class LiveLinkLightStaticData(LiveLinkTransformStaticData)
```

Static data for Light data.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkLightTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_attenuation_radius_supported`` (bool):  [Read-Write] Whether AttenuationRadius can be used in the frame data. Only used for spot lights
- ``is_inner_cone_angle_supported`` (bool):  [Read-Write] Whether InnerConeAngle can be used in the frame data. Only used for spot lights
- ``is_intensity_supported`` (bool):  [Read-Write] Whether Intensity can be used in the frame data
- ``is_light_color_supported`` (bool):  [Read-Write] Whether LightColor can be used in the frame data
- ``is_location_supported`` (bool):  [Read-Write] Whether location in frame data should be used
- ``is_outer_cone_angle_supported`` (bool):  [Read-Write] Whether OuterConeAngle can be used in the frame data. Only used for spot lights
- ``is_rotation_supported`` (bool):  [Read-Write] Whether rotation in frame data should be used
- ``is_scale_supported`` (bool):  [Read-Write] Whether scale in frame data should be used
- ``is_soft_source_radius_supported`` (bool):  [Read-Write] Whether SoftSourceRadius can be used in the frame data. Only used for spot lights
- ``is_source_lenght_supported`` (bool):  [Read-Write] Whether SourceLength can be used in the frame data. Only used for spot lights
- ``is_source_radius_supported`` (bool):  [Read-Write] Whether SourceRadius can be used in the frame data. Only used for spot lights
- ``is_temperature_supported`` (bool):  [Read-Write] Whether Temperature can be used in the frame data
- ``property_names`` (Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkLightStaticData.__init__"></a>

#### __init__

```python
def __init__(property_names: Array[Name] = [],
             is_location_supported: bool = False,
             is_rotation_supported: bool = False,
             is_scale_supported: bool = False,
             is_temperature_supported: bool = False,
             is_intensity_supported: bool = False,
             is_light_color_supported: bool = False,
             is_inner_cone_angle_supported: bool = False,
             is_outer_cone_angle_supported: bool = False,
             is_attenuation_radius_supported: bool = False,
             is_source_lenght_supported: bool = False,
             is_source_radius_supported: bool = False,
             is_soft_source_radius_supported: bool = False) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_temperature_supported"></a>

#### is_temperature_supported

```python
@property
def is_temperature_supported() -> bool
```

(bool):  [Read-Write] Whether Temperature can be used in the frame data

<a id="unreal.LiveLinkLightStaticData.is_temperature_supported"></a>

#### is_temperature_supported

```python
@is_temperature_supported.setter
def is_temperature_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_intensity_supported"></a>

#### is_intensity_supported

```python
@property
def is_intensity_supported() -> bool
```

(bool):  [Read-Write] Whether Intensity can be used in the frame data

<a id="unreal.LiveLinkLightStaticData.is_intensity_supported"></a>

#### is_intensity_supported

```python
@is_intensity_supported.setter
def is_intensity_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_light_color_supported"></a>

#### is_light_color_supported

```python
@property
def is_light_color_supported() -> bool
```

(bool):  [Read-Write] Whether LightColor can be used in the frame data

<a id="unreal.LiveLinkLightStaticData.is_light_color_supported"></a>

#### is_light_color_supported

```python
@is_light_color_supported.setter
def is_light_color_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_inner_cone_angle_supported"></a>

#### is_inner_cone_angle_supported

```python
@property
def is_inner_cone_angle_supported() -> bool
```

(bool):  [Read-Write] Whether InnerConeAngle can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_inner_cone_angle_supported"></a>

#### is_inner_cone_angle_supported

```python
@is_inner_cone_angle_supported.setter
def is_inner_cone_angle_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_outer_cone_angle_supported"></a>

#### is_outer_cone_angle_supported

```python
@property
def is_outer_cone_angle_supported() -> bool
```

(bool):  [Read-Write] Whether OuterConeAngle can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_outer_cone_angle_supported"></a>

#### is_outer_cone_angle_supported

```python
@is_outer_cone_angle_supported.setter
def is_outer_cone_angle_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_attenuation_radius_supported"></a>

#### is_attenuation_radius_supported

```python
@property
def is_attenuation_radius_supported() -> bool
```

(bool):  [Read-Write] Whether AttenuationRadius can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_attenuation_radius_supported"></a>

#### is_attenuation_radius_supported

```python
@is_attenuation_radius_supported.setter
def is_attenuation_radius_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_source_lenght_supported"></a>

#### is_source_lenght_supported

```python
@property
def is_source_lenght_supported() -> bool
```

(bool):  [Read-Write] Whether SourceLength can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_source_lenght_supported"></a>

#### is_source_lenght_supported

```python
@is_source_lenght_supported.setter
def is_source_lenght_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_source_radius_supported"></a>

#### is_source_radius_supported

```python
@property
def is_source_radius_supported() -> bool
```

(bool):  [Read-Write] Whether SourceRadius can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_source_radius_supported"></a>

#### is_source_radius_supported

```python
@is_source_radius_supported.setter
def is_source_radius_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightStaticData.is_soft_source_radius_supported"></a>

#### is_soft_source_radius_supported

```python
@property
def is_soft_source_radius_supported() -> bool
```

(bool):  [Read-Write] Whether SoftSourceRadius can be used in the frame data. Only used for spot lights

<a id="unreal.LiveLinkLightStaticData.is_soft_source_radius_supported"></a>

#### is_soft_source_radius_supported

```python
@is_soft_source_radius_supported.setter
def is_soft_source_radius_supported(value: bool) -> None
```

<a id="unreal.LiveLinkLightFrameData"></a>