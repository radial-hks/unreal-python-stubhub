## AutomationScreenshotOptions Objects

```python
class AutomationScreenshotOptions(StructBase)
```

Automation Screenshot Options

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: AutomationScreenshotOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delay`` (float):  [Read-Write] The delay before we take the screenshot (measured in seconds). Both this delay and the frame delay must be met before the screenshot is taken.
- ``disable_noisy_rendering_features`` (bool):  [Read-Write] Disables Anti-Aliasing, Motion Blur, Screen Space Reflections, Eye Adaptation, Tonemapper and Contact
  Shadows, because those features contribute a lot to the noise in the final rendered image.  If you're
  explicitly looking for changes. Unchecking the option will make accessible the Disable Eye Adaptation
  checkbox.
- ``disable_tonemapping`` (bool):  [Read-Write] Disables Eye Adaptation and sets Tonemapper to fixed gamma curve. Should generally be on unless
  testing tone mapping or other post-processing results.
- ``frame_delay`` (int32):  [Read-Write] The delay before we take the screenshot (measured in number of frames). Both this frame delay and the time delay must be met before the screenshot is taken.
- ``ignore_anti_aliasing`` (bool):  [Read-Write] If this is true, we search neighboring pixels looking for the expected pixel as what may have happened, is
  that the pixel shifted a little.
- ``ignore_colors`` (bool):  [Read-Write] If this is true, all we compare is luminance of the scene.
- ``maximum_global_error`` (float):  [Read-Write] After you've accounted for color tolerance changes, you now need to control for total acceptable error.
  Which depending on how pixels were colored on triangle edges may be a few percent of the image being
  outside the tolerance levels.
- ``maximum_local_error`` (float):  [Read-Write] After you've accounted for color tolerance changes, you now need to control for local acceptable error.
  Which depending on how pixels were colored on triangle edges may be a few percent of the image being
  outside the tolerance levels.  Unlike the MaximumGlobalError, the MaximumLocalError works by focusing
  on a smaller subset of the image.  These chunks will have be compared to the local error, in an attempt
  to locate hot spots of change that are important, that would be ignored by the global error.
- ``override_override_time_to`` (bool):  [Read-Write]
- ``override_time_to`` (double):  [Read-Write] Overrides World Time, Real Time to the value provided.  Sets Delta Time to 0.  Only
  affects the time being sent to the render thread and materials.  The time accumulating
  on the game thread is unaffected.
- ``resolution`` (Vector2D):  [Read-Write] The desired resolution of the screenshot, if none is provided, it will use the default for the
  platform setup in the automation settings.
- ``tolerance`` (ComparisonTolerance):  [Read-Write] These are quick defaults for tolerance levels, we default to low, because generally there's some
  constant variability in every pixel's color introduced by TxAA.
- ``tolerance_amount`` (ComparisonToleranceAmount):  [Read-Write] For each channel and brightness levels you can control a region where the colors are found to be
  essentially the same.  Generally this is necessary as modern rendering techniques tend to introduce
  noise constantly to hide aliasing.
- ``view_settings`` (AutomationViewSettings):  [Read-Write] Assign custom view settings to control which rendering options we allow on while taking the
  screenshot.
- ``visualize_buffer`` (Name):  [Read-Write] Allows you to screenshot a buffer other than the default final lit scene image.  Useful if you're
  trying to build a test for a specific GBuffer, that may be harder to tell if errors are introduced
  in it.

<a id="unreal.AutomationScreenshotOptions.__init__"></a>

#### __init__

```python
def __init__(resolution: Vector2D = [0.000000, 0.000000],
             delay: float = 0.000000,
             frame_delay: int = 0,
             override_override_time_to: bool = False,
             override_time_to: float = 0.000000,
             disable_noisy_rendering_features: bool = False,
             disable_tonemapping: bool = False,
             view_settings: AutomationViewSettings = None,
             visualize_buffer: Name = "None",
             tolerance: ComparisonTolerance = ComparisonTolerance.ZERO,
             tolerance_amount: ComparisonToleranceAmount = [],
             maximum_local_error: float = 0.000000,
             maximum_global_error: float = 0.000000,
             ignore_anti_aliasing: bool = False,
             ignore_colors: bool = False) -> None
```

