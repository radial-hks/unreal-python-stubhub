## DisplayClusterConfigurationPostprocess Objects

```python
class DisplayClusterConfigurationPostprocess(
        DisplayClusterConfigurationPolymorphicEntity)
```

Display Cluster Configuration Postprocess

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_custom`` (bool):  [Read-Write] When a custom policy is selected from the details panel.
  This is needed in the event a custom policy is selected
  but the custom type is a default policy. This allows users
  to further customize default policies if necessary.

  EditAnywhere is required so we can manipulate the property
  through a handle. Details will hide it from showing.
- ``order`` (int32):  [Read-Write] Control postprocess rendering order. Bigger value rendered last
- ``parameters`` (Map[str, str]):  [Read-Write] Generic parameters map
- ``type`` (str):  [Read-Write] Polymorphic entity type

<a id="unreal.DisplayClusterConfigurationPostprocess.__init__"></a>

#### __init__

```python
def __init__(type: str = "",
             parameters: Map[str, str] = {},
             order: int = 0) -> None
```

<a id="unreal.DisplayClusterConfigurationPostprocess.order"></a>

#### order

```python
@property
def order() -> int
```

(int32):  [Read-Only] Control postprocess rendering order. Bigger value rendered last

<a id="unreal.DisplayClusterConfigurationClusterItemReferenceList"></a>