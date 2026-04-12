## ActorPerceptionBlueprintInfo Objects

```python
class ActorPerceptionBlueprintInfo(StructBase)
```

Actor Perception Blueprint Info

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_friendly`` (bool):  [Read-Write]
- ``is_hostile`` (bool):  [Read-Write]
- ``last_sensed_stimuli`` (Array[AIStimulus]):  [Read-Write]
- ``target`` (Actor):  [Read-Write]

<a id="unreal.ActorPerceptionBlueprintInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(target: Actor = None,
             last_sensed_stimuli: Array[AIStimulus] = [],
             is_hostile: bool = False,
             is_friendly: bool = False) -> None
```

<a id="unreal.ActorPerceptionBlueprintInfo.target"></a>

#### target

```python
@property
def target() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.ActorPerceptionBlueprintInfo.target"></a>

#### target

```python
@target.setter
def target(value: Actor) -> None
```

<a id="unreal.ActorPerceptionBlueprintInfo.last_sensed_stimuli"></a>

#### last\_sensed\_stimuli

```python
@property
def last_sensed_stimuli() -> Array[AIStimulus]
```

(Array[AIStimulus]):  [Read-Write]

<a id="unreal.ActorPerceptionBlueprintInfo.last_sensed_stimuli"></a>

#### last\_sensed\_stimuli

```python
@last_sensed_stimuli.setter
def last_sensed_stimuli(value: Array[AIStimulus]) -> None
```

<a id="unreal.ActorPerceptionBlueprintInfo.is_hostile"></a>

#### is\_hostile

```python
@property
def is_hostile() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ActorPerceptionBlueprintInfo.is_hostile"></a>

#### is\_hostile

```python
@is_hostile.setter
def is_hostile(value: bool) -> None
```

<a id="unreal.ActorPerceptionBlueprintInfo.is_friendly"></a>

#### is\_friendly

```python
@property
def is_friendly() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ActorPerceptionBlueprintInfo.is_friendly"></a>

#### is\_friendly

```python
@is_friendly.setter
def is_friendly(value: bool) -> None
```

<a id="unreal.AISenseAffiliationFilter"></a>