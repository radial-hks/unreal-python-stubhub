## PCGActorFilter Objects

```python
class PCGActorFilter(EnumBase)
```

EPCGActor Filter

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGActorSelector.h

<a id="unreal.PCGActorFilter.SELF"></a>

#### SELF

0: This actor (either the original PCG actor or the partition actor if partitioning is enabled).

<a id="unreal.PCGActorFilter.PARENT"></a>

#### PARENT

1: The parent of this actor in the hierarchy.

<a id="unreal.PCGActorFilter.ROOT"></a>

#### ROOT

2: The top most parent of this actor in the hierarchy.

<a id="unreal.PCGActorFilter.ALL_WORLD_ACTORS"></a>

#### ALL_WORLD_ACTORS

3: All actors in world.

<a id="unreal.PCGActorFilter.ORIGINAL"></a>

#### ORIGINAL

4: The source PCG actor (rather than the generated partition actor).

<a id="unreal.PCGActorFilter.FROM_INPUT"></a>

#### FROM_INPUT

5: Consider only the provided list of actors

<a id="unreal.PCGActorSelection"></a>