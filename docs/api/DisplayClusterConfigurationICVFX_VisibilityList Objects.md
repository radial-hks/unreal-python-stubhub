## DisplayClusterConfigurationICVFX_VisibilityList Objects

```python
class DisplayClusterConfigurationICVFX_VisibilityList(StructBase)
```

Display Cluster Configuration ICVFX Visibility List

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_layers`` (Array[ActorLayer]):  [Read-Write] Actor layers.
  Warning: This option has a very expensive performance cost, especially on big projects.
- ``actors`` (Array[Actor]):  [Read-Write] {ActorsTooltip}
- ``root_actor_component_names`` (Array[str]):  [Read-Write] Reference to RootActor components by names

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.__init__"></a>

#### __init__

```python
def __init__(actor_layers: Array[ActorLayer] = [],
             actors: Array[Actor] = [],
             root_actor_component_names: Array[str] = []) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.actor_layers"></a>

#### actor_layers

```python
@property
def actor_layers() -> Array[ActorLayer]
```

(Array[ActorLayer]):  [Read-Write] Actor layers.
Warning: This option has a very expensive performance cost, especially on big projects.

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.actor_layers"></a>

#### actor_layers

```python
@actor_layers.setter
def actor_layers(value: Array[ActorLayer]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.actors"></a>

#### actors

```python
@property
def actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] {ActorsTooltip}

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.actors"></a>

#### actors

```python
@actors.setter
def actors(value: Array[Actor]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.root_actor_component_names"></a>

#### root_actor_component_names

```python
@property
def root_actor_component_names() -> Array[str]
```

(Array[str]):  [Read-Write] Reference to RootActor components by names

<a id="unreal.DisplayClusterConfigurationICVFX_VisibilityList.root_actor_component_names"></a>

#### root_actor_component_names

```python
@root_actor_component_names.setter
def root_actor_component_names(value: Array[str]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CustomSize"></a>