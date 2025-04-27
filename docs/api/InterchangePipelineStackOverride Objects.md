## InterchangePipelineStackOverride Objects

```python
class InterchangePipelineStackOverride(Object)
```

This class is used to pass override pipelines in the ImportAssetTask Options member.

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_pipelines`` (Array[SoftObjectPath]):  [Read-Write]

<a id="unreal.InterchangePipelineStackOverride.override_pipelines"></a>

#### override_pipelines

```python
@property
def override_pipelines() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write]

<a id="unreal.InterchangePipelineStackOverride.override_pipelines"></a>

#### override_pipelines

```python
@override_pipelines.setter
def override_pipelines(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.InterchangePipelineStackOverride.add_python_pipeline"></a>

#### add_python_pipeline

```python
def add_python_pipeline(pipeline_base: InterchangePythonPipelineBase) -> None
```

x.add_python_pipeline(pipeline_base) -> None
Add Python Pipeline

Args:
    pipeline_base (InterchangePythonPipelineBase):

<a id="unreal.InterchangePipelineStackOverride.add_pipeline"></a>

#### add_pipeline

```python
def add_pipeline(pipeline_base: InterchangePipelineBase) -> None
```

x.add_pipeline(pipeline_base) -> None
Add Pipeline

Args:
    pipeline_base (InterchangePipelineBase):

<a id="unreal.InterchangePipelineStackOverride.add_blueprint_pipeline"></a>

#### add_blueprint_pipeline

```python
def add_blueprint_pipeline(
        pipeline_base: InterchangeBlueprintPipelineBase) -> None
```

x.add_blueprint_pipeline(pipeline_base) -> None
Add Blueprint Pipeline

Args:
    pipeline_base (InterchangeBlueprintPipelineBase):

<a id="unreal.InterchangeManager"></a>