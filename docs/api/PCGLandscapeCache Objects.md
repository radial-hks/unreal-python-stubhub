## PCGLandscapeCache Objects

```python
class PCGLandscapeCache(Object)
```

PCGLandscape Cache

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLandscapeCache.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_entry_count`` (int32):  [Read-Only]
- ``cached_layer_names`` (Set[Name]):  [Read-Only] TODO: separate by landscape
- ``cooked_serialized_contents`` (PCGLandscapeCacheSerializationContents):  [Read-Write]
- ``serialization_mode`` (PCGLandscapeCacheSerializationMode):  [Read-Write]

<a id="unreal.PCGLandscapeCache.serialization_mode"></a>

#### serialization_mode

```python
@property
def serialization_mode() -> PCGLandscapeCacheSerializationMode
```

(PCGLandscapeCacheSerializationMode):  [Read-Write]

<a id="unreal.PCGLandscapeCache.serialization_mode"></a>

#### serialization_mode

```python
@serialization_mode.setter
def serialization_mode(value: PCGLandscapeCacheSerializationMode) -> None
```

<a id="unreal.PCGLandscapeCache.cooked_serialized_contents"></a>

#### cooked_serialized_contents

```python
@property
def cooked_serialized_contents() -> PCGLandscapeCacheSerializationContents
```

(PCGLandscapeCacheSerializationContents):  [Read-Write]

<a id="unreal.PCGLandscapeCache.cooked_serialized_contents"></a>

#### cooked_serialized_contents

```python
@cooked_serialized_contents.setter
def cooked_serialized_contents(
        value: PCGLandscapeCacheSerializationContents) -> None
```

<a id="unreal.PCGLandscapeCache.cache_entry_count"></a>

#### cache_entry_count

```python
@property
def cache_entry_count() -> int
```

(int32):  [Read-Only]

<a id="unreal.PCGPartitionActor"></a>