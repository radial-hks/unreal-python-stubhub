## OnVegetationCreatingEventArgs Objects

```python
class OnVegetationCreatingEventArgs(EventArgsBase)
```

On Vegetation Creating Event Args

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: RuntimeModelerAPI
- **File**: WdpModelerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_id`` (int64):  [Read-Write]
- ``entity_type`` (Name):  [Read-Write]
- ``tip`` (str):  [Read-Write]

<a id="unreal.OnVegetationCreatingEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_id: int = 0,
             entity_type: Name = "None",
             tip: str = "") -> None
```

<a id="unreal.OnVegetationCreatingEventArgs.entity_id"></a>

#### entity\_id

```python
@property
def entity_id() -> int
```

(int64):  [Read-Write]

<a id="unreal.OnVegetationCreatingEventArgs.entity_id"></a>

#### entity\_id

```python
@entity_id.setter
def entity_id(value: int) -> None
```

<a id="unreal.OnVegetationCreatingEventArgs.entity_type"></a>

#### entity\_type

```python
@property
def entity_type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.OnVegetationCreatingEventArgs.entity_type"></a>

#### entity\_type

```python
@entity_type.setter
def entity_type(value: Name) -> None
```

<a id="unreal.OnVegetationCreatingEventArgs.tip"></a>

#### tip

```python
@property
def tip() -> str
```

(str):  [Read-Write]

<a id="unreal.OnVegetationCreatingEventArgs.tip"></a>

#### tip

```python
@tip.setter
def tip(value: str) -> None
```

<a id="unreal.OnVegetationCreatedEventArgs"></a>