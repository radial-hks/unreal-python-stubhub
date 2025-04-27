## ViewTargetBlendFunction Objects

```python
class ViewTargetBlendFunction(EnumBase)
```

Options that define how to blend when changing view targets.
see: FViewTargetTransitionParams, SetViewTarget

**C++ Source:**

- **Module**: Engine
- **File**: PlayerCameraManager.h

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_LINEAR"></a>

#### VT_BLEND_LINEAR

0: Camera does a simple linear interpolation.

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_CUBIC"></a>

#### VT_BLEND_CUBIC

1: Camera has a slight ease in and ease out, but amount of ease cannot be tweaked.

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_EASE_IN"></a>

#### VT_BLEND_EASE_IN

2: Camera immediately accelerates, but smoothly decelerates into the target.  Ease amount controlled by BlendExp.

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_EASE_OUT"></a>

#### VT_BLEND_EASE_OUT

3: Camera smoothly accelerates, but does not decelerate into the target.  Ease amount controlled by BlendExp.

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_EASE_IN_OUT"></a>

#### VT_BLEND_EASE_IN_OUT

4: Camera smoothly accelerates and decelerates.  Ease amount controlled by BlendExp.

<a id="unreal.ViewTargetBlendFunction.VT_BLEND_PRE_BLENDED"></a>

#### VT_BLEND_PRE_BLENDED

5: The game's camera system has already performed the blending. Engine should not blend at all

<a id="unreal.SoundSpatializationAlgorithm"></a>