## LiveLinkTimecodeProviderEvaluationType Objects

```python
class LiveLinkTimecodeProviderEvaluationType(EnumBase)
```

ELive Link Timecode Provider Evaluation Type

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkTimecodeProvider.h

<a id="unreal.LiveLinkTimecodeProviderEvaluationType.LERP"></a>

#### LERP

0: Interpolate between, or extrapolate using the 2 frames that are the closest to the current world time.

<a id="unreal.LiveLinkTimecodeProviderEvaluationType.NEAREST"></a>

#### NEAREST

1: Use the frame that is closest to the current world time.

<a id="unreal.LiveLinkTimecodeProviderEvaluationType.LATEST"></a>

#### LATEST

2: Use the newest frame that was received.

<a id="unreal.LiveLinkAxis"></a>