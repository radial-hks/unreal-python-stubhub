## SlateRHIRendererSettings Objects

```python
class SlateRHIRendererSettings(DeveloperSettings)
```

Settings used to control slate rendering

**C++ Source:**

- **Module**: SlateRHIRenderer
- **File**: SlateRHIRendererSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``slate_post_settings`` (Map[SlatePostRT, SlatePostSettings]):  [Read-Write] Map of all slate post RT's and their settings
  Note that each post RT used in a frame will result in 1 full framebuffer copy for slate to sample from.
  If a post RT is not used, no copy will occur & that post RT will be resized to 1x1 after 2 frames of non-use.

  By default only SlatePostRT_0 is enabled. The rest must manually be enabled in settings below.
          // Map is nice since needs no editor customization. After initial run there should be no more than 5 lookups each frame.

<a id="unreal.SlateRHIRendererSettings.get_slate_post_setting"></a>

#### get_slate_post_setting

```python
def get_slate_post_setting(post_buffer_bit: SlatePostRT) -> SlatePostSettings
```

x.get_slate_post_setting(post_buffer_bit) -> SlatePostSettings
Get settings struct for a particular post buffer index

Args:
    post_buffer_bit (SlatePostRT): 

Returns:
    SlatePostSettings:

<a id="unreal.SlateRHIRendererSettings.get_mutable_slate_post_setting"></a>

#### get_mutable_slate_post_setting

```python
def get_mutable_slate_post_setting(
        post_buffer_bit: SlatePostRT) -> SlatePostSettings
```

x.get_mutable_slate_post_setting(post_buffer_bit) -> SlatePostSettings
Get settings struct for a particular post buffer index

Args:
    post_buffer_bit (SlatePostRT): 

Returns:
    SlatePostSettings:

<a id="unreal.ListViewBase"></a>