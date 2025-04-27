## DisplayClusterConfigurationPrimaryNode Objects

```python
class DisplayClusterConfigurationPrimaryNode(StructBase)
```

Display Cluster Configuration Primary Node

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (str):  [Read-Write]
- ``ports`` (DisplayClusterConfigurationPrimaryNodePorts):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationPrimaryNode.__init__"></a>

#### __init__

```python
def __init__(id: str = "",
             ports: DisplayClusterConfigurationPrimaryNodePorts = []) -> None
```

<a id="unreal.DisplayClusterConfigurationPrimaryNode.id"></a>

#### id

```python
@property
def id() -> str
```

(str):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationPrimaryNode.ports"></a>

#### ports

```python
@property
def ports() -> DisplayClusterConfigurationPrimaryNodePorts
```

(DisplayClusterConfigurationPrimaryNodePorts):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationMasterNode"></a>