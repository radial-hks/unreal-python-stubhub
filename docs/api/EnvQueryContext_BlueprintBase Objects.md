## EnvQueryContext_BlueprintBase Objects

```python
class EnvQueryContext_BlueprintBase(EnvQueryContext)
```

Env Query Context Blueprint Base

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryContext_BlueprintBase.h

<a id="unreal.EnvQueryContext_BlueprintBase.provide_single_location"></a>

#### provide_single_location

```python
def provide_single_location(querier_object: Object,
                            querier_actor: Actor) -> Vector
```

x.provide_single_location(querier_object, querier_actor) -> Vector
Provide Single Location

Args:
    querier_object (Object): 
    querier_actor (Actor): 

Returns:
    Vector: 

    resulting_location (Vector):

<a id="unreal.EnvQueryContext_BlueprintBase.provide_single_actor"></a>

#### provide_single_actor

```python
def provide_single_actor(querier_object: Object,
                         querier_actor: Actor) -> Actor
```

x.provide_single_actor(querier_object, querier_actor) -> Actor
Provide Single Actor

Args:
    querier_object (Object): 
    querier_actor (Actor): 

Returns:
    Actor: 

    resulting_actor (Actor):

<a id="unreal.EnvQueryContext_BlueprintBase.provide_locations_set"></a>

#### provide_locations_set

```python
def provide_locations_set(querier_object: Object,
                          querier_actor: Actor) -> Array[Vector]
```

x.provide_locations_set(querier_object, querier_actor) -> Array[Vector]
Provide Locations Set

Args:
    querier_object (Object): 
    querier_actor (Actor): 

Returns:
    Array[Vector]: 

    resulting_location_set (Array[Vector]):

<a id="unreal.EnvQueryContext_BlueprintBase.provide_actors_set"></a>

#### provide_actors_set

```python
def provide_actors_set(querier_object: Object,
                       querier_actor: Actor) -> Array[Actor]
```

x.provide_actors_set(querier_object, querier_actor) -> Array[Actor]
Provide Actors Set

Args:
    querier_object (Object): 
    querier_actor (Actor): 

Returns:
    Array[Actor]: 

    resulting_actors_set (Array[Actor]):

<a id="unreal.EnvQuery"></a>