## PawnSensingComponent Objects

```python
class PawnSensingComponent(ActorComponent)
```

Pawn Sensing Component

**C++ Source:**

- **Module**: AIModule
- **File**: PawnSensingComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_sensing_updates`` (bool):  [Read-Write] If true, component will perform sensing updates. At runtime change this using SetSensingUpdatesEnabled().
- ``hear_noises`` (bool):  [Read-Write] If true, we will perform audibility tests and will be notified when a Pawn makes a noise that can be heard. Default: true
  IMPORTANT NOTE: If we can see pawns (bSeePawns is true), and the pawn is visible, noise notifications are not triggered.
- ``hearing_max_sound_age`` (float):  [Read-Write] Max age of sounds we can hear. Should be greater than SensingInterval, or you might miss hearing some sounds!
- ``hearing_threshold`` (float):  [Read-Write] Max distance at which a makenoise(1.0) loudness sound can be heard, regardless of occlusion
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``los_hearing_threshold`` (float):  [Read-Write] Max distance at which a makenoise(1.0) loudness sound can be heard if unoccluded (LOSHearingThreshold should be > HearingThreshold)
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_hear_noise`` (HearNoiseDelegate):  [Read-Write] Delegate to execute when we hear a noise from a Pawn's PawnNoiseEmitterComponent.
- ``on_see_pawn`` (SeePawnDelegate):  [Read-Write] Delegate to execute when we see a Pawn.
- ``only_sense_players`` (bool):  [Read-Write] If true, will only sense player-controlled pawns in the world. Default: true
- ``peripheral_vision_angle`` (float):  [Read-Write] How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``see_pawns`` (bool):  [Read-Write] If true, we will perform visibility tests and will trigger notifications when a Pawn is visible. Default: true
- ``sensing_interval`` (float):  [Read-Write] Amount of time between pawn sensing updates. Use SetSensingInterval() to adjust this at runtime. A value <= 0 prevents any updates.
- ``sight_radius`` (float):  [Read-Write] Maximum sight distance.

<a id="unreal.PawnSensingComponent.hearing_threshold"></a>

#### hearing_threshold

```python
@property
def hearing_threshold() -> float
```

(float):  [Read-Write] Max distance at which a makenoise(1.0) loudness sound can be heard, regardless of occlusion

<a id="unreal.PawnSensingComponent.hearing_threshold"></a>

#### hearing_threshold

```python
@hearing_threshold.setter
def hearing_threshold(value: float) -> None
```

<a id="unreal.PawnSensingComponent.los_hearing_threshold"></a>

#### los_hearing_threshold

```python
@property
def los_hearing_threshold() -> float
```

(float):  [Read-Write] Max distance at which a makenoise(1.0) loudness sound can be heard if unoccluded (LOSHearingThreshold should be > HearingThreshold)

<a id="unreal.PawnSensingComponent.los_hearing_threshold"></a>

#### los_hearing_threshold

```python
@los_hearing_threshold.setter
def los_hearing_threshold(value: float) -> None
```

<a id="unreal.PawnSensingComponent.sight_radius"></a>

#### sight_radius

```python
@property
def sight_radius() -> float
```

(float):  [Read-Write] Maximum sight distance.

<a id="unreal.PawnSensingComponent.sight_radius"></a>

#### sight_radius

```python
@sight_radius.setter
def sight_radius(value: float) -> None
```

<a id="unreal.PawnSensingComponent.sensing_interval"></a>

#### sensing_interval

```python
@property
def sensing_interval() -> float
```

(float):  [Read-Only] Amount of time between pawn sensing updates. Use SetSensingInterval() to adjust this at runtime. A value <= 0 prevents any updates.

<a id="unreal.PawnSensingComponent.sight_counter_interval"></a>

#### sight_counter_interval

```python
@property
def sight_counter_interval() -> float
```

deprecated: 'sight_counter_interval' was renamed to 'sensing_interval'.

<a id="unreal.PawnSensingComponent.hearing_max_sound_age"></a>

#### hearing_max_sound_age

```python
@property
def hearing_max_sound_age() -> float
```

(float):  [Read-Write] Max age of sounds we can hear. Should be greater than SensingInterval, or you might miss hearing some sounds!

<a id="unreal.PawnSensingComponent.hearing_max_sound_age"></a>

#### hearing_max_sound_age

```python
@hearing_max_sound_age.setter
def hearing_max_sound_age(value: float) -> None
```

<a id="unreal.PawnSensingComponent.enable_sensing_updates"></a>

#### enable_sensing_updates

```python
@property
def enable_sensing_updates() -> bool
```

(bool):  [Read-Only] If true, component will perform sensing updates. At runtime change this using SetSensingUpdatesEnabled().

<a id="unreal.PawnSensingComponent.only_sense_players"></a>

#### only_sense_players

```python
@property
def only_sense_players() -> bool
```

