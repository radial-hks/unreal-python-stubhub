## DCPSectionSDKLibrary Objects

```python
class DCPSectionSDKLibrary(BlueprintFunctionLibrary)
```

DCPSection SDKLibrary

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPSectionSDKLibrary.h

<a id="unreal.DCPSectionSDKLibrary.dcpsdk_start_section"></a>

#### dcpsdk\_start\_section

```python
@classmethod
def dcpsdk_start_section(cls, eid: Eid) -> DCPSDKResult
```

X.dcpsdk_start_section(eid) -> DCPSDKResult
DCPSDK Start Section

Args:
    eid (Eid): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSectionSDKLibrary.dcpsdk_end_section"></a>

#### dcpsdk\_end\_section

```python
@classmethod
def dcpsdk_end_section(cls) -> DCPSDKResult
```

X.dcpsdk_end_section() -> DCPSDKResult
DCPSDK End Section

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary"></a>