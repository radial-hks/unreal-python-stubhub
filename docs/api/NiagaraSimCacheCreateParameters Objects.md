## NiagaraSimCacheCreateParameters Objects

```python
class NiagaraSimCacheCreateParameters(StructBase)
```

Niagara Sim Cache Create Parameters

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSimCache.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_data_interface_caching`` (bool):  [Read-Write] When enabled Data Interface data will be stored in the SimCache.
  This can result in a large increase to the cache size, depending on what Data Interfaces are used
- ``allow_interpolation`` (bool):  [Read-Write] When enabled we allow the cache to be generated for interpolation.
  This will increase the memory usage for the cache slightly but can allow you to reduce the capture rate.
  By default we will capture and interpolate all Position & Quat types, you can adjust this using the include / exclude list.
- ``allow_rebasing`` (bool):  [Read-Write] When enabled allows the SimCache to be re-based.
  i.e. World space emitters can be moved to the new component's location
- ``allow_serialize_large_cache`` (bool):  [Read-Write] When enabled the cache will support serializing large amounts of cache data.
- ``allow_velocity_extrapolation`` (bool):  [Read-Write] When enabled we allow the cache to be generated for extrapolation.
  This will force the velocity attribute to be maintained.
- ``attribute_capture_mode`` (NiagaraSimCacheAttributeCaptureMode):  [Read-Write] How do we want to capture attributes for the simulation cache.
  The mode selected depends on what situations the cache can be used in.
- ``explicit_capture_attributes`` (Array[Name]):  [Read-Write] List of attributes to capture when the capture attribute capture mode is set to explicit.
  For example, adding MyEmitter.Particles.Position will only gather that attribute inside the cache.
- ``include_debug_data`` (bool):  [Read-Write] When enabled additional information is stored that can be useful for debugging a simulation
- ``interpolation_exclude_attributes`` (Array[Name]):  [Read-Write] List of specific Attributes to exclude interpolation for.  They must be types that are supported for interpolation.
  For example, MyEmitter.Particles.MyPosition would force MyPosition to be interpolated.
- ``interpolation_include_attributes`` (Array[Name]):  [Read-Write] List of specific Attributes to include when using interpolation.  They must be types that are supported for interpolation.
  For example, MyEmitter.Particles.MyPosition would force MyPosition to be interpolated.
- ``rebase_exclude_attributes`` (Array[Name]):  [Read-Write] List of Attributes to force exclude from the SimCache rebase, they should be the full path to the attribute
  For example, MyEmitter.Particles.MyQuat would force the particle attribute MyQuat to be included for MyEmitter
- ``rebase_include_attributes`` (Array[Name]):  [Read-Write] List of Attributes to force include in the SimCache rebase, they should be the full path to the attribute
  For example, MyEmitter.Particles.MyQuat would force the particle attribute MyQuat to be included for MyEmitter

<a id="unreal.NiagaraSimCacheCreateParameters.__init__"></a>

#### __init__

```python
def __init__(
        attribute_capture_mode:
    NiagaraSimCacheAttributeCaptureMode = NiagaraSimCacheAttributeCaptureMode.
    ALL,
        allow_rebasing: bool = False,
        allow_data_interface_caching: bool = False,
        allow_interpolation: bool = False,
        allow_velocity_extrapolation: bool = False,
        allow_serialize_large_cache: bool = False,
        include_debug_data: bool = False,
        rebase_include_attributes: Array[Name] = [],
        rebase_exclude_attributes: Array[Name] = [],
        interpolation_include_attributes: Array[Name] = [],
        interpolation_exclude_attributes: Array[Name] = [],
        explicit_capture_attributes: Array[Name] = []) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.attribute_capture_mode"></a>

#### attribute_capture_mode

```python
@property
def attribute_capture_mode() -> NiagaraSimCacheAttributeCaptureMode
```

(NiagaraSimCacheAttributeCaptureMode):  [Read-Write] How do we want to capture attributes for the simulation cache.
The mode selected depends on what situations the cache can be used in.

<a id="unreal.NiagaraSimCacheCreateParameters.attribute_capture_mode"></a>

#### attribute_capture_mode

```python
@attribute_capture_mode.setter
def attribute_capture_mode(value: NiagaraSimCacheAttributeCaptureMode) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.allow_rebasing"></a>

#### allow_rebasing

```python
@property
def allow_rebasing() -> bool
```

(bool):  [Read-Write] When enabled allows the SimCache to be re-based.
i.e. World space emitters can be moved to the new component's location

<a id="unreal.NiagaraSimCacheCreateParameters.allow_rebasing"></a>

#### allow_rebasing

