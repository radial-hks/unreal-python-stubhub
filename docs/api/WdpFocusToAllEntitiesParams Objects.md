## WdpFocusToAllEntitiesParams Objects

```python
class WdpFocusToAllEntitiesParams(ParamsBase)
```

Wdp Focus to All Entities Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_types`` (Array[Name]):  [Read-Only]
- ``filter_for_exclude`` (bool):  [Read-Only]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WdpFocusToAllEntitiesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_types: Array[Name] = [],
             filter_for_exclude: bool = False) -> None
```

<a id="unreal.WdpFocusToAllEntitiesParams.entity_types"></a>

#### entity\_types

```python
@property
def entity_types() -> Array[Name]
```

(Array[Name]):  [Read-Only]

<a id="unreal.WdpFocusToAllEntitiesParams.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@property
def filter_for_exclude() -> bool
```

(bool):  [Read-Only]

<a id="unreal.CameraStepMoveParams"></a>