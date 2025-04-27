## DisplayClusterConfigurationInputSyncPolicy Objects

```python
class DisplayClusterConfigurationInputSyncPolicy(
        DisplayClusterConfigurationPolymorphicEntity)
```

Display Cluster Configuration Input Sync Policy

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_custom`` (bool):  [Read-Write] When a custom policy is selected from the details panel.
  This is needed in the event a custom policy is selected
  but the custom type is a default policy. This allows users
  to further customize default policies if necessary.

  EditAnywhere is required so we can manipulate the property
  through a handle. Details will hide it from showing.
- ``parameters`` (Map[str, str]):  [Read-Write] Generic parameters map
- ``type`` (str):  [Read-Write] Polymorphic entity type

<a id="unreal.DisplayClusterConfigurationInputSyncPolicy.__init__"></a>

#### __init__

```python
def __init__(type: str = "", parameters: Map[str, str] = {}) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterSync"></a>