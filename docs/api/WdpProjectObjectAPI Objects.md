## WdpProjectObjectAPI Objects

```python
class WdpProjectObjectAPI(StandardApiClassBase)
```

Wdp Project Object API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpProjectEntityAPI.h

<a id="unreal.WdpProjectObjectAPI.set_transform"></a>

#### set\_transform

```python
def set_transform(
        params: ProjectObjectTransformParams) -> Optional[ResultBase]
```

x.set_transform(params) -> ResultBase or None
Set Transform

Args:
    params (ProjectObjectTransformParams): 

Returns:
    ResultBase or None: 

    result (ResultBase):

<a id="unreal.WdpProjectObjectAPI.get_transform"></a>

#### get\_transform

```python
def get_transform(
        params: IntEidArrayParams) -> Optional[ProjectObjectTransformResult]
```

x.get_transform(params) -> ProjectObjectTransformResult or None
Get Transform

Args:
    params (IntEidArrayParams): 

Returns:
    ProjectObjectTransformResult or None: 

    result (ProjectObjectTransformResult):

<a id="unreal.WdpProjectLayerAPI"></a>