## MetaSoundCacheSubsystem Objects

```python
class MetaSoundCacheSubsystem(AudioEngineSubsystem)
```

UMetaSoundCacheSubsystem

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundOperatorCacheSubsystem.h

<a id="unreal.MetaSoundCacheSubsystem.touch_or_precache_meta_sound"></a>

#### touch_or_precache_meta_sound

```python
def touch_or_precache_meta_sound(meta_sound: MetaSoundSource,
                                 num_instances: int = 1) -> None
```

x.touch_or_precache_meta_sound(meta_sound, num_instances=1) -> None
same as PrecacheMetaSound except cached operator that already exists in the cache will be moved to the top instead of building,
      any operators that we couldn't move to the top, will be built.
      (i.e. if 2 operators are already cached and Num Instances is 4, it will construct 2 and move the existing 2 to the top of the cache)

Args:
    meta_sound (MetaSoundSource): 
    num_instances (int32):

<a id="unreal.MetaSoundCacheSubsystem.remove_cached_operators_for_meta_sound"></a>

#### remove_cached_operators_for_meta_sound

```python
def remove_cached_operators_for_meta_sound(
        meta_sound: MetaSoundSource) -> None
```

x.remove_cached_operators_for_meta_sound(meta_sound) -> None
Clear the operator pool of any operators associated with the given MetaSound

Args:
    meta_sound (MetaSoundSource):

<a id="unreal.MetaSoundCacheSubsystem.precache_meta_sound"></a>

#### precache_meta_sound

```python
def precache_meta_sound(meta_sound: MetaSoundSource,
                        num_instances: int = 1) -> None
```

x.precache_meta_sound(meta_sound, num_instances=1) -> None
Builds the requested number of MetaSound operators (asynchronously) and puts them in the pool for playback.
      (If these operators are not yet available when the MetaSound attempts to play, one will be created Independent of this request.)

Args:
    meta_sound (MetaSoundSource): 
    num_instances (int32):

<a id="unreal.MetasoundOutputBlueprintAccess"></a>