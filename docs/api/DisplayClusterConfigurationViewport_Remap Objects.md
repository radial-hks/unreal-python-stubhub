## DisplayClusterConfigurationViewport_Remap Objects

```python
class DisplayClusterConfigurationViewport_Remap(StructBase)
```

Configuration for all remapping to apply to a single viewport

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ViewportRemap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_remap`` (DisplayClusterConfigurationViewport_RemapData):  [Read-Write] The base remap to apply to the entire viewport, used to apply flipping and rotation to the viewport
- ``enable`` (bool):  [Read-Write] Enables or disables viweport output remapping

<a id="unreal.DisplayClusterConfigurationViewport_Remap.__init__"></a>

#### __init__

```python
def __init__(
    enable: bool = False,
    base_remap: DisplayClusterConfigurationViewport_RemapData = [[0, 0, 0, 0],
                                                                 [0, 0, 0,
                                                                  0], 0.000000,
                                                                 False, False]
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Remap.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enables or disables viweport output remapping

<a id="unreal.DisplayClusterConfigurationViewport_Remap.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Remap.base_remap"></a>

#### base_remap

```python
@property
def base_remap() -> DisplayClusterConfigurationViewport_RemapData
```

(DisplayClusterConfigurationViewport_RemapData):  [Read-Write] The base remap to apply to the entire viewport, used to apply flipping and rotation to the viewport

<a id="unreal.DisplayClusterConfigurationViewport_Remap.base_remap"></a>

#### base_remap

```python
@base_remap.setter
def base_remap(value: DisplayClusterConfigurationViewport_RemapData) -> None
```

<a id="unreal.KeyMappingRow"></a>