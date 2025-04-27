## FCTweenBPActionFloat Objects

```python
class FCTweenBPActionFloat(FCTweenBPAction)
```

FCTween BPAction Float

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBPActionFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_easing`` (TweenUpdateFloatOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame
- ``on_complete`` (TweenEventOutputPin):  [Read-Write]
- ``on_loop`` (TweenEventOutputPin):  [Read-Write]
- ``on_yoyo`` (TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPActionFloat.apply_easing"></a>

#### apply_easing

```python
@property
def apply_easing() -> TweenUpdateFloatOutputPin
```

(TweenUpdateFloatOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame

<a id="unreal.FCTweenBPActionFloat.apply_easing"></a>

#### apply_easing

```python
@apply_easing.setter
def apply_easing(value: TweenUpdateFloatOutputPin) -> None
```

<a id="unreal.FCTweenBPActionQuat"></a>