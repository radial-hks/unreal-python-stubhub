## AvaAlignBetweenWeightedActor Objects

```python
class AvaAlignBetweenWeightedActor(StructBase)
```

Represents an actor with a weight and an enabled state.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaAlignBetweenModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_weak`` (Actor):  [Read-Write] An actor that will effect the placement location.
- ``enabled`` (bool):  [Read-Write] If true, will consider this weighted actor when calculating the placement location.
- ``weight`` (float):  [Read-Write] How much effect this actor has on the placement location.

<a id="unreal.AvaAlignBetweenWeightedActor.__init__"></a>

#### __init__

```python
def __init__(actor_weak: Actor = None,
             weight: float = 0.000000,
             enabled: bool = False) -> None
```

<a id="unreal.AvaAlignBetweenWeightedActor.actor_weak"></a>

#### actor_weak

```python
@property
def actor_weak() -> Actor
```

(Actor):  [Read-Write] An actor that will effect the placement location.

<a id="unreal.AvaAlignBetweenWeightedActor.actor_weak"></a>

#### actor_weak

```python
@actor_weak.setter
def actor_weak(value: Actor) -> None
```

<a id="unreal.AvaAlignBetweenWeightedActor.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] How much effect this actor has on the placement location.

<a id="unreal.AvaAlignBetweenWeightedActor.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.AvaAlignBetweenWeightedActor.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] If true, will consider this weighted actor when calculating the placement location.

<a id="unreal.AvaAlignBetweenWeightedActor.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.AvaBooleanModifierSharedChannelInfo"></a>