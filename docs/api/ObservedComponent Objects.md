## ObservedComponent Objects

```python
class ObservedComponent(StructBase)
```

Observed Component

**C++ Source:**

- **Plugin**: ChaosCaching
- **Module**: ChaosCaching
- **File**: CacheManagerActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_name`` (Name):  [Read-Write] Unique name for the cache, used as a key into the cache collection
- ``is_simulating`` (bool):  [Read-Write] Capture of the initial state of the component before cache manager takes control.
- ``playback_enabled`` (bool):  [Read-Write] Whether this component is enabled for playback, this allow a cache to hold many component but only replay some of them.
- ``soft_component_ref`` (SoftComponentReference):  [Read-Write] The component observed by this object for either playback or recording
- ``usd_cache_directory`` (DirectoryPath):  [Read-Write] USD cache directory, if supported for this simulated structure type.

<a id="unreal.ObservedComponent.__init__"></a>

#### __init__

```python
def __init__(cache_name: Name = "None",
             soft_component_ref: SoftComponentReference = [None, "None"],
             is_simulating: bool = False,
             playback_enabled: bool = False,
             usd_cache_directory: DirectoryPath = [""]) -> None
```

<a id="unreal.ObservedComponent.cache_name"></a>

#### cache_name

```python
@property
def cache_name() -> Name
```

(Name):  [Read-Write] Unique name for the cache, used as a key into the cache collection

<a id="unreal.ObservedComponent.cache_name"></a>

#### cache_name

```python
@cache_name.setter
def cache_name(value: Name) -> None
```

<a id="unreal.ObservedComponent.soft_component_ref"></a>

#### soft_component_ref

```python
@property
def soft_component_ref() -> SoftComponentReference
```

(SoftComponentReference):  [Read-Write] The component observed by this object for either playback or recording

<a id="unreal.ObservedComponent.soft_component_ref"></a>

#### soft_component_ref

```python
@soft_component_ref.setter
def soft_component_ref(value: SoftComponentReference) -> None
```

<a id="unreal.ObservedComponent.is_simulating"></a>

#### is_simulating

```python
@property
def is_simulating() -> bool
```

(bool):  [Read-Only] Capture of the initial state of the component before cache manager takes control.

<a id="unreal.ObservedComponent.playback_enabled"></a>

#### playback_enabled

```python
@property
def playback_enabled() -> bool
```

(bool):  [Read-Write] Whether this component is enabled for playback, this allow a cache to hold many component but only replay some of them.

<a id="unreal.ObservedComponent.playback_enabled"></a>

#### playback_enabled

```python
@playback_enabled.setter
def playback_enabled(value: bool) -> None
```

<a id="unreal.ObservedComponent.usd_cache_directory"></a>

#### usd_cache_directory

```python
@property
def usd_cache_directory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] USD cache directory, if supported for this simulated structure type.

<a id="unreal.ObservedComponent.usd_cache_directory"></a>

#### usd_cache_directory

```python
@usd_cache_directory.setter
def usd_cache_directory(value: DirectoryPath) -> None
```

<a id="unreal.RCNetworkAddress"></a>