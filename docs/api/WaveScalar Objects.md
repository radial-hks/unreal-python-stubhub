## WaveScalar Objects

```python
class WaveScalar(FieldNodeFloat)
```

Set a temporal wave scalar value according to the sample distance from the field position.

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``falloff`` (FieldFalloffType):  [Read-Write] Type of falloff function used if the falloff function is picked
- ``function`` (WaveFunctionType):  [Read-Write] Wave function used for the field
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``magnitude`` (float):  [Read-Write] Magnitude of the wave function
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``period`` (float):  [Read-Write] Time over which the wave will travel from one peak to another one. The wave velocity is proportional to wavelength/period
- ``position`` (Vector):  [Read-Write] Center position of the wave field
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``wavelength`` (float):  [Read-Write] Distance between 2 wave peaks

<a id="unreal.WaveScalar.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write] Magnitude of the wave function

<a id="unreal.WaveScalar.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.WaveScalar.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Center position of the wave field

<a id="unreal.WaveScalar.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.WaveScalar.wavelength"></a>

#### wavelength

```python
@property
def wavelength() -> float
```

(float):  [Read-Write] Distance between 2 wave peaks

<a id="unreal.WaveScalar.wavelength"></a>

#### wavelength

```python
@wavelength.setter
def wavelength(value: float) -> None
```

<a id="unreal.WaveScalar.period"></a>

#### period

```python
@property
def period() -> float
```

(float):  [Read-Write] Time over which the wave will travel from one peak to another one. The wave velocity is proportional to wavelength/period

<a id="unreal.WaveScalar.period"></a>

#### period

```python
@period.setter
def period(value: float) -> None
```

<a id="unreal.WaveScalar.function"></a>

#### function

```python
@property
def function() -> WaveFunctionType
```

(WaveFunctionType):  [Read-Write] Wave function used for the field

<a id="unreal.WaveScalar.function"></a>

#### function

```python
@function.setter
def function(value: WaveFunctionType) -> None
```

<a id="unreal.WaveScalar.falloff"></a>

#### falloff

```python
@property
def falloff() -> FieldFalloffType
```

(FieldFalloffType):  [Read-Write] Type of falloff function used if the falloff function is picked

<a id="unreal.WaveScalar.falloff"></a>

#### falloff

```python
@falloff.setter
def falloff(value: FieldFalloffType) -> None
```

<a id="unreal.WaveScalar.set_wave_scalar"></a>

#### set_wave_scalar

```python
def set_wave_scalar(magnitude: float = 1.000000,
                    position: Vector = ...,
                    wavelength: float = 1000.000000,
                    period: float = 1.000000,
                    time: float = ...,
                    function: WaveFunctionType = ...,
                    falloff: FieldFalloffType = ...) -> WaveScalar
```

x.set_wave_scalar(magnitude=1.000000, position, wavelength=1000.000000, period=1.000000, time, function, falloff) -> WaveScalar
Set a temporal wave scalar value according to the sample distance from the field position.

Args:
    magnitude (float): Magnitude of the wave function
    position (Vector): Center position of the wave field
    wavelength (float): Distance between 2 wave peaks
    period (float): Time over which the wave will travel from one peak to another one. The wave velocity is proportional to wavelength/period
    time (float): 
    function (WaveFunctionType): Wave function used for the field
    falloff (FieldFalloffType): Type of falloff function used if the falloff function is picked

Returns:
    WaveScalar:

<a id="unreal.RadialFalloff"></a>