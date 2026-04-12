## AutomationLibrary Objects

```python
class AutomationLibrary(BlueprintFunctionLibrary)
```

Automation Blueprint Function Library

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: AutomationBlueprintFunctionLibrary.h

<a id="unreal.AutomationLibrary.take_high_res_screenshot"></a>

#### take\_high\_res\_screenshot

```python
@classmethod
def take_high_res_screenshot(
        cls,
        res_x: int,
        res_y: int,
        filename: str,
        camera: CameraActor = None,
        mask_enabled: bool = False,
        capture_hdr: bool = False,
        comparison_tolerance: ComparisonTolerance = ComparisonTolerance.LOW,
        comparison_notes: str = "",
        delay: float = 0.000000,
        force_game_view: bool = True) -> AutomationEditorTask
```

X.take_high_res_screenshot(res_x, res_y, filename, camera=None, mask_enabled=False, capture_hdr=False, comparison_tolerance=ComparisonTolerance.LOW, comparison_notes="", delay=0.000000, force_game_view=True) -> AutomationEditorTask
take high res screenshot in editor.

Args:
    res_x (int32): 
    res_y (int32): 
    filename (str): 
    camera (CameraActor): 
    mask_enabled (bool): 
    capture_hdr (bool): 
    comparison_tolerance (ComparisonTolerance): 
    comparison_notes (str): 
    delay (float): 
    force_game_view (bool): 

Returns:
    AutomationEditorTask:

<a id="unreal.AutomationLibrary.take_automation_screenshot_of_ui"></a>

#### take\_automation\_screenshot\_of\_ui

```python
@classmethod
def take_automation_screenshot_of_ui(
        cls, world_context_object: Object, latent_info: LatentActionInfo,
        name: str, options: AutomationScreenshotOptions) -> None
```

X.take_automation_screenshot_of_ui(world_context_object, latent_info, name, options) -> None
Take Automation Screenshot Of UI

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    name (str): 
    options (AutomationScreenshotOptions):

<a id="unreal.AutomationLibrary.take_automation_screenshot_at_camera"></a>

#### take\_automation\_screenshot\_at\_camera

```python
@classmethod
def take_automation_screenshot_at_camera(
        cls,
        world_context_object: Object,
        latent_info: LatentActionInfo,
        camera: CameraActor,
        name_override: str = "",
        notes: str = ...,
        options: AutomationScreenshotOptions = ...) -> None
```

X.take_automation_screenshot_at_camera(world_context_object, latent_info, camera, name_override="", notes, options) -> None
Takes a screenshot of the game's viewport, from a particular camera actors POV.  Does not capture any UI.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    camera (CameraActor): 
    name_override (str): 
    notes (str): 
    options (AutomationScreenshotOptions):

<a id="unreal.AutomationLibrary.take_automation_screenshot"></a>

#### take\_automation\_screenshot

```python
@classmethod
def take_automation_screenshot(
        cls,
        world_context_object: Object,
        latent_info: LatentActionInfo,
        name: str = "",
        notes: str = ...,
        options: AutomationScreenshotOptions = ...) -> None
```

X.take_automation_screenshot(world_context_object, latent_info, name="", notes, options) -> None
Takes a screenshot of the game's viewport.  Does not capture any UI.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    name (str): 
    notes (str): 
    options (AutomationScreenshotOptions):

<a id="unreal.AutomationLibrary.set_test_telemetry_storage"></a>

#### set\_test\_telemetry\_storage

```python
@classmethod
def set_test_telemetry_storage(cls, storage_name: str) -> None
```

X.set_test_telemetry_storage(storage_name) -> None
Set Telemetry data storage name of currently running automated test.

Args:
    storage_name (str):

<a id="unreal.AutomationLibrary.set_scalability_quality_to_low"></a>

#### set\_scalability\_quality\_to\_low

```python
@classmethod
def set_scalability_quality_to_low(cls, world_context_object: Object) -> None
```

