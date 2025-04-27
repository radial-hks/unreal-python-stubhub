## MovieGraphRenderPropertyModifier Objects

```python
class MovieGraphRenderPropertyModifier(MovieGraphCollectionModifier)
```

Modifies actor visibility.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden.
- ``cast_shadow_while_hidden`` (bool):  [Read-Write] If true, the primitive will cast shadows even if it is hidden.
- ``casts_shadows`` (bool):  [Read-Write] If true, the primitive will cast shadows.
- ``holdout`` (bool):  [Read-Write] If true, the primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections,
  indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``is_hidden`` (bool):  [Read-Write] If true, the actor will not be visible and will not contribute to any secondary effects (shadows, indirect
  lighting) unless their respective flags are set below.
- ``override_b_affect_indirect_lighting_while_hidden`` (bool):  [Read-Write]
- ``override_b_cast_shadow_while_hidden`` (bool):  [Read-Write]
- ``override_b_casts_shadows`` (bool):  [Read-Write]
- ``override_b_holdout`` (bool):  [Read-Write]
- ``override_b_is_hidden`` (bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_is_hidden"></a>

#### override_b_is_hidden

```python
@property
def override_b_is_hidden() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_is_hidden"></a>

#### override_b_is_hidden

```python
@override_b_is_hidden.setter
def override_b_is_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_casts_shadows"></a>

#### override_b_casts_shadows

```python
@property
def override_b_casts_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_casts_shadows"></a>

#### override_b_casts_shadows

```python
@override_b_casts_shadows.setter
def override_b_casts_shadows(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_cast_shadow_while_hidden"></a>

#### override_b_cast_shadow_while_hidden

```python
@property
def override_b_cast_shadow_while_hidden() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_cast_shadow_while_hidden"></a>

#### override_b_cast_shadow_while_hidden

```python
@override_b_cast_shadow_while_hidden.setter
def override_b_cast_shadow_while_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_affect_indirect_lighting_while_hidden"></a>

#### override_b_affect_indirect_lighting_while_hidden

```python
@property
def override_b_affect_indirect_lighting_while_hidden() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_affect_indirect_lighting_while_hidden"></a>

#### override_b_affect_indirect_lighting_while_hidden

```python
@override_b_affect_indirect_lighting_while_hidden.setter
def override_b_affect_indirect_lighting_while_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_holdout"></a>

#### override_b_holdout

```python
@property
def override_b_holdout() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderPropertyModifier.override_b_holdout"></a>

#### override_b_holdout

```python
@override_b_holdout.setter
def override_b_holdout(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.is_hidden"></a>

#### is_hidden

```python
@property
def is_hidden() -> bool
```

(bool):  [Read-Write] If true, the actor will not be visible and will not contribute to any secondary effects (shadows, indirect
lighting) unless their respective flags are set below.

<a id="unreal.MovieGraphRenderPropertyModifier.is_hidden"></a>

#### is_hidden

```python
@is_hidden.setter
def is_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.casts_shadows"></a>

#### casts_shadows

```python
@property
def casts_shadows() -> bool
```

(bool):  [Read-Write] If true, the primitive will cast shadows.

<a id="unreal.MovieGraphRenderPropertyModifier.casts_shadows"></a>

#### casts_shadows

```python
@casts_shadows.setter
def casts_shadows(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.cast_shadow_while_hidden"></a>

#### cast_shadow_while_hidden

```python
@property
def cast_shadow_while_hidden() -> bool
```

(bool):  [Read-Write] If true, the primitive will cast shadows even if it is hidden.

<a id="unreal.MovieGraphRenderPropertyModifier.cast_shadow_while_hidden"></a>

#### cast_shadow_while_hidden

```python
@cast_shadow_while_hidden.setter
def cast_shadow_while_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.affect_indirect_lighting_while_hidden"></a>

#### affect_indirect_lighting_while_hidden

```python
@property
def affect_indirect_lighting_while_hidden() -> bool
```

(bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden.

<a id="unreal.MovieGraphRenderPropertyModifier.affect_indirect_lighting_while_hidden"></a>

#### affect_indirect_lighting_while_hidden

```python
@affect_indirect_lighting_while_hidden.setter
def affect_indirect_lighting_while_hidden(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.holdout"></a>

#### holdout

```python
@property
def holdout() -> bool
```

(bool):  [Read-Write] If true, the primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections,
indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.

<a id="unreal.MovieGraphRenderPropertyModifier.holdout"></a>

#### holdout

```python
@holdout.setter
def holdout(value: bool) -> None
```

<a id="unreal.MovieGraphRenderPropertyModifier.undo_modifier"></a>

#### undo_modifier

```python
def undo_modifier() -> None
```

x.undo_modifier() -> None
Undo Modifier

<a id="unreal.MovieGraphRenderPropertyModifier.set_hidden"></a>

#### set_hidden

```python
def set_hidden(is_hidden: bool) -> None
```

x.set_hidden(is_hidden) -> None
~UObject Interface

Args:
    is_hidden (bool):

<a id="unreal.MovieGraphRenderPropertyModifier.is_hidden"></a>

#### is_hidden

```python
def is_hidden() -> bool
```

x.is_hidden() -> bool
Is Hidden

Returns:
    bool:

<a id="unreal.MovieGraphRenderPropertyModifier.apply_modifier"></a>

#### apply_modifier

```python
def apply_modifier(world: World) -> None
```

x.apply_modifier(world) -> None
Apply Modifier

Args:
    world (World):

<a id="unreal.MoviePipelineVisibilityModifier"></a>