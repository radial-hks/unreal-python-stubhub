## PlatformGameInstance Objects

```python
class PlatformGameInstance(GameInstance)
```

UObject based class for handling mobile events. Having this object as an option gives the app lifetime access to these global delegates. The component UApplicationLifecycleComponent is destroyed at level loads

**C++ Source:**

- **Module**: Engine
- **File**: BlueprintPlatformLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_failed_to_register_for_remote_notifications_delegate`` (PlatformFailedToRegisterForRemoteNotificationsDelegate):  [Read-Write] called when the application fails to register for remote notifications
- ``application_has_entered_foreground_delegate`` (PlatformDelegate):  [Read-Write] Called when the application is returning to the foreground (reverse any processing done in the EnterBackground delegate)
- ``application_has_reactivated_delegate`` (PlatformDelegate):  [Read-Write] Called when the application has been reactivated (reverse any processing done in the Deactivate delegate)
- ``application_received_local_notification_delegate`` (PlatformReceivedLocalNotificationDelegate):  [Read-Write] called when the application receives a local notification
- ``application_received_remote_notification_delegate`` (PlatformReceivedRemoteNotificationDelegate):  [Read-Write] called when the application receives a remote notification
- ``application_received_screen_orientation_changed_notification_delegate`` (PlatformScreenOrientationChangedDelegate):  [Read-Write] called when the application receives a screen orientation change notification
- ``application_received_startup_arguments_delegate`` (PlatformStartupArgumentsDelegate):  [Read-Write] Called with arguments passed to the application on statup, perhaps meta data passed on by another application which launched this one.
- ``application_registered_for_remote_notifications_delegate`` (PlatformRegisteredForRemoteNotificationsDelegate):  [Read-Write] called when the user grants permission to register for remote notifications
- ``application_registered_for_user_notifications_delegate`` (PlatformRegisteredForUserNotificationsDelegate):  [Read-Write] called when the user grants permission to register for notifications
- ``application_should_unload_resources_delegate`` (PlatformDelegate):  [Read-Write] Called when the OS is running low on resources and asks the application to free up any cached resources, drop graphics quality etc.
- ``application_will_deactivate_delegate`` (PlatformDelegate):  [Read-Write] This is called when the application is about to be deactivated (e.g., due to a phone call or SMS or the sleep button).
  The game should be paused if possible, etc...
- ``application_will_enter_background_delegate`` (PlatformDelegate):  [Read-Write] This is called when the application is being backgrounded (e.g., due to switching
  to another app or closing it via the home button)
  The game should release shared resources, save state, etc..., since it can be
  terminated from the background state without any further warning.
- ``application_will_terminate_delegate`` (PlatformDelegate):  [Read-Write] This *may* be called when the application is getting terminated by the OS.
  There is no guarantee that this will ever be called on a mobile device,
  save state when ApplicationWillEnterBackgroundDelegate is called instead.
- ``on_input_device_connection_change`` (OnUserInputDeviceConnectionChange):  [Read-Write] Callback for when an input device connection state has changed (a new gamepad was connected or disconnected)
- ``on_pawn_controller_changed_delegates`` (OnPawnControllerChanged):  [Read-Write] gets triggered shortly after a pawn's controller is set. Most of the time
      it signals that the Controller has changed but in edge cases (like during
      replication) it might end up broadcasting the same pawn-controller pair
      more than once
- ``on_user_input_device_pairing_change`` (OnUserInputDevicePairingChange):  [Read-Write] Callback when an input device has changed pairings (the owning platform user has changed for that device)

<a id="unreal.PlatformGameInstance.application_will_deactivate_delegate"></a>

#### application_will_deactivate_delegate

