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

#### on_game_user_settings_ui_needs_update

```python
@property
def on_game_user_settings_ui_needs_update() -> OnGameUserSettingsUINeedsUpdate
```

(OnGameUserSettingsUINeedsUpdate):  [Read-Write]

<a id="unreal.GameUserSettings.on_game_user_settings_ui_needs_update"></a>

#### on_game_user_settings_ui_needs_update

```python
@on_game_user_settings_ui_needs_update.setter
def on_game_user_settings_ui_needs_update(
        value: OnGameUserSettingsUINeedsUpdate) -> None
```

<a id="unreal.GameUserSettings.validate_settings"></a>

#### validate_settings

```python
def validate_settings() -> None
```

x.validate_settings() -> None
Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

<a id="unreal.GameUserSettings.supports_hdr_display_output"></a>

#### supports_hdr_display_output

```python
def supports_hdr_display_output() -> bool
```

x.supports_hdr_display_output() -> bool
Whether the curently running system supports HDR display output

Returns:
    bool:

<a id="unreal.GameUserSettings.set_v_sync_enabled"></a>

#### set_v_sync_enabled

```python
def set_v_sync_enabled(enable: bool) -> None
```

x.set_v_sync_enabled(enable) -> None
Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

Args:
    enable (bool):

<a id="unreal.GameUserSettings.set_visual_effect_quality"></a>

#### set_visual_effect_quality

```python
def set_visual_effect_quality(value: int) -> None
```

x.set_visual_effect_quality(value) -> None
Sets the visual effects quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_view_distance_quality"></a>

#### set_view_distance_quality

```python
def set_view_distance_quality(value: int) -> None
```

x.set_view_distance_quality(value) -> None
Sets the view distance quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_to_defaults"></a>

#### set_to_defaults

```python
def set_to_defaults() -> None
```

x.set_to_defaults() -> None
Set to Defaults

<a id="unreal.GameUserSettings.set_texture_quality"></a>

#### set_texture_quality

```python
def set_texture_quality(value: int) -> None
```

x.set_texture_quality(value) -> None
Sets the texture quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic  (gets clamped if needed)

<a id="unreal.GameUserSettings.set_shadow_quality"></a>

#### set_shadow_quality

```python
def set_shadow_quality(value: int) -> None
```

x.set_shadow_quality(value) -> None
Sets the shadow quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_shading_quality"></a>

#### set_shading_quality

```python
def set_shading_quality(value: int) -> None
```

x.set_shading_quality(value) -> None
Sets the shading quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_screen_resolution"></a>

#### set_screen_resolution

```python
def set_screen_resolution(resolution: IntPoint) -> None
```

x.set_screen_resolution(resolution) -> None
Sets the user setting for game screen resolution, in pixels.

Args:
    resolution (IntPoint):

<a id="unreal.GameUserSettings.set_resolution_scale_value_ex"></a>

#### set_resolution_scale_value_ex

```python
def set_resolution_scale_value_ex(new_scale_value: float) -> None
```

x.set_resolution_scale_value_ex(new_scale_value) -> None
Sets the current resolution scale

Args:
    new_scale_value (float):

<a id="unreal.GameUserSettings.set_resolution_scale_normalized"></a>

#### set_resolution_scale_normalized

```python
def set_resolution_scale_normalized(new_scale_normalized: float) -> None
```

x.set_resolution_scale_normalized(new_scale_normalized) -> None
Sets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

Args:
    new_scale_normalized (float):

<a id="unreal.GameUserSettings.set_reflection_quality"></a>

#### set_reflection_quality

```python
def set_reflection_quality(value: int) -> None
```

x.set_reflection_quality(value) -> None
Sets the reflection quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_post_processing_quality"></a>

#### set_post_processing_quality

```python
def set_post_processing_quality(value: int) -> None
```

x.set_post_processing_quality(value) -> None
Sets the post-processing quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_overall_scalability_level"></a>

#### set_overall_scalability_level

```python
def set_overall_scalability_level(value: int) -> None
```

x.set_overall_scalability_level(value) -> None
Changes all scalability settings at once based on a single overall quality level

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic

<a id="unreal.GameUserSettings.set_global_illumination_quality"></a>

#### set_global_illumination_quality

```python
def set_global_illumination_quality(value: int) -> None
```

x.set_global_illumination_quality(value) -> None
Sets the global illumination quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_fullscreen_mode"></a>

#### set_fullscreen_mode

```python
def set_fullscreen_mode(fullscreen_mode: WindowMode) -> None
```

x.set_fullscreen_mode(fullscreen_mode) -> None
Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