<a id="unreal.AutomationScreenshotOptions.resolution"></a>

#### resolution

```python
@property
def resolution() -> Vector2D
```

(Vector2D):  [Read-Write] The desired resolution of the screenshot, if none is provided, it will use the default for the
platform setup in the automation settings.

<a id="unreal.AutomationScreenshotOptions.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: Vector2D) -> None
```

<a id="unreal.AutomationScreenshotOptions.delay"></a>

#### delay

```python
@property
def delay() -> float
```

(float):  [Read-Write] The delay before we take the screenshot (measured in seconds). Both this delay and the frame delay must be met before the screenshot is taken.

<a id="unreal.AutomationScreenshotOptions.delay"></a>

#### delay

```python
@delay.setter
def delay(value: float) -> None
```

<a id="unreal.AutomationScreenshotOptions.frame_delay"></a>

#### frame_delay

```python
@property
def frame_delay() -> int
```

(int32):  [Read-Write] The delay before we take the screenshot (measured in number of frames). Both this frame delay and the time delay must be met before the screenshot is taken.

<a id="unreal.AutomationScreenshotOptions.frame_delay"></a>

#### frame_delay

```python
@frame_delay.setter
def frame_delay(value: int) -> None
```

<a id="unreal.AutomationScreenshotOptions.override_override_time_to"></a>

#### override_override_time_to

```python
@property
def override_override_time_to() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AutomationScreenshotOptions.override_override_time_to"></a>

#### override_override_time_to

```python
@override_override_time_to.setter
def override_override_time_to(value: bool) -> None
```

<a id="unreal.AutomationScreenshotOptions.override_time_to"></a>

#### override_time_to

```python
@property
def override_time_to() -> float
```

(double):  [Read-Write] Overrides World Time, Real Time to the value provided.  Sets Delta Time to 0.  Only
affects the time being sent to the render thread and materials.  The time accumulating
on the game thread is unaffected.

<a id="unreal.AutomationScreenshotOptions.override_time_to"></a>

#### override_time_to

```python
@override_time_to.setter
def override_time_to(value: float) -> None
```

<a id="unreal.AutomationScreenshotOptions.disable_noisy_rendering_features"></a>

#### disable_noisy_rendering_features

```python
@property
def disable_noisy_rendering_features() -> bool
```

(bool):  [Read-Write] Disables Anti-Aliasing, Motion Blur, Screen Space Reflections, Eye Adaptation, Tonemapper and Contact
Shadows, because those features contribute a lot to the noise in the final rendered image.  If you're
explicitly looking for changes. Unchecking the option will make accessible the Disable Eye Adaptation
checkbox.

<a id="unreal.AutomationScreenshotOptions.disable_noisy_rendering_features"></a>

#### disable_noisy_rendering_features

```python
@disable_noisy_rendering_features.setter
def disable_noisy_rendering_features(value: bool) -> None
```

<a id="unreal.AutomationScreenshotOptions.disable_tonemapping"></a>

#### disable_tonemapping

```python
@property
def disable_tonemapping() -> bool
```

(bool):  [Read-Write] Disables Eye Adaptation and sets Tonemapper to fixed gamma curve. Should generally be on unless
testing tone mapping or other post-processing results.

<a id="unreal.AutomationScreenshotOptions.disable_tonemapping"></a>

#### disable_tonemapping

```python
@disable_tonemapping.setter
def disable_tonemapping(value: bool) -> None
```

<a id="unreal.AutomationScreenshotOptions.view_settings"></a>

#### view_settings

```python
@property
def view_settings() -> AutomationViewSettings
```

(AutomationViewSettings):  [Read-Write] Assign custom view settings to control which rendering options we allow on while taking the
screenshot.

<a id="unreal.AutomationScreenshotOptions.view_settings"></a>

#### view_settings

