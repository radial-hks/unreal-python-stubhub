## DisplayClusterConfigurationICVFX_CameraOCIO Objects

```python
class DisplayClusterConfigurationICVFX_CameraOCIO(StructBase)
```

Display Cluster Configuration ICVFX Camera OCIO

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_nodes_ocio_configuration`` (DisplayClusterConfigurationOCIOConfiguration):  [Read-Write] OCIO Display look configuration for all nodes
- ``per_node_ocio_profiles`` (Array[DisplayClusterConfigurationOCIOProfile]):  [Read-Write] Apply an OpenColorIO configuration on a per-node or group-of-nodes basis.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraOCIO.__init__"></a>

#### __init__

```python
def __init__(
    all_nodes_ocio_configuration:
    DisplayClusterConfigurationOCIOConfiguration = [
        False,
        [
            None, ["", -1, ""], ["", -1, ""], ["", ""],
            OpenColorIOViewTransformDirection.FORWARD
        ]
    ],
    per_node_ocio_profiles: Array[DisplayClusterConfigurationOCIOProfile] = []
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraOCIO.all_nodes_ocio_configuration"></a>

#### all_nodes_ocio_configuration

```python
@property
def all_nodes_ocio_configuration(
) -> DisplayClusterConfigurationOCIOConfiguration
```

(DisplayClusterConfigurationOCIOConfiguration):  [Read-Write] OCIO Display look configuration for all nodes

<a id="unreal.DisplayClusterConfigurationICVFX_CameraOCIO.all_nodes_ocio_configuration"></a>

#### all_nodes_ocio_configuration

```python
@all_nodes_ocio_configuration.setter
def all_nodes_ocio_configuration(
        value: DisplayClusterConfigurationOCIOConfiguration) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraOCIO.per_node_ocio_profiles"></a>

#### per_node_ocio_profiles

```python
@property
def per_node_ocio_profiles() -> Array[DisplayClusterConfigurationOCIOProfile]
```

(Array[DisplayClusterConfigurationOCIOProfile]):  [Read-Write] Apply an OpenColorIO configuration on a per-node or group-of-nodes basis.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraOCIO.per_node_ocio_profiles"></a>

#### per_node_ocio_profiles

```python
@per_node_ocio_profiles.setter
def per_node_ocio_profiles(
        value: Array[DisplayClusterConfigurationOCIOProfile]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardOCIO"></a>