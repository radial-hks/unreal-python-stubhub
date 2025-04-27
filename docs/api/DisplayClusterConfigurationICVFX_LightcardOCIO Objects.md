## DisplayClusterConfigurationICVFX_LightcardOCIO Objects

```python
class DisplayClusterConfigurationICVFX_LightcardOCIO(StructBase)
```

Display Cluster Configuration ICVFX Lightcard OCIO

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_ocio`` (DisplayClusterConfigurationICVFX_LightcardCustomOCIO):  [Read-Write] Custom OpenColorIO configuration for Light Cards.
- ``lightcard_ocio_mode`` (DisplayClusterConfigurationViewportLightcardOCIOMode):  [Read-Write] Light Cards OCIO mode.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO.__init__"></a>

#### __init__

```python
def __init__(
    lightcard_ocio_mode:
    DisplayClusterConfigurationViewportLightcardOCIOMode = DisplayClusterConfigurationViewportLightcardOCIOMode
    .N_DISPLAY,
    custom_ocio: DisplayClusterConfigurationICVFX_LightcardCustomOCIO = [[
        False,
        [
            None, ["", -1, ""], ["", -1, ""], ["", ""],
            OpenColorIOViewTransformDirection.FORWARD
        ]
    ], []]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO.lightcard_ocio_mode"></a>

#### lightcard_ocio_mode

```python
@property
def lightcard_ocio_mode(
) -> DisplayClusterConfigurationViewportLightcardOCIOMode
```

(DisplayClusterConfigurationViewportLightcardOCIOMode):  [Read-Write] Light Cards OCIO mode.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO.lightcard_ocio_mode"></a>

#### lightcard_ocio_mode

```python
@lightcard_ocio_mode.setter
def lightcard_ocio_mode(
        value: DisplayClusterConfigurationViewportLightcardOCIOMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO.custom_ocio"></a>

#### custom_ocio

```python
@property
def custom_ocio() -> DisplayClusterConfigurationICVFX_LightcardCustomOCIO
```

(DisplayClusterConfigurationICVFX_LightcardCustomOCIO):  [Read-Write] Custom OpenColorIO configuration for Light Cards.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO.custom_ocio"></a>

#### custom_ocio

```python
@custom_ocio.setter
def custom_ocio(
        value: DisplayClusterConfigurationICVFX_LightcardCustomOCIO) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList"></a>