```python
@property
def application_will_deactivate_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] This is called when the application is about to be deactivated (e.g., due to a phone call or SMS or the sleep button).
The game should be paused if possible, etc...

<a id="unreal.PlatformGameInstance.application_will_deactivate_delegate"></a>

#### application_will_deactivate_delegate

```python
@application_will_deactivate_delegate.setter
def application_will_deactivate_delegate(value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_has_reactivated_delegate"></a>

#### application_has_reactivated_delegate

```python
@property
def application_has_reactivated_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] Called when the application has been reactivated (reverse any processing done in the Deactivate delegate)

<a id="unreal.PlatformGameInstance.application_has_reactivated_delegate"></a>

#### application_has_reactivated_delegate

```python
@application_has_reactivated_delegate.setter
def application_has_reactivated_delegate(value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_will_enter_background_delegate"></a>

#### application_will_enter_background_delegate

```python
@property
def application_will_enter_background_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] This is called when the application is being backgrounded (e.g., due to switching
to another app or closing it via the home button)
The game should release shared resources, save state, etc..., since it can be
terminated from the background state without any further warning.

<a id="unreal.PlatformGameInstance.application_will_enter_background_delegate"></a>

#### application_will_enter_background_delegate

```python
@application_will_enter_background_delegate.setter
def application_will_enter_background_delegate(
        value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_has_entered_foreground_delegate"></a>

#### application_has_entered_foreground_delegate

```python
@property
def application_has_entered_foreground_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] Called when the application is returning to the foreground (reverse any processing done in the EnterBackground delegate)

<a id="unreal.PlatformGameInstance.application_has_entered_foreground_delegate"></a>

#### application_has_entered_foreground_delegate

```python
@application_has_entered_foreground_delegate.setter
def application_has_entered_foreground_delegate(
        value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_will_terminate_delegate"></a>

#### application_will_terminate_delegate

```python
@property
def application_will_terminate_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] This *may* be called when the application is getting terminated by the OS.
There is no guarantee that this will ever be called on a mobile device,
save state when ApplicationWillEnterBackgroundDelegate is called instead.

<a id="unreal.PlatformGameInstance.application_will_terminate_delegate"></a>

#### application_will_terminate_delegate

```python
@application_will_terminate_delegate.setter
def application_will_terminate_delegate(value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_should_unload_resources_delegate"></a>

#### application_should_unload_resources_delegate

```python
@property
def application_should_unload_resources_delegate() -> PlatformDelegate
```

(PlatformDelegate):  [Read-Write] Called when the OS is running low on resources and asks the application to free up any cached resources, drop graphics quality etc.

<a id="unreal.PlatformGameInstance.application_should_unload_resources_delegate"></a>

#### application_should_unload_resources_delegate

```python
@application_should_unload_resources_delegate.setter
def application_should_unload_resources_delegate(
        value: PlatformDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_received_startup_arguments_delegate"></a>

#### application_received_startup_arguments_delegate

```python
@property
def application_received_startup_arguments_delegate(
) -> PlatformStartupArgumentsDelegate
```

(PlatformStartupArgumentsDelegate):  [Read-Write] Called with arguments passed to the application on statup, perhaps meta data passed on by another application which launched this one.

<a id="unreal.PlatformGameInstance.application_received_startup_arguments_delegate"></a>

#### application_received_startup_arguments_delegate

```python
@application_received_startup_arguments_delegate.setter
def application_received_startup_arguments_delegate(
        value: PlatformStartupArgumentsDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_registered_for_remote_notifications_delegate"></a>

#### application_registered_for_remote_notifications_delegate

```python
@property
def application_registered_for_remote_notifications_delegate(
) -> PlatformRegisteredForRemoteNotificationsDelegate
```

(PlatformRegisteredForRemoteNotificationsDelegate):  [Read-Write] called when the user grants permission to register for remote notifications

<a id="unreal.PlatformGameInstance.application_registered_for_remote_notifications_delegate"></a>

#### application_registered_for_remote_notifications_delegate

```python
@application_registered_for_remote_notifications_delegate.setter
def application_registered_for_remote_notifications_delegate(
        value: PlatformRegisteredForRemoteNotificationsDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_registered_for_user_notifications_delegate"></a>

#### application_registered_for_user_notifications_delegate

```python
@property
def application_registered_for_user_notifications_delegate(
) -> PlatformRegisteredForUserNotificationsDelegate
```

(PlatformRegisteredForUserNotificationsDelegate):  [Read-Write] called when the user grants permission to register for notifications

<a id="unreal.PlatformGameInstance.application_registered_for_user_notifications_delegate"></a>

#### application_registered_for_user_notifications_delegate

```python
@application_registered_for_user_notifications_delegate.setter
def application_registered_for_user_notifications_delegate(
        value: PlatformRegisteredForUserNotificationsDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_failed_to_register_for_remote_notifications_delegate"></a>

#### application_failed_to_register_for_remote_notifications_delegate

```python
@property
def application_failed_to_register_for_remote_notifications_delegate(
) -> PlatformFailedToRegisterForRemoteNotificationsDelegate
```

(PlatformFailedToRegisterForRemoteNotificationsDelegate):  [Read-Write] called when the application fails to register for remote notifications

<a id="unreal.PlatformGameInstance.application_failed_to_register_for_remote_notifications_delegate"></a>

#### application_failed_to_register_for_remote_notifications_delegate

```python
@application_failed_to_register_for_remote_notifications_delegate.setter
def application_failed_to_register_for_remote_notifications_delegate(
        value: PlatformFailedToRegisterForRemoteNotificationsDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_received_remote_notification_delegate"></a>

#### application_received_remote_notification_delegate

```python
@property
def application_received_remote_notification_delegate(
) -> PlatformReceivedRemoteNotificationDelegate
```

(PlatformReceivedRemoteNotificationDelegate):  [Read-Write] called when the application receives a remote notification

<a id="unreal.PlatformGameInstance.application_received_remote_notification_delegate"></a>

#### application_received_remote_notification_delegate

```python
@application_received_remote_notification_delegate.setter
def application_received_remote_notification_delegate(
        value: PlatformReceivedRemoteNotificationDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_received_local_notification_delegate"></a>

#### application_received_local_notification_delegate

```python
@property
def application_received_local_notification_delegate(
) -> PlatformReceivedLocalNotificationDelegate
```

(PlatformReceivedLocalNotificationDelegate):  [Read-Write] called when the application receives a local notification

<a id="unreal.PlatformGameInstance.application_received_local_notification_delegate"></a>

#### application_received_local_notification_delegate

```python
@application_received_local_notification_delegate.setter
def application_received_local_notification_delegate(
        value: PlatformReceivedLocalNotificationDelegate) -> None
```

<a id="unreal.PlatformGameInstance.application_received_screen_orientation_changed_notification_delegate"></a>

#### application_received_screen_orientation_changed_notification_delegate

```python
@property
def application_received_screen_orientation_changed_notification_delegate(
) -> PlatformScreenOrientationChangedDelegate
```

(PlatformScreenOrientationChangedDelegate):  [Read-Write] called when the application receives a screen orientation change notification

<a id="unreal.PlatformGameInstance.application_received_screen_orientation_changed_notification_delegate"></a>

#### application_received_screen_orientation_changed_notification_delegate

```python
@application_received_screen_orientation_changed_notification_delegate.setter
def application_received_screen_orientation_changed_notification_delegate(
        value: PlatformScreenOrientationChangedDelegate) -> None
```

<a id="unreal.PlatformLibrary"></a>