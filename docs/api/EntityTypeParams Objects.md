## EntityTypeParams Objects

```python
class EntityTypeParams(ParamsBase)
```

Entity Type Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: ApiParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``entity_type`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.EntityTypeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "", entity_type: str = "") -> None
```

<a id="unreal.EntityTypeParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityTypeParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.EntityTypeParams.entity_type"></a>

#### entity\_type

```python
@property
def entity_type() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityTypeParams.entity_type"></a>

#### entity\_type

```python
@entity_type.setter
def entity_type(value: str) -> None
```

<a id="unreal.EidArray"></a>