Args:
    fullscreen_mode (WindowMode):

<a id="unreal.GameUserSettings.set_frame_rate_limit"></a>

#### set_frame_rate_limit

```python
def set_frame_rate_limit(new_limit: float) -> None
```

x.set_frame_rate_limit(new_limit) -> None
Sets the user's frame rate limit (0 will disable frame rate limiting)

Args:
    new_limit (float):

<a id="unreal.GameUserSettings.set_foliage_quality"></a>

#### set_foliage_quality

```python
def set_foliage_quality(value: int) -> None
```

x.set_foliage_quality(value) -> None
Sets the foliage quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.set_dynamic_resolution_enabled"></a>

#### set_dynamic_resolution_enabled

```python
def set_dynamic_resolution_enabled(enable: bool) -> None
```

x.set_dynamic_resolution_enabled(enable) -> None
Sets the user setting for dynamic resolution. See UGameUserSettings::bUseDynamicResolution.

Args:
    enable (bool):

<a id="unreal.GameUserSettings.set_benchmark_fallback_values"></a>

#### set_benchmark_fallback_values

```python
def set_benchmark_fallback_values() -> None
```

x.set_benchmark_fallback_values() -> None
Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

<a id="unreal.GameUserSettings.set_audio_quality_level"></a>

#### set_audio_quality_level

```python
def set_audio_quality_level(quality_level: int) -> None
```

x.set_audio_quality_level(quality_level) -> None
Sets the user's audio quality level setting

Args:
    quality_level (int32):

<a id="unreal.GameUserSettings.set_anti_aliasing_quality"></a>

#### set_anti_aliasing_quality

```python
def set_anti_aliasing_quality(value: int) -> None
```

x.set_anti_aliasing_quality(value) -> None
Sets the anti-aliasing quality (0..4, higher is better)

Args:
    value (int32): 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

<a id="unreal.GameUserSettings.save_settings"></a>

#### save_settings

```python
def save_settings() -> None
```

x.save_settings() -> None
Save the user settings to persistent storage (automatically happens as part of ApplySettings)

<a id="unreal.GameUserSettings.run_hardware_benchmark"></a>

#### run_hardware_benchmark

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

#### revert_video_mode

```python
def revert_video_mode() -> None
```

x.revert_video_mode() -> None
Revert video mode (fullscreenmode/resolution) back to the last user confirmed values

<a id="unreal.GameUserSettings.reset_to_current_settings"></a>

#### reset_to_current_settings

```python
def reset_to_current_settings() -> None
```

x.reset_to_current_settings() -> None
This function resets all settings to the current system settings

<a id="unreal.GameUserSettings.load_settings"></a>

#### load_settings

```python
def load_settings(force_reload: bool = False) -> None
```

x.load_settings(force_reload=False) -> None
Loads the user settings from persistent storage

Args:
    force_reload (bool):

<a id="unreal.GameUserSettings.is_v_sync_enabled"></a>

#### is_v_sync_enabled

```python
def is_v_sync_enabled() -> bool
```

x.is_v_sync_enabled() -> bool
Returns the user setting for vsync.

Returns:
    bool:

<a id="unreal.GameUserSettings.is_v_sync_dirty"></a>

#### is_v_sync_dirty

```python
def is_v_sync_dirty() -> bool
```

x.is_v_sync_dirty() -> bool
Checks if the vsync user setting is different from current system setting

Returns:
    bool:

<a id="unreal.GameUserSettings.is_screen_resolution_dirty"></a>

#### is_screen_resolution_dirty

```python
def is_screen_resolution_dirty() -> bool
```

x.is_screen_resolution_dirty() -> bool
Checks if the Screen Resolution user setting is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.is_hdr_enabled"></a>

#### is_hdr_enabled

```python
def is_hdr_enabled() -> bool
```

x.is_hdr_enabled() -> bool
Is HDREnabled

Returns:
    bool:

<a id="unreal.GameUserSettings.is_fullscreen_mode_dirty"></a>

#### is_fullscreen_mode_dirty

```python
def is_fullscreen_mode_dirty() -> bool
```

x.is_fullscreen_mode_dirty() -> bool
Checks if the FullscreenMode user setting is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dynamic_resolution_enabled"></a>

#### is_dynamic_resolution_enabled

```python
def is_dynamic_resolution_enabled() -> bool
```

x.is_dynamic_resolution_enabled() -> bool
Returns the user setting for dynamic resolution.

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dynamic_resolution_dirty"></a>

#### is_dynamic_resolution_dirty

```python
def is_dynamic_resolution_dirty() -> bool
```

