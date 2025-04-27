## ApplicationLifecycleComponent Objects

```python
class ApplicationLifecycleComponent(ActorComponent)
```

Component to handle receiving notifications from the OS about application state (activated, suspended, termination, etc).

**C++ Source:**

- **Module**: Engine
- **File**: ApplicationLifecycleComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_has_entered_foreground_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] Called when the application is returning to the foreground (reverse any processing done in the EnterBackground delegate)
- ``application_has_reactivated_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] Called when the application has been reactivated (reverse any processing done in the Deactivate delegate)
- ``application_received_startup_arguments_delegate`` (ApplicationStartupArgumentsDelegate):  [Read-Write] Called with arguments passed to the application on statup, perhaps meta data passed on by another application which launched this one.
- ``application_should_unload_resources_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] Called when the OS is running low on resources and asks the application to free up any cached resources, drop graphics quality etc.
- ``application_will_deactivate_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] This is called when the application is about to be deactivated (e.g., due to a phone call or SMS or the sleep button).
  The game should be paused if possible, etc...
- ``application_will_enter_background_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] This is called when the application is being backgrounded (e.g., due to switching
  to another app or closing it via the home button)
  The game should release shared resources, save state, etc..., since it can be
  terminated from the background state without any further warning.
- ``application_will_terminate_delegate`` (ApplicationLifetimeDelegate):  [Read-Write] This *may* be called when the application is getting terminated by the OS.
  There is no guarantee that this will ever be called on a mobile device,
  save state when ApplicationWillEnterBackgroundDelegate is called instead.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_low_power_mode_delegate`` (OnLowPowerModeDelegate):  [Read-Write] Called when we are in low power mode
- ``on_temperature_change_delegate`` (OnTemperatureChangeDelegate):  [Read-Write] Called when temperature level has changed, and receives the severity
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ApplicationLifecycleComponent.application_will_deactivate_delegate"></a>

#### application_will_deactivate_delegate

```python
@property
def application_will_deactivate_delegate() -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] This is called when the application is about to be deactivated (e.g., due to a phone call or SMS or the sleep button).
The game should be paused if possible, etc...

<a id="unreal.ApplicationLifecycleComponent.application_will_deactivate_delegate"></a>

#### application_will_deactivate_delegate

```python
@application_will_deactivate_delegate.setter
def application_will_deactivate_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_has_reactivated_delegate"></a>

#### application_has_reactivated_delegate

```python
@property
def application_has_reactivated_delegate() -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] Called when the application has been reactivated (reverse any processing done in the Deactivate delegate)

<a id="unreal.ApplicationLifecycleComponent.application_has_reactivated_delegate"></a>

#### application_has_reactivated_delegate

```python
@application_has_reactivated_delegate.setter
def application_has_reactivated_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_will_enter_background_delegate"></a>

#### application_will_enter_background_delegate

```python
@property
def application_will_enter_background_delegate(
) -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] This is called when the application is being backgrounded (e.g., due to switching
to another app or closing it via the home button)
The game should release shared resources, save state, etc..., since it can be
terminated from the background state without any further warning.

<a id="unreal.ApplicationLifecycleComponent.application_will_enter_background_delegate"></a>

#### application_will_enter_background_delegate

```python
@application_will_enter_background_delegate.setter
def application_will_enter_background_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_has_entered_foreground_delegate"></a>

#### application_has_entered_foreground_delegate

```python
@property
def application_has_entered_foreground_delegate(
) -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] Called when the application is returning to the foreground (reverse any processing done in the EnterBackground delegate)

<a id="unreal.ApplicationLifecycleComponent.application_has_entered_foreground_delegate"></a>

#### application_has_entered_foreground_delegate

```python
@application_has_entered_foreground_delegate.setter
def application_has_entered_foreground_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_will_terminate_delegate"></a>

#### application_will_terminate_delegate

```python
@property
def application_will_terminate_delegate() -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] This *may* be called when the application is getting terminated by the OS.
There is no guarantee that this will ever be called on a mobile device,
save state when ApplicationWillEnterBackgroundDelegate is called instead.

<a id="unreal.ApplicationLifecycleComponent.application_will_terminate_delegate"></a>

#### application_will_terminate_delegate

```python
@application_will_terminate_delegate.setter
def application_will_terminate_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_should_unload_resources_delegate"></a>

#### application_should_unload_resources_delegate

```python
@property
def application_should_unload_resources_delegate(
) -> ApplicationLifetimeDelegate
```

(ApplicationLifetimeDelegate):  [Read-Write] Called when the OS is running low on resources and asks the application to free up any cached resources, drop graphics quality etc.

<a id="unreal.ApplicationLifecycleComponent.application_should_unload_resources_delegate"></a>

#### application_should_unload_resources_delegate

```python
@application_should_unload_resources_delegate.setter
def application_should_unload_resources_delegate(
        value: ApplicationLifetimeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.application_received_startup_arguments_delegate"></a>

#### application_received_startup_arguments_delegate

```python
@property
def application_received_startup_arguments_delegate(
) -> ApplicationStartupArgumentsDelegate
```

(ApplicationStartupArgumentsDelegate):  [Read-Write] Called with arguments passed to the application on statup, perhaps meta data passed on by another application which launched this one.

<a id="unreal.ApplicationLifecycleComponent.application_received_startup_arguments_delegate"></a>

#### application_received_startup_arguments_delegate

```python
@application_received_startup_arguments_delegate.setter
def application_received_startup_arguments_delegate(
        value: ApplicationStartupArgumentsDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.on_temperature_change_delegate"></a>

#### on_temperature_change_delegate

```python
@property
def on_temperature_change_delegate() -> OnTemperatureChangeDelegate
```

(OnTemperatureChangeDelegate):  [Read-Write] Called when temperature level has changed, and receives the severity

<a id="unreal.ApplicationLifecycleComponent.on_temperature_change_delegate"></a>

#### on_temperature_change_delegate

```python
@on_temperature_change_delegate.setter
def on_temperature_change_delegate(value: OnTemperatureChangeDelegate) -> None
```

<a id="unreal.ApplicationLifecycleComponent.on_low_power_mode_delegate"></a>

#### on_low_power_mode_delegate

```python
@property
def on_low_power_mode_delegate() -> OnLowPowerModeDelegate
```

(OnLowPowerModeDelegate):  [Read-Write] Called when we are in low power mode

<a id="unreal.ApplicationLifecycleComponent.on_low_power_mode_delegate"></a>

#### on_low_power_mode_delegate

```python
@on_low_power_mode_delegate.setter
def on_low_power_mode_delegate(value: OnLowPowerModeDelegate) -> None
```

<a id="unreal.ArrowComponent"></a>