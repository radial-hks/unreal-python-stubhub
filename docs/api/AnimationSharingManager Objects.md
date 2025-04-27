## AnimationSharingManager Objects

```python
class AnimationSharingManager(Object)
```

Animation Sharing Manager

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``per_skeleton_data`` (Array[AnimSharingInstance]):  [Read-Only] Sharing data required for the unique Skeleton setups

<a id="unreal.AnimationSharingManager.register_actor_with_skeleton_bp"></a>

#### register_actor_with_skeleton_bp

```python
def register_actor_with_skeleton_bp(actor: Actor,
                                    sharing_skeleton: Skeleton) -> None
```

x.register_actor_with_skeleton_bp(actor, sharing_skeleton) -> None
Register an Actor with this Animation Sharing manager, according to the SharingSkeleton

Args:
    actor (Actor): 
    sharing_skeleton (Skeleton):

<a id="unreal.AnimationSharingManager.get_animation_sharing_manager"></a>

#### get_animation_sharing_manager

```python
@classmethod
def get_animation_sharing_manager(
        cls, world_context_object: Object) -> AnimationSharingManager
```

X.get_animation_sharing_manager(world_context_object) -> AnimationSharingManager
Returns the AnimationSharing Manager, nullptr if none was set up

Args:
    world_context_object (Object): 

Returns:
    AnimationSharingManager:

<a id="unreal.AnimationSharingManager.create_animation_sharing_manager"></a>

#### create_animation_sharing_manager

```python
@classmethod
def create_animation_sharing_manager(cls, world_context_object: Object,
                                     setup: AnimationSharingSetup) -> bool
```

X.create_animation_sharing_manager(world_context_object, setup) -> bool
Create an Animation Sharing Manager using the provided Setup

Args:
    world_context_object (Object): 
    setup (AnimationSharingSetup): 

Returns:
    bool:

<a id="unreal.AnimationSharingManager.animation_sharing_enabled"></a>

#### animation_sharing_enabled

```python
@classmethod
def animation_sharing_enabled(cls) -> bool
```

X.animation_sharing_enabled() -> bool
Returns whether or not the animation sharing is enabled

Returns:
    bool:

<a id="unreal.AnimationSharingSetup"></a>