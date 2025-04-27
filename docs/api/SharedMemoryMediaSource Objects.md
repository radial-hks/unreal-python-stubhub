## SharedMemoryMediaSource Objects

```python
class SharedMemoryMediaSource(MediaSource)
```

Media source for SharedMemory streams.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: SharedMemoryMedia
- **File**: SharedMemoryMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mode`` (SharedMemoryMediaSourceMode):  [Read-Write] Mode of operation when receiving data.
  Framelocked - Matches source and local frame numbers. Always use this mode in nDisplay.
  Genlocked - It doesn't match frame numbers, but it also doesn't skip frames, so will hold back the sender if it is faster than the receiver.
  Freerun - It always grabs the latest frame. It may skip frames if they arrive too fast.
- ``unique_name`` (str):  [Read-Write] Shared memory will be found by using this name. Should match the media output setting.
- ``zero_latency`` (bool):  [Read-Write] Zero latency option to wait for the cross gpu texture rendered on the same frame. May adversely affect fps. Only applicable in Framelocked mode.

<a id="unreal.SharedMemoryMediaSource.unique_name"></a>

#### unique_name

```python
@property
def unique_name() -> str
```

(str):  [Read-Write] Shared memory will be found by using this name. Should match the media output setting.

<a id="unreal.SharedMemoryMediaSource.unique_name"></a>

#### unique_name

```python
@unique_name.setter
def unique_name(value: str) -> None
```

<a id="unreal.SharedMemoryMediaSource.mode"></a>

#### mode

```python
@property
def mode() -> SharedMemoryMediaSourceMode
```

(SharedMemoryMediaSourceMode):  [Read-Write] Mode of operation when receiving data.
Framelocked - Matches source and local frame numbers. Always use this mode in nDisplay.
Genlocked - It doesn't match frame numbers, but it also doesn't skip frames, so will hold back the sender if it is faster than the receiver.
Freerun - It always grabs the latest frame. It may skip frames if they arrive too fast.

<a id="unreal.SharedMemoryMediaSource.mode"></a>

#### mode

```python
@mode.setter
def mode(value: SharedMemoryMediaSourceMode) -> None
```

<a id="unreal.SharedMemoryMediaSource.zero_latency"></a>

#### zero_latency

```python
@property
def zero_latency() -> bool
```

(bool):  [Read-Write] Zero latency option to wait for the cross gpu texture rendered on the same frame. May adversely affect fps. Only applicable in Framelocked mode.

<a id="unreal.SharedMemoryMediaSource.zero_latency"></a>

#### zero_latency

```python
@zero_latency.setter
def zero_latency(value: bool) -> None
```

<a id="unreal.LayersBlueprintLibrary"></a>