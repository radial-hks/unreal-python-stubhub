## CEClonerEffectorExtension Objects

```python
class CEClonerEffectorExtension(CEClonerExtensionBase)
```

Extension dealing with effectors options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerEffectorExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effector_actors_weak`` (Array[Actor]):  [Read-Write] Effectors actors linked to this cloner

<a id="unreal.CEClonerEffectorExtension.unlink_effector"></a>

#### unlink_effector

```python
def unlink_effector(effector_actor: Actor) -> bool
```

x.unlink_effector(effector_actor) -> bool
Unlinks the effector actor and reset the cloner simulation

Args:
    effector_actor (Actor): 

Returns:
    bool:

<a id="unreal.CEClonerEffectorExtension.link_effector"></a>

#### link_effector

```python
def link_effector(effector_actor: Actor) -> bool
```

x.link_effector(effector_actor) -> bool
Links new actor effectors to apply transformation on clones

Args:
    effector_actor (Actor): 

Returns:
    bool:

<a id="unreal.CEClonerEffectorExtension.is_effector_linked"></a>

#### is_effector_linked

```python
def is_effector_linked(effector_actor: Actor) -> bool
```

x.is_effector_linked(effector_actor) -> bool
Checks if an effector is linked with this cloner

Args:
    effector_actor (Actor): 

Returns:
    bool:

<a id="unreal.CEClonerEffectorExtension.get_effector_count"></a>

#### get_effector_count

```python
def get_effector_count() -> int
```

x.get_effector_count() -> int32
Gets the number of effectors applied on this cloner

Returns:
    int32:

<a id="unreal.CEClonerEmitterSpawnExtension"></a>