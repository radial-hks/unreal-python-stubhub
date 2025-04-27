## TimecodeProviderSynchronizationState Objects

```python
class TimecodeProviderSynchronizationState(EnumBase)
```

Possible states of TimecodeProvider.

**C++ Source:**

- **Module**: Engine
- **File**: TimecodeProvider.h

<a id="unreal.TimecodeProviderSynchronizationState.CLOSED"></a>

#### CLOSED

0: TimecodeProvider has not been initialized or has been shutdown.

<a id="unreal.TimecodeProviderSynchronizationState.ERROR"></a>

#### ERROR

1: Unrecoverable error occurred during Synchronization.

<a id="unreal.TimecodeProviderSynchronizationState.SYNCHRONIZED"></a>

#### SYNCHRONIZED

2: TimecodeProvider is currently synchronized with the source.

<a id="unreal.TimecodeProviderSynchronizationState.SYNCHRONIZING"></a>

#### SYNCHRONIZING

3: TimecodeProvider is initialized and being prepared for synchronization.

<a id="unreal.MovieSceneBuiltInEasing"></a>