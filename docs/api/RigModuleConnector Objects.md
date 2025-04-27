## RigModuleConnector Objects

```python
class RigModuleConnector(StructBase)
```

Rig Module Connector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigModuleDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
- ``settings`` (RigConnectorSettings):  [Read-Write]

<a id="unreal.RigModuleConnector.__init__"></a>

#### __init__

```python
def __init__(
    name: str = "",
    settings: RigConnectorSettings = ["", ConnectorType.PRIMARY, False, []]
) -> None
```

<a id="unreal.RigModuleConnector.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.RigModuleConnector.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.RigModuleConnector.settings"></a>

#### settings

```python
@property
def settings() -> RigConnectorSettings
```

(RigConnectorSettings):  [Read-Write]

<a id="unreal.RigModuleConnector.settings"></a>

#### settings

```python
@settings.setter
def settings(value: RigConnectorSettings) -> None
```

<a id="unreal.RigConnectorSettings"></a>