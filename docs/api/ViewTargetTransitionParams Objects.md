## ViewTargetTransitionParams Objects

```python
class ViewTargetTransitionParams(StructBase)
```

A set of parameters to describe how to transition between view targets.

**C++ Source:**

- **Module**: Engine
- **File**: PlayerCameraManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_exp`` (float):  [Read-Write] Exponent, used by certain blend functions to control the shape of the curve.
- ``blend_function`` (ViewTargetBlendFunction):  [Read-Write] Function to apply to the blend parameter.
- ``blend_time`` (float):  [Read-Write] Total duration of blend to pending view target. 0 means no blending.
- ``lock_outgoing`` (bool):  [Read-Write] If true, lock outgoing viewtarget to last frame's camera POV for the remainder of the blend.
  This is useful if you plan to teleport the old viewtarget, but don't want to affect the blend.

<a id="unreal.ViewTargetTransitionParams.__init__"></a>

#### __init__

```python
def __init__(blend_time: float = 0.000000,
             blend_function: ViewTargetBlendFunction = ViewTargetBlendFunction.
             VT_BLEND_LINEAR,
             blend_exp: float = 0.000000,
             lock_outgoing: bool = False) -> None
```

<a id="unreal.ViewTargetTransitionParams.blend_time"></a>

#### blend_time

```python
@property
def blend_time() -> float
```

(float):  [Read-Write] Total duration of blend to pending view target. 0 means no blending.

<a id="unreal.ViewTargetTransitionParams.blend_time"></a>

#### blend_time

```python
@blend_time.setter
def blend_time(value: float) -> None
```

<a id="unreal.ViewTargetTransitionParams.blend_function"></a>

#### blend_function

```python
@property
def blend_function() -> ViewTargetBlendFunction
```

(ViewTargetBlendFunction):  [Read-Write] Function to apply to the blend parameter.

<a id="unreal.ViewTargetTransitionParams.blend_function"></a>

#### blend_function

```python
@blend_function.setter
def blend_function(value: ViewTargetBlendFunction) -> None
```

<a id="unreal.ViewTargetTransitionParams.blend_exp"></a>

#### blend_exp

```python
@property
def blend_exp() -> float
```

(float):  [Read-Write] Exponent, used by certain blend functions to control the shape of the curve.

<a id="unreal.ViewTargetTransitionParams.blend_exp"></a>

#### blend_exp

```python
@blend_exp.setter
def blend_exp(value: float) -> None
```

<a id="unreal.ViewTargetTransitionParams.lock_outgoing"></a>

#### lock_outgoing

```python
@property
def lock_outgoing() -> bool
```

(bool):  [Read-Write] If true, lock outgoing viewtarget to last frame's camera POV for the remainder of the blend.
This is useful if you plan to teleport the old viewtarget, but don't want to affect the blend.

<a id="unreal.ViewTargetTransitionParams.lock_outgoing"></a>

#### lock_outgoing

```python
@lock_outgoing.setter
def lock_outgoing(value: bool) -> None
```

<a id="unreal.ReverbSettings"></a>