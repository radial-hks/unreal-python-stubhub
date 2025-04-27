## RigConnectorSettings Objects

```python
class RigConnectorSettings(StructBase)
```

Rig Connector Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write]
- ``optional`` (bool):  [Read-Write]
- ``rules`` (Array[RigConnectionRuleStash]):  [Read-Write]
- ``type`` (ConnectorType):  [Read-Write]

<a id="unreal.RigConnectorSettings.__init__"></a>

#### __init__

```python
def __init__(description: str = "",
             type: ConnectorType = ConnectorType.PRIMARY,
             optional: bool = False,
             rules: Array[RigConnectionRuleStash] = []) -> None
```

<a id="unreal.RigConnectorSettings.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Write]

<a id="unreal.RigConnectorSettings.description"></a>

#### description

```python
@description.setter
def description(value: str) -> None
```

<a id="unreal.RigConnectorSettings.type"></a>

#### type

```python
@property
def type() -> ConnectorType
```

(ConnectorType):  [Read-Write]

<a id="unreal.RigConnectorSettings.type"></a>

#### type

```python
@type.setter
def type(value: ConnectorType) -> None
```

<a id="unreal.RigConnectorSettings.optional"></a>

#### optional

```python
@property
def optional() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigConnectorSettings.optional"></a>

#### optional

```python
@optional.setter
def optional(value: bool) -> None
```

<a id="unreal.RigConnectorSettings.rules"></a>

#### rules

```python
@property
def rules() -> Array[RigConnectionRuleStash]
```

(Array[RigConnectionRuleStash]):  [Read-Write]

<a id="unreal.RigConnectorSettings.rules"></a>

#### rules

```python
@rules.setter
def rules(value: Array[RigConnectionRuleStash]) -> None
```

<a id="unreal.RigConnectionRuleStash"></a>