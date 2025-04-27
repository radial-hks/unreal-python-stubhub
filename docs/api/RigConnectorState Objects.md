## RigConnectorState Objects

```python
class RigConnectorState(StructBase)
```

Rig Connector State

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``resolved_target`` (RigElementKey):  [Read-Write]
- ``settings`` (RigConnectorSettings):  [Read-Write]

<a id="unreal.RigConnectorState.__init__"></a>

#### __init__

```python
def __init__(
    name: Name = "None",
    resolved_target: RigElementKey = [RigElementType.NONE, "None"],
    settings: RigConnectorSettings = ["", ConnectorType.PRIMARY, False, []]
) -> None
```

<a id="unreal.RigConnectorState.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigConnectorState.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigConnectorState.resolved_target"></a>

#### resolved_target

```python
@property
def resolved_target() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigConnectorState.resolved_target"></a>

#### resolved_target

```python
@resolved_target.setter
def resolved_target(value: RigElementKey) -> None
```

<a id="unreal.RigConnectorState.settings"></a>

#### settings

```python
@property
def settings() -> RigConnectorSettings
```

(RigConnectorSettings):  [Read-Write]

<a id="unreal.RigConnectorState.settings"></a>

#### settings

```python
@settings.setter
def settings(value: RigConnectorSettings) -> None
```

<a id="unreal.RigConnectorElement"></a>