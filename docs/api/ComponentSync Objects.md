## ComponentSync Objects

```python
class ComponentSync(StructBase)
```

Component Sync

**C++ Source:**

- **Module**: Engine
- **File**: LODSyncComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``sync_option`` (SyncOption):  [Read-Write]

<a id="unreal.ComponentSync.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             sync_option: SyncOption = SyncOption.DRIVE) -> None
```

<a id="unreal.ComponentSync.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ComponentSync.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ComponentSync.sync_option"></a>

#### sync_option

```python
@property
def sync_option() -> SyncOption
```

(SyncOption):  [Read-Write]

<a id="unreal.ComponentSync.sync_option"></a>

#### sync_option

```python
@sync_option.setter
def sync_option(value: SyncOption) -> None
```

<a id="unreal.MaterialSpriteElement"></a>