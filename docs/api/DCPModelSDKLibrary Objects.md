## DCPModelSDKLibrary Objects

```python
class DCPModelSDKLibrary(BlueprintFunctionLibrary)
```

DCPModel SDKLibrary

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPModelSDKLibrary.h

<a id="unreal.DCPModelSDKLibrary.dcpsdk_set_model_visibility"></a>

#### dcpsdk\_set\_model\_visibility

```python
@classmethod
def dcpsdk_set_model_visibility(cls, eid: int,
                                visibility: bool) -> DCPSDKResult
```

X.dcpsdk_set_model_visibility(eid, visibility) -> DCPSDKResult
DCPSDK Set Model Visibility

Args:
    eid (int64): 
    visibility (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPModelSDKLibrary.dcpsdk_get_actived_model_eid"></a>

#### dcpsdk\_get\_actived\_model\_eid

```python
@classmethod
def dcpsdk_get_actived_model_eid(cls) -> Tuple[DCPSDKResult, int]
```

X.dcpsdk_get_actived_model_eid() -> (DCPSDKResult, eid=int64)
DCPSDK Get Actived Model Eid

Returns:
    int64: 

    eid (int64):

<a id="unreal.DCPModelSDKLibrary.dcpsdk_focus_model"></a>

#### dcpsdk\_focus\_model

```python
@classmethod
def dcpsdk_focus_model(cls, eid: int) -> DCPSDKResult
```

X.dcpsdk_focus_model(eid) -> DCPSDKResult
DCPSDK Focus Model

Args:
    eid (int64): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPModelSDKLibrary.dcpsdk_deactive_model"></a>

#### dcpsdk\_deactive\_model

```python
@classmethod
def dcpsdk_deactive_model(cls) -> DCPSDKResult
```

X.dcpsdk_deactive_model() -> DCPSDKResult
DCPSDK Deactive Model

Returns:
    DCPSDKResult:

<a id="unreal.DCPModelSDKLibrary.dcpsdk_active_model"></a>

#### dcpsdk\_active\_model

```python
@classmethod
def dcpsdk_active_model(cls, eid: int) -> DCPSDKResult
```

X.dcpsdk_active_model(eid) -> DCPSDKResult
DCPSDK Active Model

Args:
    eid (int64): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary"></a>