x.is_dynamic_resolution_dirty() -> bool
Checks if the dynamic resolution user setting is different from current system setting

Returns:
    bool:

<a id="unreal.GameUserSettings.is_dirty"></a>

#### is_dirty

```python
def is_dirty() -> bool
```

x.is_dirty() -> bool
Checks if any user settings is different from current

Returns:
    bool:

<a id="unreal.GameUserSettings.get_visual_effect_quality"></a>

#### get_visual_effect_quality

```python
def get_visual_effect_quality() -> int
```

x.get_visual_effect_quality() -> int32
Returns the visual effects quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_view_distance_quality"></a>

#### get_view_distance_quality

```python
def get_view_distance_quality() -> int
```

x.get_view_distance_quality() -> int32
Returns the view distance quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_texture_quality"></a>

#### get_texture_quality

```python
def get_texture_quality() -> int
```

x.get_texture_quality() -> int32
Returns the texture quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_sync_interval"></a>

#### get_sync_interval

```python
@classmethod
def get_sync_interval(cls) -> int
```

X.get_sync_interval() -> int32
Get Sync Interval

Returns:
    int32:

<a id="unreal.GameUserSettings.get_shadow_quality"></a>

#### get_shadow_quality

```python
def get_shadow_quality() -> int
```

x.get_shadow_quality() -> int32
Returns the shadow quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_shading_quality"></a>

#### get_shading_quality

```python
def get_shading_quality() -> int
```

x.get_shading_quality() -> int32
Returns the shading quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_screen_resolution"></a>

#### get_screen_resolution

```python
def get_screen_resolution() -> IntPoint
```

x.get_screen_resolution() -> IntPoint
Returns the user setting for game screen resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_resolution_scale_normalized"></a>

#### get_resolution_scale_normalized

```python
def get_resolution_scale_normalized() -> float
```

x.get_resolution_scale_normalized() -> float
Gets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

Returns:
    float:

<a id="unreal.GameUserSettings.get_resolution_scale_information_ex"></a>

#### get_resolution_scale_information_ex

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

#### get_reflection_quality

```python
def get_reflection_quality() -> int
```

x.get_reflection_quality() -> int32
Returns the reflection quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_recommended_resolution_scale"></a>

#### get_recommended_resolution_scale

```python
def get_recommended_resolution_scale() -> float
```

x.get_recommended_resolution_scale() -> float
Gets the recommended resolution quality based on LastRecommendedScreenWidth/Height and the current screen resolution

Returns:
    float:

<a id="unreal.GameUserSettings.get_preferred_fullscreen_mode"></a>

#### get_preferred_fullscreen_mode

```python
def get_preferred_fullscreen_mode() -> WindowMode
```

x.get_preferred_fullscreen_mode() -> WindowMode
Returns the user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_post_processing_quality"></a>

#### get_post_processing_quality

```python
def get_post_processing_quality() -> int
```

x.get_post_processing_quality() -> int32
Returns the post-processing quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_overall_scalability_level"></a>

#### get_overall_scalability_level

```python
def get_overall_scalability_level() -> int
```

x.get_overall_scalability_level() -> int32
Returns the overall scalability level (can return -1 if the settings are custom)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_last_confirmed_screen_resolution"></a>

#### get_last_confirmed_screen_resolution

```python
def get_last_confirmed_screen_resolution() -> IntPoint
```

x.get_last_confirmed_screen_resolution() -> IntPoint
Returns the last confirmed user setting for game screen resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_last_confirmed_fullscreen_mode"></a>

#### get_last_confirmed_fullscreen_mode

```python
def get_last_confirmed_fullscreen_mode() -> WindowMode
```

x.get_last_confirmed_fullscreen_mode() -> WindowMode
Returns the last confirmed user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_global_illumination_quality"></a>

#### get_global_illumination_quality

```python
def get_global_illumination_quality() -> int
```

x.get_global_illumination_quality() -> int32
Returns the global illumination quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_game_user_settings"></a>

#### get_game_user_settings

```python
@classmethod
def get_game_user_settings(cls) -> GameUserSettings
```

X.get_game_user_settings() -> GameUserSettings
Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

Returns:
    GameUserSettings:

<a id="unreal.GameUserSettings.get_fullscreen_mode"></a>

#### get_fullscreen_mode

```python
def get_fullscreen_mode() -> WindowMode
```

x.get_fullscreen_mode() -> WindowMode
Returns the user setting for game window fullscreen mode.

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_frame_rate_limit"></a>

#### get_frame_rate_limit

```python
def get_frame_rate_limit() -> float
```

x.get_frame_rate_limit() -> float
Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

