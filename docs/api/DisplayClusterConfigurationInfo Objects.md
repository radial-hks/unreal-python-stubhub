## DisplayClusterConfigurationInfo Objects

```python
class DisplayClusterConfigurationInfo(StructBase)
```

Display Cluster Configuration Info

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_path`` (str):  [Read-Only]
- ``description`` (str):  [Read-Write]
- ``version`` (str):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationInfo.__init__"></a>

#### __init__

```python
def __init__(description: str = "",
             version: str = "",
             asset_path: str = "") -> None
```

<a id="unreal.DisplayClusterConfigurationInfo.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationInfo.description"></a>

#### description

```python
@description.setter
def description(value: str) -> None
```

<a id="unreal.DisplayClusterConfigurationInfo.version"></a>

#### version

```python
@property
def version() -> str
```

(str):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationInfo.asset_path"></a>

#### asset_path

```python
@property
def asset_path() -> str
```

(str):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationPrimaryNodePorts"></a>