X.set_scalability_quality_to_low(world_context_object) -> None
Set Scalability Quality to Low

Args:
    world_context_object (Object):

<a id="unreal.AutomationLibrary.set_scalability_quality_to_epic"></a>

#### set\_scalability\_quality\_to\_epic

```python
@classmethod
def set_scalability_quality_to_epic(cls, world_context_object: Object) -> None
```

X.set_scalability_quality_to_epic(world_context_object) -> None
Set Scalability Quality to Epic

Args:
    world_context_object (Object):

<a id="unreal.AutomationLibrary.set_scalability_quality_level_relative_to_max"></a>

#### set\_scalability\_quality\_level\_relative\_to\_max

```python
@classmethod
def set_scalability_quality_level_relative_to_max(cls,
                                                  world_context_object: Object,
                                                  value: int = 1) -> None
```

X.set_scalability_quality_level_relative_to_max(world_context_object, value=1) -> None
Sets all other settings based on an overall value

Args:
    world_context_object (Object): 
    value (int32): 0:Cinematic, 1:Epic...etc.

<a id="unreal.AutomationLibrary.set_editor_viewport_visualize_buffer"></a>

#### set\_editor\_viewport\_visualize\_buffer

```python
@classmethod
def set_editor_viewport_visualize_buffer(cls, buffer_name: Name) -> None
```

X.set_editor_viewport_visualize_buffer(buffer_name) -> None
Sets all viewports of the first found level editor to have the VisualizeBuffer ViewMode and also display a given buffer (BaseColor/Metallic/Roughness/etc.) *

Args:
    buffer_name (Name):

<a id="unreal.AutomationLibrary.set_editor_viewport_view_mode"></a>

#### set\_editor\_viewport\_view\_mode

```python
@classmethod
def set_editor_viewport_view_mode(cls, index: ViewModeIndex) -> None
```

X.set_editor_viewport_view_mode(index) -> None
Sets all viewports of the first found level editor to have the given ViewMode (Lit/Unlit/etc.) *

Args:
    index (ViewModeIndex):

<a id="unreal.AutomationLibrary.get_stat_inc_max"></a>

#### get\_stat\_inc\_max

```python
@classmethod
def get_stat_inc_max(cls, stat_name: Name) -> float
```

X.get_stat_inc_max(stat_name) -> float
Get Stat Inc Max

Args:
    stat_name (Name): 

Returns:
    float:

<a id="unreal.AutomationLibrary.get_stat_inc_average"></a>

#### get\_stat\_inc\_average

```python
@classmethod
def get_stat_inc_average(cls, stat_name: Name) -> float
```

X.get_stat_inc_average(stat_name) -> float
Get Stat Inc Average

Args:
    stat_name (Name): 

Returns:
    float:

<a id="unreal.AutomationLibrary.get_stat_exc_max"></a>

#### get\_stat\_exc\_max

```python
@classmethod
def get_stat_exc_max(cls, stat_name: Name) -> float
```

X.get_stat_exc_max(stat_name) -> float
Get Stat Exc Max

Args:
    stat_name (Name): 

Returns:
    float:

<a id="unreal.AutomationLibrary.get_stat_exc_average"></a>

#### get\_stat\_exc\_average

```python
@classmethod
def get_stat_exc_average(cls, stat_name: Name) -> float
```

X.get_stat_exc_average(stat_name) -> float
Get Stat Exc Average

Args:
    stat_name (Name): 

Returns:
    float:

<a id="unreal.AutomationLibrary.get_stat_call_count"></a>

#### get\_stat\_call\_count

```python
@classmethod
def get_stat_call_count(cls, stat_name: Name) -> float
```

X.get_stat_call_count(stat_name) -> float
Get Stat Call Count

Args:
    stat_name (Name): 

Returns:
    float:

<a id="unreal.AutomationLibrary.get_default_screenshot_options_for_rendering"></a>

#### get\_default\_screenshot\_options\_for\_rendering