```python
@allow_rebasing.setter
def allow_rebasing(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.allow_data_interface_caching"></a>

#### allow_data_interface_caching

```python
@property
def allow_data_interface_caching() -> bool
```

(bool):  [Read-Write] When enabled Data Interface data will be stored in the SimCache.
This can result in a large increase to the cache size, depending on what Data Interfaces are used

<a id="unreal.NiagaraSimCacheCreateParameters.allow_data_interface_caching"></a>

#### allow_data_interface_caching

```python
@allow_data_interface_caching.setter
def allow_data_interface_caching(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.allow_interpolation"></a>

#### allow_interpolation

```python
@property
def allow_interpolation() -> bool
```

(bool):  [Read-Write] When enabled we allow the cache to be generated for interpolation.
This will increase the memory usage for the cache slightly but can allow you to reduce the capture rate.
By default we will capture and interpolate all Position & Quat types, you can adjust this using the include / exclude list.

<a id="unreal.NiagaraSimCacheCreateParameters.allow_interpolation"></a>

#### allow_interpolation

```python
@allow_interpolation.setter
def allow_interpolation(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.allow_velocity_extrapolation"></a>

#### allow_velocity_extrapolation

```python
@property
def allow_velocity_extrapolation() -> bool
```

(bool):  [Read-Write] When enabled we allow the cache to be generated for extrapolation.
This will force the velocity attribute to be maintained.

<a id="unreal.NiagaraSimCacheCreateParameters.allow_velocity_extrapolation"></a>

#### allow_velocity_extrapolation

```python
@allow_velocity_extrapolation.setter
def allow_velocity_extrapolation(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.allow_serialize_large_cache"></a>

#### allow_serialize_large_cache

```python
@property
def allow_serialize_large_cache() -> bool
```

(bool):  [Read-Write] When enabled the cache will support serializing large amounts of cache data.

<a id="unreal.NiagaraSimCacheCreateParameters.allow_serialize_large_cache"></a>

#### allow_serialize_large_cache

```python
@allow_serialize_large_cache.setter
def allow_serialize_large_cache(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.include_debug_data"></a>

#### include_debug_data

```python
@property
def include_debug_data() -> bool
```

(bool):  [Read-Write] When enabled additional information is stored that can be useful for debugging a simulation

<a id="unreal.NiagaraSimCacheCreateParameters.include_debug_data"></a>

#### include_debug_data

```python
@include_debug_data.setter
def include_debug_data(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.rebase_include_attributes"></a>

#### rebase_include_attributes

```python
@property
def rebase_include_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write] List of Attributes to force include in the SimCache rebase, they should be the full path to the attribute
For example, MyEmitter.Particles.MyQuat would force the particle attribute MyQuat to be included for MyEmitter

<a id="unreal.NiagaraSimCacheCreateParameters.rebase_include_attributes"></a>

#### rebase_include_attributes

```python
@rebase_include_attributes.setter
def rebase_include_attributes(value: Array[Name]) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.rebase_exclude_attributes"></a>

#### rebase_exclude_attributes

```python
@property
def rebase_exclude_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write] List of Attributes to force exclude from the SimCache rebase, they should be the full path to the attribute
For example, MyEmitter.Particles.MyQuat would force the particle attribute MyQuat to be included for MyEmitter

<a id="unreal.NiagaraSimCacheCreateParameters.rebase_exclude_attributes"></a>

#### rebase_exclude_attributes

```python
@rebase_exclude_attributes.setter
def rebase_exclude_attributes(value: Array[Name]) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.interpolation_include_attributes"></a>

#### interpolation_include_attributes

```python
@property
def interpolation_include_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write] List of specific Attributes to include when using interpolation.  They must be types that are supported for interpolation.
For example, MyEmitter.Particles.MyPosition would force MyPosition to be interpolated.

<a id="unreal.NiagaraSimCacheCreateParameters.interpolation_include_attributes"></a>

#### interpolation_include_attributes

```python
@interpolation_include_attributes.setter
def interpolation_include_attributes(value: Array[Name]) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.interpolation_exclude_attributes"></a>

#### interpolation_exclude_attributes

```python
@property
def interpolation_exclude_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write] List of specific Attributes to exclude interpolation for.  They must be types that are supported for interpolation.
For example, MyEmitter.Particles.MyPosition would force MyPosition to be interpolated.

<a id="unreal.NiagaraSimCacheCreateParameters.interpolation_exclude_attributes"></a>

#### interpolation_exclude_attributes

```python
@interpolation_exclude_attributes.setter
def interpolation_exclude_attributes(value: Array[Name]) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters.explicit_capture_attributes"></a>

#### explicit_capture_attributes

```python
@property
def explicit_capture_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write] List of attributes to capture when the capture attribute capture mode is set to explicit.
For example, adding MyEmitter.Particles.Position will only gather that attribute inside the cache.

<a id="unreal.NiagaraSimCacheCreateParameters.explicit_capture_attributes"></a>

#### explicit_capture_attributes

```python
@explicit_capture_attributes.setter
def explicit_capture_attributes(value: Array[Name]) -> None
```

<a id="unreal.SphericalPontoon"></a>