```python
@view_settings.setter
def view_settings(value: AutomationViewSettings) -> None
```

<a id="unreal.AutomationScreenshotOptions.visualize_buffer"></a>

#### visualize_buffer

```python
@property
def visualize_buffer() -> Name
```

(Name):  [Read-Write] Allows you to screenshot a buffer other than the default final lit scene image.  Useful if you're
trying to build a test for a specific GBuffer, that may be harder to tell if errors are introduced
in it.

<a id="unreal.AutomationScreenshotOptions.visualize_buffer"></a>

#### visualize_buffer

```python
@visualize_buffer.setter
def visualize_buffer(value: Name) -> None
```

<a id="unreal.AutomationScreenshotOptions.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> ComparisonTolerance
```

(ComparisonTolerance):  [Read-Write] These are quick defaults for tolerance levels, we default to low, because generally there's some
constant variability in every pixel's color introduced by TxAA.

<a id="unreal.AutomationScreenshotOptions.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: ComparisonTolerance) -> None
```

<a id="unreal.AutomationScreenshotOptions.tolerance_amount"></a>

#### tolerance_amount

```python
@property
def tolerance_amount() -> ComparisonToleranceAmount
```

(ComparisonToleranceAmount):  [Read-Write] For each channel and brightness levels you can control a region where the colors are found to be
essentially the same.  Generally this is necessary as modern rendering techniques tend to introduce
noise constantly to hide aliasing.

<a id="unreal.AutomationScreenshotOptions.tolerance_amount"></a>

#### tolerance_amount

```python
@tolerance_amount.setter
def tolerance_amount(value: ComparisonToleranceAmount) -> None
```

<a id="unreal.AutomationScreenshotOptions.maximum_local_error"></a>

#### maximum_local_error

```python
@property
def maximum_local_error() -> float
```

(float):  [Read-Write] After you've accounted for color tolerance changes, you now need to control for local acceptable error.
Which depending on how pixels were colored on triangle edges may be a few percent of the image being
outside the tolerance levels.  Unlike the MaximumGlobalError, the MaximumLocalError works by focusing
on a smaller subset of the image.  These chunks will have be compared to the local error, in an attempt
to locate hot spots of change that are important, that would be ignored by the global error.

<a id="unreal.AutomationScreenshotOptions.maximum_local_error"></a>

#### maximum_local_error

```python
@maximum_local_error.setter
def maximum_local_error(value: float) -> None
```

<a id="unreal.AutomationScreenshotOptions.maximum_global_error"></a>

#### maximum_global_error

```python
@property
def maximum_global_error() -> float
```

(float):  [Read-Write] After you've accounted for color tolerance changes, you now need to control for total acceptable error.
Which depending on how pixels were colored on triangle edges may be a few percent of the image being
outside the tolerance levels.

<a id="unreal.AutomationScreenshotOptions.maximum_global_error"></a>

#### maximum_global_error

```python
@maximum_global_error.setter
def maximum_global_error(value: float) -> None
```

<a id="unreal.AutomationScreenshotOptions.ignore_anti_aliasing"></a>

#### ignore_anti_aliasing

```python
@property
def ignore_anti_aliasing() -> bool
```

(bool):  [Read-Write] If this is true, we search neighboring pixels looking for the expected pixel as what may have happened, is
that the pixel shifted a little.

<a id="unreal.AutomationScreenshotOptions.ignore_anti_aliasing"></a>

#### ignore_anti_aliasing

```python
@ignore_anti_aliasing.setter
def ignore_anti_aliasing(value: bool) -> None
```

<a id="unreal.AutomationScreenshotOptions.ignore_colors"></a>

#### ignore_colors

```python
@property
def ignore_colors() -> bool
```

(bool):  [Read-Write] If this is true, all we compare is luminance of the scene.

<a id="unreal.AutomationScreenshotOptions.ignore_colors"></a>

#### ignore_colors

```python
@ignore_colors.setter
def ignore_colors(value: bool) -> None
```

<a id="unreal.AutomationWaitForLoadingOptions"></a>