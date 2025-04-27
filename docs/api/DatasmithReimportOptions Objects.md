## DatasmithReimportOptions Objects

```python
class DatasmithReimportOptions(StructBase)
```

Datasmith Reimport Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``respawn_deleted_actors`` (bool):  [Read-Write] Specifies whether or not to add back Actors you've deleted from the current Level
- ``update_actors`` (bool):  [Read-Write] Specifies whether or not to update Datasmith Scene Actors in the current Level

<a id="unreal.DatasmithReimportOptions.__init__"></a>

#### __init__

```python
def __init__(update_actors: bool = False,
             respawn_deleted_actors: bool = False) -> None
```

<a id="unreal.DatasmithReimportOptions.update_actors"></a>

#### update_actors

```python
@property
def update_actors() -> bool
```

(bool):  [Read-Write] Specifies whether or not to update Datasmith Scene Actors in the current Level

<a id="unreal.DatasmithReimportOptions.update_actors"></a>

#### update_actors

```python
@update_actors.setter
def update_actors(value: bool) -> None
```

<a id="unreal.DatasmithReimportOptions.respawn_deleted_actors"></a>

#### respawn_deleted_actors

```python
@property
def respawn_deleted_actors() -> bool
```

(bool):  [Read-Write] Specifies whether or not to add back Actors you've deleted from the current Level

<a id="unreal.DatasmithReimportOptions.respawn_deleted_actors"></a>

#### respawn_deleted_actors

```python
@respawn_deleted_actors.setter
def respawn_deleted_actors(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions"></a>