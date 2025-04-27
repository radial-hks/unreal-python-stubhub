## FCTweenBPActionRotator Objects

```python
class FCTweenBPActionRotator(FCTweenBPAction)
```

FCTween BPAction Rotator

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBPActionRotator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_easing`` (TweenUpdateRotatorOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame
- ``on_complete`` (TweenEventOutputPin):  [Read-Write]
- ``on_loop`` (TweenEventOutputPin):  [Read-Write]
- ``on_yoyo`` (TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPActionRotator.apply_easing"></a>

#### apply_easing

```python
@property
def apply_easing() -> TweenUpdateRotatorOutputPin
```

(TweenUpdateRotatorOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame

<a id="unreal.FCTweenBPActionRotator.apply_easing"></a>

#### apply_easing

```python
@apply_easing.setter
def apply_easing(value: TweenUpdateRotatorOutputPin) -> None
```

<a id="unreal.FCTweenBPActionVector"></a>