## AnimNotifyEvent Objects

```python
class AnimNotifyEvent(AnimLinkableElement)
```

Triggers an animation notify.  Each AnimNotifyEvent contains an AnimNotify object
which has its Notify method called and passed to the animation.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_filtered_via_request`` (bool):  [Read-Write] Allow notify event to be filtered if requested at runtime (e. g. via an Anim Graph Message)
- ``link_method`` (AnimLinkMethod):  [Read-Write] The method we are using to calculate our times
- ``linked_sequence`` (AnimSequenceBase):  [Read-Only] The Animation Sequence that this montage element will link to, when the sequence changes
  in either length or rate; the element will correctly place itself in relation to the sequence
- ``montage_tick_type`` (MontageNotifyTickType):  [Read-Write]
- ``notify`` (AnimNotify):  [Read-Write]
- ``notify_filter_lod`` (int32):  [Read-Write] LOD to start filtering this notify from.
- ``notify_filter_type`` (NotifyFilterType):  [Read-Write] Defines a method for filtering notifies (stopping them triggering) e.g. by looking at the meshes current LOD
- ``notify_name`` (Name):  [Read-Write]
- ``notify_state_class`` (AnimNotifyState):  [Read-Write]
- ``notify_trigger_chance`` (float):  [Read-Write] Defines the chance of of this notify triggering, 0 = No Chance, 1 = Always triggers
- ``slot_index`` (int32):  [Read-Write] The slot index we are currently using within LinkedMontage
- ``trigger_on_dedicated_server`` (bool):  [Read-Write] If disabled this notify will be skipped on dedicated servers
- ``trigger_on_follower`` (bool):  [Read-Write] If enabled this notify will trigger when the animation is a follower in a sync group (by default only the sync group leaders notifies trigger
- ``trigger_weight_threshold`` (float):  [Read-Write]

<a id="unreal.AnimNotifyEvent.__init__"></a>

#### __init__

```python
def __init__(
        trigger_weight_threshold: float = 0.000000,
        notify_name: Name = "None",
        notify: AnimNotify = None,
        notify_state_class: AnimNotifyState = None,
        montage_tick_type: MontageNotifyTickType = MontageNotifyTickType.
    QUEUED,
        notify_trigger_chance: float = 0.000000,
        notify_filter_type: NotifyFilterType = NotifyFilterType.NO_FILTERING,
        notify_filter_lod: int = 0,
        can_be_filtered_via_request: bool = False,
        trigger_on_dedicated_server: bool = False,
        trigger_on_follower: bool = False) -> None
```

<a id="unreal.AnimNotifyEvent.trigger_weight_threshold"></a>

#### trigger_weight_threshold

```python
@property
def trigger_weight_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNotifyEvent.trigger_weight_threshold"></a>

#### trigger_weight_threshold

```python
@trigger_weight_threshold.setter
def trigger_weight_threshold(value: float) -> None
```

<a id="unreal.AnimNotifyEvent.notify_name"></a>

#### notify_name

```python
@property
def notify_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.AnimNotifyEvent.notify"></a>

#### notify

```python
@property
def notify() -> AnimNotify
```

(AnimNotify):  [Read-Write]

<a id="unreal.AnimNotifyEvent.notify"></a>

#### notify

```python
@notify.setter
def notify(value: AnimNotify) -> None
```

<a id="unreal.AnimNotifyEvent.notify_state_class"></a>

#### notify_state_class

```python
@property
def notify_state_class() -> AnimNotifyState
```

(AnimNotifyState):  [Read-Write]

<a id="unreal.AnimNotifyEvent.notify_state_class"></a>

#### notify_state_class

```python
@notify_state_class.setter
def notify_state_class(value: AnimNotifyState) -> None
```

<a id="unreal.AnimNotifyEvent.montage_tick_type"></a>

#### montage_tick_type

```python
@property
def montage_tick_type() -> MontageNotifyTickType
```

(MontageNotifyTickType):  [Read-Write]

<a id="unreal.AnimNotifyEvent.montage_tick_type"></a>

#### montage_tick_type

```python
@montage_tick_type.setter
def montage_tick_type(value: MontageNotifyTickType) -> None
```

<a id="unreal.AnimNotifyEvent.notify_trigger_chance"></a>

#### notify_trigger_chance

```python
@property
def notify_trigger_chance() -> float
```

(float):  [Read-Write] Defines the chance of of this notify triggering, 0 = No Chance, 1 = Always triggers

<a id="unreal.AnimNotifyEvent.notify_trigger_chance"></a>

#### notify_trigger_chance

```python
@notify_trigger_chance.setter
def notify_trigger_chance(value: float) -> None
```

<a id="unreal.AnimNotifyEvent.notify_filter_type"></a>

#### notify_filter_type

```python
@property
def notify_filter_type() -> NotifyFilterType
```

(NotifyFilterType):  [Read-Write] Defines a method for filtering notifies (stopping them triggering) e.g. by looking at the meshes current LOD

<a id="unreal.AnimNotifyEvent.notify_filter_type"></a>

#### notify_filter_type

```python
@notify_filter_type.setter
def notify_filter_type(value: NotifyFilterType) -> None
```

<a id="unreal.AnimNotifyEvent.notify_filter_lod"></a>

#### notify_filter_lod

```python
@property
def notify_filter_lod() -> int
```

(int32):  [Read-Write] LOD to start filtering this notify from.

<a id="unreal.AnimNotifyEvent.notify_filter_lod"></a>

#### notify_filter_lod

```python
@notify_filter_lod.setter
def notify_filter_lod(value: int) -> None
```

<a id="unreal.AnimNotifyEvent.can_be_filtered_via_request"></a>

#### can_be_filtered_via_request

```python
@property
def can_be_filtered_via_request() -> bool
```

(bool):  [Read-Write] Allow notify event to be filtered if requested at runtime (e. g. via an Anim Graph Message)

<a id="unreal.AnimNotifyEvent.can_be_filtered_via_request"></a>

#### can_be_filtered_via_request

```python
@can_be_filtered_via_request.setter
def can_be_filtered_via_request(value: bool) -> None
```

<a id="unreal.AnimNotifyEvent.trigger_on_dedicated_server"></a>

#### trigger_on_dedicated_server

```python
@property
def trigger_on_dedicated_server() -> bool
```

(bool):  [Read-Write] If disabled this notify will be skipped on dedicated servers

<a id="unreal.AnimNotifyEvent.trigger_on_dedicated_server"></a>

#### trigger_on_dedicated_server

```python
@trigger_on_dedicated_server.setter
def trigger_on_dedicated_server(value: bool) -> None
```

<a id="unreal.AnimNotifyEvent.trigger_on_follower"></a>

#### trigger_on_follower

```python
@property
def trigger_on_follower() -> bool
```

(bool):  [Read-Write] If enabled this notify will trigger when the animation is a follower in a sync group (by default only the sync group leaders notifies trigger

<a id="unreal.AnimNotifyEvent.trigger_on_follower"></a>

#### trigger_on_follower

```python
@trigger_on_follower.setter
def trigger_on_follower(value: bool) -> None
```

<a id="unreal.AnimSyncMarker"></a>