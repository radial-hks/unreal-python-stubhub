## ProjectObjectTransformResult Objects

```python
class ProjectObjectTransformResult(ResultBase)
```

Project Object Transform Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpProjectEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``transforms`` (Array[ProjectObjectTransform]):  [Read-Write]

<a id="unreal.ProjectObjectTransformResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             transforms: Array[ProjectObjectTransform] = []) -> None
```

<a id="unreal.ProjectObjectTransformResult.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[ProjectObjectTransform]
```

(Array[ProjectObjectTransform]):  [Read-Only]

<a id="unreal.ProjectLayerAPISetLayerHiddenParams"></a>