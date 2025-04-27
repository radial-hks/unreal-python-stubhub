## ActorSoundParameterInterface Objects

```python
class ActorSoundParameterInterface(Interface)
```

Actor Sound Parameter Interface

**C++ Source:**

- **Module**: Engine
- **File**: ActorSoundParameterInterface.h

<a id="unreal.ActorSoundParameterInterface.get_actor_sound_params"></a>

#### get_actor_sound_params

```python
def get_actor_sound_params() -> Array[AudioParameter]
```

x.get_actor_sound_params() -> Array[AudioParameter]
Overrides logic for gathering AudioParameters to set by default when an AudioComponent/ActiveSound plays with a given actor as its Owner.

Returns:
    Array[AudioParameter]: 

    params (Array[AudioParameter]):

<a id="unreal.SoundParameterControllerInterface"></a>