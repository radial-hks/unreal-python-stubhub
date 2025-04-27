## ActorDesc Objects

```python
class ActorDesc(StructBase)
```

Snapshot of an actor descriptor, which represents the state of an actor on disk.
The actor may or may not be loaded.

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_is_editor_only`` (bool):  [Read-Only] Actor's editor-only property.
- ``actor_package`` (Name):  [Read-Only] Actor's package name.
- ``actor_path`` (Name):  [Read-Only] Actor's path name.
- ``bounds`` (Box):  [Read-Only] Streaming bounds of this actor.
- ``class_`` (SoftObjectPath):  [Read-Only] Actor class, can point to a native or Blueprint class and may be redirected.
- ``data_layer_assets`` (Array[SoftObjectPath]):  [Read-Only] Actor's data layer assets.
- ``guid`` (Guid):  [Read-Only] The actor GUID of this descriptor.
- ``is_spatially_loaded`` (bool):  [Read-Only] Actor's streaming state.
- ``label`` (Name):  [Read-Only] Actor's label.
- ``name`` (Name):  [Read-Only] Internal name of the actor.
- ``native_class`` (type(Class)):  [Read-Only] Actor first native class.
- ``runtime_grid`` (Name):  [Read-Only] Actor's target runtime grid.

<a id="unreal.ActorDesc.__init__"></a>

#### __init__

```python
def __init__(guid: Guid = [],
             native_class: Class = None,
             class_: SoftObjectPath = [""],
             name: Name = "None",
             label: Name = "None",
             bounds: Box = [[0.000000, 0.000000, 0.000000],
                            [0.000000, 0.000000, 0.000000], False],
             runtime_grid: Name = "None",
             is_spatially_loaded: bool = False,
             actor_is_editor_only: bool = False,
             actor_package: Name = "None",
             actor_path: Name = "None",
             data_layer_assets: Array[SoftObjectPath] = []) -> None
```

<a id="unreal.ActorDesc.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Only] The actor GUID of this descriptor.

<a id="unreal.ActorDesc.native_class"></a>

#### native_class

```python
@property
def native_class() -> Class
```

(type(Class)):  [Read-Only] Actor first native class.

<a id="unreal.ActorDesc.class_"></a>

#### class_

```python
@property
def class_() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only] Actor class, can point to a native or Blueprint class and may be redirected.

<a id="unreal.ActorDesc.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] Internal name of the actor.

<a id="unreal.ActorDesc.label"></a>

#### label

```python
@property
def label() -> Name
```

(Name):  [Read-Only] Actor's label.

<a id="unreal.ActorDesc.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Only] Streaming bounds of this actor.

<a id="unreal.ActorDesc.runtime_grid"></a>

#### runtime_grid

```python
@property
def runtime_grid() -> Name
```

(Name):  [Read-Only] Actor's target runtime grid.

<a id="unreal.ActorDesc.is_spatially_loaded"></a>

#### is_spatially_loaded

```python
@property
def is_spatially_loaded() -> bool
```

(bool):  [Read-Only] Actor's streaming state.

<a id="unreal.ActorDesc.actor_is_editor_only"></a>

#### actor_is_editor_only

```python
@property
def actor_is_editor_only() -> bool
```

(bool):  [Read-Only] Actor's editor-only property.

<a id="unreal.ActorDesc.actor_package"></a>

#### actor_package

```python
@property
def actor_package() -> Name
```

(Name):  [Read-Only] Actor's package name.

<a id="unreal.ActorDesc.actor_path"></a>

#### actor_path

```python
@property
def actor_path() -> Name
```

(Name):  [Read-Only] Actor's path name.

<a id="unreal.ActorDesc.data_layer_assets"></a>

#### data_layer_assets

```python
@property
def data_layer_assets() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Only] Actor's data layer assets.

<a id="unreal.WorldPartitionHLODDestructionTag"></a>