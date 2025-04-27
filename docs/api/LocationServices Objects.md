## LocationServices Objects

```python
class LocationServices(BlueprintFunctionLibrary)
```

Location Services

**C++ Source:**

- **Plugin**: LocationServicesBPLibrary
- **Module**: LocationServicesBPLibrary
- **File**: LocationServicesBPLibrary.h

<a id="unreal.LocationServices.stop_location_services"></a>

#### stop_location_services

```python
@classmethod
def stop_location_services(cls) -> bool
```

X.stop_location_services() -> bool
Stops the updates of location from the Location Service that was started with StartLocationService

Returns:
    bool: true if stop is successful

<a id="unreal.LocationServices.start_location_services"></a>

#### start_location_services

```python
@classmethod
def start_location_services(cls) -> bool
```

X.start_location_services() -> bool
Starts requesting location updates from the appropriate Location Service

Returns:
    bool: true if startup successful

<a id="unreal.LocationServices.is_location_accuracy_available"></a>

#### is_location_accuracy_available

```python
@classmethod
def is_location_accuracy_available(cls, accuracy: LocationAccuracy) -> bool
```

X.is_location_accuracy_available(accuracy) -> bool
Checks if the supplied Accuracy is available on the current device.

Args:
    accuracy (LocationAccuracy): the accuracy to check

Returns:
    bool: true if the mobile device can support the Accuracy, false if it will use a different accuracy

<a id="unreal.LocationServices.init_location_services"></a>

#### init_location_services

```python
@classmethod
def init_location_services(cls, accuracy: LocationAccuracy,
                           update_frequency: float,
                           min_distance_filter: float) -> bool
```

X.init_location_services(accuracy, update_frequency, min_distance_filter) -> bool
Called to set up the Location Service before use

Args:
    accuracy (LocationAccuracy): as seen in the enum above
    update_frequency (float): in milliseconds. (Android only)
    min_distance_filter (float): 

Returns:
    bool: true if Initialization was succesful

<a id="unreal.LocationServices.get_location_services_impl"></a>

#### get_location_services_impl

```python
@classmethod
def get_location_services_impl(cls) -> LocationServicesImpl
```

X.get_location_services_impl() -> LocationServicesImpl
* Returns the Location Services implementation object. Intended to be used to set up the FLocationServicesData_OnLocationChanged
* delegate in Blueprints.
*

Returns:
    LocationServicesImpl: the Android or IOS impl object

<a id="unreal.LocationServices.get_last_known_location"></a>

#### get_last_known_location

```python
@classmethod
def get_last_known_location(cls) -> LocationServicesData
```

X.get_last_known_location() -> LocationServicesData
Returns the last location information returned by the location service. If no location update has been made, will return
a default-value-filled struct.

Returns:
    LocationServicesData: the last known location from updates

<a id="unreal.LocationServices.are_location_services_enabled"></a>

#### are_location_services_enabled

```python
@classmethod
def are_location_services_enabled(cls) -> bool
```

X.are_location_services_enabled() -> bool
Checks if the Location Services on the mobile device are enabled for this application

Returns:
    bool: true if the mobile device has enabled the appropriate service for the app

<a id="unreal.LocationServicesImpl"></a>