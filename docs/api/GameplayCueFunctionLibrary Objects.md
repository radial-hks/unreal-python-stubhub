## GameplayCueFunctionLibrary Objects

```python
class GameplayCueFunctionLibrary(BlueprintFunctionLibrary)
```

UGameplayCueFunctionLibrary

    Helpful utility function for working with gameplay cues.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueFunctionLibrary.h

<a id="unreal.GameplayCueFunctionLibrary.remove_gameplay_cue_on_actor"></a>

#### remove\_gameplay\_cue\_on\_actor

```python
@classmethod
def remove_gameplay_cue_on_actor(cls, target: Actor,
                                 gameplay_cue_tag: GameplayTag,
                                 parameters: GameplayCueParameters) -> None
```

X.remove_gameplay_cue_on_actor(target, gameplay_cue_tag, parameters) -> None
Invoke the removed event for a gameplay cue on the target actor. This should be paired with an AddGameplayCueOnActor call.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

Args:
    target (Actor): 
    gameplay_cue_tag (GameplayTag): 
    parameters (GameplayCueParameters):

<a id="unreal.GameplayCueFunctionLibrary.make_gameplay_cue_parameters_from_hit_result"></a>

#### make\_gameplay\_cue\_parameters\_from\_hit\_result

```python
@classmethod
def make_gameplay_cue_parameters_from_hit_result(
        cls, hit_result: HitResult) -> GameplayCueParameters
```

X.make_gameplay_cue_parameters_from_hit_result(hit_result) -> GameplayCueParameters
Builds gameplay cue parameters using data from a hit result.

Args:
    hit_result (HitResult): 

Returns:
    GameplayCueParameters:

<a id="unreal.GameplayCueFunctionLibrary.execute_gameplay_cue_on_actor"></a>

#### execute\_gameplay\_cue\_on\_actor

```python
@classmethod
def execute_gameplay_cue_on_actor(cls, target: Actor,
                                  gameplay_cue_tag: GameplayTag,
                                  parameters: GameplayCueParameters) -> None
```

X.execute_gameplay_cue_on_actor(target, gameplay_cue_tag, parameters) -> None
Invoke a one time "instant" execute event for a gameplay cue on the target actor.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

Args:
    target (Actor): 
    gameplay_cue_tag (GameplayTag): 
    parameters (GameplayCueParameters):

<a id="unreal.GameplayCueFunctionLibrary.add_gameplay_cue_on_actor"></a>

#### add\_gameplay\_cue\_on\_actor

```python
@classmethod
def add_gameplay_cue_on_actor(cls, target: Actor,
                              gameplay_cue_tag: GameplayTag,
                              parameters: GameplayCueParameters) -> None
```

X.add_gameplay_cue_on_actor(target, gameplay_cue_tag, parameters) -> None
Invoke the added event for a gameplay cue on the target actor. This should be paired with a RemoveGameplayCueOnActor call.
* If the actor has an ability system, the event will fire on authority only and will be replicated.
* If the actor does not have an ability system, the event will only be fired locally.

Args:
    target (Actor): 
    gameplay_cue_tag (GameplayTag): 
    parameters (GameplayCueParameters):

<a id="unreal.GameplayCueInterface"></a>