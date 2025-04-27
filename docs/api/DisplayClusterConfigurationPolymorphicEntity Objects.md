## DisplayClusterConfigurationPolymorphicEntity Objects

```python
class DisplayClusterConfigurationPolymorphicEntity(StructBase)
```

Display Cluster Configuration Polymorphic Entity

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
- ``parameters`` (Map[str, str]):  [Read-Write] Generic parameters map
- ``type`` (str):  [Read-Write] Polymorphic entity type

<a id="unreal.DisplayClusterConfigurationPolymorphicEntity.__init__"></a>

#### __init__

```python
def __init__(type: str = "", parameters: Map[str, str] = {}) -> None
```

<a id="unreal.DisplayClusterConfigurationPolymorphicEntity.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Only] Polymorphic entity type

<a id="unreal.DisplayClusterConfigurationPolymorphicEntity.parameters"></a>

#### parameters

```python
@property
def parameters() -> Map[str, str]
```

(Map[str, str]):  [Read-Only] Generic parameters map

<a id="unreal.DisplayClusterConfigurationRenderSyncPolicy"></a>