Returns:
    float:

<a id="unreal.GameUserSettings.get_frame_pace"></a>

#### get_frame_pace

```python
@classmethod
def get_frame_pace(cls) -> int
```

X.get_frame_pace() -> int32
Gets the current frame pacing frame rate in fps, or 0 if none

Returns:
    int32:

<a id="unreal.GameUserSettings.get_foliage_quality"></a>

#### get_foliage_quality

```python
def get_foliage_quality() -> int
```

x.get_foliage_quality() -> int32
Returns the foliage quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.get_desktop_resolution"></a>

#### get_desktop_resolution

```python
def get_desktop_resolution() -> IntPoint
```

x.get_desktop_resolution() -> IntPoint
Returns user's desktop resolution, in pixels.

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_default_window_position"></a>

#### get_default_window_position

```python
@classmethod
def get_default_window_position(cls) -> IntPoint
```

X.get_default_window_position() -> IntPoint
Returns the default window position when no position is set

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_default_window_mode"></a>

#### get_default_window_mode

```python
@classmethod
def get_default_window_mode(cls) -> WindowMode
```

X.get_default_window_mode() -> WindowMode
Returns the default window mode when no mode is set

Returns:
    WindowMode:

<a id="unreal.GameUserSettings.get_default_resolution_scale"></a>

#### get_default_resolution_scale

```python
def get_default_resolution_scale() -> float
```

x.get_default_resolution_scale() -> float
Gets the desired resolution quality based on DesiredScreenWidth/Height and the current screen resolution

Returns:
    float:

<a id="unreal.GameUserSettings.get_default_resolution"></a>

#### get_default_resolution

```python
@classmethod
def get_default_resolution(cls) -> IntPoint
```

X.get_default_resolution() -> IntPoint
Returns the default resolution when no resolution is set

Returns:
    IntPoint:

<a id="unreal.GameUserSettings.get_current_hdr_display_nits"></a>

#### get_current_hdr_display_nits

```python
def get_current_hdr_display_nits() -> int
```

x.get_current_hdr_display_nits() -> int32
Returns 0 if HDR isn't supported or is turned off

Returns:
    int32:

<a id="unreal.GameUserSettings.get_audio_quality_level"></a>

#### get_audio_quality_level

```python
def get_audio_quality_level() -> int
```

x.get_audio_quality_level() -> int32
Returns the user's audio quality level setting

Returns:
    int32:

<a id="unreal.GameUserSettings.get_anti_aliasing_quality"></a>

#### get_anti_aliasing_quality

```python
def get_anti_aliasing_quality() -> int
```

x.get_anti_aliasing_quality() -> int32
Returns the anti-aliasing quality (0..4, higher is better)

Returns:
    int32:

<a id="unreal.GameUserSettings.enable_hdr_display_output"></a>

#### enable_hdr_display_output

```python
def enable_hdr_display_output(enable: bool, display_nits: int = 1000) -> None
```

x.enable_hdr_display_output(enable, display_nits=1000) -> None
Enables or disables HDR display output. Can be called again to change the desired nit level

Args:
    enable (bool): 
    display_nits (int32):

<a id="unreal.GameUserSettings.confirm_video_mode"></a>

#### confirm_video_mode

```python
def confirm_video_mode() -> None
```

x.confirm_video_mode() -> None
Mark current video mode settings (fullscreenmode/resolution) as being confirmed by the user

<a id="unreal.GameUserSettings.apply_settings"></a>

#### apply_settings

```python
def apply_settings(check_for_command_line_overrides: bool = True) -> None
```

x.apply_settings(check_for_command_line_overrides=True) -> None
Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

Args:
    check_for_command_line_overrides (bool):

<a id="unreal.GameUserSettings.apply_resolution_settings"></a>

#### apply_resolution_settings

```python
def apply_resolution_settings(check_for_command_line_overrides: bool) -> None
```

x.apply_resolution_settings(check_for_command_line_overrides) -> None
Apply Resolution Settings

Args:
    check_for_command_line_overrides (bool):

<a id="unreal.GameUserSettings.apply_non_resolution_settings"></a>

#### apply_non_resolution_settings

```python
def apply_non_resolution_settings() -> None
```

x.apply_non_resolution_settings() -> None
Apply Non Resolution Settings

<a id="unreal.GameUserSettings.apply_hardware_benchmark_results"></a>

#### apply_hardware_benchmark_results

```python
def apply_hardware_benchmark_results() -> None
```

x.apply_hardware_benchmark_results() -> None
Applies the settings stored in ScalabilityQuality and saves settings

<a id="unreal.InputDeviceLibrary"></a>