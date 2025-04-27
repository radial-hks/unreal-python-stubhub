## GeometryCacheStreamerSettings Objects

```python
class GeometryCacheStreamerSettings(DeveloperSettings)
```

Settings for the GeometryCache streamer

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCacheStreamer
- **File**: GeometryCacheStreamerSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``look_ahead_buffer`` (float):  [Read-Write] The amount of animation (in seconds) to stream ahead of time (per stream)
- ``max_memory_allowed`` (float):  [Read-Write] The maximum total amount of streamed data allowed in memory (for all streams)

<a id="unreal.GeometryCacheStreamerSettings.look_ahead_buffer"></a>

#### look_ahead_buffer

```python
@property
def look_ahead_buffer() -> float
```

(float):  [Read-Write] The amount of animation (in seconds) to stream ahead of time (per stream)

<a id="unreal.GeometryCacheStreamerSettings.look_ahead_buffer"></a>

#### look_ahead_buffer

```python
@look_ahead_buffer.setter
def look_ahead_buffer(value: float) -> None
```

<a id="unreal.GeometryCacheStreamerSettings.max_memory_allowed"></a>

#### max_memory_allowed

```python
@property
def max_memory_allowed() -> float
```

(float):  [Read-Write] The maximum total amount of streamed data allowed in memory (for all streams)

<a id="unreal.GeometryCacheStreamerSettings.max_memory_allowed"></a>

#### max_memory_allowed

```python
@max_memory_allowed.setter
def max_memory_allowed(value: float) -> None
```

<a id="unreal.GeographicCoordinatesFunctionLibrary"></a>