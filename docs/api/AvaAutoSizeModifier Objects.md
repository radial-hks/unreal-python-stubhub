## AvaAutoSizeModifier Objects

```python
class AvaAutoSizeModifier(AvaGeometryBaseModifier)
```

Adapts the modified actor geometry size/scale to match reference actor bounds and act as a background

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaAutoSizeModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fit_mode`` (AvaAutoSizeFitMode):  [Read-Write]
- ``ignore_hidden_actors`` (bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container.
  deprecated: Use ReferenceActor instead
- ``include_children`` (bool):  [Read-Write] If true, will include children bounds too and compute the new size
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``padding_horizontal`` (double):  [Read-Write] Padding for left and right side
- ``padding_vertical`` (double):  [Read-Write] Padding for top and bottom side
- ``reference_actor`` (AvaSceneTreeActor):  [Read-Write]
- ``reference_actor_weak`` (Actor):  [Read-Write] The actor affecting the modifier. This is user selectable if the Reference Container is set to "Other".
  deprecated: Use ReferenceActor instead
- ``reference_container`` (AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy.
  deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoSizeModifier.reference_container"></a>

#### reference_container

```python
@property
def reference_container() -> AvaReferenceContainer
```

(AvaReferenceContainer):  [Read-Write] The method for finding a reference actor based on it's position in the parent's hierarchy.
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoSizeModifier.reference_container"></a>

#### reference_container

```python
@reference_container.setter
def reference_container(value: AvaReferenceContainer) -> None
```

<a id="unreal.AvaAutoSizeModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@property
def reference_actor_weak() -> Actor
```

(Actor):  [Read-Write] The actor affecting the modifier. This is user selectable if the Reference Container is set to "Other".
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoSizeModifier.reference_actor_weak"></a>

#### reference_actor_weak

```python
@reference_actor_weak.setter
def reference_actor_weak(value: Actor) -> None
```

<a id="unreal.AvaAutoSizeModifier.ignore_hidden_actors"></a>

#### ignore_hidden_actors

```python
@property
def ignore_hidden_actors() -> bool
```

(bool):  [Read-Write] If true, will search for the next visible actor based on the selected reference container.
deprecated: Use ReferenceActor instead

<a id="unreal.AvaAutoSizeModifier.ignore_hidden_actors"></a>

#### ignore_hidden_actors

```python
@ignore_hidden_actors.setter
def ignore_hidden_actors(value: bool) -> None
```

<a id="unreal.AvaAutoSizeModifier.padding_vertical"></a>

#### padding_vertical

```python
@property
def padding_vertical() -> float
```

(double):  [Read-Write] Padding for top and bottom side

<a id="unreal.AvaAutoSizeModifier.padding_vertical"></a>

#### padding_vertical

```python
@padding_vertical.setter
def padding_vertical(value: float) -> None
```

<a id="unreal.AvaAutoSizeModifier.padding_horizontal"></a>

#### padding_horizontal

```python
@property
def padding_horizontal() -> float
```

(double):  [Read-Write] Padding for left and right side

<a id="unreal.AvaAutoSizeModifier.padding_horizontal"></a>

#### padding_horizontal

```python
@padding_horizontal.setter
def padding_horizontal(value: float) -> None
```

<a id="unreal.AvaAutoSizeModifier.set_reference_actor"></a>

#### set_reference_actor

```python
def set_reference_actor(reference_actor: AvaSceneTreeActor) -> None
```

x.set_reference_actor(reference_actor) -> None
Set Reference Actor

Args:
    reference_actor (AvaSceneTreeActor):

<a id="unreal.AvaAutoSizeModifier.set_padding_vertical"></a>

#### set_padding_vertical

```python
def set_padding_vertical(padding: float) -> None
```

x.set_padding_vertical(padding) -> None
Set Padding Vertical

Args:
    padding (double):

<a id="unreal.AvaAutoSizeModifier.set_padding_horizontal"></a>

#### set_padding_horizontal

```python
def set_padding_horizontal(padding: float) -> None
```

x.set_padding_horizontal(padding) -> None
Set Padding Horizontal

Args:
    padding (double):

<a id="unreal.AvaAutoSizeModifier.set_include_children"></a>

#### set_include_children

```python
def set_include_children(include_children: bool) -> None
```

x.set_include_children(include_children) -> None
Set Include Children

Args:
    include_children (bool):

<a id="unreal.AvaAutoSizeModifier.set_fit_mode"></a>

#### set_fit_mode

```python
def set_fit_mode(fit_mode: AvaAutoSizeFitMode) -> None
```

x.set_fit_mode(fit_mode) -> None
Set Fit Mode

Args:
    fit_mode (AvaAutoSizeFitMode):

<a id="unreal.AvaAutoSizeModifier.get_reference_actor"></a>

#### get_reference_actor

```python
def get_reference_actor() -> AvaSceneTreeActor
```

x.get_reference_actor() -> AvaSceneTreeActor
Get Reference Actor

Returns:
    AvaSceneTreeActor:

<a id="unreal.AvaAutoSizeModifier.get_padding_vertical"></a>

#### get_padding_vertical

```python
def get_padding_vertical() -> float
```

x.get_padding_vertical() -> double
Get Padding Vertical

Returns:
    double:

<a id="unreal.AvaAutoSizeModifier.get_padding_horizontal"></a>

#### get_padding_horizontal

```python
def get_padding_horizontal() -> float
```

x.get_padding_horizontal() -> double
Get Padding Horizontal

Returns:
    double:

<a id="unreal.AvaAutoSizeModifier.get_include_children"></a>

#### get_include_children

```python
def get_include_children() -> bool
```

x.get_include_children() -> bool
Get Include Children

Returns:
    bool:

<a id="unreal.AvaAutoSizeModifier.get_fit_mode"></a>

#### get_fit_mode

```python
def get_fit_mode() -> AvaAutoSizeFitMode
```

x.get_fit_mode() -> AvaAutoSizeFitMode
Get Fit Mode

Returns:
    AvaAutoSizeFitMode:

<a id="unreal.AvaContentBackgroundModifier"></a>