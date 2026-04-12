## PickMaterialApiResult Objects

```python
class PickMaterialApiResult(ResultBase)
```

Pick Material Api Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_id`` (str):  [Read-Write]
- ``eid`` (int64):  [Read-Write]
- ``material_index`` (int32):  [Read-Write]
- ``material_name`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.PickMaterialApiResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             eid: int = 0,
             component_id: str = "",
             position: Vector = [0.000000, 0.000000, 0.000000],
             material_name: str = "",
             material_index: int = 0) -> None
```

<a id="unreal.PickMaterialApiResult.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.PickMaterialApiResult.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.PickMaterialApiResult.component_id"></a>

#### component\_id

```python
@property
def component_id() -> str
```

(str):  [Read-Write]

<a id="unreal.PickMaterialApiResult.component_id"></a>

#### component\_id

```python
@component_id.setter
def component_id(value: str) -> None
```

<a id="unreal.PickMaterialApiResult.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PickMaterialApiResult.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.PickMaterialApiResult.material_name"></a>

#### material\_name

```python
@property
def material_name() -> str
```

(str):  [Read-Write]

<a id="unreal.PickMaterialApiResult.material_name"></a>

#### material\_name

```python
@material_name.setter
def material_name(value: str) -> None
```

<a id="unreal.PickMaterialApiResult.material_index"></a>

#### material\_index

```python
@property
def material_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.PickMaterialApiResult.material_index"></a>

#### material\_index

```python
@material_index.setter
def material_index(value: int) -> None
```

<a id="unreal.EntityClickedEventArgs"></a>