(bool):  [Read-Write] If true, will only sense player-controlled pawns in the world. Default: true

<a id="unreal.PawnSensingComponent.only_sense_players"></a>

#### only_sense_players

```python
@only_sense_players.setter
def only_sense_players(value: bool) -> None
```

<a id="unreal.PawnSensingComponent.see_pawns"></a>

#### see_pawns

```python
@property
def see_pawns() -> bool
```

(bool):  [Read-Write] If true, we will perform visibility tests and will trigger notifications when a Pawn is visible. Default: true

<a id="unreal.PawnSensingComponent.see_pawns"></a>

#### see_pawns

```python
@see_pawns.setter
def see_pawns(value: bool) -> None
```

<a id="unreal.PawnSensingComponent.b_wants_see_player_notify"></a>

#### b_wants_see_player_notify

```python
@property
def b_wants_see_player_notify() -> bool
```

deprecated: 'b_wants_see_player_notify' was renamed to 'see_pawns'.

<a id="unreal.PawnSensingComponent.b_wants_see_player_notify"></a>

#### b_wants_see_player_notify

```python
@b_wants_see_player_notify.setter
def b_wants_see_player_notify(value: bool) -> None
```

<a id="unreal.PawnSensingComponent.hear_noises"></a>

#### hear_noises

```python
@property
def hear_noises() -> bool
```

(bool):  [Read-Write] If true, we will perform audibility tests and will be notified when a Pawn makes a noise that can be heard. Default: true
IMPORTANT NOTE: If we can see pawns (bSeePawns is true), and the pawn is visible, noise notifications are not triggered.

<a id="unreal.PawnSensingComponent.hear_noises"></a>

#### hear_noises

```python
@hear_noises.setter
def hear_noises(value: bool) -> None
```

<a id="unreal.PawnSensingComponent.on_see_pawn"></a>

#### on_see_pawn

```python
@property
def on_see_pawn() -> SeePawnDelegate
```

(SeePawnDelegate):  [Read-Write] Delegate to execute when we see a Pawn.

<a id="unreal.PawnSensingComponent.on_see_pawn"></a>

#### on_see_pawn

```python
@on_see_pawn.setter
def on_see_pawn(value: SeePawnDelegate) -> None
```

<a id="unreal.PawnSensingComponent.on_hear_noise"></a>

#### on_hear_noise

```python
@property
def on_hear_noise() -> HearNoiseDelegate
```

(HearNoiseDelegate):  [Read-Write] Delegate to execute when we hear a noise from a Pawn's PawnNoiseEmitterComponent.

<a id="unreal.PawnSensingComponent.on_hear_noise"></a>

#### on_hear_noise

```python
@on_hear_noise.setter
def on_hear_noise(value: HearNoiseDelegate) -> None
```

<a id="unreal.PawnSensingComponent.peripheral_vision_angle"></a>

#### peripheral_vision_angle

```python
@property
def peripheral_vision_angle() -> float
```

(float):  [Read-Only] How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime.

<a id="unreal.PawnSensingComponent.set_sensing_updates_enabled"></a>

#### set_sensing_updates_enabled

```python
def set_sensing_updates_enabled(enabled: bool) -> None
```

x.set_sensing_updates_enabled(enabled) -> None
Enables or disables sensing updates. The timer is reset in either case.

Args:
    enabled (bool):

<a id="unreal.PawnSensingComponent.set_sensing_interval"></a>

#### set_sensing_interval

```python
def set_sensing_interval(new_sensing_interval: float) -> None
```

x.set_sensing_interval(new_sensing_interval) -> None
Changes the SensingInterval.
If we are currently waiting for an interval, this can either extend or shorten that interval.
A value <= 0 prevents any updates.

Args:
    new_sensing_interval (float):

<a id="unreal.PawnSensingComponent.set_peripheral_vision_angle"></a>

#### set_peripheral_vision_angle

```python
def set_peripheral_vision_angle(new_peripheral_vision_angle: float) -> None
```

x.set_peripheral_vision_angle(new_peripheral_vision_angle) -> None
Sets PeripheralVisionAngle. Calculates PeripheralVisionCosine from PeripheralVisionAngle

Args:
    new_peripheral_vision_angle (float):

<a id="unreal.PawnSensingComponent.get_peripheral_vision_cosine"></a>

#### get_peripheral_vision_cosine

```python
def get_peripheral_vision_cosine() -> float
```

x.get_peripheral_vision_cosine() -> float
Get Peripheral Vision Cosine

Returns:
    float:

<a id="unreal.PawnSensingComponent.get_peripheral_vision_angle"></a>

#### get_peripheral_vision_angle

```python
def get_peripheral_vision_angle() -> float
```

x.get_peripheral_vision_angle() -> float
Get Peripheral Vision Angle

Returns:
    float:

<a id="unreal.SensingComponent"></a>