## WdpGlobalSettingsAPI Objects

```python
class WdpGlobalSettingsAPI(StandardApiClassBase)
```

Wdp Global Settings API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpGlobalSettingsAPI.h

<a id="unreal.WdpGlobalSettingsAPI.set_screen_percentage"></a>

#### set\_screen\_percentage

```python
def set_screen_percentage(
        params: WdpGlobalSettingsScreenPercentageParams
) -> Optional[ResultBase]
```

x.set_screen_percentage(params) -> ResultBase or None
Set Screen Percentage

Args:
    params (WdpGlobalSettingsScreenPercentageParams): 

Returns:
    ResultBase or None: 

    results (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_resolution"></a>

#### set\_resolution

```python
def set_resolution(
        params: WdpGlobalSettingsResolutionParams) -> Optional[ResultBase]
```

x.set_resolution(params) -> ResultBase or None
Set Resolution

Args:
    params (WdpGlobalSettingsResolutionParams): 

Returns:
    ResultBase or None: 

    results (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_interactive_mode"></a>

#### set\_interactive\_mode

```python
def set_interactive_mode(
        params: WdpSetInteractiveModeParams) -> Optional[ResultBase]
```

x.set_interactive_mode(params) -> ResultBase or None
Set Interactive Mode

Args:
    params (WdpSetInteractiveModeParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_gizmo_setting"></a>

#### set\_gizmo\_setting

```python
def set_gizmo_setting(
        params: WdpSetGizmoSettingParams) -> Optional[ResultBase]
```

x.set_gizmo_setting(params) -> ResultBase or None
Set Gizmo Setting

Args:
    params (WdpSetGizmoSettingParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_frame_rate_limit"></a>

#### set\_frame\_rate\_limit

```python
def set_frame_rate_limit(
        params: WdpGlobalSettingsFPSParams) -> Optional[ResultBase]
```

x.set_frame_rate_limit(params) -> ResultBase or None
APIs

Args:
    params (WdpGlobalSettingsFPSParams): 

Returns:
    ResultBase or None: 

    results (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_coord_z_ref"></a>

#### set\_coord\_z\_ref

```python
def set_coord_z_ref(
        params: WdpGlobalSetCoordZTypeParams) -> Optional[ResultBase]
```

x.set_coord_z_ref(params) -> ResultBase or None
Set Coord ZRef

Args:
    params (WdpGlobalSetCoordZTypeParams): 

Returns:
    ResultBase or None: 

    results (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.set_audio_volume"></a>

#### set\_audio\_volume

```python
def set_audio_volume(
        params: WdpGlobalSettingsSoundParams) -> Optional[ResultBase]
```

x.set_audio_volume(params) -> ResultBase or None
Set Audio Volume

Args:
    params (WdpGlobalSettingsSoundParams): 

Returns:
    ResultBase or None: 

    result (ResultBase):

<a id="unreal.WdpGlobalSettingsAPI.get_screen_percentage"></a>

#### get\_screen\_percentage

```python
def get_screen_percentage(
        params: ParamsBase
) -> Optional[WdpGlobalSettingsScreenPercentageResults]
```

x.get_screen_percentage(params) -> WdpGlobalSettingsScreenPercentageResults or None
Get Screen Percentage

Args:
    params (ParamsBase): 

Returns:
    WdpGlobalSettingsScreenPercentageResults or None: 

    results (WdpGlobalSettingsScreenPercentageResults):

<a id="unreal.WdpGlobalSettingsAPI.get_resolution"></a>

#### get\_resolution

```python
def get_resolution(
        params: ParamsBase) -> Optional[WdpGlobalSettingsResolutionResults]
```

x.get_resolution(params) -> WdpGlobalSettingsResolutionResults or None
Get Resolution

Args:
    params (ParamsBase): 

Returns:
    WdpGlobalSettingsResolutionResults or None: 

    results (WdpGlobalSettingsResolutionResults):

<a id="unreal.WdpGlobalSettingsAPI.get_frame_rate_limit"></a>

#### get\_frame\_rate\_limit

```python
def get_frame_rate_limit(
        params: ParamsBase) -> Optional[WdpGlobalSettingsFPSResults]
```

x.get_frame_rate_limit(params) -> WdpGlobalSettingsFPSResults or None
Get Frame Rate Limit

Args:
    params (ParamsBase): 

Returns:
    WdpGlobalSettingsFPSResults or None: 

    results (WdpGlobalSettingsFPSResults):

<a id="unreal.WdpGlobalSettingsAPI.get_coord_z_ref"></a>

#### get\_coord\_z\_ref

```python
def get_coord_z_ref(
        params: ParamsBase) -> Optional[WdpGlobalGetCoordZTypeParams]
```

x.get_coord_z_ref(params) -> WdpGlobalGetCoordZTypeParams or None
Get Coord ZRef

Args:
    params (ParamsBase): 

Returns:
    WdpGlobalGetCoordZTypeParams or None: 

    results (WdpGlobalGetCoordZTypeParams):

<a id="unreal.WdpGlobalSettingsAPI.get_api_version"></a>

#### get\_api\_version

```python
def get_api_version(params: ParamsBase) -> Optional[WdpGlobalGetVersionParams]
```

x.get_api_version(params) -> WdpGlobalGetVersionParams or None
Get Api Version

Args:
    params (ParamsBase): 

Returns:
    WdpGlobalGetVersionParams or None: 

    results (WdpGlobalGetVersionParams):

<a id="unreal.WdpGroupAPI"></a>