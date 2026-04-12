## SelectionBaseColor Objects

```python
class SelectionBaseColor(ParamsBase)
```

Selection Base Color

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpSelectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_color`` (Color):  [Read-Write]
- ``entity_type`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.SelectionBaseColor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_type: Name = "None",
             base_color: Color = [0, 0, 0, 0]) -> None
```

<a id="unreal.SelectionBaseColor.entity_type"></a>

#### entity\_type

```python
@property
def entity_type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.SelectionBaseColor.entity_type"></a>

#### entity\_type

```python
@entity_type.setter
def entity_type(value: Name) -> None
```

<a id="unreal.SelectionBaseColor.base_color"></a>

#### base\_color

```python
@property
def base_color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.SelectionBaseColor.base_color"></a>

#### base\_color

```python
@base_color.setter
def base_color(value: Color) -> None
```

<a id="unreal.GlobalHoverEnable"></a>