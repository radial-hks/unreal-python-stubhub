## PCGGetDataFromActorMode Objects

```python
class PCGGetDataFromActorMode(EnumBase)
```

EPCGGet Data from Actor Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDataFromActor.h

<a id="unreal.PCGGetDataFromActorMode.PARSE_ACTOR_COMPONENTS"></a>

#### PARSE_ACTOR_COMPONENTS

0: Parse the found actor(s) for relevant components such as Primitives, Splines, and Volumes.

<a id="unreal.PCGGetDataFromActorMode.GET_SINGLE_POINT"></a>

#### GET_SINGLE_POINT

1: Produces a single point per actor with the actor transform and bounds.

<a id="unreal.PCGGetDataFromActorMode.GET_DATA_FROM_PROPERTY"></a>

#### GET_DATA_FROM_PROPERTY

2: Gets a data collection from an actor property.

<a id="unreal.PCGGetDataFromActorMode.GET_DATA_FROM_PCG_COMPONENT"></a>

#### GET_DATA_FROM_PCG_COMPONENT

3: Copy generated output from other PCG components on the found actor(s).

<a id="unreal.PCGGetDataFromActorMode.GET_DATA_FROM_PCG_COMPONENT_OR_PARSE_COMPONENTS"></a>

#### GET_DATA_FROM_PCG_COMPONENT_OR_PARSE_COMPONENTS

4: Attempts to copy generated output from other PCG components on the found actor(s), otherwise, falls back to parsing actor components.

<a id="unreal.PCGGetDataFromActorMode.GET_ACTOR_REFERENCE"></a>

#### GET_ACTOR_REFERENCE

5: Produces one entry per actor with only the actor reference.

<a id="unreal.PCGGetDataFromActorMode.GET_COMPONENTS_REFERENCE"></a>

#### GET_COMPONENTS_REFERENCE

6: Produces one entry per component within the actor selection.

<a id="unreal.PCGDifferenceMode"></a>