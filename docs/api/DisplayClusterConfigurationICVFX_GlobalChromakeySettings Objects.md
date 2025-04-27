## DisplayClusterConfigurationICVFX_GlobalChromakeySettings Objects

```python
class DisplayClusterConfigurationICVFX_GlobalChromakeySettings(StructBase)
```

Chromakey settings that are global for all ICVFX cameras in a root actor

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chromakey_color`` (LinearColor):  [Read-Write] Chromakey Color
- ``chromakey_markers`` (DisplayClusterConfigurationICVFX_ChromakeyMarkers):  [Read-Write] Display Chromakey Markers to facilitate camera tracking in post production.

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings.__init__"></a>

#### __init__

```python
def __init__(
    chromakey_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    chromakey_markers: DisplayClusterConfigurationICVFX_ChromakeyMarkers = [
        True, [0.000000, 0.250000, 0.000000, 1.000000], None, 0.500000,
        1.500000, [0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings.chromakey_color"></a>

#### chromakey_color

```python
@property
def chromakey_color() -> LinearColor
```

(LinearColor):  [Read-Write] Chromakey Color

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings.chromakey_color"></a>

#### chromakey_color

```python
@chromakey_color.setter
def chromakey_color(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings.chromakey_markers"></a>

#### chromakey_markers

```python
@property
def chromakey_markers() -> DisplayClusterConfigurationICVFX_ChromakeyMarkers
```

(DisplayClusterConfigurationICVFX_ChromakeyMarkers):  [Read-Write] Display Chromakey Markers to facilitate camera tracking in post production.

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings.chromakey_markers"></a>

#### chromakey_markers

```python
@chromakey_markers.setter
def chromakey_markers(
        value: DisplayClusterConfigurationICVFX_ChromakeyMarkers) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings"></a>