```python
@classmethod
def get_default_screenshot_options_for_rendering(
        cls,
        tolerance: ComparisonTolerance = ComparisonTolerance.LOW,
        delay: float = 0.200000) -> AutomationScreenshotOptions
```

X.get_default_screenshot_options_for_rendering(tolerance=ComparisonTolerance.LOW, delay=0.200000) -> AutomationScreenshotOptions
Get Default Screenshot Options for Rendering

Args:
    tolerance (ComparisonTolerance): 
    delay (float): 

Returns:
    AutomationScreenshotOptions:

<a id="unreal.AutomationLibrary.get_default_screenshot_options_for_gameplay"></a>

#### get\_default\_screenshot\_options\_for\_gameplay

```python
@classmethod
def get_default_screenshot_options_for_gameplay(
        cls,
        tolerance: ComparisonTolerance = ComparisonTolerance.LOW,
        delay: float = 0.200000) -> AutomationScreenshotOptions
```

X.get_default_screenshot_options_for_gameplay(tolerance=ComparisonTolerance.LOW, delay=0.200000) -> AutomationScreenshotOptions
Get Default Screenshot Options for Gameplay

Args:
    tolerance (ComparisonTolerance): 
    delay (float): 

Returns:
    AutomationScreenshotOptions:

<a id="unreal.AutomationLibrary.finish_loading_before_screenshot"></a>

#### finish\_loading\_before\_screenshot

```python
@classmethod
def finish_loading_before_screenshot(cls) -> None
```

X.finish_loading_before_screenshot() -> None
Finish Loading Before Screenshot

<a id="unreal.AutomationLibrary.enable_stat_group"></a>

#### enable\_stat\_group

```python
@classmethod
def enable_stat_group(cls, world_context_object: Object,
                      group_name: Name) -> None
```

X.enable_stat_group(world_context_object, group_name) -> None
Enable Stat Group

Args:
    world_context_object (Object): 
    group_name (Name):

<a id="unreal.AutomationLibrary.disable_stat_group"></a>

#### disable\_stat\_group

```python
@classmethod
def disable_stat_group(cls, world_context_object: Object,
                       group_name: Name) -> None
```

X.disable_stat_group(world_context_object, group_name) -> None
Disable Stat Group

Args:
    world_context_object (Object): 
    group_name (Name):

<a id="unreal.AutomationLibrary.compare_image_against_reference"></a>

#### compare\_image\_against\_reference

```python
@classmethod
def compare_image_against_reference(
        cls,
        image_file_path: str,
        comparison_name: str = "",
        comparison_tolerance: ComparisonTolerance = ComparisonTolerance.LOW,
        comparison_notes: str = "",
        world_context_object: Object = None) -> bool
```

X.compare_image_against_reference(image_file_path, comparison_name="", comparison_tolerance=ComparisonTolerance.LOW, comparison_notes="", world_context_object=None) -> bool
request image comparison.

Args:
    image_file_path (str): Absolute path to the image location. All 8bit RGBA channels supported formats by the engine are accepted.
    comparison_name (str): Optional name for the comparison, by default the basename of ImageFilePath is used
    comparison_tolerance (ComparisonTolerance): 
    comparison_notes (str): 
    world_context_object (Object): 

Returns:
    bool: True if comparison was successfully enqueued

<a id="unreal.AutomationLibrary.automation_wait_for_loading"></a>

#### automation\_wait\_for\_loading

```python
@classmethod
def automation_wait_for_loading(
        cls, world_context_object: Object, latent_info: LatentActionInfo,
        options: AutomationWaitForLoadingOptions) -> None
```

X.automation_wait_for_loading(world_context_object, latent_info, options) -> None
Automation Wait for Loading

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    options (AutomationWaitForLoadingOptions):

<a id="unreal.AutomationLibrary.are_automated_tests_running"></a>

#### are\_automated\_tests\_running

```python
@classmethod
def are_automated_tests_running(cls) -> bool
```

