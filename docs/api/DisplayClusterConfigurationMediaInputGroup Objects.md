## DisplayClusterConfigurationMediaInputGroup Objects

```python
class DisplayClusterConfigurationMediaInputGroup(
        DisplayClusterConfigurationMediaInput)
```

* Media input group (ICVFX, Full frame)

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_nodes`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that use media source below
- ``media_source`` (MediaSource):  [Read-Write] Media source to use

<a id="unreal.DisplayClusterConfigurationMediaInputGroup.__init__"></a>

#### __init__

```python
def __init__(
    media_source: MediaSource = None,
    cluster_nodes: DisplayClusterConfigurationClusterItemReferenceList = [[]]
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaInputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@property
def cluster_nodes() -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that use media source below

<a id="unreal.DisplayClusterConfigurationMediaInputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@cluster_nodes.setter
def cluster_nodes(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings"></a>