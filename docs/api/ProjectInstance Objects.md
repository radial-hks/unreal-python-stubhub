## ProjectInstance Objects

```python
class ProjectInstance(StructBase)
```

Project Instance

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpBuiltInEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor`` (Actor):  [Read-Write]
- ``component_name`` (Name):  [Read-Write]
- ``index`` (int32):  [Read-Write]

<a id="unreal.ProjectInstance.__init__"></a>

#### \_\_init\_\_

```python
def __init__(actor: Actor = None,
             component_name: Name = "None",
             index: int = 0) -> None
```

<a id="unreal.ProjectInstance.actor"></a>

#### actor

```python
@property
def actor() -> Actor
```

(Actor):  [Read-Only]

<a id="unreal.ProjectInstance.component_name"></a>

#### component\_name

```python
@property
def component_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.ProjectInstance.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.PresetEntityData"></a>