## BasicInfoAtom Objects

```python
class BasicInfoAtom(EntityAtomBase)
```

Basic Info Atom

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: BasicInfoAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_data`` (str):  [Read-Write]
- ``custom_id`` (str):  [Read-Write]
- ``entity_name`` (str):  [Read-Write]
- ``parent_eid`` (int64):  [Read-Write]

<a id="unreal.BasicInfoAtom.entity_name"></a>

#### entity\_name

```python
@property
def entity_name() -> str
```

(str):  [Read-Only]

<a id="unreal.BasicInfoAtom.custom_id"></a>

#### custom\_id

```python
@property
def custom_id() -> str
```

(str):  [Read-Only]

<a id="unreal.BasicInfoAtom.custom_data"></a>

#### custom\_data

```python
@property
def custom_data() -> str
```

(str):  [Read-Only]

<a id="unreal.BasicInfoAtom.parent_eid"></a>

#### parent\_eid

```python
@property
def parent_eid() -> int
```

(int64):  [Read-Only]

<a id="unreal.EntityChildrenAtom"></a>