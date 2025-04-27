## ActorPerceptionUpdateInfo Objects

```python
class ActorPerceptionUpdateInfo(StructBase)
```

Actor Perception Update Info

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``stimulus`` (AIStimulus):  [Read-Write] Updated stimulus
- ``target`` (Actor):  [Read-Write] Actor associated to the stimulus (can be null)
- ``target_id`` (int32):  [Read-Write] Id of to the stimulus source

<a id="unreal.ActorPerceptionUpdateInfo.__init__"></a>

#### __init__

```python
def __init__(
    target_id: int = 0,
    target: Actor = None,
    stimulus: AIStimulus = [
        340282346638528859811704183484516925440.000000,
        340282346638528859811704183484516925440.000000, -1.000000,
        [
            340282346638528859811704183484516925440.000000,
            340282346638528859811704183484516925440.000000,
            340282346638528859811704183484516925440.000000
        ],
        [
            340282346638528859811704183484516925440.000000,
            340282346638528859811704183484516925440.000000,
            340282346638528859811704183484516925440.000000
        ], "None", False
    ]
) -> None
```

<a id="unreal.ActorPerceptionUpdateInfo.target_id"></a>

#### target_id

```python
@property
def target_id() -> int
```

(int32):  [Read-Write] Id of to the stimulus source

<a id="unreal.ActorPerceptionUpdateInfo.target_id"></a>

#### target_id

```python
@target_id.setter
def target_id(value: int) -> None
```

<a id="unreal.ActorPerceptionUpdateInfo.target"></a>

#### target

```python
@property
def target() -> Actor
```

(Actor):  [Read-Write] Actor associated to the stimulus (can be null)

<a id="unreal.ActorPerceptionUpdateInfo.target"></a>

#### target

```python
@target.setter
def target(value: Actor) -> None
```

<a id="unreal.ActorPerceptionUpdateInfo.stimulus"></a>

#### stimulus

```python
@property
def stimulus() -> AIStimulus
```

(AIStimulus):  [Read-Write] Updated stimulus

<a id="unreal.ActorPerceptionUpdateInfo.stimulus"></a>

#### stimulus

```python
@stimulus.setter
def stimulus(value: AIStimulus) -> None
```

<a id="unreal.AIStimulus"></a>