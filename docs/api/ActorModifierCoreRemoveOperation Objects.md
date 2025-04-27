## ActorModifierCoreRemoveOperation Objects

```python
class ActorModifierCoreRemoveOperation(StructBase)
```

Actor Modifier Core Remove Operation

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreLibraryDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``remove_dependencies`` (bool):  [Read-Write]
- ``remove_modifier`` (ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreRemoveOperation.__init__"></a>

#### __init__

```python
def __init__(remove_modifier: ActorModifierCoreBase = None,
             remove_dependencies: bool = False) -> None
```

<a id="unreal.ActorModifierCoreRemoveOperation.remove_modifier"></a>

#### remove_modifier

```python
@property
def remove_modifier() -> ActorModifierCoreBase
```

(ActorModifierCoreBase):  [Read-Write]

<a id="unreal.ActorModifierCoreRemoveOperation.remove_modifier"></a>

#### remove_modifier

```python
@remove_modifier.setter
def remove_modifier(value: ActorModifierCoreBase) -> None
```

<a id="unreal.ActorModifierCoreRemoveOperation.remove_dependencies"></a>

#### remove_dependencies

```python
@property
def remove_dependencies() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ActorModifierCoreRemoveOperation.remove_dependencies"></a>

#### remove_dependencies

```python
@remove_dependencies.setter
def remove_dependencies(value: bool) -> None
```

<a id="unreal.AvaTag"></a>