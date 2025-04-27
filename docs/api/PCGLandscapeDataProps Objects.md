## PCGLandscapeDataProps Objects

```python
class PCGLandscapeDataProps(StructBase)
```

PCGLandscape Data Props

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLandscapeData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``get_actor_reference`` (bool):  [Read-Write] Controls whether the points from this landscape will return the actor from which they originate (e.g. which Landscape Proxy)
- ``get_component_coordinates`` (bool):  [Read-Write] Controls whether the component coordinates will be added the point as attributes ('CoordinateX', 'CoordinateY')
- ``get_height_only`` (bool):  [Read-Write] Controls whether the points projected on the landscape will return the normal/tangent (if false) or only the position (if true)
- ``get_layer_weights`` (bool):  [Read-Write] Controls whether data from landscape layers will be retrieved (turning it off is an optimization if that data is not needed)
- ``get_physical_material`` (bool):  [Read-Write] Controls whether the points from the landscape will have their physical material added as the "PhysicalMaterial" attribute

<a id="unreal.PCGLandscapeDataProps.__init__"></a>

#### __init__

```python
def __init__(get_height_only: bool = False,
             get_layer_weights: bool = False,
             get_actor_reference: bool = False,
             get_physical_material: bool = False,
             get_component_coordinates: bool = False) -> None
```

<a id="unreal.PCGLandscapeDataProps.get_height_only"></a>

#### get_height_only

```python
@property
def get_height_only() -> bool
```

(bool):  [Read-Write] Controls whether the points projected on the landscape will return the normal/tangent (if false) or only the position (if true)

<a id="unreal.PCGLandscapeDataProps.get_height_only"></a>

#### get_height_only

```python
@get_height_only.setter
def get_height_only(value: bool) -> None
```

<a id="unreal.PCGLandscapeDataProps.get_layer_weights"></a>

#### get_layer_weights

```python
@property
def get_layer_weights() -> bool
```

(bool):  [Read-Write] Controls whether data from landscape layers will be retrieved (turning it off is an optimization if that data is not needed)

<a id="unreal.PCGLandscapeDataProps.get_layer_weights"></a>

#### get_layer_weights

```python
@get_layer_weights.setter
def get_layer_weights(value: bool) -> None
```

<a id="unreal.PCGLandscapeDataProps.get_actor_reference"></a>

#### get_actor_reference

```python
@property
def get_actor_reference() -> bool
```

(bool):  [Read-Write] Controls whether the points from this landscape will return the actor from which they originate (e.g. which Landscape Proxy)

<a id="unreal.PCGLandscapeDataProps.get_actor_reference"></a>

#### get_actor_reference

```python
@get_actor_reference.setter
def get_actor_reference(value: bool) -> None
```

<a id="unreal.PCGLandscapeDataProps.get_physical_material"></a>

#### get_physical_material

```python
@property
def get_physical_material() -> bool
```

(bool):  [Read-Write] Controls whether the points from the landscape will have their physical material added as the "PhysicalMaterial" attribute

<a id="unreal.PCGLandscapeDataProps.get_physical_material"></a>

#### get_physical_material

```python
@get_physical_material.setter
def get_physical_material(value: bool) -> None
```

<a id="unreal.PCGLandscapeDataProps.get_component_coordinates"></a>

#### get_component_coordinates

```python
@property
def get_component_coordinates() -> bool
```

(bool):  [Read-Write] Controls whether the component coordinates will be added the point as attributes ('CoordinateX', 'CoordinateY')

<a id="unreal.PCGLandscapeDataProps.get_component_coordinates"></a>

#### get_component_coordinates

```python
@get_component_coordinates.setter
def get_component_coordinates(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams"></a>