## RigUnit_ResolveConnector Objects

```python
class RigUnit_ResolveConnector(RigUnit_RigModulesBase)
```

Returns the resolved item of the connector.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_RigModules.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``connector`` (RigElementKey):  [Read-Write] * The key of the connector to resolve
- ``is_connected`` (bool):  [Read-Write] * Returns true if the connector is resolved to a target.
- ``result`` (RigElementKey):  [Read-Write] * The resulting item the connector is resolved to
- ``skip_socket`` (bool):  [Read-Write] * If the connector is resolved to a socket the node
  * will return the socket's direct parent (skipping it).

<a id="unreal.RigUnit_ResolveConnector.__init__"></a>

#### __init__

```python
def __init__(connector: RigElementKey = [RigElementType.NONE, "None"],
             skip_socket: bool = False,
             result: RigElementKey = [RigElementType.NONE, "None"],
             is_connected: bool = False) -> None
```

<a id="unreal.RigUnit_ResolveConnector.connector"></a>

#### connector

```python
@property
def connector() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The key of the connector to resolve

<a id="unreal.RigUnit_ResolveConnector.connector"></a>

#### connector

```python
@connector.setter
def connector(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ResolveConnector.skip_socket"></a>

#### skip_socket

```python
@property
def skip_socket() -> bool
```

(bool):  [Read-Write] * If the connector is resolved to a socket the node
* will return the socket's direct parent (skipping it).

<a id="unreal.RigUnit_ResolveConnector.skip_socket"></a>

#### skip_socket

```python
@skip_socket.setter
def skip_socket(value: bool) -> None
```

<a id="unreal.RigUnit_ResolveConnector.result"></a>

#### result

```python
@property
def result() -> RigElementKey
```

(RigElementKey):  [Read-Only] * The resulting item the connector is resolved to

<a id="unreal.RigUnit_ResolveConnector.is_connected"></a>

#### is_connected

```python
@property
def is_connected() -> bool
```

(bool):  [Read-Only] * Returns true if the connector is resolved to a target.

<a id="unreal.RigUnit_GetCurrentNameSpace"></a>