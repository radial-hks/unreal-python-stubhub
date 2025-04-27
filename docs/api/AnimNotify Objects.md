## AnimNotify Objects

```python
class AnimNotify(Object)
```

Anim Notify

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotify.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors

<a id="unreal.AnimNotify.notify_color"></a>

#### notify_color

```python
@property
def notify_color() -> Color
```

(Color):  [Read-Only] Color of Notify in editor

<a id="unreal.AnimNotify.should_fire_in_editor"></a>

#### should_fire_in_editor

```python
@property
def should_fire_in_editor() -> bool
```

(bool):  [Read-Only] Whether this notify instance should fire in animation editors

<a id="unreal.AnimNotify.received_notify"></a>

#### received_notify

```python
def received_notify(mesh_comp: SkeletalMeshComponent,
                    animation: AnimSequenceBase,
                    event_reference: AnimNotifyEventReference) -> bool
```

x.received_notify(mesh_comp, animation, event_reference) -> bool
Received Notify

Args:
    mesh_comp (SkeletalMeshComponent): 
    animation (AnimSequenceBase): 
    event_reference (AnimNotifyEventReference): 

Returns:
    bool:

<a id="unreal.AnimNotify.get_notify_name"></a>

#### get_notify_name

```python
def get_notify_name() -> str
```

x.get_notify_name() -> str
Implementable event to get a custom name for the notify

Returns:
    str:

<a id="unreal.AnimNotify.get_default_trigger_weight_threshold"></a>

#### get_default_trigger_weight_threshold

```python
def get_default_trigger_weight_threshold() -> float
```

x.get_default_trigger_weight_threshold() -> float
TriggerWeightThreshold to use when creating notifies of this type

Returns:
    float:

<a id="unreal.AnimNotify_PlayMontageNotify"></a>