## EnvQueryGenerator_BlueprintBase Objects

```python
class EnvQueryGenerator_BlueprintBase(EnvQueryGenerator)
```

Env Query Generator Blueprint Base

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryGenerator_BlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_sort_tests`` (bool):  [Read-Write] if set, tests will be automatically sorted for best performance before running query
- ``can_run_async`` (bool):  [Read-Write] To be overwritten by MassEnvQueryGenerators to indicate that they will run asynchronously.
- ``context`` (type(Class)):  [Read-Write] context
- ``generated_item_type`` (type(Class)):  [Read-Write]
  todo: this should show up only in the generator's BP, but due to the way EQS editor is generating widgets it's there as well It's a bug and we'll fix it
- ``generators_action_description`` (Text):  [Read-Write] A short description of what test does, like "Generate pawn named Joe"
- ``option_name`` (str):  [Read-Write]

<a id="unreal.EnvQueryGenerator_BlueprintBase.get_querier"></a>

#### get_querier

```python
def get_querier() -> Object
```

x.get_querier() -> Object
Get Querier

Returns:
    Object:

<a id="unreal.EnvQueryGenerator_BlueprintBase.do_item_generation_from_actors"></a>

#### do_item_generation_from_actors

```python
def do_item_generation_from_actors(context_actors: Array[Actor]) -> None
```

x.do_item_generation_from_actors(context_actors) -> None
Do Item Generation from Actors

Args:
    context_actors (Array[Actor]):

<a id="unreal.EnvQueryGenerator_BlueprintBase.do_item_generation"></a>

#### do_item_generation

```python
def do_item_generation(context_locations: Array[Vector]) -> None
```

x.do_item_generation(context_locations) -> None
Do Item Generation

Args:
    context_locations (Array[Vector]):

<a id="unreal.EnvQueryGenerator_BlueprintBase.add_generated_vector"></a>

#### add_generated_vector

```python
def add_generated_vector(generated_vector: Vector) -> None
```

x.add_generated_vector(generated_vector) -> None
Add Generated Vector

Args:
    generated_vector (Vector):

<a id="unreal.EnvQueryGenerator_BlueprintBase.add_generated_actor"></a>

#### add_generated_actor

```python
def add_generated_actor(generated_actor: Actor) -> None
```

x.add_generated_actor(generated_actor) -> None
Add Generated Actor

Args:
    generated_actor (Actor):

<a id="unreal.GridPathAIController"></a>