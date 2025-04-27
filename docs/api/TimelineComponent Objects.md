## TimelineComponent Objects

```python
class TimelineComponent(ActorComponent)
```

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
Events can be triggered at keyframes along the timeline.
Floats, vectors, and colors are interpolated between keyframes along the timeline.

**C++ Source:**

- **Module**: Engine
- **File**: TimelineComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.TimelineComponent.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Stop playback of timeline

<a id="unreal.TimelineComponent.set_vector_curve"></a>

#### set_vector_curve

```python
def set_vector_curve(new_vector_curve: CurveVector,
                     vector_track_name: Name) -> None
```

x.set_vector_curve(new_vector_curve, vector_track_name) -> None
Update a certain vector track's curve

Args:
    new_vector_curve (CurveVector): 
    vector_track_name (Name):

<a id="unreal.TimelineComponent.set_timeline_post_update_func"></a>

#### set_timeline_post_update_func

```python
def set_timeline_post_update_func(
        new_timeline_post_update_func: OnTimelineEvent) -> None
```

x.set_timeline_post_update_func(new_timeline_post_update_func) -> None
Set the delegate to call after each timeline tick

Args:
    new_timeline_post_update_func (OnTimelineEvent):

<a id="unreal.TimelineComponent.set_timeline_length_mode"></a>

#### set_timeline_length_mode

```python
def set_timeline_length_mode(new_length_mode: TimelineLengthMode) -> None
```

x.set_timeline_length_mode(new_length_mode) -> None
Sets the length mode of the timeline

Args:
    new_length_mode (TimelineLengthMode):

<a id="unreal.TimelineComponent.set_timeline_length"></a>

#### set_timeline_length

```python
def set_timeline_length(new_length: float) -> None
```

x.set_timeline_length(new_length) -> None
Set length of the timeline

Args:
    new_length (float):

<a id="unreal.TimelineComponent.set_timeline_finished_func"></a>

#### set_timeline_finished_func

```python
def set_timeline_finished_func(
        new_timeline_finished_func: OnTimelineEvent) -> None
```

x.set_timeline_finished_func(new_timeline_finished_func) -> None
Set the delegate to call when timeline is finished

Args:
    new_timeline_finished_func (OnTimelineEvent):

<a id="unreal.TimelineComponent.set_play_rate"></a>

#### set_play_rate

```python
def set_play_rate(new_rate: float) -> None
```

x.set_play_rate(new_rate) -> None
Sets the new play rate for this timeline

Args:
    new_rate (float):

<a id="unreal.TimelineComponent.set_playback_position"></a>

#### set_playback_position

```python
def set_playback_position(new_position: float,
                          fire_events: bool,
                          fire_update: bool = True) -> None
```

x.set_playback_position(new_position, fire_events, fire_update=True) -> None
Jump to a position in the timeline.

Args:
    new_position (float): 
    fire_events (bool): If true, event functions that are between current position and new playback position will fire.
    fire_update (bool): If true, the update output exec will fire after setting the new playback position.

<a id="unreal.TimelineComponent.set_new_time"></a>

#### set_new_time

```python
def set_new_time(new_time: float) -> None
```

x.set_new_time(new_time) -> None
Set the new playback position time to use

Args:
    new_time (float):

<a id="unreal.TimelineComponent.set_looping"></a>

#### set_looping

```python
def set_looping(new_looping: bool) -> None
```

x.set_looping(new_looping) -> None
true means we would loop, false means we should not.

Args:
    new_looping (bool):

<a id="unreal.TimelineComponent.set_linear_color_curve"></a>

#### set_linear_color_curve

```python
def set_linear_color_curve(new_linear_color_curve: CurveLinearColor,
                           linear_color_track_name: Name) -> None
```

x.set_linear_color_curve(new_linear_color_curve, linear_color_track_name) -> None
Update a certain linear color track's curve

Args:
    new_linear_color_curve (CurveLinearColor): 
    linear_color_track_name (Name):

<a id="unreal.TimelineComponent.set_ignore_time_dilation"></a>

#### set_ignore_time_dilation

```python
def set_ignore_time_dilation(new_ignore_time_dilation: bool) -> None
```

x.set_ignore_time_dilation(new_ignore_time_dilation) -> None
Set whether to ignore time dilation.

Args:
    new_ignore_time_dilation (bool):

<a id="unreal.TimelineComponent.set_float_curve"></a>

#### set_float_curve

```python
def set_float_curve(new_float_curve: CurveFloat,
                    float_track_name: Name) -> None
```

