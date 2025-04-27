## ControlRigShapeDefinition Objects

```python
class ControlRigShapeDefinition(StructBase)
```

Control Rig Shape Definition

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigGizmoLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``shape_name`` (Name):  [Read-Write]
- ``static_mesh`` (StaticMesh):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.ControlRigShapeDefinition.__init__"></a>

#### __init__

```python
def __init__(
    shape_name: Name = "None",
    static_mesh: StaticMesh = None,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.ControlRigShapeDefinition.shape_name"></a>

#### shape_name

```python
@property
def shape_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.ControlRigShapeDefinition.gizmo_name"></a>

#### gizmo_name

```python
@property
def gizmo_name() -> Name
```

deprecated: 'gizmo_name' was renamed to 'shape_name'.

<a id="unreal.ControlRigShapeDefinition.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Only]

<a id="unreal.ControlRigShapeDefinition.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.ControlRigGizmoDefinition"></a>