X.are_automated_tests_running() -> bool
Lets you know if any automated tests are running, or are about to run and the automation system is spinning up tests.

Returns:
    bool:

<a id="unreal.AutomationLibrary.add_test_warning"></a>

#### add\_test\_warning

```python
@classmethod
def add_test_warning(cls, log_item: str) -> None
```

X.add_test_warning(log_item) -> None
Add warning to currently running automated test.

Args:
    log_item (str):

<a id="unreal.AutomationLibrary.add_test_telemetry_data"></a>

#### add\_test\_telemetry\_data

```python
@classmethod
def add_test_telemetry_data(cls,
                            data_point: str,
                            measurement: float,
                            context: str = "") -> None
```

X.add_test_telemetry_data(data_point, measurement, context="") -> None
Add Telemetry data to currently running automated test.

Args:
    data_point (str): 
    measurement (float): 
    context (str):

<a id="unreal.AutomationLibrary.add_test_info"></a>

#### add\_test\_info

```python
@classmethod
def add_test_info(cls, log_item: str) -> None
```

X.add_test_info(log_item) -> None
Add info to currently running automated test.

Args:
    log_item (str):

<a id="unreal.AutomationLibrary.add_test_error"></a>

#### add\_test\_error

```python
@classmethod
def add_test_error(cls, log_item: str) -> None
```

X.add_test_error(log_item) -> None
Add error to currently running automated test.

Args:
    log_item (str):

<a id="unreal.AutomationLibrary.add_expected_plain_log_message"></a>

#### add\_expected\_plain\_log\_message

```python
@classmethod
def add_expected_plain_log_message(cls,
                                   expected_string: str,
                                   occurrences: int = 1,
                                   exact_match: bool = False) -> None
```

X.add_expected_plain_log_message(expected_string, occurrences=1, exact_match=False) -> None
Expect a specific log message to match a plain string during an automated test regardless of its verbosity

Args:
    expected_string (str): 
    occurrences (int32): 
    exact_match (bool):

<a id="unreal.AutomationLibrary.add_expected_plain_log_error"></a>

#### add\_expected\_plain\_log\_error

```python
@classmethod
def add_expected_plain_log_error(cls,
                                 expected_string: str,
                                 occurrences: int = 1,
                                 exact_match: bool = False) -> None
```

X.add_expected_plain_log_error(expected_string, occurrences=1, exact_match=False) -> None
Mute the report of log error and warning matching a plain string during an automated test

Args:
    expected_string (str): 
    occurrences (int32): 
    exact_match (bool):

<a id="unreal.AutomationLibrary.add_expected_log_message"></a>

#### add\_expected\_log\_message

```python
@classmethod
def add_expected_log_message(cls,
                             expected_pattern_string: str,
                             occurrences: int = 1,
                             exact_match: bool = False,
                             is_regex: bool = True) -> None
```

X.add_expected_log_message(expected_pattern_string, occurrences=1, exact_match=False, is_regex=True) -> None
Expect a specific log message to match a pattern during an automated test regardless of its verbosity. Treat the pattern as regex by default.

Args:
    expected_pattern_string (str): 
    occurrences (int32): 
    exact_match (bool): 
    is_regex (bool):

<a id="unreal.AutomationLibrary.add_expected_log_error"></a>

#### add\_expected\_log\_error

```python
@classmethod
def add_expected_log_error(cls,
                           expected_pattern_string: str,
                           occurrences: int = 1,
                           exact_match: bool = False,
                           is_regex: bool = True) -> None
```

X.add_expected_log_error(expected_pattern_string, occurrences=1, exact_match=False, is_regex=True) -> None
Mute the report of log error and warning matching a pattern during an automated test. Treat the pattern as regex by default.

Args:
    expected_pattern_string (str): Expects a Regex pattern.
    occurrences (int32): 
    exact_match (bool): 
    is_regex (bool):

<a id="unreal.FuncTestRenderingComponent"></a>