## TargetingSourceContext Objects

```python
class TargetingSourceContext(StructBase)
```

struct: FTargetingSourceContext Stores context information about a targeting request.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSystemTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instigator_actor`` (Actor):  [Read-Write] The optional instigator the targeting request is owned by (i.e. owner of a projectile)
- ``source_actor`` (Actor):  [Read-Write] The optional actor the targeting request sources from (i.e. player/projectile/etc)
- ``source_location`` (Vector):  [Read-Write] The optional location the targeting request will source from (i.e. do AOE targeting at x/y/z location)
- ``source_object`` (Object):  [Read-Write] The optional reference to a source uobject to use in the context
- ``source_socket_name`` (Name):  [Read-Write] The optional socket name to use on the source actor (if an actor is defined)

<a id="unreal.TargetingSourceContext.__init__"></a>

#### \_\_init\_\_

```python
def __init__(source_actor: Actor = None,
             instigator_actor: Actor = None,
             source_location: Vector = [0.000000, 0.000000, 0.000000],
             source_socket_name: Name = "None",
             source_object: Object = None) -> None
```

<a id="unreal.TargetingSourceContext.source_actor"></a>

#### source\_actor

```python
@property
def source_actor() -> Actor
```

(Actor):  [Read-Write] The optional actor the targeting request sources from (i.e. player/projectile/etc)

<a id="unreal.TargetingSourceContext.source_actor"></a>

#### source\_actor

```python
@source_actor.setter
def source_actor(value: Actor) -> None
```

<a id="unreal.TargetingSourceContext.instigator_actor"></a>

#### instigator\_actor

```python
@property
def instigator_actor() -> Actor
```

(Actor):  [Read-Write] The optional instigator the targeting request is owned by (i.e. owner of a projectile)

<a id="unreal.TargetingSourceContext.instigator_actor"></a>

#### instigator\_actor

```python
@instigator_actor.setter
def instigator_actor(value: Actor) -> None
```

<a id="unreal.TargetingSourceContext.source_location"></a>

#### source\_location

```python
@property
def source_location() -> Vector
```

(Vector):  [Read-Write] The optional location the targeting request will source from (i.e. do AOE targeting at x/y/z location)

<a id="unreal.TargetingSourceContext.source_location"></a>

#### source\_location

```python
@source_location.setter
def source_location(value: Vector) -> None
```

<a id="unreal.TargetingSourceContext.source_socket_name"></a>

#### source\_socket\_name

```python
@property
def source_socket_name() -> Name
```

(Name):  [Read-Write] The optional socket name to use on the source actor (if an actor is defined)

<a id="unreal.TargetingSourceContext.source_socket_name"></a>

#### source\_socket\_name

```python
@source_socket_name.setter
def source_socket_name(value: Name) -> None
```

<a id="unreal.TargetingSourceContext.source_object"></a>

#### source\_object

```python
@property
def source_object() -> Object
```

(Object):  [Read-Write] The optional reference to a source uobject to use in the context

<a id="unreal.TargetingSourceContext.source_object"></a>

#### source\_object

```python
@source_object.setter
def source_object(value: Object) -> None
```

<a id="unreal.SmartObjectUserCapsuleParams"></a>