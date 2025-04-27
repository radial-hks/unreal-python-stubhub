## AnimationModifier Objects

```python
class AnimationModifier(Object)
```

Animation Modifier

**C++ Source:**

- **Module**: AnimationModifiers
- **File**: AnimationModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.

<a id="unreal.AnimationModifier.on_revert"></a>

#### on_revert

```python
def on_revert(animation_sequence: AnimSequence) -> None
```

x.on_revert(animation_sequence) -> None
On Revert

Args:
    animation_sequence (AnimSequence):

<a id="unreal.AnimationModifier.on_apply"></a>

#### on_apply

```python
def on_apply(animation_sequence: AnimSequence) -> None
```

x.on_apply(animation_sequence) -> None
Executed when the Animation is initialized (native event for debugging / testing purposes)

Args:
    animation_sequence (AnimSequence):

<a id="unreal.MovieSceneSpawnableChaosCacheBinding"></a>