## ActorForWorldTransforms Objects

```python
class ActorForWorldTransforms(StructBase)
```

Description of an actor selected parts we can find world transforms on

**C++ Source:**

- **Module**: MovieScene
- **File**: ActorForWorldTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor`` (Actor):  [Read-Write]
- ``component`` (SceneComponent):  [Read-Write]
- ``socket_name`` (Name):  [Read-Write]

<a id="unreal.ActorForWorldTransforms.__init__"></a>

#### __init__

```python
def __init__(actor: Actor = None,
             component: SceneComponent = None,
             socket_name: Name = "None") -> None
```

<a id="unreal.ActorForWorldTransforms.actor"></a>

#### actor

```python
@property
def actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.ActorForWorldTransforms.actor"></a>

#### actor

```python
@actor.setter
def actor(value: Actor) -> None
```

<a id="unreal.ActorForWorldTransforms.component"></a>

#### component

```python
@property
def component() -> SceneComponent
```

(SceneComponent):  [Read-Write]

<a id="unreal.ActorForWorldTransforms.component"></a>

#### component

```python
@component.setter
def component(value: SceneComponent) -> None
```

<a id="unreal.ActorForWorldTransforms.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ActorForWorldTransforms.socket_name"></a>

#### socket_name

```python
@socket_name.setter
def socket_name(value: Name) -> None
```

<a id="unreal.MovieSceneConditionContext"></a>