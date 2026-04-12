## ChinaMapMigrationQueryResult Objects

```python
class ChinaMapMigrationQueryResult(ResultBase)
```

China Map Migration Query Result

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ChinaMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``migaration_ids`` (Array[str]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.ChinaMapMigrationQueryResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             migaration_ids: Array[str] = []) -> None
```

<a id="unreal.ChinaMapMigrationQueryResult.migaration_ids"></a>

#### migaration\_ids

```python
@property
def migaration_ids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.ChinaMapMigrationQueryResult.migaration_ids"></a>

#### migaration\_ids

```python
@migaration_ids.setter
def migaration_ids(value: Array[str]) -> None
```

<a id="unreal.UpdateAttrParams"></a>