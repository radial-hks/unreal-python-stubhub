## MaxConcurrentResolutionRule Objects

```python
class MaxConcurrentResolutionRule(EnumBase)
```

EMax Concurrent Resolution Rule

**C++ Source:**

- **Module**: Engine
- **File**: SoundConcurrency.h

<a id="unreal.MaxConcurrentResolutionRule.PREVENT_NEW"></a>

#### PREVENT\_NEW

0: When Max Concurrent sounds are active do not start a new sound.

<a id="unreal.MaxConcurrentResolutionRule.STOP_OLDEST"></a>

#### STOP\_OLDEST

1: When Max Concurrent sounds are active stop the oldest and start a new one.

<a id="unreal.MaxConcurrentResolutionRule.STOP_FARTHEST_THEN_PREVENT_NEW"></a>

#### STOP\_FARTHEST\_THEN\_PREVENT\_NEW

2: When Max Concurrent sounds are active stop the furthest sound.  If all sounds are the same distance then do not start a new sound.

<a id="unreal.MaxConcurrentResolutionRule.STOP_FARTHEST_THEN_OLDEST"></a>

#### STOP\_FARTHEST\_THEN\_OLDEST

3: When Max Concurrent sounds are active stop the furthest sound.  If all sounds are the same distance then stop the oldest.

<a id="unreal.MaxConcurrentResolutionRule.STOP_LOWEST_PRIORITY"></a>

#### STOP\_LOWEST\_PRIORITY

4: Stop the lowest priority sound in the group. If all sounds are the same priority, then it will stop the oldest sound in the group.

<a id="unreal.MaxConcurrentResolutionRule.STOP_QUIETEST"></a>

#### STOP\_QUIETEST

5: Stop the sound that is quietest in the group.

<a id="unreal.MaxConcurrentResolutionRule.STOP_LOWEST_PRIORITY_THEN_PREVENT_NEW"></a>

#### STOP\_LOWEST\_PRIORITY\_THEN\_PREVENT\_NEW

6: Stop the lowest priority sound in the group. If all sounds are the same priority, then it won't play a new sound.

<a id="unreal.ConcurrencyVolumeScaleMode"></a>