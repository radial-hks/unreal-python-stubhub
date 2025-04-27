## NiagaraDataChannelSearchParameters Objects

```python
class NiagaraDataChannelSearchParameters(StructBase)
```

Parameters used when retrieving a specific set of Data Channel Data to read or write.
Many Data Channel types will have multiple internal sets of data and these parameters control which the Channel should return to users for access.
An example of this would be the Islands Data Channel type which will subdivide the world and have a different set of data for each sub division.
It will return to users the correct data for their location based on these parameters.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannelPublic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write] In cases where there is no owning component for data being read or written to a data channel, we simply pass in a location. We can also use this when bOverrideLocaiton is set.
- ``override_location`` (bool):  [Read-Write] If true, even if an owning component is set, the data channel should use the Location value rather than the component location. If this is false, the NDC will get any location needed from the owning component.
- ``owning_component`` (SceneComponent):  [Read-Write] In cases where there is an owning component such as an object spawning from itself etc, then we pass that component in. Some handlers may only use it's location but others may make use of more data.

<a id="unreal.NiagaraDataChannelSearchParameters.__init__"></a>

#### __init__

```python
def __init__(owning_component: SceneComponent = None,
             location: Vector = [0.000000, 0.000000, 0.000000],
             override_location: bool = False) -> None
```

<a id="unreal.NiagaraDataChannelSearchParameters.owning_component"></a>

#### owning_component

```python
@property
def owning_component() -> SceneComponent
```

(SceneComponent):  [Read-Write] In cases where there is an owning component such as an object spawning from itself etc, then we pass that component in. Some handlers may only use it's location but others may make use of more data.

<a id="unreal.NiagaraDataChannelSearchParameters.owning_component"></a>

#### owning_component

```python
@owning_component.setter
def owning_component(value: SceneComponent) -> None
```

<a id="unreal.NiagaraDataChannelSearchParameters.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] In cases where there is no owning component for data being read or written to a data channel, we simply pass in a location. We can also use this when bOverrideLocaiton is set.

<a id="unreal.NiagaraDataChannelSearchParameters.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.NiagaraDataChannelSearchParameters.override_location"></a>

#### override_location

```python
@property
def override_location() -> bool
```

(bool):  [Read-Write] If true, even if an owning component is set, the data channel should use the Location value rather than the component location. If this is false, the NDC will get any location needed from the owning component.

<a id="unreal.NiagaraDataChannelSearchParameters.override_location"></a>

#### override_location

```python
@override_location.setter
def override_location(value: bool) -> None
```

<a id="unreal.BasicParticleData"></a>