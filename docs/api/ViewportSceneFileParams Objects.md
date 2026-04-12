## ViewportSceneFileParams Objects

```python
class ViewportSceneFileParams(StructBase)
```

Viewport Scene File Params

**C++ Source:**

- **Plugin**: CustomProgram
- **Module**: CustomProgram
- **File**: CustomProgramLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``author`` (str):  [Read-Write]
- ``model_info`` (Array[CustomModelInfo]):  [Read-Write]
- ``scene_file_name`` (str):  [Read-Write]
- ``sence_id`` (str):  [Read-Write]
- ``time`` (str):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(scene_file_name: str = "",
             author: str = "",
             time: str = "",
             sence_id: str = "",
             model_info: Array[CustomModelInfo] = []) -> None
```

<a id="unreal.ViewportSceneFileParams.scene_file_name"></a>

#### scene\_file\_name

```python
@property
def scene_file_name() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.scene_file_name"></a>

#### scene\_file\_name

```python
@scene_file_name.setter
def scene_file_name(value: str) -> None
```

<a id="unreal.ViewportSceneFileParams.author"></a>

#### author

```python
@property
def author() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.author"></a>

#### author

```python
@author.setter
def author(value: str) -> None
```

<a id="unreal.ViewportSceneFileParams.time"></a>

#### time

```python
@property
def time() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.time"></a>

#### time

```python
@time.setter
def time(value: str) -> None
```

<a id="unreal.ViewportSceneFileParams.sence_id"></a>

#### sence\_id

```python
@property
def sence_id() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.sence_id"></a>

#### sence\_id

```python
@sence_id.setter
def sence_id(value: str) -> None
```

<a id="unreal.ViewportSceneFileParams.model_info"></a>

#### model\_info

```python
@property
def model_info() -> Array[CustomModelInfo]
```

(Array[CustomModelInfo]):  [Read-Write]

<a id="unreal.ViewportSceneFileParams.model_info"></a>

#### model\_info

```python
@model_info.setter
def model_info(value: Array[CustomModelInfo]) -> None
```

<a id="unreal.ViewportSceneFileThreeParamArray"></a>