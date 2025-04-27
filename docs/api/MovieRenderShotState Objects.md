## MovieRenderShotState Objects

```python
class MovieRenderShotState(EnumBase)
```

What is the current state of a shot? States are processed in order from first to last but not
all states are required, ie: WarmUp and MotionBlur can be disabled and the shot will never
pass through this state.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

<a id="unreal.MovieRenderShotState.UNINITIALIZED"></a>

#### UNINITIALIZED

0: The shot has not been initialized yet.

<a id="unreal.MovieRenderShotState.WARMING_UP"></a>

#### WARMING_UP

1: The shot is warming up. Engine ticks are passing but no frames are being produced.

<a id="unreal.MovieRenderShotState.MOTION_BLUR"></a>

#### MOTION_BLUR

2: * The shot is doing additional pre-roll for motion blur. No frames are being produced,
* but the rendering pipeline is being run to seed histories.

<a id="unreal.MovieRenderShotState.RENDERING"></a>

#### RENDERING

3: * The shot is working on producing frames and may be currently doing a sub-frame or
* a whole frame.

<a id="unreal.MovieRenderShotState.COOLING_DOWN"></a>

#### COOLING_DOWN

4: The shot is cooling down. Engine ticks are passing and frames are being rendered, but
not saved to disk. This is needed because temporal-based denoisers need to look at the
future (which would be after a shot) to finish the current frames of the shot.

<a id="unreal.MovieRenderShotState.FINISHED"></a>

#### FINISHED

5: * The shot has produced all frames it will produce. No more evaluation should be
* done for this shot once it reaches this state.

<a id="unreal.MoviePipelineShutterTiming"></a>