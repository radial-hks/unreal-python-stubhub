## GameUserSettings Objects

```python
class GameUserSettings(Object)
```

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

**C++ Source:**

- **Module**: Engine
- **File**: GameUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_game_user_settings_ui_needs_update`` (OnGameUserSettingsUINeedsUpdate):  [Read-Write]

<a id="unreal.GameUserSettings.on_game_user_settings_ui_needs_update"></a>

#### on\_game\_user\_settings\_ui\_needs\_update

```python
@property
def on_game_user_settings_ui_needs_update() -> OnGameUserSettingsUINeedsUpdate
```

(OnGameUserSettingsUINeedsUpdate):  [Read-Write]

<a id="unreal.GameUserSettings.on_game_user_settings_ui_needs_update"></a>

#### on\_game\_user\_settings\_ui\_needs\_update

```python
@on_game_user_settings_ui_needs_update.setter
def on_game_user_settings_ui_needs_update(
        value: OnGameUserSettingsUINeedsUpdate) -> None
```

<a id="unreal.GameUserSettings.validate_settings"></a>

#### validate\_settings

```python
def validate_settings() -> None
```

x.validate_settings() -> None
Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

<a id="unreal.GameUserSettings.supports_hdr_display_output"></a>

#### supports\_hdr\_display\_output

```python
def supports_hdr_display_output() -> bool
```

x.supports_hdr_display_output() -> bool
Whether the curently running system supports HDR display output

Returns:
    bool:

<a id="unreal.GameUserSettings.set_v_sync_enabled"></a>

#### set\_v\_sync\_enabled

```python
def set_v_sync_enabled(enable: bool) -> None
```

x.set_v_sync_enabled(enable) -> None
Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

Args:
    enable (bool):

<a id="unreal.GameUserSettings.set_visual_effect_quality"></a>

#### set\_visual\_effect\_quality

```python
def set_visual_effect_quality(value: int) -> None
```

x.set_visual_effect_quality(value) -> None
Sets the visual effects quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_view_distance_quality"></a>

#### set\_view\_distance\_quality

```python
def set_view_distance_quality(value: int) -> None
```

x.set_view_distance_quality(value) -> None
Sets the view distance quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_to_defaults"></a>

#### set\_to\_defaults

```python
def set_to_defaults() -> None
```

x.set_to_defaults() -> None
Set to Defaults

<a id="unreal.GameUserSettings.set_texture_quality"></a>

#### set\_texture\_quality

```python
def set_texture_quality(value: int) -> None
```

x.set_texture_quality(value) -> None
Sets the texture quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic  (gets clamped if needed)

<a id="unreal.GameUserSettings.set_shadow_quality"></a>

#### set\_shadow\_quality

```python
def set_shadow_quality(value: int) -> None
```

x.set_shadow_quality(value) -> None
Sets the shadow quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_shading_quality"></a>

#### set\_shading\_quality

```python
def set_shading_quality(value: int) -> None
```

x.set_shading_quality(value) -> None
Sets the shading quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_screen_resolution"></a>

#### set\_screen\_resolution

```python
def set_screen_resolution(resolution: IntPoint) -> None
```

x.set_screen_resolution(resolution) -> None
Sets the user setting for game screen resolution, in pixels.

Args:
    resolution (IntPoint):

<a id="unreal.GameUserSettings.set_resolution_scale_value_ex"></a>

#### set\_resolution\_scale\_value\_ex

```python
def set_resolution_scale_value_ex(new_scale_value: float) -> None
```

x.set_resolution_scale_value_ex(new_scale_value) -> None
Sets the current resolution scale

Args:
    new_scale_value (float):

<a id="unreal.GameUserSettings.set_resolution_scale_normalized"></a>

#### set\_resolution\_scale\_normalized

```python
def set_resolution_scale_normalized(new_scale_normalized: float) -> None
```

x.set_resolution_scale_normalized(new_scale_normalized) -> None
Sets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

Args:
    new_scale_normalized (float):

