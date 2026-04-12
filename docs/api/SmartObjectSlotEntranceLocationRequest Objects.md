## SmartObjectSlotEntranceLocationRequest Objects

```python
class SmartObjectSlotEntranceLocationRequest(StructBase)
```

Struct used to request slot entry or exit location.

When used with actor, it is generally enough to set the UserActor. In that case NavigationData, ValidationFilter,
and UserCapsule are queried via the INavAgentInterface and USmartObjectUserComponent on the actor if they are _not_ set.

If the user actor is not available (e.g. with Mass), then ValidationFilter and UserCapsule must be defined, and if bProjectNavigationLocation is set NavigationData must be valid.

The location validation is done in following order:
 - navigation projection
 - trace ground location (uses altered location from navigation test if applicable)
 - check transition trajectory (test between unmodified navigation location and slow location)

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_entrance_location_overlap`` (bool):  [Read-Write] If true, check user capsule collisions at the entrance location. Uses capsule dimensions set in the validation filter.
- ``check_slot_location_overlap`` (bool):  [Read-Write] If true, check user capsule collisions at the slot location. Uses capsule dimensions set in an annotation on the slot.
- ``check_transition_trajectory`` (bool):  [Read-Write] If true, check collisions between navigation location and slot location. If collisions are found, an entry is discarded.
- ``location_type`` (SmartObjectSlotNavigationLocationType):  [Read-Write] Enum indicating if we're looking for a location to enter or exit the Smart Object slot.
- ``navigation_data`` (NavigationData):  [Read-Write] Navigation data to use for the navigation queries. If not set and UserActor is valid, the navigation data is queried via INavAgentInterface.
- ``project_navigation_location`` (bool):  [Read-Write] If true, try to project the location on navigable area. If projection fails, an entry is discarded.
- ``search_location`` (Vector):  [Read-Write] Search location that may be used to select an entry from multiple candidates. (e.g. user actor location).
- ``select_method`` (FSmartObjectSlotEntrySelectionMethod):  [Read-Write] How to select an entry when a slot has multiple entries.
- ``trace_ground_location`` (bool):  [Read-Write] If true, try to trace the location on ground. If trace fails, an entry is discarded.
- ``use_slot_location_as_fallback`` (bool):  [Read-Write] If true, include slot location as a candidate if no navigation annotation is present.
- ``user_actor`` (Actor):  [Read-Write] Actor that is using the smart object slot. (Optional)
- ``user_capsule_params`` (SmartObjectUserCapsuleParams):  [Read-Write] Size of the user of the smart object. If not set and UserActor is valid, the dimensions are queried via INavAgentInterface.
- ``validation_filter`` (type(Class)):  [Read-Write] Filter to use for the validation. If not set and UserActor is valid, the filter is queried via USmartObjectUserComponent.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        user_actor: Actor = None,
        validation_filter: Class = None,
        navigation_data: NavigationData = None,
        user_capsule_params: SmartObjectUserCapsuleParams = [
            35.000000, 180.000000, 50.000000
        ],
        search_location: Vector = [0.000000, 0.000000, 0.000000],
        select_method:
    FSmartObjectSlotEntrySelectionMethod = FSmartObjectSlotEntrySelectionMethod
    .FIRST,
        location_type:
    SmartObjectSlotNavigationLocationType = SmartObjectSlotNavigationLocationType
    .ENTRY,
        project_navigation_location: bool = False,
        trace_ground_location: bool = False,
        check_transition_trajectory: bool = False,
        check_entrance_location_overlap: bool = False,
        check_slot_location_overlap: bool = False,
        use_slot_location_as_fallback: bool = False) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.user_actor"></a>

#### user\_actor

```python
@property
def user_actor() -> Actor
```

(Actor):  [Read-Write] Actor that is using the smart object slot. (Optional)

<a id="unreal.SmartObjectSlotEntranceLocationRequest.user_actor"></a>

#### user\_actor

```python
@user_actor.setter
def user_actor(value: Actor) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.validation_filter"></a>

#### validation\_filter

```python
@property
def validation_filter() -> Class
```

(type(Class)):  [Read-Write] Filter to use for the validation. If not set and UserActor is valid, the filter is queried via USmartObjectUserComponent.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.validation_filter"></a>

#### validation\_filter

```python
@validation_filter.setter
def validation_filter(value: Class) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.navigation_data"></a>

#### navigation\_data

```python
@property
def navigation_data() -> NavigationData
```

