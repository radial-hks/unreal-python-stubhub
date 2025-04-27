## AnimationSharingScalability Objects

```python
class AnimationSharingScalability(StructBase)
```

Animation Sharing Scalability

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_significance_value`` (PerPlatformFloat):  [Read-Write] Significance value tied to whether or not a transition should be blended
- ``maximum_number_concurrent_blends`` (PerPlatformInt):  [Read-Write] Maximum number of blends which can be running concurrently
- ``tick_significance_value`` (PerPlatformFloat):  [Read-Write] Significance value tied to whether or not the leader pose components should be ticking
- ``use_blend_transitions`` (PerPlatformBool):  [Read-Write] Flag whether or not to use blend transitions between states

<a id="unreal.AnimationSharingScalability.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneNiagaraCacheParams"></a>