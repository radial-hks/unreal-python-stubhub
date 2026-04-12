## InterchangeStackInfo Objects

```python
class InterchangeStackInfo(StructBase)
```

Interchange Stack Info

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangePipelineConfigurationBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pipelines`` (Array[InterchangePipelineBase]):  [Read-Write]
- ``stack_name`` (Name):  [Read-Write]

<a id="unreal.InterchangeStackInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(stack_name: Name = "None",
             pipelines: Array[InterchangePipelineBase] = []) -> None
```

<a id="unreal.InterchangeStackInfo.stack_name"></a>

#### stack\_name

```python
@property
def stack_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.InterchangeStackInfo.stack_name"></a>

#### stack\_name

```python
@stack_name.setter
def stack_name(value: Name) -> None
```

<a id="unreal.InterchangeStackInfo.pipelines"></a>

#### pipelines

```python
@property
def pipelines() -> Array[InterchangePipelineBase]
```

(Array[InterchangePipelineBase]):  [Read-Write]

<a id="unreal.InterchangeStackInfo.pipelines"></a>

#### pipelines

```python
@pipelines.setter
def pipelines(value: Array[InterchangePipelineBase]) -> None
```

<a id="unreal.ImportAssetParameters"></a>