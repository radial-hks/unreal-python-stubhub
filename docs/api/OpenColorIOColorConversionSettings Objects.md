## OpenColorIOColorConversionSettings Objects

```python
class OpenColorIOColorConversionSettings(StructBase)
```

Identifies a OCIO ColorSpace conversion.

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIOColorSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``configuration_source`` (OpenColorIOConfiguration):  [Read-Write] The source color space name.
- ``destination_color_space`` (OpenColorIOColorSpace):  [Read-Write] The destination color space name.
- ``destination_display_view`` (OpenColorIODisplayView):  [Read-Write] The destination display view name.
- ``display_view_direction`` (OpenColorIOViewTransformDirection):  [Read-Write] The display view direction.
- ``source_color_space`` (OpenColorIOColorSpace):  [Read-Write] The source color space name.

<a id="unreal.OpenColorIOColorConversionSettings.__init__"></a>

#### __init__

```python
def __init__(
    configuration_source: OpenColorIOConfiguration = None,
    source_color_space: OpenColorIOColorSpace = ["", -1, ""],
    destination_color_space: OpenColorIOColorSpace = ["", -1, ""],
    destination_display_view: OpenColorIODisplayView = ["", ""],
    display_view_direction:
    OpenColorIOViewTransformDirection = OpenColorIOViewTransformDirection.
    FORWARD
) -> None
```

<a id="unreal.OpenColorIOColorConversionSettings.configuration_source"></a>

#### configuration_source

```python
@property
def configuration_source() -> OpenColorIOConfiguration
```

(OpenColorIOConfiguration):  [Read-Write] The source color space name.

<a id="unreal.OpenColorIOColorConversionSettings.configuration_source"></a>

#### configuration_source

```python
@configuration_source.setter
def configuration_source(value: OpenColorIOConfiguration) -> None
```

<a id="unreal.OpenColorIOColorConversionSettings.source_color_space"></a>

#### source_color_space

```python
@property
def source_color_space() -> OpenColorIOColorSpace
```

(OpenColorIOColorSpace):  [Read-Write] The source color space name.

<a id="unreal.OpenColorIOColorConversionSettings.source_color_space"></a>

#### source_color_space

```python
@source_color_space.setter
def source_color_space(value: OpenColorIOColorSpace) -> None
```

<a id="unreal.OpenColorIOColorConversionSettings.destination_color_space"></a>

#### destination_color_space

```python
@property
def destination_color_space() -> OpenColorIOColorSpace
```

(OpenColorIOColorSpace):  [Read-Write] The destination color space name.

<a id="unreal.OpenColorIOColorConversionSettings.destination_color_space"></a>

#### destination_color_space

```python
@destination_color_space.setter
def destination_color_space(value: OpenColorIOColorSpace) -> None
```

<a id="unreal.OpenColorIOColorConversionSettings.destination_display_view"></a>

#### destination_display_view

```python
@property
def destination_display_view() -> OpenColorIODisplayView
```

(OpenColorIODisplayView):  [Read-Write] The destination display view name.

<a id="unreal.OpenColorIOColorConversionSettings.destination_display_view"></a>

#### destination_display_view

```python
@destination_display_view.setter
def destination_display_view(value: OpenColorIODisplayView) -> None
```

<a id="unreal.OpenColorIOColorConversionSettings.display_view_direction"></a>

#### display_view_direction

```python
@property
def display_view_direction() -> OpenColorIOViewTransformDirection
```

(OpenColorIOViewTransformDirection):  [Read-Write] The display view direction.

<a id="unreal.OpenColorIOColorConversionSettings.display_view_direction"></a>

#### display_view_direction

```python
@display_view_direction.setter
def display_view_direction(value: OpenColorIOViewTransformDirection) -> None
```

<a id="unreal.OpenColorIODisplayConfiguration"></a>