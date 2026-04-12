## AesEditorEntitiesRemoveMessage Objects

```python
class AesEditorEntitiesRemoveMessage(StructBase)
```

Aes Editor Entities Remove Message

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorMode
- **File**: AesEditorGameplayTags.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_ids`` (Array[int64]):  [Read-Write]
- ``layer_name`` (Name):  [Read-Write]

<a id="unreal.AesEditorEntitiesRemoveMessage.__init__"></a>

#### \_\_init\_\_

```python
def __init__(layer_name: Name = "None", entity_ids: Array[int] = []) -> None
```

<a id="unreal.AesEditorEntitiesRemoveMessage.layer_name"></a>

#### layer\_name

```python
@property
def layer_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesEditorEntitiesRemoveMessage.layer_name"></a>

#### layer\_name

```python
@layer_name.setter
def layer_name(value: Name) -> None
```

<a id="unreal.AesEditorEntitiesRemoveMessage.entity_ids"></a>

#### entity\_ids

```python
@property
def entity_ids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.AesEditorEntitiesRemoveMessage.entity_ids"></a>

#### entity\_ids

```python
@entity_ids.setter
def entity_ids(value: Array[int]) -> None
```

<a id="unreal.AesRoadReplaceMessage"></a>