<a id="unreal.GameUserSettings.set_reflection_quality"></a>

#### set\_reflection\_quality

```python
def set_reflection_quality(value: int) -> None
```

x.set_reflection_quality(value) -> None
Sets the reflection quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_post_processing_quality"></a>

#### set\_post\_processing\_quality

```python
def set_post_processing_quality(value: int) -> None
```

x.set_post_processing_quality(value) -> None
Sets the post-processing quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_overall_scalability_level"></a>

#### set\_overall\_scalability\_level

```python
def set_overall_scalability_level(value: int) -> None
```

x.set_overall_scalability_level(value) -> None
Changes all scalability settings at once based on a single overall quality level

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic

<a id="unreal.GameUserSettings.set_global_illumination_quality"></a>

#### set\_global\_illumination\_quality

```python
def set_global_illumination_quality(value: int) -> None
```

x.set_global_illumination_quality(value) -> None
Sets the global illumination quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_fullscreen_mode"></a>

#### set\_fullscreen\_mode

```python
def set_fullscreen_mode(fullscreen_mode: WindowMode) -> None
```

x.set_fullscreen_mode(fullscreen_mode) -> None
Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

Args:
    fullscreen_mode (WindowMode):

<a id="unreal.GameUserSettings.set_frame_rate_limit"></a>

#### set\_frame\_rate\_limit

```python
def set_frame_rate_limit(new_limit: float) -> None
```

x.set_frame_rate_limit(new_limit) -> None
Sets the user's frame rate limit (0 will disable frame rate limiting)

Args:
    new_limit (float):

<a id="unreal.GameUserSettings.set_foliage_quality"></a>

#### set\_foliage\_quality

```python
def set_foliage_quality(value: int) -> None
```

x.set_foliage_quality(value) -> None
Sets the foliage quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_dynamic_resolution_enabled"></a>

#### set\_dynamic\_resolution\_enabled

```python
def set_dynamic_resolution_enabled(enable: bool) -> None
```

x.set_dynamic_resolution_enabled(enable) -> None
Sets the user setting for dynamic resolution. See UGameUserSettings::bUseDynamicResolution.

Args:
    enable (bool):

<a id="unreal.GameUserSettings.set_benchmark_fallback_values"></a>

#### set\_benchmark\_fallback\_values

```python
def set_benchmark_fallback_values() -> None
```

x.set_benchmark_fallback_values() -> None
Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

<a id="unreal.GameUserSettings.set_audio_quality_level"></a>

#### set\_audio\_quality\_level

```python
def set_audio_quality_level(quality_level: int) -> None
```

x.set_audio_quality_level(quality_level) -> None
Sets the user's audio quality level setting

Args:
    quality_level (int32):

<a id="unreal.GameUserSettings.set_anti_aliasing_quality"></a>

#### set\_anti\_aliasing\_quality

```python
def set_anti_aliasing_quality(value: int) -> None
```

x.set_anti_aliasing_quality(value) -> None
Sets the anti-aliasing quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.save_settings"></a>

#### save\_settings

```python
def save_settings() -> None
```

x.save_settings() -> None
Save the user settings to persistent storage (automatically happens as part of ApplySettings)

<a id="unreal.GameUserSettings.run_hardware_benchmark"></a>

#### run\_hardware\_benchmark

```python
def run_hardware_benchmark(work_scale: int = 10,
                           cpu_multiplier: float = 1.000000,
                           gpu_multiplier: float = 1.000000) -> None
```

x.run_hardware_benchmark(work_scale=10, cpu_multiplier=1.000000, gpu_multiplier=1.000000) -> None
Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

Args:
    work_scale (int32): 
    cpu_multiplier (float): 
    gpu_multiplier (float):

<a id="unreal.GameUserSettings.revert_video_mode"></a>

#### revert\_video\_mode

```python
def revert_video_mode() -> None
```

x.revert_video_mode() -> None
Revert video mode (fullscreenmode/resolution) back to the last user confirmed values

