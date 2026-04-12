## ActorInitStateChangedParams Objects

```python
class ActorInitStateChangedParams(StructBase)
```

Parameters struct for Init State change functions

**C++ Source:**

- **Plugin**: ModularGameplay
- **Module**: ModularGameplay
- **File**: GameFrameworkComponentDelegates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``feature_name`` (Name):  [Read-Write] Name of the feature that changed
- ``feature_state`` (GameplayTag):  [Read-Write] The new state of the feature
- ``implementer`` (Object):  [Read-Write] The object (often a component) that implements the feature
- ``owning_actor`` (Actor):  [Read-Write] The actor owning the feature that changed

<a id="unreal.ActorInitStateChangedParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(owning_actor: Actor = None,
             feature_name: Name = "None",
             implementer: Object = None,
             feature_state: GameplayTag = ["None"]) -> None
```

<a id="unreal.ActorInitStateChangedParams.owning_actor"></a>

#### owning\_actor

```python
@property
def owning_actor() -> Actor
```

(Actor):  [Read-Write] The actor owning the feature that changed

<a id="unreal.ActorInitStateChangedParams.owning_actor"></a>

#### owning\_actor

```python
@owning_actor.setter
def owning_actor(value: Actor) -> None
```

<a id="unreal.ActorInitStateChangedParams.feature_name"></a>

#### feature\_name

```python
@property
def feature_name() -> Name
```

(Name):  [Read-Write] Name of the feature that changed

<a id="unreal.ActorInitStateChangedParams.feature_name"></a>

#### feature\_name

```python
@feature_name.setter
def feature_name(value: Name) -> None
```

<a id="unreal.ActorInitStateChangedParams.implementer"></a>

#### implementer

```python
@property
def implementer() -> Object
```

(Object):  [Read-Write] The object (often a component) that implements the feature

<a id="unreal.ActorInitStateChangedParams.implementer"></a>

#### implementer

```python
@implementer.setter
def implementer(value: Object) -> None
```

<a id="unreal.ActorInitStateChangedParams.feature_state"></a>

#### feature\_state

```python
@property
def feature_state() -> GameplayTag
```

(GameplayTag):  [Read-Write] The new state of the feature

<a id="unreal.ActorInitStateChangedParams.feature_state"></a>

#### feature\_state

```python
@feature_state.setter
def feature_state(value: GameplayTag) -> None
```

<a id="unreal.FastArraySerializerItem"></a>