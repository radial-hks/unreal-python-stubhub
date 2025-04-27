## PlatformLibrary Objects

```python
class PlatformLibrary(BlueprintFunctionLibrary)
```

Blueprint Platform Library

**C++ Source:**

- **Module**: Engine
- **File**: BlueprintPlatformLibrary.h

<a id="unreal.PlatformLibrary.set_allowed_device_orientation"></a>

#### set_allowed_device_orientation

```python
@classmethod
def set_allowed_device_orientation(
        cls, new_allowed_device_orientation: ScreenOrientation) -> None
```

X.set_allowed_device_orientation(new_allowed_device_orientation) -> None
Set the allowed orientation of the device.

Args:
    new_allowed_device_orientation (ScreenOrientation):

<a id="unreal.PlatformLibrary.schedule_local_notification_from_now"></a>

#### schedule_local_notification_from_now

```python
@classmethod
def schedule_local_notification_from_now(cls, in_seconds_from_now: int,
                                         title: Text, body: Text, action: Text,
                                         activation_event: str) -> int
```

X.schedule_local_notification_from_now(in_seconds_from_now, title, body, action, activation_event) -> int32
Schedule a local notification to fire inSecondsFromNow from now

Args:
    in_seconds_from_now (int32): The seconds until the notification should fire
    title (Text): The title of the notification
    body (Text): The more detailed description of the notification
    action (Text): The text to be displayed on the slider controller
    activation_event (str): A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

Returns:
    int32:

<a id="unreal.PlatformLibrary.schedule_local_notification_badge_from_now"></a>

#### schedule_local_notification_badge_from_now

```python
@classmethod
def schedule_local_notification_badge_from_now(cls, in_seconds_from_now: int,
                                               activation_event: str) -> None
```

X.schedule_local_notification_badge_from_now(in_seconds_from_now, activation_event) -> None
Schedule a local notification badge to fire inSecondsFromNow from now

Args:
    in_seconds_from_now (int32): The seconds until the notification should fire
    activation_event (str): A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

<a id="unreal.PlatformLibrary.schedule_local_notification_badge_at_time"></a>

#### schedule_local_notification_badge_at_time

```python
@classmethod
def schedule_local_notification_badge_at_time(cls, fire_date_time: DateTime,
                                              local_time: bool,
                                              activation_event: str) -> int
```

X.schedule_local_notification_badge_at_time(fire_date_time, local_time, activation_event) -> int32
Schedule a local notification badge at a specific time, inLocalTime specifies the current local time or if UTC time should be used

Args:
    fire_date_time (DateTime): The time at which to fire the local notification
    local_time (bool): If true the provided time is in the local timezone, if false it is in UTC
    activation_event (str): A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

Returns:
    int32:

<a id="unreal.PlatformLibrary.schedule_local_notification_at_time"></a>

#### schedule_local_notification_at_time

```python
@classmethod
def schedule_local_notification_at_time(cls, fire_date_time: DateTime,
                                        local_time: bool, title: Text,
                                        body: Text, action: Text,
                                        activation_event: str) -> int
```

X.schedule_local_notification_at_time(fire_date_time, local_time, title, body, action, activation_event) -> int32
Schedule a local notification at a specific time, inLocalTime specifies the current local time or if UTC time should be used

Args:
    fire_date_time (DateTime): The time at which to fire the local notification
    local_time (bool): If true the provided time is in the local timezone, if false it is in UTC
    title (Text): The title of the notification
    body (Text): The more detailed description of the notification
    action (Text): The text to be displayed on the slider controller
    activation_event (str): A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

Returns:
    int32:

<a id="unreal.PlatformLibrary.get_launch_notification"></a>

#### get_launch_notification

```python
@classmethod
def get_launch_notification(cls) -> Tuple[bool, str, int]
```

X.get_launch_notification() -> (notification_launched_app=bool, activation_event=str, fire_date=int32)
Get the local notification that was used to launch the app

Returns:
    tuple: 

    notification_launched_app (bool): Return true if a notification was used to launch the app

    activation_event (str): Returns the name of the ActivationEvent if a notification was used to launch the app

    fire_date (int32): Returns the time the notification was activated

<a id="unreal.PlatformLibrary.get_device_orientation"></a>

#### get_device_orientation

```python
@classmethod
def get_device_orientation(cls) -> ScreenOrientation
```

X.get_device_orientation() -> ScreenOrientation
Returns the current orientation of the device: will be either Portrait, LandscapeLeft, PortraitUpsideDown or LandscapeRight.

Returns:
    ScreenOrientation: An EDeviceScreenOrientation value.

<a id="unreal.PlatformLibrary.get_allowed_device_orientation"></a>

#### get_allowed_device_orientation

```python
@classmethod
def get_allowed_device_orientation(cls) -> ScreenOrientation
```

X.get_allowed_device_orientation() -> ScreenOrientation
Returns the allowed orientation of the device. This is NOT the same as GetDeviceOrientation, which only returns Portrait, LandscapeLeft,
PortraitUpsideDown or LandscapeRight. The allowed orientation limits what orientation your device can have. So if you set the allowed orientation
to LandscapeLeft, GetDeviceOrientation will only ever return LandscapeLeft. But if you set the allowed orientation to LandscapeSensor, you are actually
restricting the allowed orientations to LandscapeLeft OR LandscapeRight (depending on the sensor), so GetDeviceOrientation might return LandscapeLeft OR LandscapeRight.

Returns:
    ScreenOrientation: An EDeviceScreenOrientation value.

<a id="unreal.PlatformLibrary.clear_all_local_notifications"></a>

#### clear_all_local_notifications

```python
@classmethod
def clear_all_local_notifications(cls) -> None
```

X.clear_all_local_notifications() -> None
Clear all pending local notifications. Typically this will be done before scheduling new notifications when going into the background

<a id="unreal.PlatformLibrary.cancel_local_notification_by_id"></a>

#### cancel_local_notification_by_id

```python
@classmethod
def cancel_local_notification_by_id(cls, notification_id: int) -> None
```

X.cancel_local_notification_by_id(notification_id) -> None
Cancel a local notification given the ActivationEvent

Args:
    notification_id (int32): The Id returned from one of the ScheduleLocalNotification* functions

<a id="unreal.PlatformLibrary.cancel_local_notification"></a>

#### cancel_local_notification

```python
@classmethod
def cancel_local_notification(cls, activation_event: str) -> None
```

X.cancel_local_notification(activation_event) -> None
Cancel a local notification given the ActivationEvent

Args:
    activation_event (str): The string passed into the Schedule call for the notification to be cancelled

<a id="unreal.ImportanceSamplingLibrary"></a>