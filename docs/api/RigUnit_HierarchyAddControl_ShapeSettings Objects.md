## RigUnit_HierarchyAddControl_ShapeSettings Objects

```python
class RigUnit_HierarchyAddControl_ShapeSettings(StructBase)
```

Rig Unit Hierarchy Add Control Shape Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.__init__"></a>

#### __init__

```python
def __init__(
    visible: bool = False,
    name: Name = "None",
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ShapeSettings.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings"></a>