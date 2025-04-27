## DisplayClusterConfigurationClusterSync Objects

```python
class DisplayClusterConfigurationClusterSync(StructBase)
```

Display Cluster Configuration Cluster Sync

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_sync_policy`` (DisplayClusterConfigurationInputSyncPolicy):  [Read-Write]
- ``render_sync_policy`` (DisplayClusterConfigurationRenderSyncPolicy):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationClusterSync.__init__"></a>

#### __init__

```python
def __init__(
    render_sync_policy: DisplayClusterConfigurationRenderSyncPolicy = ["", {}],
    input_sync_policy: DisplayClusterConfigurationInputSyncPolicy = ["", {}]
) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterSync.render_sync_policy"></a>

#### render_sync_policy

```python
@property
def render_sync_policy() -> DisplayClusterConfigurationRenderSyncPolicy
```

(DisplayClusterConfigurationRenderSyncPolicy):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationClusterSync.input_sync_policy"></a>

#### input_sync_policy

```python
@property
def input_sync_policy() -> DisplayClusterConfigurationInputSyncPolicy
```

(DisplayClusterConfigurationInputSyncPolicy):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationNetworkSettings"></a>