<a id="unreal.GameUserSettings.reset_to_current_settings"></a>

#### reset\_to\_current\_settings

```python
def reset_to_current_settings() -> None
```

x.reset_to_current_settings() -> None
This function resets all settings to the current system settings

<a id="unreal.GameUserSettings.load_settings"></a>

#### load\_settings

```python
def load_settings(force_reload: bool = False) -> None
```

x.load_settings(force_reload=False) -> None
Loads the user settings from persistent storage

Args:
    force_reload (bool):

<a id="unreal.GameUserSettings.is_v_sync_enabled"></a>

#### is\_v\_sync\_enabled

```python
def is_v_sync_enabled() -> bool
```

x.is_v_sync_enabled() -> bool
Returns the user setting for vsync.

Returns:
    bool:

<a id="unreal.GameUserSettings.is_v_sync_dirty"></a>

#### is\_v\_sync\_dirty

```python
def is_v_sync_dirty() -> bool
```

x.is_v_sync_dirty() -> bool
Checks if the vsync user setting is different from current system setting

Returns:
    bool:

<a id="unreal.GameUserSettings.is_screen_resolution_dirty"></a>

#### is\_screen\_resolution\_dirty

```python
def is_screen_resolution_dirty() -> bool
```

x.is_screen_resolution_dirty() -> bool
Checks if the Screen Resolution user setting is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.is_hdr_enabled"></a>

#### is\_hdr\_enabled

```python
def is_hdr_enabled() -> bool
```

x.is_hdr_enabled() -> bool
Is HDREnabled

Returns:
    bool:

<a id="unreal.GameUserSettings.is_fullscreen_mode_dirty"></a>

#### is\_fullscreen\_mode\_dirty

```python
def is_fullscreen_mode_dirty() -> bool
```

x.is_fullscreen_mode_dirty() -> bool
Checks if the FullscreenMode user setting is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dynamic_resolution_enabled"></a>

#### is\_dynamic\_resolution\_enabled

```python
def is_dynamic_resolution_enabled() -> bool
```

x.is_dynamic_resolution_enabled() -> bool
Returns the user setting for dynamic resolution.

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dynamic_resolution_dirty"></a>

#### is\_dynamic\_resolution\_dirty

```python
def is_dynamic_resolution_dirty() -> bool
```

x.is_dynamic_resolution_dirty() -> bool
Checks if the dynamic resolution user setting is different from current system setting

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dirty"></a>

#### is\_dirty

```python
def is_dirty() -> bool
```

x.is_dirty() -> bool
Checks if any user settings is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.get_visual_effect_quality"></a>

#### get\_visual\_effect\_quality

```python
def get_visual_effect_quality() -> int
```

x.get_visual_effect_quality() -> int32
Returns the visual effects quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_view_distance_quality"></a>

#### get\_view\_distance\_quality

```python
def get_view_distance_quality() -> int
```

x.get_view_distance_quality() -> int32
Returns the view distance quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_texture_quality"></a>

#### get\_texture\_quality

```python
def get_texture_quality() -> int
```

x.get_texture_quality() -> int32
Returns the texture quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_sync_interval"></a>

#### get\_sync\_interval

```python
@classmethod
def get_sync_interval(cls) -> int
```

X.get_sync_interval() -> int32
Get Sync Interval

Returns:
    int32:

<a id="unreal.GameUserSettings.get_shadow_quality"></a>

#### get\_shadow\_quality

```python
def get_shadow_quality() -> int
```

x.get_shadow_quality() -> int32
Returns the shadow quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_shading_quality"></a>

#### get\_shading\_quality

```python
def get_shading_quality() -> int
```

x.get_shading_quality() -> int32
Returns the shading quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_screen_resolution"></a>

#### get\_screen\_resolution

```python
def get_screen_resolution() -> IntPoint
```

x.get_screen_resolution() -> IntPoint
Returns the user setting for game screen resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_resolution_scale_normalized"></a>