x.set_float_curve(new_float_curve, float_track_name) -> None
Update a certain float track's curve

Args:
    new_float_curve (CurveFloat): 
    float_track_name (Name):

<a id="unreal.TimelineComponent.reverse_from_end"></a>

#### reverse_from_end

```python
def reverse_from_end() -> None
```

x.reverse_from_end() -> None
Start playback of timeline in reverse from the end

<a id="unreal.TimelineComponent.reverse"></a>

#### reverse

```python
def reverse() -> None
```

x.reverse() -> None
Start playback of timeline in reverse

<a id="unreal.TimelineComponent.play_from_start"></a>

#### play_from_start

```python
def play_from_start() -> None
```

x.play_from_start() -> None
Start playback of timeline from the start

<a id="unreal.TimelineComponent.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Start playback of timeline

<a id="unreal.TimelineComponent.is_reversing"></a>

#### is_reversing

```python
def is_reversing() -> bool
```

x.is_reversing() -> bool
Get whether we are reversing or not

Returns:
    bool:

<a id="unreal.TimelineComponent.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Get whether this timeline is playing or not.

Returns:
    bool:

<a id="unreal.TimelineComponent.is_looping"></a>

#### is_looping

```python
def is_looping() -> bool
```

x.is_looping() -> bool
Get whether we are looping or not

Returns:
    bool:

<a id="unreal.TimelineComponent.get_timeline_length"></a>

#### get_timeline_length

```python
def get_timeline_length() -> float
```

x.get_timeline_length() -> float
Get length of the timeline

Returns:
    float:

<a id="unreal.TimelineComponent.get_scaled_timeline_length"></a>

#### get_scaled_timeline_length

```python
def get_scaled_timeline_length() -> float
```

x.get_scaled_timeline_length() -> float
Get length of the timeline divided by the play rate

Returns:
    float:

<a id="unreal.TimelineComponent.get_play_rate"></a>

#### get_play_rate

```python
def get_play_rate() -> float
```

x.get_play_rate() -> float
Get the current play rate for this timeline

Returns:
    float:

<a id="unreal.TimelineComponent.get_playback_position"></a>

#### get_playback_position

```python
def get_playback_position() -> float
```

x.get_playback_position() -> float
Get the current playback position of the Timeline

Returns:
    float:

<a id="unreal.TimelineComponent.get_ignore_time_dilation"></a>

#### get_ignore_time_dilation

```python
def get_ignore_time_dilation() -> bool
```

x.get_ignore_time_dilation() -> bool
Get whether to ignore time dilation.

Returns:
    bool:

<a id="unreal.TimelineComponent.add_interp_vector"></a>

#### add_interp_vector

```python
def add_interp_vector(vector_curve: CurveVector,
                      interp_func: OnTimelineVector,
                      property_name: Name = "None",
                      track_name: Name = "None") -> None
```

x.add_interp_vector(vector_curve, interp_func, property_name="None", track_name="None") -> None
Add a vector interpolation to the timeline

Args:
    vector_curve (CurveVector): 
    interp_func (OnTimelineVector): 
    property_name (Name): 
    track_name (Name):

<a id="unreal.TimelineComponent.add_interp_linear_color"></a>

#### add_interp_linear_color

```python
def add_interp_linear_color(linear_color_curve: CurveLinearColor,
                            interp_func: OnTimelineLinearColor,
                            property_name: Name = "None",
                            track_name: Name = "None") -> None
```

x.add_interp_linear_color(linear_color_curve, interp_func, property_name="None", track_name="None") -> None
Add a linear color interpolation to the timeline

Args:
    linear_color_curve (CurveLinearColor): 
    interp_func (OnTimelineLinearColor): 
    property_name (Name): 
    track_name (Name):

<a id="unreal.TimelineComponent.add_interp_float"></a>

#### add_interp_float

```python
def add_interp_float(float_curve: CurveFloat,
                     interp_func: OnTimelineFloat,
                     property_name: Name = "None",
                     track_name: Name = "None") -> None
```

x.add_interp_float(float_curve, interp_func, property_name="None", track_name="None") -> None
Add a float interpolation to the timeline

Args:
    float_curve (CurveFloat): 
    interp_func (OnTimelineFloat): 
    property_name (Name): 
    track_name (Name):

<a id="unreal.TimelineComponent.add_event"></a>

#### add_event

```python
def add_event(time: float, event_func: OnTimelineEvent) -> None
```

x.add_event(time, event_func) -> None
Add a callback event to the timeline

Args:
    time (float): 
    event_func (OnTimelineEvent):

<a id="unreal.TriggerBase"></a>