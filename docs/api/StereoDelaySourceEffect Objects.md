## StereoDelaySourceEffect Objects

```python
class StereoDelaySourceEffect(EnumBase)
```

EStereo Delay Source Effect

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectStereoDelay.h

<a id="unreal.StereoDelaySourceEffect.NORMAL"></a>

#### NORMAL

0: Left input mixes with left delay line output and feeds to left output.
Right input mixes with right delay line output and feeds to right output.

<a id="unreal.StereoDelaySourceEffect.CROSS"></a>

#### CROSS

1: Left input mixes right delay line output and feeds to right output.
Right input mixes with left delay line output and feeds to left output.

<a id="unreal.StereoDelaySourceEffect.PING_PONG"></a>

#### PING_PONG

2: Left input mixes with left delay line output and feeds to right output.
Right input mixes with right delay line output and feeds to left output.

<a id="unreal.StereoDelayFiltertype"></a>