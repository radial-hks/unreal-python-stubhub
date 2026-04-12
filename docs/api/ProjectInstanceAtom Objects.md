## ProjectInstanceAtom Objects

```python
class ProjectInstanceAtom(EntityAtomBase)
```

Project Instance Atom

**C++ Source:**

- **Plugin**: AesTilesEntity
- **Module**: WdpProjectModel
- **File**: ProjectInstanceAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_data`` (str):  [Read-Write]
- ``entity_name`` (str):  [Read-Write]
- ``hidden_nodes`` (Array[int32]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.ProjectInstanceAtom.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ProjectInstanceAtom.entity_name"></a>

#### entity\_name

```python
@property
def entity_name() -> str
```

(str):  [Read-Only]

<a id="unreal.ProjectInstanceAtom.custom_data"></a>

#### custom\_data

```python
@property
def custom_data() -> str
```

(str):  [Read-Only]

<a id="unreal.ProjectInstanceAtom.hidden_nodes"></a>

#### hidden\_nodes

```python
@property
def hidden_nodes() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.ProjectInstancePickAtom"></a>