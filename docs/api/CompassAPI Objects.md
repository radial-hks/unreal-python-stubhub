## CompassAPI Objects

```python
class CompassAPI(ApiClassBase)
```

Compass API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CompassAPI.h

<a id="unreal.CompassAPI.start_compass"></a>

#### start\_compass

```python
def start_compass(
        start_compass_params: StartCompassParams) -> Optional[EidResult]
```

x.start_compass(start_compass_params) -> EidResult or None
APIs

Args:
    start_compass_params (StartCompassParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.CompassAPI.end_compass"></a>

#### end\_compass

```python
def end_compass(params: ParamsBase) -> Optional[EidResult]
```

x.end_compass(params) -> EidResult or None
End Compass

Args:
    params (ParamsBase): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.CoveringBoundAPI"></a>