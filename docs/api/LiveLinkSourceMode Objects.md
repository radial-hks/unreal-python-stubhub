## LiveLinkSourceMode Objects

```python
class LiveLinkSourceMode(EnumBase)
```

ELive Link Source Mode

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkSourceSettings.h

<a id="unreal.LiveLinkSourceMode.LATEST"></a>

#### LATEST

0: The source will the latest frame available to evaluate its subjects.
This mode will not attempt any type of interpolation or time synchronization.

<a id="unreal.LiveLinkSourceMode.ENGINE_TIME"></a>

#### ENGINE_TIME

1: The source will use the engine's time to evaluate its subjects.
This mode is most useful when smooth animation is desired.

<a id="unreal.LiveLinkSourceMode.TIMECODE"></a>

#### TIMECODE

2: The source will use the engine's timecode to evaluate its subjects.
This mode is most useful when sources need to be synchronized with
multiple other external inputs
(such as video or other time synchronized sources).
Should not be used when the engine isn't setup with a Timecode provider.

<a id="unreal.MVVMBlueprintPinStatus"></a>