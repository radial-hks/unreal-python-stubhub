## FCTweenBPActionVector2D Objects

```python
class FCTweenBPActionVector2D(FCTweenBPAction)
```

FCTween BPAction Vector 2D

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBPActionVector2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_easing`` (TweenUpdateVector2DOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame
- ``on_complete`` (TweenEventOutputPin):  [Read-Write]
- ``on_loop`` (TweenEventOutputPin):  [Read-Write]
- ``on_yoyo`` (TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPActionVector2D.apply_easing"></a>

#### apply_easing

```python
@property
def apply_easing() -> TweenUpdateVector2DOutputPin
```

(TweenUpdateVector2DOutputPin):  [Read-Write] Triggered every tween update. use "Value" to get the tweened float for this frame

<a id="unreal.FCTweenBPActionVector2D.apply_easing"></a>

#### apply_easing

```python
@apply_easing.setter
def apply_easing(value: TweenUpdateVector2DOutputPin) -> None
```

<a id="unreal.BaseComponent"></a>