#### get\_resolution\_scale\_normalized

```python
def get_resolution_scale_normalized() -> float
```

x.get_resolution_scale_normalized() -> float
Gets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

Returns:
    float:

<a id="unreal.GameUserSettings.get_resolution_scale_information_ex"></a>

#### get\_resolution\_scale\_information\_ex

```python
def get_resolution_scale_information_ex() -> Tuple[float, float, float, float]
```

x.get_resolution_scale_information_ex() -> (current_scale_normalized=float, current_scale_value=float, min_scale_value=float, max_scale_value=float)
Returns the current resolution scale and the range

Returns:
    tuple: 

    current_scale_normalized (float): 

    current_scale_value (float): 

    min_scale_value (float): 

    max_scale_value (float):

<a id="unreal.GameUserSettings.get_reflection_quality"></a>

#### get\_reflection\_quality

```python
def get_reflection_quality() -> int
```

x.get_reflection_quality() -> int32
Returns the reflection quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_recommended_resolution_scale"></a>

#### get\_recommended\_resolution\_scale

```python
def get_recommended_resolution_scale() -> float
```

x.get_recommended_resolution_scale() -> float
Gets the recommended resolution quality based on LastRecommendedScreenWidth/Height and the current screen resolution

Returns:
    float:

<a id="unreal.GameUserSettings.get_preferred_fullscreen_mode"></a>

#### get\_preferred\_fullscreen\_mode

```python
def get_preferred_fullscreen_mode() -> WindowMode
```

x.get_preferred_fullscreen_mode() -> WindowMode
Returns the user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_post_processing_quality"></a>

#### get\_post\_processing\_quality

```python
def get_post_processing_quality() -> int
```

x.get_post_processing_quality() -> int32
Returns the post-processing quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_overall_scalability_level"></a>

#### get\_overall\_scalability\_level

```python
def get_overall_scalability_level() -> int
```

x.get_overall_scalability_level() -> int32
Returns the overall scalability level (can return -1 if the settings are custom)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_last_confirmed_screen_resolution"></a>

#### get\_last\_confirmed\_screen\_resolution

```python
def get_last_confirmed_screen_resolution() -> IntPoint
```

x.get_last_confirmed_screen_resolution() -> IntPoint
Returns the last confirmed user setting for game screen resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_last_confirmed_fullscreen_mode"></a>

#### get\_last\_confirmed\_fullscreen\_mode

```python
def get_last_confirmed_fullscreen_mode() -> WindowMode
```

x.get_last_confirmed_fullscreen_mode() -> WindowMode
Returns the last confirmed user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_global_illumination_quality"></a>

#### get\_global\_illumination\_quality

```python
def get_global_illumination_quality() -> int
```

x.get_global_illumination_quality() -> int32
Returns the global illumination quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_game_user_settings"></a>

#### get\_game\_user\_settings

```python
@classmethod
def get_game_user_settings(cls) -> GameUserSettings
```

X.get_game_user_settings() -> GameUserSettings
Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

Returns:
    GameUserSettings:

<a id="unreal.GameUserSettings.get_fullscreen_mode"></a>

#### get\_fullscreen\_mode

```python
def get_fullscreen_mode() -> WindowMode
```

x.get_fullscreen_mode() -> WindowMode
Returns the user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_frame_rate_limit"></a>

#### get\_frame\_rate\_limit

```python
def get_frame_rate_limit() -> float
```

x.get_frame_rate_limit() -> float
Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

Returns:
    float:

<a id="unreal.GameUserSettings.get_frame_pace"></a>

#### get\_frame\_pace

```python
@classmethod
def get_frame_pace(cls) -> int
```

X.get_frame_pace() -> int32
Gets the current frame pacing frame rate in fps, or 0 if none

Returns:
    int32:

<a id="unreal.GameUserSettings.get_foliage_quality"></a>

#### get\_foliage\_quality

```python
def get_foliage_quality() -> int
```

