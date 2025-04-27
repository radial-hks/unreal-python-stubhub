## DisplayClusterConfigurationMediaOutputGroup Objects

```python
class DisplayClusterConfigurationMediaOutputGroup(
        DisplayClusterConfigurationMediaOutput)
```

* Media output group (ICVFX, Full Frame)

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_nodes`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that export media via MediaOutput below
- ``media_output`` (MediaOutput):  [Read-Write] Media output to use
- ``output_sync_policy`` (DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write] Media output synchronization policy

<a id="unreal.DisplayClusterConfigurationMediaOutputGroup.__init__"></a>

#### __init__

```python
def __init__(
    media_output: MediaOutput = None,
    output_sync_policy: DisplayClusterMediaOutputSynchronizationPolicy = None,
    cluster_nodes: DisplayClusterConfigurationClusterItemReferenceList = [[]]
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaOutputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@property
def cluster_nodes() -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that export media via MediaOutput below

<a id="unreal.DisplayClusterConfigurationMediaOutputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@cluster_nodes.setter
def cluster_nodes(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaInput"></a>