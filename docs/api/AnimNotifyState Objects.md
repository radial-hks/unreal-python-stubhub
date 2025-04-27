## AnimNotifyState Objects

```python
class AnimNotifyState(Object)
```

Anim Notify State

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState.notify_color"></a>

#### notify_color

```python
@property
def notify_color() -> Color
```

(Color):  [Read-Only] Color of Notify in editor

<a id="unreal.AnimNotifyState.should_fire_in_editor"></a>

#### should_fire_in_editor

```python
@property
def should_fire_in_editor() -> bool
```

(bool):  [Read-Only] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState.received_notify_tick"></a>

#### received_notify_tick

```python
def received_notify_tick(mesh_comp: SkeletalMeshComponent,
                         animation: AnimSequenceBase, frame_delta_time: float,
                         event_reference: AnimNotifyEventReference) -> bool
```

x.received_notify_tick(mesh_comp, animation, frame_delta_time, event_reference) -> bool
Received Notify Tick

Args:
    mesh_comp (SkeletalMeshComponent): 
    animation (AnimSequenceBase): 
    frame_delta_time (float): 
    event_reference (AnimNotifyEventReference): 

Returns:
    bool:

<a id="unreal.AnimNotifyState.received_notify_end"></a>

#### received_notify_end

```python
def received_notify_end(mesh_comp: SkeletalMeshComponent,
                        animation: AnimSequenceBase,
                        event_reference: AnimNotifyEventReference) -> bool
```

x.received_notify_end(mesh_comp, animation, event_reference) -> bool
Received Notify End

Args:
    mesh_comp (SkeletalMeshComponent): 
    animation (AnimSequenceBase): 
    event_reference (AnimNotifyEventReference): 

Returns:
    bool:

<a id="unreal.AnimNotifyState.received_notify_begin"></a>

#### received_notify_begin

```python
def received_notify_begin(mesh_comp: SkeletalMeshComponent,
                          animation: AnimSequenceBase, total_duration: float,
                          event_reference: AnimNotifyEventReference) -> bool
```

x.received_notify_begin(mesh_comp, animation, total_duration, event_reference) -> bool
Received Notify Begin

Args:
    mesh_comp (SkeletalMeshComponent): 
    animation (AnimSequenceBase): 
    total_duration (float): 
    event_reference (AnimNotifyEventReference): 

Returns:
    bool:

<a id="unreal.AnimNotifyState.get_notify_name"></a>

#### get_notify_name

```python
def get_notify_name() -> str
```

x.get_notify_name() -> str
Implementable event to get a custom name for the notify

Returns:
    str:

<a id="unreal.AnimNotifyState.get_default_trigger_weight_threshold"></a>

#### get_default_trigger_weight_threshold

```python
def get_default_trigger_weight_threshold() -> float
```

x.get_default_trigger_weight_threshold() -> float
TriggerWeightThreshold to use when creating notifies of this type

Returns:
    float:

<a id="unreal.AnimNotify_PlayMontageNotifyWindow"></a>