x.get_foliage_quality() -> int32
Returns the foliage quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_desktop_resolution"></a>

#### get\_desktop\_resolution

```python
def get_desktop_resolution() -> IntPoint
```

x.get_desktop_resolution() -> IntPoint
Returns user's desktop resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_default_window_position"></a>

#### get\_default\_window\_position

```python
@classmethod
def get_default_window_position(cls) -> IntPoint
```

X.get_default_window_position() -> IntPoint
Returns the default window position when no position is set

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_default_window_mode"></a>

#### get\_default\_window\_mode

```python
@classmethod
def get_default_window_mode(cls) -> WindowMode
```

X.get_default_window_mode() -> WindowMode
Returns the default window mode when no mode is set

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_default_resolution_scale"></a>

#### get\_default\_resolution\_scale

```python
def get_default_resolution_scale() -> float
```

x.get_default_resolution_scale() -> float
Gets the desired resolution quality based on DesiredScreenWidth/Height and the current screen resolution

Returns:
    float:

<a id="unreal.GameUserSettings.get_default_resolution"></a>

#### get\_default\_resolution

```python
@classmethod
def get_default_resolution(cls) -> IntPoint
```

X.get_default_resolution() -> IntPoint
Returns the default resolution when no resolution is set

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_current_hdr_display_nits"></a>

#### get\_current\_hdr\_display\_nits

```python
def get_current_hdr_display_nits() -> int
```

x.get_current_hdr_display_nits() -> int32
Returns 0 if HDR isn't supported or is turned off

Returns:
    int32:

<a id="unreal.GameUserSettings.get_audio_quality_level"></a>

#### get\_audio\_quality\_level

```python
def get_audio_quality_level() -> int
```

x.get_audio_quality_level() -> int32
Returns the user's audio quality level setting

Returns:
    int32:

<a id="unreal.GameUserSettings.get_anti_aliasing_quality"></a>

#### get\_anti\_aliasing\_quality

```python
def get_anti_aliasing_quality() -> int
```

x.get_anti_aliasing_quality() -> int32
Returns the anti-aliasing quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.enable_hdr_display_output"></a>

#### enable\_hdr\_display\_output

```python
def enable_hdr_display_output(enable: bool, display_nits: int = 1000) -> None
```

x.enable_hdr_display_output(enable, display_nits=1000) -> None
Enables or disables HDR display output. Can be called again to change the desired nit level

Args:
    enable (bool): 
    display_nits (int32):

<a id="unreal.GameUserSettings.confirm_video_mode"></a>

#### confirm\_video\_mode

```python
def confirm_video_mode() -> None
```

x.confirm_video_mode() -> None
Mark current video mode settings (fullscreenmode/resolution) as being confirmed by the user

<a id="unreal.GameUserSettings.apply_settings"></a>

#### apply\_settings

```python
def apply_settings(check_for_command_line_overrides: bool = True) -> None
```

x.apply_settings(check_for_command_line_overrides=True) -> None
Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

Args:
    check_for_command_line_overrides (bool):

<a id="unreal.GameUserSettings.apply_resolution_settings"></a>

#### apply\_resolution\_settings

```python
def apply_resolution_settings(check_for_command_line_overrides: bool) -> None
```

x.apply_resolution_settings(check_for_command_line_overrides) -> None
Apply Resolution Settings

Args:
    check_for_command_line_overrides (bool):

<a id="unreal.GameUserSettings.apply_non_resolution_settings"></a>

#### apply\_non\_resolution\_settings

```python
def apply_non_resolution_settings() -> None
```

x.apply_non_resolution_settings() -> None
Apply Non Resolution Settings

<a id="unreal.GameUserSettings.apply_hardware_benchmark_results"></a>

#### apply\_hardware\_benchmark\_results

```python
def apply_hardware_benchmark_results() -> None
```

x.apply_hardware_benchmark_results() -> None
Applies the settings stored in ScalabilityQuality and saves settings

<a id="unreal.InputDeviceLibrary"></a>