## FCTweenBPActionVector Objects

```python
class FCTweenBPActionVector(FCTweenBPAction)
```

FCTween BPAction Vector

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBPActionVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_easing`` (TweenUpdateVectorOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame
- ``on_complete`` (TweenEventOutputPin):  [Read-Write]
- ``on_loop`` (TweenEventOutputPin):  [Read-Write]
- ``on_yoyo`` (TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPActionVector.apply_easing"></a>

#### apply_easing

```python
@property
def apply_easing() -> TweenUpdateVectorOutputPin
```

(TweenUpdateVectorOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame

<a id="unreal.FCTweenBPActionVector.apply_easing"></a>

#### apply_easing

```python
@apply_easing.setter
def apply_easing(value: TweenUpdateVectorOutputPin) -> None
```

<a id="unreal.FCTweenBPActionVector2D"></a>