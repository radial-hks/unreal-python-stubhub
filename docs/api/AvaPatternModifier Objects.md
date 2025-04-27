## AvaPatternModifier Objects

```python
class AvaPatternModifier(AvaGeometryBaseModifier)
```

This modifier clones a shape following various layouts and options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaPatternModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``circle_layout_options`` (AvaPatternModifierCircleLayoutOptions):  [Read-Write] Circle layout options
- ``grid_layout_options`` (AvaPatternModifierGridLayoutOptions):  [Read-Write] Grid layout options
- ``layout`` (AvaPatternModifierLayout):  [Read-Write]
- ``line_layout_options`` (AvaPatternModifierLineLayoutOptions):  [Read-Write] Line layout options
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled

<a id="unreal.AvaPatternModifier.set_line_layout_options"></a>

#### set_line_layout_options

```python
def set_line_layout_options(
        options: AvaPatternModifierLineLayoutOptions) -> None
```

x.set_line_layout_options(options) -> None
Set Line Layout Options

Args:
    options (AvaPatternModifierLineLayoutOptions):

<a id="unreal.AvaPatternModifier.set_layout"></a>

#### set_layout

```python
def set_layout(layout: AvaPatternModifierLayout) -> None
```

x.set_layout(layout) -> None
Set Layout

Args:
    layout (AvaPatternModifierLayout):

<a id="unreal.AvaPatternModifier.set_grid_layout_options"></a>

#### set_grid_layout_options

```python
def set_grid_layout_options(
        options: AvaPatternModifierGridLayoutOptions) -> None
```

x.set_grid_layout_options(options) -> None
Set Grid Layout Options

Args:
    options (AvaPatternModifierGridLayoutOptions):

<a id="unreal.AvaPatternModifier.set_circle_layout_options"></a>

#### set_circle_layout_options

```python
def set_circle_layout_options(
        options: AvaPatternModifierCircleLayoutOptions) -> None
```

x.set_circle_layout_options(options) -> None
Set Circle Layout Options

Args:
    options (AvaPatternModifierCircleLayoutOptions):

<a id="unreal.AvaPatternModifier.get_line_layout_options"></a>

#### get_line_layout_options

```python
def get_line_layout_options() -> AvaPatternModifierLineLayoutOptions
```

x.get_line_layout_options() -> AvaPatternModifierLineLayoutOptions
Get Line Layout Options

Returns:
    AvaPatternModifierLineLayoutOptions:

<a id="unreal.AvaPatternModifier.get_layout"></a>

#### get_layout

```python
def get_layout() -> AvaPatternModifierLayout
```

x.get_layout() -> AvaPatternModifierLayout
Get Layout

Returns:
    AvaPatternModifierLayout:

<a id="unreal.AvaPatternModifier.get_grid_layout_options"></a>

#### get_grid_layout_options

```python
def get_grid_layout_options() -> AvaPatternModifierGridLayoutOptions
```

x.get_grid_layout_options() -> AvaPatternModifierGridLayoutOptions
Get Grid Layout Options

Returns:
    AvaPatternModifierGridLayoutOptions:

<a id="unreal.AvaPatternModifier.get_circle_layout_options"></a>

#### get_circle_layout_options

```python
def get_circle_layout_options() -> AvaPatternModifierCircleLayoutOptions
```

x.get_circle_layout_options() -> AvaPatternModifierCircleLayoutOptions
Get Circle Layout Options

Returns:
    AvaPatternModifierCircleLayoutOptions:

<a id="unreal.AvaCloneModifier"></a>