(NavigationData):  [Read-Write] Navigation data to use for the navigation queries. If not set and UserActor is valid, the navigation data is queried via INavAgentInterface.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.navigation_data"></a>

#### navigation\_data

```python
@navigation_data.setter
def navigation_data(value: NavigationData) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.user_capsule_params"></a>

#### user\_capsule\_params

```python
@property
def user_capsule_params() -> SmartObjectUserCapsuleParams
```

(SmartObjectUserCapsuleParams):  [Read-Write] Size of the user of the smart object. If not set and UserActor is valid, the dimensions are queried via INavAgentInterface.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.user_capsule_params"></a>

#### user\_capsule\_params

```python
@user_capsule_params.setter
def user_capsule_params(value: SmartObjectUserCapsuleParams) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.search_location"></a>

#### search\_location

```python
@property
def search_location() -> Vector
```

(Vector):  [Read-Write] Search location that may be used to select an entry from multiple candidates. (e.g. user actor location).

<a id="unreal.SmartObjectSlotEntranceLocationRequest.search_location"></a>

#### search\_location

```python
@search_location.setter
def search_location(value: Vector) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.select_method"></a>

#### select\_method

```python
@property
def select_method() -> FSmartObjectSlotEntrySelectionMethod
```

(FSmartObjectSlotEntrySelectionMethod):  [Read-Write] How to select an entry when a slot has multiple entries.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.select_method"></a>

#### select\_method

```python
@select_method.setter
def select_method(value: FSmartObjectSlotEntrySelectionMethod) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.location_type"></a>

#### location\_type

```python
@property
def location_type() -> SmartObjectSlotNavigationLocationType
```

(SmartObjectSlotNavigationLocationType):  [Read-Write] Enum indicating if we're looking for a location to enter or exit the Smart Object slot.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.location_type"></a>

#### location\_type

```python
@location_type.setter
def location_type(value: SmartObjectSlotNavigationLocationType) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.project_navigation_location"></a>

#### project\_navigation\_location

```python
@property
def project_navigation_location() -> bool
```

(bool):  [Read-Write] If true, try to project the location on navigable area. If projection fails, an entry is discarded.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.project_navigation_location"></a>

#### project\_navigation\_location

```python
@project_navigation_location.setter
def project_navigation_location(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.trace_ground_location"></a>

#### trace\_ground\_location

```python
@property
def trace_ground_location() -> bool
```

(bool):  [Read-Write] If true, try to trace the location on ground. If trace fails, an entry is discarded.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.trace_ground_location"></a>

#### trace\_ground\_location

```python
@trace_ground_location.setter
def trace_ground_location(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_transition_trajectory"></a>

#### check\_transition\_trajectory

```python
@property
def check_transition_trajectory() -> bool
```

(bool):  [Read-Write] If true, check collisions between navigation location and slot location. If collisions are found, an entry is discarded.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_transition_trajectory"></a>

#### check\_transition\_trajectory

```python
@check_transition_trajectory.setter
def check_transition_trajectory(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_entrance_location_overlap"></a>

#### check\_entrance\_location\_overlap

```python
@property
def check_entrance_location_overlap() -> bool
```

(bool):  [Read-Write] If true, check user capsule collisions at the entrance location. Uses capsule dimensions set in the validation filter.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_entrance_location_overlap"></a>

#### check\_entrance\_location\_overlap

```python
@check_entrance_location_overlap.setter
def check_entrance_location_overlap(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_slot_location_overlap"></a>

#### check\_slot\_location\_overlap

```python
@property
def check_slot_location_overlap() -> bool
```

(bool):  [Read-Write] If true, check user capsule collisions at the slot location. Uses capsule dimensions set in an annotation on the slot.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.check_slot_location_overlap"></a>

#### check\_slot\_location\_overlap

```python
@check_slot_location_overlap.setter
def check_slot_location_overlap(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationRequest.use_slot_location_as_fallback"></a>

#### use\_slot\_location\_as\_fallback

```python
@property
def use_slot_location_as_fallback() -> bool
```

(bool):  [Read-Write] If true, include slot location as a candidate if no navigation annotation is present.

<a id="unreal.SmartObjectSlotEntranceLocationRequest.use_slot_location_as_fallback"></a>

#### use\_slot\_location\_as\_fallback

```python
@use_slot_location_as_fallback.setter
def use_slot_location_as_fallback(value: bool) -> None
```

<a id="unreal.SmartObjectSlotEntranceLocationResult"></a>