## SharedMemoryMediaSourceMode Objects

```python
class SharedMemoryMediaSourceMode(EnumBase)
```

Mode of operation when receiving data.
Framelocked - Matches source and local frame numbers. Always use this mode in nDisplay.
Genlocked - It doesn't match frame numbers, but it also doesn't skip frames, so will hold back the sender if it is faster than the receiver.
Freerun - It always grabs the latest frame. It may skip frames if they arrive too fast.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: SharedMemoryMedia
- **File**: SharedMemoryMediaSource.h

<a id="unreal.SharedMemoryMediaSourceMode.FRAMELOCKED"></a>

#### FRAMELOCKED

0

<a id="unreal.SharedMemoryMediaSourceMode.GENLOCKED"></a>

#### GENLOCKED

1: Matches source and local frame numbers. Always use this mode in nDisplay.

<a id="unreal.SharedMemoryMediaSourceMode.FREERUN"></a>

#### FREERUN

2: It doesn't match frame numbers, but it also doesn't skip frames, so will hold back the sender if it is faster than the receiver.

<a id="unreal.DisplayClusterConfigurationMediaSplitType"></a>