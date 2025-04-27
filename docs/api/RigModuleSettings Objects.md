## RigModuleSettings Objects

```python
class RigModuleSettings(StructBase)
```

Rig Module Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigModuleDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (str):  [Read-Write] The category of the module
- ``description`` (str):  [Read-Write] The description of the module
- ``exposed_connectors`` (Array[RigModuleConnector]):  [Read-Write]
- ``icon`` (SoftObjectPath):  [Read-Write] The icon used for the module in the module library
- ``identifier`` (RigModuleIdentifier):  [Read-Write] The identifier used to retrieve the module in the module library
- ``keywords`` (str):  [Read-Write] The keywords of the module

<a id="unreal.RigModuleSettings.__init__"></a>

#### __init__

```python
def __init__(identifier: RigModuleIdentifier = ["", "Module"],
             icon: SoftObjectPath = [""],
             category: str = "",
             keywords: str = "",
             description: str = "",
             exposed_connectors: Array[RigModuleConnector] = []) -> None
```

<a id="unreal.RigModuleSettings.identifier"></a>

#### identifier

```python
@property
def identifier() -> RigModuleIdentifier
```

(RigModuleIdentifier):  [Read-Write] The identifier used to retrieve the module in the module library

<a id="unreal.RigModuleSettings.identifier"></a>

#### identifier

```python
@identifier.setter
def identifier(value: RigModuleIdentifier) -> None
```

<a id="unreal.RigModuleSettings.icon"></a>

#### icon

```python
@property
def icon() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] The icon used for the module in the module library

<a id="unreal.RigModuleSettings.icon"></a>

#### icon

```python
@icon.setter
def icon(value: SoftObjectPath) -> None
```

<a id="unreal.RigModuleSettings.category"></a>

#### category

```python
@property
def category() -> str
```

(str):  [Read-Write] The category of the module

<a id="unreal.RigModuleSettings.category"></a>

#### category

```python
@category.setter
def category(value: str) -> None
```

<a id="unreal.RigModuleSettings.keywords"></a>

#### keywords

```python
@property
def keywords() -> str
```

(str):  [Read-Write] The keywords of the module

<a id="unreal.RigModuleSettings.keywords"></a>

#### keywords

```python
@keywords.setter
def keywords(value: str) -> None
```

<a id="unreal.RigModuleSettings.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Write] The description of the module

<a id="unreal.RigModuleSettings.description"></a>

#### description

```python
@description.setter
def description(value: str) -> None
```

<a id="unreal.RigModuleSettings.exposed_connectors"></a>

#### exposed_connectors

```python
@property
def exposed_connectors() -> Array[RigModuleConnector]
```

(Array[RigModuleConnector]):  [Read-Only]

<a id="unreal.RigModuleConnector"></a>