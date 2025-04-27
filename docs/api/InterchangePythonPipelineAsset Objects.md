## InterchangePythonPipelineAsset Objects

```python
class InterchangePythonPipelineAsset(Object)
```

* This class is a helper class for Python pipelines. It allows the class picker to filter the Content Browser instance we want to support
* in the pipeline stack.
*
* Use this class factory to be able to create an instance of a Python pipeline in the Content Browser.
* A Python pipeline does not have any locked properties, and all default values must be set in the Python script.
* This restriction exists because Python classes are transient, so any assets created from a Python class cannot be saved.

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangePythonPipelineBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``generated_pipeline`` (InterchangePythonPipelineBase):  [Read-Only] The transient pipeline we generate when we load the Python pipeline.
- ``json_default_properties`` (str):  [Read-Only]
- ``python_class`` (Class):  [Read-Write] The Python class we want to use as a pipeline.

<a id="unreal.AssetImportData"></a>