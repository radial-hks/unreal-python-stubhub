## AudioMaterialWidgetStyle Objects

```python
class AudioMaterialWidgetStyle(SlateWidgetStyle)
```

Base for the appearance of an Audio Material Slates

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate

<a id="unreal.AudioMaterialWidgetStyle.__init__"></a>

#### __init__

```python
def __init__(material: MaterialInterface = None,
             desired_size: Vector2f = [0.000000, 0.000000]) -> None
```

<a id="unreal.AudioMaterialWidgetStyle.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material used to render the Slate

<a id="unreal.AudioMaterialWidgetStyle.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.AudioMaterialWidgetStyle.desired_size"></a>

#### desired_size

```python
@property
def desired_size() -> Vector2f
```

(Vector2f):  [Read-Write] Desired Draw size of the rendered material

<a id="unreal.AudioMaterialWidgetStyle.desired_size"></a>

#### desired_size

```python
@desired_size.setter
def desired_size(value: Vector2f) -> None
```

<a id="unreal.AudioMaterialMeterStyle"></a>