## LowEntryExtendedStandardLibrary Objects

```python
class LowEntryExtendedStandardLibrary(BlueprintFunctionLibrary)
```

Low Entry Extended Standard Library

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryExtendedStandardLibrary.h

<a id="unreal.LowEntryExtendedStandardLibrary.xbox_one_platform"></a>

#### xbox\_one\_platform

```python
@classmethod
def xbox_one_platform(cls) -> bool
```

X.xbox_one_platform() -> bool
Returns true if this is the Xbox One platform (PLATFORM_XBOXONE), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.with_editor"></a>

#### with\_editor

```python
@classmethod
def with_editor(cls) -> bool
```

X.with_editor() -> bool
Returns true if this is inside the editor (WITH_EDITOR), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.windows_rt_platform"></a>

#### windows\_rt\_platform

```python
@classmethod
def windows_rt_platform(cls) -> bool
```

X.windows_rt_platform() -> bool
Returns true if this is the Windows RT platform (PLATFORM_WINRT), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.windows_rt_arm_platform"></a>

#### windows\_rt\_arm\_platform

```python
@classmethod
def windows_rt_arm_platform(cls) -> bool
```

X.windows_rt_arm_platform() -> bool
Returns true if this is the Windows RT ARM platform (PLATFORM_WINRT_ARM), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.windows_platform"></a>

#### windows\_platform

```python
@classmethod
def windows_platform(cls) -> bool
```

X.windows_platform() -> bool
Returns true if this is the Windows platform (PLATFORM_WINDOWS), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.windows_newline_character"></a>

#### windows\_newline\_character

```python
@classmethod
def windows_newline_character(cls) -> str
```

X.windows_newline_character() -> str
Returns a Windows newline character (\r\n).

This blueprint will always return a \r\n character, no matter what Operating System it is running on.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.windows64_platform"></a>

#### windows64\_platform

```python
@classmethod
def windows64_platform(cls) -> bool
```

X.windows64_platform() -> bool
Returns true if this is the Windows platform running on 64 bit (PLATFORM_WINDOWS and _WIN64), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.windows32_platform"></a>

#### windows32\_platform

```python
@classmethod
def windows32_platform(cls) -> bool
```

X.windows32_platform() -> bool
Returns true if this is the Windows platform running on 32 bit (PLATFORM_WINDOWS and not _WIN64), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.tick_seconds"></a>

#### tick\_seconds

```python
@classmethod
def tick_seconds(cls, world_context_object: Object,
                 latent_info: LatentActionInfo, ticks: int,
                 seconds_interval: float) -> int
```

X.tick_seconds(world_context_object, latent_info, ticks, seconds_interval) -> int32
Ticks for x times, with x seconds interval between each tick.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    ticks (int32): 
    seconds_interval (double): 

Returns:
    int32: 

    tick (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.tick_frames"></a>

#### tick\_frames

```python
@classmethod
def tick_frames(cls, world_context_object: Object,
                latent_info: LatentActionInfo, ticks: int,
                frames_interval: int) -> int
```

X.tick_frames(world_context_object, latent_info, ticks, frames_interval) -> int32
Ticks for x times, with x frames interval between each tick.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    ticks (int32): 
    frames_interval (int32): 

Returns:
    int32: 

    tick (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.texture_update_resource"></a>

#### texture\_update\_resource

```python
@classmethod
def texture_update_resource(cls, texture: Texture) -> None
```

X.texture_update_resource(texture) -> None
Calls Texture->UpdateResource() if the given Texture is valid.

Updating the resource of a texture might take several frames. During these frames, the texture will be blank.

Args:
    texture (Texture):

<a id="unreal.LowEntryExtendedStandardLibrary.texture_render_target2d_to_pixels"></a>

#### texture\_render\_target2d\_to\_pixels

```python
@classmethod
def texture_render_target2d_to_pixels(
    cls, texture_render_target2d: TextureRenderTarget2D
) -> Tuple[int, int, Array[Color]]
```

X.texture_render_target2d_to_pixels(texture_render_target2d) -> (width=int32, height=int32, pixels=Array[Color])
Converts a TextureRenderTarget2D into a Pixel Array.

To get the best results:
 1) In the Texture Target's settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)

Returns an empty Pixel Array if it fails, the Width and the Height will also be 0 then.

Args:
    texture_render_target2d (TextureRenderTarget2D): 

Returns:
    tuple: 

    width (int32): 

    height (int32): 

    pixels (Array[Color]):

<a id="unreal.LowEntryExtendedStandardLibrary.texture_render_target2d_to_bytes"></a>

#### texture\_render\_target2d\_to\_bytes

```python
@classmethod
def texture_render_target2d_to_bytes(
        cls,
        texture_render_target2d: TextureRenderTarget2D,
        image_format: LowEntryImageFormat,
        compression_quality: int = 0) -> Array[int]
```

X.texture_render_target2d_to_bytes(texture_render_target2d, image_format, compression_quality=0) -> Array[uint8]
Converts a TextureRenderTarget2D into a Byte Array.

Some formats will not work (like BMP, ICO and ICNS).

The Compression Quality has to be 1-100, a value of 0 will use the default value for the given ImageFormat.

To get the best results:
 1) In the Texture Target's settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)

Returns an empty Byte Array if it fails.

Args:
    texture_render_target2d (TextureRenderTarget2D): 
    image_format (LowEntryImageFormat): 
    compression_quality (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.texture2d_to_pixels"></a>

#### texture2d\_to\_pixels

```python
@classmethod
def texture2d_to_pixels(cls,
                        texture2d: Texture2D) -> Tuple[int, int, Array[Color]]
```

X.texture2d_to_pixels(texture2d) -> (width=int32, height=int32, pixels=Array[Color])
Converts a Texture2D into a Pixel Array.

Returns an empty Pixel Array if it fails, the Width and the Height will also be 0 then.

Args:
    texture2d (Texture2D): 

Returns:
    tuple: 

    width (int32): 

    height (int32): 

    pixels (Array[Color]):

<a id="unreal.LowEntryExtendedStandardLibrary.texture2d_to_bytes"></a>

#### texture2d\_to\_bytes

```python
@classmethod
def texture2d_to_bytes(cls,
                       texture2d: Texture2D,
                       image_format: LowEntryImageFormat,
                       compression_quality: int = 0) -> Array[int]
```

X.texture2d_to_bytes(texture2d, image_format, compression_quality=0) -> Array[uint8]
Converts a Texture2D into a Byte Array.

Some formats will not work (like BMP, ICO and ICNS).

The Compression Quality has to be 1-100, a value of 0 will use the default value for the given ImageFormat.

Returns an empty Byte Array if it fails.

Args:
    texture2d (Texture2D): 
    image_format (LowEntryImageFormat): 
    compression_quality (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.test_build"></a>

#### test\_build

```python
@classmethod
def test_build(cls) -> bool
```

X.test_build() -> bool
Returns true if this is a debug build (UE_BUILD_TEST), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.tab_character"></a>

#### tab\_character

```python
@classmethod
def tab_character(cls) -> str
```

X.tab_character() -> str
Returns a tab character (\t).

This blueprint will always return a \t character, no matter what Operating System it is running on.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.switch_platform"></a>

#### switch\_platform

```python
@classmethod
def switch_platform(cls) -> bool
```

X.switch_platform() -> bool
Returns true if this is the Switch platform (PLATFORM_SWITCH), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.string_to_bytes_utf8"></a>

#### string\_to\_bytes\_utf8

```python
@classmethod
def string_to_bytes_utf8(cls, string: str) -> Array[int]
```

X.string_to_bytes_utf8(string) -> Array[uint8]
Converts a String into a Byte Array (using UTF-8 encoding).

Args:
    string (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.split_bytes"></a>

#### split\_bytes

```python
@classmethod
def split_bytes(cls, byte_array: Array[int],
                length_a: int) -> Tuple[Array[int], Array[int]]
```

X.split_bytes(byte_array, length_a) -> (a=Array[uint8], b=Array[uint8])
Splits the given Byte Array into two Byte Arrays.

Args:
    byte_array (Array[uint8]): 
    length_a (int32): 

Returns:
    tuple: 

    a (Array[uint8]): 

    b (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.sound_class_set_volume"></a>

#### sound\_class\_set\_volume

```python
@classmethod
def sound_class_set_volume(cls, sound_class: SoundClass,
                           volume: float) -> None
```

X.sound_class_set_volume(sound_class, volume) -> None
Sets the volume of a Sound Class.

Args:
    sound_class (SoundClass): 
    volume (double):

<a id="unreal.LowEntryExtendedStandardLibrary.sound_class_set_pitch"></a>

#### sound\_class\_set\_pitch

```python
@classmethod
def sound_class_set_pitch(cls, sound_class: SoundClass, pitch: float) -> None
```

X.sound_class_set_pitch(sound_class, pitch) -> None
Sets the pitch of a Sound Class.

Args:
    sound_class (SoundClass): 
    pitch (double):

<a id="unreal.LowEntryExtendedStandardLibrary.sound_class_get_volume"></a>

#### sound\_class\_get\_volume

```python
@classmethod
def sound_class_get_volume(cls, sound_class: SoundClass) -> float
```

X.sound_class_get_volume(sound_class) -> double
Returns the volume of a Sound Class.

Args:
    sound_class (SoundClass): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.sound_class_get_pitch"></a>

#### sound\_class\_get\_pitch

```python
@classmethod
def sound_class_get_pitch(cls, sound_class: SoundClass) -> float
```

X.sound_class_get_pitch(sound_class) -> double
Returns the pitch of a Sound Class.

Args:
    sound_class (SoundClass): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_timespan_array_directly"></a>

#### sort\_timespan\_array\_directly

```python
@classmethod
def sort_timespan_array_directly(cls,
                                 timespan_array: Array[Timespan],
                                 reversed: bool = False) -> Array[Timespan]
```

X.sort_timespan_array_directly(timespan_array, reversed=False) -> Array[Timespan]
Sorts the given array.

Args:
    timespan_array (Array[Timespan]): 
    reversed (bool): 

Returns:
    Array[Timespan]: 

    timespan_array (Array[Timespan]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_timespan_array"></a>

#### sort\_timespan\_array

```python
@classmethod
def sort_timespan_array(cls,
                        timespan_array: Array[Timespan],
                        reversed: bool = False) -> Array[Timespan]
```

X.sort_timespan_array(timespan_array, reversed=False) -> Array[Timespan]
Sorts a copy of the given array.

Args:
    timespan_array (Array[Timespan]): 
    reversed (bool): 

Returns:
    Array[Timespan]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_struct_array_directly"></a>

#### sort\_struct\_array\_directly

```python
@classmethod
def sort_struct_array_directly(
        cls,
        struct_array: Array[InstancedStruct],
        comparator: DelegateULowEntryExtendedStandardLibraryCompareStructs,
        reversed: bool = False) -> Array[InstancedStruct]
```

X.sort_struct_array_directly(struct_array, comparator, reversed=False) -> Array[InstancedStruct]
Sorts the given array.

To create the Comparator, do this:
 - create a function that has 2 input parameters (Object and Object) and 1 output parameter (Boolean)
 - it is important that the parameters have the following names: StructA, StructB and Return
 - in that function, return true if StructA is smaller than StructB, return false otherwise
 - then, when using the Sort Struct Array blueprint, use the Create Event blueprint and set its value as the function created earlier

Args:
    struct_array (Array[InstancedStruct]): 
    comparator (DelegateULowEntryExtendedStandardLibraryCompareStructs): 
    reversed (bool): 

Returns:
    Array[InstancedStruct]: 

    struct_array (Array[InstancedStruct]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_struct_array"></a>

#### sort\_struct\_array

```python
@classmethod
def sort_struct_array(
        cls,
        struct_array: Array[InstancedStruct],
        comparator: DelegateULowEntryExtendedStandardLibraryCompareStructs,
        reversed: bool = False) -> Array[InstancedStruct]
```

X.sort_struct_array(struct_array, comparator, reversed=False) -> Array[InstancedStruct]
Sorts a copy of the given array.

To create the Comparator, do this:
 - create a function that has 2 input parameters (InstancedStruct and InstancedStruct) and 1 output parameter (Boolean)
 - it is important that the parameters have the following names: StructA, StructB and Return
 - in that function, return true if StructA is smaller than StructB, return false otherwise
 - then, when using the Sort Struct Array blueprint, use the Create Event blueprint and set its value as the function created earlier

Args:
    struct_array (Array[InstancedStruct]): 
    comparator (DelegateULowEntryExtendedStandardLibraryCompareStructs): 
    reversed (bool): 

Returns:
    Array[InstancedStruct]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_string_array_directly"></a>

#### sort\_string\_array\_directly

```python
@classmethod
def sort_string_array_directly(cls,
                               string_array: Array[str],
                               reversed: bool = False) -> Array[str]
```

X.sort_string_array_directly(string_array, reversed=False) -> Array[str]
Sorts the given array.

Args:
    string_array (Array[str]): 
    reversed (bool): 

Returns:
    Array[str]: 

    string_array (Array[str]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_string_array"></a>

#### sort\_string\_array

```python
@classmethod
def sort_string_array(cls,
                      string_array: Array[str],
                      reversed: bool = False) -> Array[str]
```

X.sort_string_array(string_array, reversed=False) -> Array[str]
Sorts a copy of the given array.

Args:
    string_array (Array[str]): 
    reversed (bool): 

Returns:
    Array[str]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_object_array_directly"></a>

#### sort\_object\_array\_directly

```python
@classmethod
def sort_object_array_directly(
        cls,
        object_array: Array[Object],
        comparator: DelegateULowEntryExtendedStandardLibraryCompareObjects,
        reversed: bool = False) -> Array[Object]
```

X.sort_object_array_directly(object_array, comparator, reversed=False) -> Array[Object]
Sorts the given array.

To create the Comparator, do this:
 - create a function that has 2 input parameters (Object and Object) and 1 output parameter (Boolean)
 - it is important that the parameters have the following names: ObjectA, ObjectB and Return
 - in that function, return true if ObjectA is smaller than ObjectB, return false otherwise
 - then, when using the Sort Object Array blueprint, use the Create Event blueprint and set its value as the function created earlier

Args:
    object_array (Array[Object]): 
    comparator (DelegateULowEntryExtendedStandardLibraryCompareObjects): 
    reversed (bool): 

Returns:
    Array[Object]: 

    object_array (Array[Object]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_object_array"></a>

#### sort\_object\_array

```python
@classmethod
def sort_object_array(
        cls,
        object_array: Array[Object],
        comparator: DelegateULowEntryExtendedStandardLibraryCompareObjects,
        reversed: bool = False) -> Array[Object]
```

X.sort_object_array(object_array, comparator, reversed=False) -> Array[Object]
Sorts a copy of the given array.

To create the Comparator, do this:
 - create a function that has 2 input parameters (Object and Object) and 1 output parameter (Boolean)
 - it is important that the parameters have the following names: ObjectA, ObjectB and Return
 - in that function, return true if ObjectA is smaller than ObjectB, return false otherwise
 - then, when using the Sort Object Array blueprint, use the Create Event blueprint and set its value as the function created earlier

Args:
    object_array (Array[Object]): 
    comparator (DelegateULowEntryExtendedStandardLibraryCompareObjects): 
    reversed (bool): 

Returns:
    Array[Object]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_integer_array_directly"></a>

#### sort\_integer\_array\_directly

```python
@classmethod
def sort_integer_array_directly(cls,
                                integer_array: Array[int],
                                reversed: bool = False) -> Array[int]
```

X.sort_integer_array_directly(integer_array, reversed=False) -> Array[int32]
Sorts the given array.

Args:
    integer_array (Array[int32]): 
    reversed (bool): 

Returns:
    Array[int32]: 

    integer_array (Array[int32]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_integer_array"></a>

#### sort\_integer\_array

```python
@classmethod
def sort_integer_array(cls,
                       integer_array: Array[int],
                       reversed: bool = False) -> Array[int]
```

X.sort_integer_array(integer_array, reversed=False) -> Array[int32]
Sorts a copy of the given array.

Args:
    integer_array (Array[int32]): 
    reversed (bool): 

Returns:
    Array[int32]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_float_array_directly"></a>

#### sort\_float\_array\_directly

```python
@classmethod
def sort_float_array_directly(cls,
                              float_array: Array[float],
                              reversed: bool = False) -> Array[float]
```

X.sort_float_array_directly(float_array, reversed=False) -> Array[float]
Sorts the given array.

Args:
    float_array (Array[float]): 
    reversed (bool): 

Returns:
    Array[float]: 

    float_array (Array[float]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_float_array"></a>

#### sort\_float\_array

```python
@classmethod
def sort_float_array(cls,
                     float_array: Array[float],
                     reversed: bool = False) -> Array[float]
```

X.sort_float_array(float_array, reversed=False) -> Array[float]
Sorts a copy of the given array.

Args:
    float_array (Array[float]): 
    reversed (bool): 

Returns:
    Array[float]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_double_array_directly"></a>

#### sort\_double\_array\_directly

```python
@classmethod
def sort_double_array_directly(cls,
                               double_array: Array[float],
                               reversed: bool = False) -> Array[float]
```

X.sort_double_array_directly(double_array, reversed=False) -> Array[double]
Sorts the given array.

Args:
    double_array (Array[double]): 
    reversed (bool): 

Returns:
    Array[double]: 

    double_array (Array[double]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_double_array"></a>

#### sort\_double\_array

```python
@classmethod
def sort_double_array(cls,
                      double_array: Array[float],
                      reversed: bool = False) -> Array[float]
```

X.sort_double_array(double_array, reversed=False) -> Array[double]
Sorts a copy of the given array.

Args:
    double_array (Array[double]): 
    reversed (bool): 

Returns:
    Array[double]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_date_time_array_directly"></a>

#### sort\_date\_time\_array\_directly

```python
@classmethod
def sort_date_time_array_directly(cls,
                                  date_time_array: Array[DateTime],
                                  reversed: bool = False) -> Array[DateTime]
```

X.sort_date_time_array_directly(date_time_array, reversed=False) -> Array[DateTime]
Sorts the given array.

Args:
    date_time_array (Array[DateTime]): 
    reversed (bool): 

Returns:
    Array[DateTime]: 

    date_time_array (Array[DateTime]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_date_time_array"></a>

#### sort\_date\_time\_array

```python
@classmethod
def sort_date_time_array(cls,
                         date_time_array: Array[DateTime],
                         reversed: bool = False) -> Array[DateTime]
```

X.sort_date_time_array(date_time_array, reversed=False) -> Array[DateTime]
Sorts a copy of the given array.

Args:
    date_time_array (Array[DateTime]): 
    reversed (bool): 

Returns:
    Array[DateTime]:

<a id="unreal.LowEntryExtendedStandardLibrary.sort_byte_array_directly"></a>

#### sort\_byte\_array\_directly

```python
@classmethod
def sort_byte_array_directly(cls,
                             byte_array: Array[int],
                             reversed: bool = False) -> Array[int]
```

X.sort_byte_array_directly(byte_array, reversed=False) -> Array[uint8]
Sorts the given array.

Args:
    byte_array (Array[uint8]): 
    reversed (bool): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.sort_byte_array"></a>

#### sort\_byte\_array

```python
@classmethod
def sort_byte_array(cls,
                    byte_array: Array[int],
                    reversed: bool = False) -> Array[int]
```

X.sort_byte_array(byte_array, reversed=False) -> Array[uint8]
Sorts a copy of the given array.

Args:
    byte_array (Array[uint8]): 
    reversed (bool): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.shipping_build"></a>

#### shipping\_build

```python
@classmethod
def shipping_build(cls) -> bool
```

X.shipping_build() -> bool
Returns true if this is a debug build (UE_BUILD_SHIPPING), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.sha512"></a>

#### sha512

```python
@classmethod
def sha512(cls,
           byte_array: Array[int],
           index: int = 0,
           length: int = 2147483647) -> Array[int]
```

X.sha512(byte_array, index=0, length=2147483647) -> Array[uint8]
Generates a SHA-512 hash, always returns 64 bytes.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.sha256"></a>

#### sha256

```python
@classmethod
def sha256(cls,
           byte_array: Array[int],
           index: int = 0,
           length: int = 2147483647) -> Array[int]
```

X.sha256(byte_array, index=0, length=2147483647) -> Array[uint8]
Generates a SHA-256 hash, always returns 32 bytes.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.sha1"></a>

#### sha1

```python
@classmethod
def sha1(cls,
         byte_array: Array[int],
         index: int = 0,
         length: int = 2147483647) -> Array[int]
```

X.sha1(byte_array, index=0, length=2147483647) -> Array[uint8]
Generates a SHA1 hash, always returns 20 bytes.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.set_world_rendering_enabled"></a>

#### set\_world\_rendering\_enabled

```python
@classmethod
def set_world_rendering_enabled(cls, enabled: bool) -> None
```

X.set_world_rendering_enabled(enabled) -> None
Causes the world rendering to be enabled or disabled.

Args:
    enabled (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.set_window_size"></a>

#### set\_window\_size

```python
@classmethod
def set_window_size(cls, width: int, height: int) -> None
```

X.set_window_size(width, height) -> None
Sets the window size in screen pixels.

Args:
    width (int32): 
    height (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.set_window_position_in_percentages_centered"></a>

#### set\_window\_position\_in\_percentages\_centered

```python
@classmethod
def set_window_position_in_percentages_centered(cls, x: float,
                                                y: float) -> None
```

X.set_window_position_in_percentages_centered(x, y) -> None
Sets the window position in screen space in percentages, relative to the primary monitor work area, from 0.0 to 1.0.

This will take the window size in account, meaning that X=0.5 and Y=0.5 will cause the window to be centered in the primary screen work area.

Args:
    x (double): 
    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.set_window_position"></a>

#### set\_window\_position

```python
@classmethod
def set_window_position(cls, x: int, y: int) -> None
```

X.set_window_position(x, y) -> None
Sets the window position in screen space.

Args:
    x (int32): 
    y (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.set_window_positiom_in_percentages_centered"></a>

#### set\_window\_positiom\_in\_percentages\_centered

```python
@classmethod
def set_window_positiom_in_percentages_centered(cls, x: float,
                                                y: float) -> None
```

X.set_window_positiom_in_percentages_centered(x, y) -> None
ReSharper disable once IdentifierTypo
deprecated: Use SetWindowPositionInPercentagesCentered instead

Args:
    x (double): 
    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.set_window_mode"></a>

#### set\_window\_mode

```python
@classmethod
def set_window_mode(cls, fullscreen: bool,
                    is_fullscreen_windowed: bool) -> None
```

X.set_window_mode(fullscreen, is_fullscreen_windowed) -> None
Sets the window mode.

If Fullscreen is false, it will be windowed.
If Fullscreen is true and IsFullscreenWindowed is false, it will be fullscreen.
If Fullscreen is true and IsFullscreenWindowed is true, it will be windowed fullscreen.

IsFullscreenWindowed is only used when Fullscreen is true.

Fullscreen and Windowed can both be true.

Args:
    fullscreen (bool): 
    is_fullscreen_windowed (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.set_split_screen_type_two_players"></a>

#### set\_split\_screen\_type\_two\_players

```python
@classmethod
def set_split_screen_type_two_players(
        cls, type: LowEntrySplitScreenTypeTwoPlayers) -> None
```

X.set_split_screen_type_two_players(type) -> None
Set the split screen type (for 2 players).

Args:
    type (LowEntrySplitScreenTypeTwoPlayers):

<a id="unreal.LowEntryExtendedStandardLibrary.set_split_screen_type_three_players"></a>

#### set\_split\_screen\_type\_three\_players

```python
@classmethod
def set_split_screen_type_three_players(
        cls, type: LowEntrySplitScreenTypeThreePlayers) -> None
```

X.set_split_screen_type_three_players(type) -> None
Set the split screen type (for 3 players).

Args:
    type (LowEntrySplitScreenTypeThreePlayers):

<a id="unreal.LowEntryExtendedStandardLibrary.set_split_screen_enabled"></a>

#### set\_split\_screen\_enabled

```python
@classmethod
def set_split_screen_enabled(cls, enabled: bool) -> None
```

X.set_split_screen_enabled(enabled) -> None
Enables or disables split screen.

Args:
    enabled (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.set_mouse_position_in_percentages"></a>

#### set\_mouse\_position\_in\_percentages

```python
@classmethod
def set_mouse_position_in_percentages(cls, x: float, y: float) -> None
```

X.set_mouse_position_in_percentages(x, y) -> None
Sets the mouse position (relative to the viewport) in percentages, from 0.0 to 1.0.

X:  0.0 is left, 1.0 is right
Y:  0.0 is top,  1.0 is bottom

Args:
    x (double): 
    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.set_mouse_position"></a>

#### set\_mouse\_position

```python
@classmethod
def set_mouse_position(cls, x: int, y: int) -> None
```

X.set_mouse_position(x, y) -> None
Sets the mouse position (relative to the viewport).

Args:
    x (int32): 
    y (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.set_mouse_locked_to_viewport"></a>

#### set\_mouse\_locked\_to\_viewport

```python
@classmethod
def set_mouse_locked_to_viewport(cls, locked: bool) -> None
```

X.set_mouse_locked_to_viewport(locked) -> None
Sets the mouse locked to the viewport (meaning the mouse cursor won't be able to get out of the viewport).

Args:
    locked (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.set_generic_team_id"></a>

#### set\_generic\_team\_id

```python
@classmethod
def set_generic_team_id(cls, target: Actor, team_id: int) -> None
```

X.set_generic_team_id(target, team_id) -> None
Sets the Team ID of the given Actor.

Args:
    target (Actor): 
    team_id (uint8):

<a id="unreal.LowEntryExtendedStandardLibrary.server_change_map"></a>

#### server\_change\_map

```python
@classmethod
def server_change_map(cls,
                      world_context_object: Object,
                      map: str,
                      args: str,
                      specific_player: PlayerController = None) -> None
```

X.server_change_map(world_context_object, map, args, specific_player=None) -> None
Changes the map of the server, and with that, everyone that is playing on the server.

Args:
    world_context_object (Object): 
    map (str): 
    args (str): 
    specific_player (PlayerController):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture_component2d_to_pixels"></a>

#### scene\_capture\_component2d\_to\_pixels

```python
@classmethod
def scene_capture_component2d_to_pixels(
    cls, scene_capture_component2d: SceneCaptureComponent2D
) -> Tuple[int, int, Array[Color]]
```

X.scene_capture_component2d_to_pixels(scene_capture_component2d) -> (width=int32, height=int32, pixels=Array[Color])
Converts a SceneCaptureComponent2D into a Pixel Array.

To get the best results:
 1) In the SceneCaptureComponent2D [Texture Target]'s settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)
 2) In the SceneCaptureComponent2D's settings, change the [Capture Source] to [Final Color (LDR) in RGB], if you don't see this option, try converting your SceneCaptureComponent2D's Actor to a blueprint Actor first
 3) To get a brighter image, in the SceneCaptureComponent2D settings (not in the CameraActor settings, but in the SceneCaptureComponent2D settings), play around with the Color Grading Contrast and Gamma (a Contrast and Gamma of X=1.0 Y=1.0 Z=1.0 W=2.0 looked quite good on my end)

Returns an empty Pixel Array if it fails, the Width and the Height will also be 0 then.

Args:
    scene_capture_component2d (SceneCaptureComponent2D): 

Returns:
    tuple: 

    width (int32): 

    height (int32): 

    pixels (Array[Color]):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture_component2d_to_bytes"></a>

#### scene\_capture\_component2d\_to\_bytes

```python
@classmethod
def scene_capture_component2d_to_bytes(
        cls,
        scene_capture_component2d: SceneCaptureComponent2D,
        image_format: LowEntryImageFormat,
        compression_quality: int = 0) -> Array[int]
```

X.scene_capture_component2d_to_bytes(scene_capture_component2d, image_format, compression_quality=0) -> Array[uint8]
Converts a SceneCaptureComponent2D into a Byte Array.

Some formats will not work (like BMP, ICO and ICNS).

The Compression Quality has to be 1-100, a value of 0 will use the default value for the given ImageFormat.

To get the best results:
 1) In the SceneCaptureComponent2D [Texture Target]'s settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)
 2) In the SceneCaptureComponent2D's settings, change the [Capture Source] to [Final Color (LDR) in RGB], if you don't see this option, try converting your SceneCaptureComponent2D's Actor to a blueprint Actor first
 3) To get a brighter image, in the SceneCaptureComponent2D settings (not in the CameraActor settings, but in the SceneCaptureComponent2D settings), play around with the Color Grading Contrast and Gamma (a Contrast and Gamma of X=1.0 Y=1.0 Z=1.0 W=2.0 looked quite good on my end)

Returns an empty Byte Array if it fails.

Args:
    scene_capture_component2d (SceneCaptureComponent2D): 
    image_format (LowEntryImageFormat): 
    compression_quality (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture_component2d_set_fov"></a>

#### scene\_capture\_component2d\_set\_fov

```python
@classmethod
def scene_capture_component2d_set_fov(
        cls, scene_capture_component2d: SceneCaptureComponent2D,
        fov: float) -> None
```

X.scene_capture_component2d_set_fov(scene_capture_component2d, fov) -> None
Sets the FOV of the given SceneCaptureComponent2D.

Args:
    scene_capture_component2d (SceneCaptureComponent2D): 
    fov (double):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture_component2d_get_fov"></a>

#### scene\_capture\_component2d\_get\_fov

```python
@classmethod
def scene_capture_component2d_get_fov(
        cls, scene_capture_component2d: SceneCaptureComponent2D) -> float
```

X.scene_capture_component2d_get_fov(scene_capture_component2d) -> double
Returns the FOV of the given SceneCaptureComponent2D.

Args:
    scene_capture_component2d (SceneCaptureComponent2D): 

Returns:
    double: 

    fov (double):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture2d_to_pixels"></a>

#### scene\_capture2d\_to\_pixels

```python
@classmethod
def scene_capture2d_to_pixels(
        cls, scene_capture2d: SceneCapture2D) -> Tuple[int, int, Array[Color]]
```

X.scene_capture2d_to_pixels(scene_capture2d) -> (width=int32, height=int32, pixels=Array[Color])
Converts a SceneCapture2D into a Pixel Array.

To get the best results:
 1) In the SceneCapture2D [Texture Target]'s settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)
 2) In the SceneCapture2D's settings, change the [Capture Source] to [Final Color (LDR) in RGB], if you don't see this option, try converting your SceneCapture2D Actor to a blueprint Actor first
 3) To get a brighter image, in the SceneCapture2D settings, play around with the Color Grading Contrast and Gamma (a Contrast and Gamma of X=1.0 Y=1.0 Z=1.0 W=2.0 looked quite good on my end)

Returns an empty Pixel Array if it fails, the Width and the Height will also be 0 then.

Args:
    scene_capture2d (SceneCapture2D): 

Returns:
    tuple: 

    width (int32): 

    height (int32): 

    pixels (Array[Color]):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture2d_to_bytes"></a>

#### scene\_capture2d\_to\_bytes

```python
@classmethod
def scene_capture2d_to_bytes(cls,
                             scene_capture2d: SceneCapture2D,
                             image_format: LowEntryImageFormat,
                             compression_quality: int = 0) -> Array[int]
```

X.scene_capture2d_to_bytes(scene_capture2d, image_format, compression_quality=0) -> Array[uint8]
Converts a SceneCapture2D into a Byte Array.

Some formats will not work (like BMP, ICO and ICNS).

The Compression Quality has to be 1-100, a value of 0 will use the default value for the given ImageFormat.

To get the best results:
 1) In the SceneCapture2D [Texture Target]'s settings, set [Render Target Format] to [RTF RGBA8] and choose a properly high Size X and Y (1000+ seems to be fine)
 2) In the SceneCapture2D's settings, change the [Capture Source] to [Final Color (LDR) in RGB], if you don't see this option, try converting your SceneCapture2D Actor to a blueprint Actor first
 3) To get a brighter image, in the SceneCapture2D settings, play around with the Color Grading Contrast and Gamma (a Contrast and Gamma of X=1.0 Y=1.0 Z=1.0 W=2.0 looked quite good on my end)

Returns an empty Byte Array if it fails.

Args:
    scene_capture2d (SceneCapture2D): 
    image_format (LowEntryImageFormat): 
    compression_quality (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture2d_set_fov"></a>

#### scene\_capture2d\_set\_fov

```python
@classmethod
def scene_capture2d_set_fov(cls, scene_capture2d: SceneCapture2D,
                            fov: float) -> None
```

X.scene_capture2d_set_fov(scene_capture2d, fov) -> None
Sets the FOV of the given SceneCapture2D's SceneCaptureComponent2D.

Args:
    scene_capture2d (SceneCapture2D): 
    fov (double):

<a id="unreal.LowEntryExtendedStandardLibrary.scene_capture2d_get_fov"></a>

#### scene\_capture2d\_get\_fov

```python
@classmethod
def scene_capture2d_get_fov(cls, scene_capture2d: SceneCapture2D) -> float
```

X.scene_capture2d_get_fov(scene_capture2d) -> double
Returns the FOV of the given SceneCapture2D's SceneCaptureComponent2D.

Args:
    scene_capture2d (SceneCapture2D): 

Returns:
    double: 

    fov (double):

<a id="unreal.LowEntryExtendedStandardLibrary.round_decimals"></a>

#### round\_decimals

```python
@classmethod
def round_decimals(cls, number: float, decimals: int) -> float
```

X.round_decimals(number, decimals) -> double
Rounds to the given Decimals.

Args:
    number (double): 
    decimals (int32): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.retriggerable_random_delay_frames"></a>

#### retriggerable\_random\_delay\_frames

```python
@classmethod
def retriggerable_random_delay_frames(
        cls,
        world_context_object: Object,
        min_frames: int = 10,
        max_frames: int = 30,
        latent_info: LatentActionInfo = ...) -> None
```

X.retriggerable_random_delay_frames(world_context_object, min_frames=10, max_frames=30, latent_info) -> None
Perform a latent action with a retriggerable random delay (specified in frames).  Calling again while it is counting down will reset the countdown to a new random Frames.
deprecated: Use a [Retriggerable Delay (Frames)] with a [Random Integer In Range] instead.

Args:
    world_context_object (Object): World context.
    min_frames (int32): minimum frames of delay.
    max_frames (int32): maximum frames of delay.
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.retriggerable_random_delay"></a>

#### retriggerable\_random\_delay

```python
@classmethod
def retriggerable_random_delay(cls,
                               world_context_object: Object,
                               min_duration: float = 0.200000,
                               max_duration: float = 0.500000,
                               latent_info: LatentActionInfo = ...) -> None
```

X.retriggerable_random_delay(world_context_object, min_duration=0.200000, max_duration=0.500000, latent_info) -> None
Perform a latent action with a retriggerable random delay (specified in seconds).  Calling again while it is counting down will reset the countdown to a new random Duration.
deprecated: Use a [Retriggerable Delay] with a [Random Float In Range] instead.

Args:
    world_context_object (Object): World context.
    min_duration (double): minimum length of delay (in seconds).
    max_duration (double): maximum length of delay (in seconds).
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.retriggerable_delay_frames"></a>

#### retriggerable\_delay\_frames

```python
@classmethod
def retriggerable_delay_frames(cls, world_context_object: Object, frames: int,
                               latent_info: LatentActionInfo) -> None
```

X.retriggerable_delay_frames(world_context_object, frames, latent_info) -> None
Perform a latent action with a retriggerable delay (specified in frames).  Calling again while it is counting down will reset the countdown to the given Frames.

Args:
    world_context_object (Object): World context.
    frames (int32): frames of delay.
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.replace_characters_except"></a>

#### replace\_characters\_except

```python
@classmethod
def replace_characters_except(cls, string: str, replacement_character: str,
                              keep_lowercase_az: bool, keep_uppercase_az: bool,
                              keep_numbers: bool,
                              other_characters_to_keep: str) -> str
```

X.replace_characters_except(string, replacement_character, keep_lowercase_az, keep_uppercase_az, keep_numbers, other_characters_to_keep) -> str
Replaces all characters with the given replacement character except the characters chosen to keep.

Args:
    string (str): 
    replacement_character (str): 
    keep_lowercase_az (bool): 
    keep_uppercase_az (bool): 
    keep_numbers (bool): 
    other_characters_to_keep (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.remove_characters_except"></a>

#### remove\_characters\_except

```python
@classmethod
def remove_characters_except(cls, string: str, keep_lowercase_az: bool,
                             keep_uppercase_az: bool, keep_numbers: bool,
                             other_characters_to_keep: str) -> str
```

X.remove_characters_except(string, keep_lowercase_az, keep_uppercase_az, keep_numbers, other_characters_to_keep) -> str
Removes all characters except the characters chosen to keep.

Args:
    string (str): 
    keep_lowercase_az (bool): 
    keep_uppercase_az (bool): 
    keep_numbers (bool): 
    other_characters_to_keep (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.regex_replace"></a>

#### regex\_replace

```python
@classmethod
def regex_replace(cls, string: str, pattern: str, replacement: str) -> str
```

X.regex_replace(string, pattern, replacement) -> str
Replaces every regex match with the given replacement String.

Args:
    string (str): 
    pattern (str): 
    replacement (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.regex_match"></a>

#### regex\_match

```python
@classmethod
def regex_match(cls, string: str, pattern: str) -> bool
```

X.regex_match(string, pattern) -> bool
Returns true if a regex match was found in the given String.

Args:
    string (str): 
    pattern (str): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.regex_get_matches"></a>

#### regex\_get\_matches

```python
@classmethod
def regex_get_matches(cls, string: str,
                      pattern: str) -> Array[LowEntryRegexMatch]
```

X.regex_get_matches(string, pattern) -> Array[LowEntryRegexMatch]
Returns the begin index, end index and matched string of each regex match (including each capture group of the regex) found in the given String.

Args:
    string (str): 
    pattern (str): 

Returns:
    Array[LowEntryRegexMatch]:

<a id="unreal.LowEntryExtendedStandardLibrary.regex_count"></a>

#### regex\_count

```python
@classmethod
def regex_count(cls, string: str, pattern: str) -> int
```

X.regex_count(string, pattern) -> int32
Returns the number of times the regex matched in the given String.

Args:
    string (str): 
    pattern (str): 

Returns:
    int32:

<a id="unreal.LowEntryExtendedStandardLibrary.random_delay_frames"></a>

#### random\_delay\_frames

```python
@classmethod
def random_delay_frames(cls,
                        world_context_object: Object,
                        min_frames: int = 10,
                        max_frames: int = 30,
                        latent_info: LatentActionInfo = ...) -> None
```

X.random_delay_frames(world_context_object, min_frames=10, max_frames=30, latent_info) -> None
Perform a latent action with a random delay (specified in frames).  Calling again while it is counting down will be ignored.
deprecated: Use a [Delay (Frames)] with a [Random Integer In Range] instead.

Args:
    world_context_object (Object): World context.
    min_frames (int32): minimum frames of delay.
    max_frames (int32): maximum frames of delay.
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.random_delay"></a>

#### random\_delay

```python
@classmethod
def random_delay(cls,
                 world_context_object: Object,
                 min_duration: float = 0.200000,
                 max_duration: float = 0.500000,
                 latent_info: LatentActionInfo = ...) -> None
```

X.random_delay(world_context_object, min_duration=0.200000, max_duration=0.500000, latent_info) -> None
Perform a latent action with a random delay (specified in seconds).  Calling again while it is counting down will be ignored.
deprecated: Use a [Delay] with a [Random Float In Range] instead.

Args:
    world_context_object (Object): World context.
    min_duration (double): minimum length of delay (in seconds).
    max_duration (double): maximum length of delay (in seconds).
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.queue_executions"></a>

#### queue\_executions

```python
@classmethod
def queue_executions(cls, world_context_object: Object,
                     latent_info: LatentActionInfo) -> LowEntryExecutionQueue
```

X.queue_executions(world_context_object, latent_info) -> LowEntryExecutionQueue
Queues up executions, will run a pending execution when Next() is called.

Args:
    world_context_object (Object): World context.
    latent_info (LatentActionInfo): The latent action.

Returns:
    LowEntryExecutionQueue: 

    queue (LowEntryExecutionQueue): the queue in which the executions are stored.

<a id="unreal.LowEntryExtendedStandardLibrary.ps4_platform"></a>

#### ps4\_platform

```python
@classmethod
def ps4_platform(cls) -> bool
```

X.ps4_platform() -> bool
Returns true if this is the PS4 platform (PLATFORM_PS4), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.player_controller_get_local_player"></a>

#### player\_controller\_get\_local\_player

```python
@classmethod
def player_controller_get_local_player(
        cls, player_controller: PlayerController) -> Tuple[bool, LocalPlayer]
```

X.player_controller_get_local_player(player_controller) -> (success=bool, local_player=LocalPlayer)
Returns the LocalPlayer from the given PlayerController.

Fails if the PlayerController isn't owned by a LocalPlayer (but by a networked player instead).

Description of a LocalPlayer: Each player that is active on the current client has a LocalPlayer. It stays active across maps There may be several spawned in the case of splitscreen/coop. There may be 0 spawned on servers. See http://api.unrealengine.com/INT/API/Runtime/Engine/Engine/ULocalPlayer/index.html

Args:
    player_controller (PlayerController): 

Returns:
    tuple: 

    success (bool): 

    local_player (LocalPlayer):

<a id="unreal.LowEntryExtendedStandardLibrary.pixels_to_texture2d"></a>

#### pixels\_to\_texture2d

```python
@classmethod
def pixels_to_texture2d(cls, width: int, height: int,
                        pixels: Array[Color]) -> Texture2D
```

X.pixels_to_texture2d(width, height, pixels) -> Texture2D
Converts a Pixel Array into an image (Texture2D).

Returns nullptr if it fails.

Args:
    width (int32): 
    height (int32): 
    pixels (Array[Color]): 

Returns:
    Texture2D:

<a id="unreal.LowEntryExtendedStandardLibrary.pixels_to_existing_texture2d"></a>

#### pixels\_to\_existing\_texture2d

```python
@classmethod
def pixels_to_existing_texture2d(
        cls, texture2d: Texture2D, width: int, height: int,
        pixels: Array[Color]) -> Tuple[Texture2D, bool]
```

X.pixels_to_existing_texture2d(texture2d, width, height, pixels) -> (Texture2D, reused_given_texture2d=bool)
Converts a Pixel Array into an image (Texture2D).

Returns nullptr if it fails.

Will re-use the given Texture2D if possible, ReusedGivenTexture2D will be true if it was possible.

Args:
    texture2d (Texture2D): 
    width (int32): 
    height (int32): 
    pixels (Array[Color]): 

Returns:
    bool: 

    reused_given_texture2d (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.pixels_to_bytes"></a>

#### pixels\_to\_bytes

```python
@classmethod
def pixels_to_bytes(cls,
                    width: int,
                    height: int,
                    pixels: Array[Color],
                    image_format: LowEntryImageFormat,
                    compression_quality: int = 0) -> Array[int]
```

X.pixels_to_bytes(width, height, pixels, image_format, compression_quality=0) -> Array[uint8]
Converts a Pixel Array into a Byte Array.

Some formats will not work (like BMP, ICO and ICNS).

The Compression Quality has to be 1-100, a value of 0 will use the default value for the given ImageFormat.

Returns an empty Byte Array if it fails.

Args:
    width (int32): 
    height (int32): 
    pixels (Array[Color]): 
    image_format (LowEntryImageFormat): 
    compression_quality (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.pearson"></a>

#### pearson

```python
@classmethod
def pearson(cls,
            byte_array: Array[int],
            hash_length: int,
            index: int = 0,
            length: int = 2147483647) -> Array[int]
```

X.pearson(byte_array, hash_length, index=0, length=2147483647) -> Array[uint8]
Generates a Pearson hash, returns the given HashLength number of bytes.

Args:
    byte_array (Array[uint8]): 
    hash_length (int32): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.parse_string_into_long_bytes"></a>

#### parse\_string\_into\_long\_bytes

```python
@classmethod
def parse_string_into_long_bytes(cls, string: str) -> LowEntryLong
```

X.parse_string_into_long_bytes(string) -> LowEntryLong
Parses a string into a long.

Args:
    string (str): 

Returns:
    LowEntryLong:

<a id="unreal.LowEntryExtendedStandardLibrary.parse_string_into_long"></a>

#### parse\_string\_into\_long

```python
@classmethod
def parse_string_into_long(cls, string: str) -> int
```

X.parse_string_into_long(string) -> int64
Parses a string into an int64.

Args:
    string (str): 

Returns:
    int64:

<a id="unreal.LowEntryExtendedStandardLibrary.parse_string_into_double_bytes"></a>

#### parse\_string\_into\_double\_bytes

```python
@classmethod
def parse_string_into_double_bytes(cls, string: str) -> LowEntryDouble
```

X.parse_string_into_double_bytes(string) -> LowEntryDouble
Parses a string into a double.

Args:
    string (str): 

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryExtendedStandardLibrary.parsed_hashcash_is_valid"></a>

#### parsed\_hashcash\_is\_valid

```python
@classmethod
def parsed_hashcash_is_valid(cls, target: LowEntryParsedHashcash) -> bool
```

X.parsed_hashcash_is_valid(target) -> bool
Returns true if this Parsed Hashcash is valid, returns false if it is not valid.

Args:
    target (LowEntryParsedHashcash): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.next_queue_execution"></a>

#### next\_queue\_execution

```python
@classmethod
def next_queue_execution(cls, queue: LowEntryExecutionQueue) -> None
```

X.next_queue_execution(queue) -> None
Runs a pending execution (if any).

Args:
    queue (LowEntryExecutionQueue):

<a id="unreal.LowEntryExtendedStandardLibrary.newline_character"></a>

#### newline\_character

```python
@classmethod
def newline_character(cls) -> str
```

X.newline_character() -> str
Returns a newline character (\n).

This blueprint will always return a \n character, no matter what Operating System it is running on.

Note: It is actually called a line feed, the blueprint is called Newline Character for recognition purposes.
On *nix systems \n is used as a newline character, on Windows \r\n is used as a newline character.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.min_string"></a>

#### min\_string

```python
@classmethod
def min_string(cls, a: str, b: str) -> str
```

X.min_string(a, b) -> str
Returns the minimum value of the given values.

Args:
    a (str): 
    b (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.min_of_timespan_array"></a>

#### min\_of\_timespan\_array

```python
@classmethod
def min_of_timespan_array(
        cls, timespan_array: Array[Timespan]) -> Tuple[int, Timespan]
```

X.min_of_timespan_array(timespan_array) -> (index_of_min_value=int32, min_value=Timespan)
Returns the minimum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    timespan_array (Array[Timespan]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (Timespan):

<a id="unreal.LowEntryExtendedStandardLibrary.min_of_string_array"></a>

#### min\_of\_string\_array

```python
@classmethod
def min_of_string_array(cls, string_array: Array[str]) -> Tuple[int, str]
```

X.min_of_string_array(string_array) -> (index_of_min_value=int32, min_value=str)
Returns the minimum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    string_array (Array[str]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (str):

<a id="unreal.LowEntryExtendedStandardLibrary.min_of_date_time_array"></a>

#### min\_of\_date\_time\_array

```python
@classmethod
def min_of_date_time_array(
        cls, date_time_array: Array[DateTime]) -> Tuple[int, DateTime]
```

X.min_of_date_time_array(date_time_array) -> (index_of_min_value=int32, min_value=DateTime)
Returns the minimum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    date_time_array (Array[DateTime]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (DateTime):

<a id="unreal.LowEntryExtendedStandardLibrary.merge_bytes"></a>

#### merge\_bytes

```python
@classmethod
def merge_bytes(cls, a: Array[int], b: Array[int]) -> Array[int]
```

X.merge_bytes(a, b) -> Array[uint8]
Merges multiple Byte Arrays into one.
deprecated: This function is commutative, meaning it sometimes causes bytes to be merged in an incorrect order. Use the new Merge Bytes node instead.

Args:
    a (Array[uint8]): 
    b (Array[uint8]): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.md5"></a>

#### md5

```python
@classmethod
def md5(cls,
        byte_array: Array[int],
        index: int = 0,
        length: int = 2147483647) -> Array[int]
```

X.md5(byte_array, index=0, length=2147483647) -> Array[uint8]
Generates a MD5 hash, always returns 16 bytes.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.max_string"></a>

#### max\_string

```python
@classmethod
def max_string(cls, a: str, b: str) -> str
```

X.max_string(a, b) -> str
Returns the maximum value of the given values.

Args:
    a (str): 
    b (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.max_of_timespan_array"></a>

#### max\_of\_timespan\_array

```python
@classmethod
def max_of_timespan_array(
        cls, timespan_array: Array[Timespan]) -> Tuple[int, Timespan]
```

X.max_of_timespan_array(timespan_array) -> (index_of_max_value=int32, max_value=Timespan)
Returns the maximum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    timespan_array (Array[Timespan]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (Timespan):

<a id="unreal.LowEntryExtendedStandardLibrary.max_of_string_array"></a>

#### max\_of\_string\_array

```python
@classmethod
def max_of_string_array(cls, string_array: Array[str]) -> Tuple[int, str]
```

X.max_of_string_array(string_array) -> (index_of_max_value=int32, max_value=str)
Returns the maximum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    string_array (Array[str]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (str):

<a id="unreal.LowEntryExtendedStandardLibrary.max_of_date_time_array"></a>

#### max\_of\_date\_time\_array

```python
@classmethod
def max_of_date_time_array(
        cls, date_time_array: Array[DateTime]) -> Tuple[int, DateTime]
```

X.max_of_date_time_array(date_time_array) -> (index_of_max_value=int32, max_value=DateTime)
Returns the maximum value of all array entries and the index at which it was found. Returns an index of -1 if the given array is empty.

Args:
    date_time_array (Array[DateTime]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (DateTime):

<a id="unreal.LowEntryExtendedStandardLibrary.mac_platform"></a>

#### mac\_platform

```python
@classmethod
def mac_platform(cls) -> bool
```

X.mac_platform() -> bool
Returns true if this is the Mac platform (PLATFORM_MAC), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.long_to_bytes"></a>

#### long\_to\_bytes

```python
@classmethod
def long_to_bytes(cls, value: int) -> Array[int]
```

X.long_to_bytes(value) -> Array[uint8]
Converts a signed long (int64) into a Byte Array (4 bytes).

Args:
    value (int64): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.long_create_zero"></a>

#### long\_create\_zero

```python
@classmethod
def long_create_zero(cls) -> LowEntryLong
```

X.long_create_zero() -> LowEntryLong
Creates a new long (bytes), a long is always 8 bytes.

Returns:
    LowEntryLong:

<a id="unreal.LowEntryExtendedStandardLibrary.long_create"></a>

#### long\_create

```python
@classmethod
def long_create(cls,
                byte_array: Array[int],
                index: int = 0,
                length: int = 2147483647) -> LowEntryLong
```

X.long_create(byte_array, index=0, length=2147483647) -> LowEntryLong
Creates a new long (bytes), a long is always 8 bytes (give less bytes and it will pad with 0, give more bytes and it will only take the first 8).

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryLong:

<a id="unreal.LowEntryExtendedStandardLibrary.load_video"></a>

#### load\_video

```python
@classmethod
def load_video(cls,
               media_sound_component: MediaSoundComponent,
               url: str,
               play_on_open: bool = True,
               loop: bool = True) -> Tuple[bool, MediaPlayer, MediaTexture]
```

X.load_video(media_sound_component, url, play_on_open=True, loop=True) -> (success=bool, media_player=MediaPlayer, media_texture=MediaTexture)
Loads a video.

Requires a:
 - MediaSoundComponent (to hear the video), this is created by using the "Add Media Sound Component" blueprint on an object on which you want to hear the sound on, also, don't forget to run the "Start" blueprint on the Media Sound Component, otherwise you won't hear anything
 - URL (could be a HTTP/HTTPS URL, or a relative or absolute filepath, more on that below)
 - PlayOnOpen (determines whether "Play" should be automatically called on the returned MediaPlayer, if this is false, the video/sound won't start until you call "Play" on the returned MediaPlayer yourself)
 - Loop (determines whether the video/sound should keep playing, or whether it should just play one time and then stop)

Returns a:
 - MediaPlayer (to play/pause/etc the video)
 - MediaTexture (to see the video)

This blueprint also returns a boolean called Success.
 - true, everything went well, every returned Object is valid
 - false, something went wrong, every returned Object is NULL

The URL is either:
 - a HTTP/HTTPS URL, for example "http://public.lowentry.com/files/test_data/TestVideoMp4.mp4"
 - a relative filepath URL of a video located in "YourProject/Content/Movies/" formatted like "./Movies/YourVideo.mp4"
 - an absolute filepath URL of a video prefixed by "file://", for example "file://C:/Program Files/Epic Games/4.13/Engine/Binaries/Win64/YourVideo.mp4"

Some tips:
 - only MP4 (MPEG-4) can be played on every platform, so it's best to only use MP4 (MPEG-4) videos for now

Additional tips:
 - this blueprint can also be used to load sound assets, just ignore the returned Texture in that case
 - if no MediaSoundComponent is given, or if Start wasn't called on the MediaSoundComponent, you won't hear any sound

Screenshots:
 - screenshots on how to use this blueprint correctly can be found at: https://public.lowentry.com/#files/LowEntryUE4/ue4/images/tutorials/load_video/

Args:
    media_sound_component (MediaSoundComponent): 
    url (str): 
    play_on_open (bool): 
    loop (bool): 

Returns:
    tuple: 

    success (bool): 

    media_player (MediaPlayer): 

    media_texture (MediaTexture):

<a id="unreal.LowEntryExtendedStandardLibrary.linux_platform"></a>

#### linux\_platform

```python
@classmethod
def linux_platform(cls) -> bool
```

X.linux_platform() -> bool
Returns true if this is the Linux platform (PLATFORM_LINUX), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_string_string"></a>

#### less\_string\_string

```python
@classmethod
def less_string_string(cls, a: str, b: str) -> bool
```

X.less_string_string(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (str): 
    b (str): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_integer_float"></a>

#### less\_integer\_float

```python
@classmethod
def less_integer_float(cls, a: int, b: float) -> bool
```

X.less_integer_float(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_integer_byte"></a>

#### less\_integer\_byte

```python
@classmethod
def less_integer_byte(cls, a: int, b: int) -> bool
```

X.less_integer_byte(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_float_integer"></a>

#### less\_float\_integer

```python
@classmethod
def less_float_integer(cls, a: float, b: int) -> bool
```

X.less_float_integer(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_float_byte"></a>

#### less\_float\_byte

```python
@classmethod
def less_float_byte(cls, a: float, b: int) -> bool
```

X.less_float_byte(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_string_string"></a>

#### less\_equal\_string\_string

```python
@classmethod
def less_equal_string_string(cls, a: str, b: str) -> bool
```

X.less_equal_string_string(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (str): 
    b (str): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_integer_float"></a>

#### less\_equal\_integer\_float

```python
@classmethod
def less_equal_integer_float(cls, a: int, b: float) -> bool
```

X.less_equal_integer_float(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_integer_byte"></a>

#### less\_equal\_integer\_byte

```python
@classmethod
def less_equal_integer_byte(cls, a: int, b: int) -> bool
```

X.less_equal_integer_byte(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_float_integer"></a>

#### less\_equal\_float\_integer

```python
@classmethod
def less_equal_float_integer(cls, a: float, b: int) -> bool
```

X.less_equal_float_integer(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_float_byte"></a>

#### less\_equal\_float\_byte

```python
@classmethod
def less_equal_float_byte(cls, a: float, b: int) -> bool
```

X.less_equal_float_byte(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_byte_integer"></a>

#### less\_equal\_byte\_integer

```python
@classmethod
def less_equal_byte_integer(cls, a: int, b: int) -> bool
```

X.less_equal_byte_integer(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_equal_byte_float"></a>

#### less\_equal\_byte\_float

```python
@classmethod
def less_equal_byte_float(cls, a: int, b: float) -> bool
```

X.less_equal_byte_float(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_byte_integer"></a>

#### less\_byte\_integer

```python
@classmethod
def less_byte_integer(cls, a: int, b: int) -> bool
```

X.less_byte_integer(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.less_byte_float"></a>

#### less\_byte\_float

```python
@classmethod
def less_byte_float(cls, a: int, b: float) -> bool
```

X.less_byte_float(a, b) -> bool
Returns true if A is less than B (A < B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_struct"></a>

#### latent\_action\_create\_struct

```python
@classmethod
def latent_action_create_struct(cls) -> LowEntryLatentActionStruct
```

X.latent_action_create_struct() -> LowEntryLatentActionStruct
Creates a new latent action.

Returns:
    LowEntryLatentActionStruct: 

    latent_action (LowEntryLatentActionStruct):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_string"></a>

#### latent\_action\_create\_string

```python
@classmethod
def latent_action_create_string(cls) -> LowEntryLatentActionString
```

X.latent_action_create_string() -> LowEntryLatentActionString
Creates a new latent action.

Returns:
    LowEntryLatentActionString: 

    latent_action (LowEntryLatentActionString):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_object"></a>

#### latent\_action\_create\_object

```python
@classmethod
def latent_action_create_object(cls) -> LowEntryLatentActionObject
```

X.latent_action_create_object() -> LowEntryLatentActionObject
Creates a new latent action.

Returns:
    LowEntryLatentActionObject: 

    latent_action (LowEntryLatentActionObject):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_none"></a>

#### latent\_action\_create\_none

```python
@classmethod
def latent_action_create_none(cls) -> LowEntryLatentActionNone
```

X.latent_action_create_none() -> LowEntryLatentActionNone
Creates a new latent action.

Returns:
    LowEntryLatentActionNone: 

    latent_action (LowEntryLatentActionNone):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_integer"></a>

#### latent\_action\_create\_integer

```python
@classmethod
def latent_action_create_integer(cls) -> LowEntryLatentActionInteger
```

X.latent_action_create_integer() -> LowEntryLatentActionInteger
Creates a new latent action.

Returns:
    LowEntryLatentActionInteger: 

    latent_action (LowEntryLatentActionInteger):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_float"></a>

#### latent\_action\_create\_float

```python
@classmethod
def latent_action_create_float(cls) -> LowEntryLatentActionFloat
```

X.latent_action_create_float() -> LowEntryLatentActionFloat
Creates a new latent action.

Returns:
    LowEntryLatentActionFloat: 

    latent_action (LowEntryLatentActionFloat):

<a id="unreal.LowEntryExtendedStandardLibrary.latent_action_create_boolean"></a>

#### latent\_action\_create\_boolean

```python
@classmethod
def latent_action_create_boolean(cls) -> LowEntryLatentActionBoolean
```

X.latent_action_create_boolean() -> LowEntryLatentActionBoolean
Creates a new latent action.

Returns:
    LowEntryLatentActionBoolean: 

    latent_action (LowEntryLatentActionBoolean):

<a id="unreal.LowEntryExtendedStandardLibrary.join_game"></a>

#### join\_game

```python
@classmethod
def join_game(cls,
              world_context_object: Object,
              server_address: str,
              args: str,
              specific_player: PlayerController = None) -> None
```

X.join_game(world_context_object, server_address, args, specific_player=None) -> None
Joins a game.

Args:
    world_context_object (Object): 
    server_address (str): 
    args (str): 
    specific_player (PlayerController):

<a id="unreal.LowEntryExtendedStandardLibrary.is_world_rendering_enabled"></a>

#### is\_world\_rendering\_enabled

```python
@classmethod
def is_world_rendering_enabled(cls) -> Tuple[bool, bool]
```

X.is_world_rendering_enabled() -> (success=bool, enabled=bool)
Retrieves whether world rendering is enabled.

Returns Success=false and Enabled=false if the world rendering enabled value could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null

Returns:
    tuple: 

    success (bool): 

    enabled (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.is_bit_set"></a>

#### is\_bit\_set

```python
@classmethod
def is_bit_set(cls, b: int, bit: int) -> bool
```

X.is_bit_set(b, bit) -> bool
Returns true if the bit is 1, returns false if the bit is 0.

Bytes start with bit 8, ending with bit 1, as such: 87654321

Args:
    b (uint8): 
    bit (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.ios_platform"></a>

#### ios\_platform

```python
@classmethod
def ios_platform(cls) -> bool
```

X.ios_platform() -> bool
Returns true if this is the IOS platform (PLATFORM_IOS), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.invert_pixel_channel_r"></a>

#### invert\_pixel\_channel\_r

```python
@classmethod
def invert_pixel_channel_r(cls, pixels: Array[Color]) -> Array[Color]
```

X.invert_pixel_channel_r(pixels) -> Array[Color]
Inverts the red channel of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.invert_pixel_channel_g"></a>

#### invert\_pixel\_channel\_g

```python
@classmethod
def invert_pixel_channel_g(cls, pixels: Array[Color]) -> Array[Color]
```

X.invert_pixel_channel_g(pixels) -> Array[Color]
Inverts the green channel of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.invert_pixel_channel_b"></a>

#### invert\_pixel\_channel\_b

```python
@classmethod
def invert_pixel_channel_b(cls, pixels: Array[Color]) -> Array[Color]
```

X.invert_pixel_channel_b(pixels) -> Array[Color]
Inverts the blue channel of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.invert_pixel_channel_a"></a>

#### invert\_pixel\_channel\_a

```python
@classmethod
def invert_pixel_channel_a(cls, pixels: Array[Color]) -> Array[Color]
```

X.invert_pixel_channel_a(pixels) -> Array[Color]
Inverts the alpha channel of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.integer_to_bytes"></a>

#### integer\_to\_bytes

```python
@classmethod
def integer_to_bytes(cls, value: int) -> Array[int]
```

X.integer_to_bytes(value) -> Array[uint8]
Converts a signed integer (int32) into a Byte Array (4 bytes).

Args:
    value (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.html5_platform"></a>

#### html5\_platform

```python
@classmethod
def html5_platform(cls) -> bool
```

X.html5_platform() -> bool
Returns true if this is the Html5 platform (PLATFORM_HTML5), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.host_game"></a>

#### host\_game

```python
@classmethod
def host_game(cls,
              world_context_object: Object,
              map: str,
              args: str,
              specific_player: PlayerController = None) -> None
```

X.host_game(world_context_object, map, args, specific_player=None) -> None
Hosts a game.

Args:
    world_context_object (Object): 
    map (str): 
    args (str): 
    specific_player (PlayerController):

<a id="unreal.LowEntryExtendedStandardLibrary.hmac"></a>

#### hmac

```python
@classmethod
def hmac(cls,
         byte_array: Array[int],
         key: Array[int],
         algorithm: LowEntryHmacAlgorithm = LowEntryHmacAlgorithm.SHA256,
         index: int = 0,
         length: int = 2147483647) -> Array[int]
```

X.hmac(byte_array, key, algorithm=LowEntryHmacAlgorithm.SHA256, index=0, length=2147483647) -> Array[uint8]
Generates a HMAC hash.

PS: the Index and Length parameters refer to the Byte Array (see the "Get Bytes Sub Array" blueprint for more information).

Args:
    byte_array (Array[uint8]): 
    key (Array[uint8]): 
    algorithm (LowEntryHmacAlgorithm): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.hex_to_bytes"></a>

#### hex\_to\_bytes

```python
@classmethod
def hex_to_bytes(cls, hex: str) -> Array[int]
```

X.hex_to_bytes(hex) -> Array[uint8]
Tries to convert a Hexadecimal (Base16) String into a Byte Array. Will return an empty Array on failure.

Args:
    hex (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash_parse_array"></a>

#### hashcash\_parse\_array

```python
@classmethod
def hashcash_parse_array(cls,
                         hashes: Array[str]) -> Array[LowEntryParsedHashcash]
```

X.hashcash_parse_array(hashes) -> Array[LowEntryParsedHashcash]
Parses and validates a Hashcash hash.

To successfully validate a Hashcash hash, do the following:
1) call this method to parse the hashes
2) check if the returned ParsedHashcashes return true for Is Parsed Hashcash Valid
3) check if the amount of bits of the returned ParsedHashcashes are of a desired number
4) check if the resources of the returned ParsedHashcashes matches the expected string
5) check if the dates of the returned ParsedHashcashes are not in the future and are not too long ago
6) check if the hash hasn't been used already (save the used Hashcash hashes in an Array for example)

You can change the order of actions if desired.

Args:
    hashes (Array[str]): 

Returns:
    Array[LowEntryParsedHashcash]:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash_parse"></a>

#### hashcash\_parse

```python
@classmethod
def hashcash_parse(cls, hash: str) -> LowEntryParsedHashcash
```

X.hashcash_parse(hash) -> LowEntryParsedHashcash
Parses and validates a Hashcash hash.

To successfully validate a Hashcash hash, do the following:
1) call this method to parse the hash
2) check if the returned ParsedHashcash returns true for Is Parsed Hashcash Valid
3) check if the amount of bits of the returned ParsedHashcash is of a desired number
4) check if the resource of the returned ParsedHashcash matches the expected string
5) check if the date of the returned ParsedHashcash is not in the future and is not too long ago
6) check if the hash hasn't been used already (save the used Hashcash hashes in an Array for example)

You can change the order of actions if desired.

Args:
    hash (str): 

Returns:
    LowEntryParsedHashcash:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash_custom_creation_date"></a>

#### hashcash\_custom\_creation\_date

```python
@classmethod
def hashcash_custom_creation_date(cls,
                                  resource: str,
                                  utc_date: DateTime,
                                  bits: int = 22) -> str
```

X.hashcash_custom_creation_date(resource, utc_date, bits=22) -> str
Creates Hashcash hashes, returns a variable amount of characters, will never return null.

The strength (or value) of the Hashcash hash is determined by the amount of given bits.

20 is an average amount of bits.
22 is a good amount of bits.
24 is a very good amount of bits.

The given 'resource' is basically an ID of the service you are 'buying' with this Hashcash, like an action or an email address or whatever, something that is unique-ish but not necessarily unique.

Hashcash hashes are only valid for a certain amount of time (depending on the receiver of the Hashcash), the given DateTime is used as the creation date of the Hashcash hash.

You can validate Hashcash hashes with the Parse Hashcash blueprints.

Args:
    resource (str): 
    utc_date (DateTime): 
    bits (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash_array_custom_creation_date"></a>

#### hashcash\_array\_custom\_creation\_date

```python
@classmethod
def hashcash_array_custom_creation_date(cls,
                                        resources: Array[str],
                                        utc_date: DateTime,
                                        bits: int = 22) -> Array[str]
```

X.hashcash_array_custom_creation_date(resources, utc_date, bits=22) -> Array[str]
Creates Hashcash hashes, each will have a variable amount of characters.

The strength (or value) of the Hashcash hashes is determined by the amount of given bits.

20 is an average amount of bits.
22 is a good amount of bits.
24 is a very good amount of bits.

The given 'resources' are basically IDs of the service you are 'buying' with this Hashcash, like actions or an email addresses or whatever, something that is unique-ish but not necessarily unique.

Hashcash hashes are only valid for a certain amount of time (depending on the receiver of the Hashcash), the given DateTime is used as the creation date of the Hashcash hashes.

You can validate Hashcash hashes with the Parse Hashcash blueprints.

Args:
    resources (Array[str]): 
    utc_date (DateTime): 
    bits (int32): 

Returns:
    Array[str]:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash_array"></a>

#### hashcash\_array

```python
@classmethod
def hashcash_array(cls, resources: Array[str], bits: int = 22) -> Array[str]
```

X.hashcash_array(resources, bits=22) -> Array[str]
Creates Hashcash hashes, each will have a variable amount of characters.

The strength (or value) of the Hashcash hashes is determined by the amount of given bits.

20 is an average amount of bits.
22 is a good amount of bits.
24 is a very good amount of bits.

The given 'resources' are basically IDs of the service you are 'buying' with this Hashcash, like actions or an email addresses or whatever, something that is unique-ish but not necessarily unique.

Hashcash hashes are only valid for a certain amount of time (depending on the receiver of the Hashcash), this blueprint uses the current date and time as the creation date of the Hashcash hashes (which is what you normally want).

You can validate Hashcash hashes with the Parse Hashcash blueprints.

Args:
    resources (Array[str]): 
    bits (int32): 

Returns:
    Array[str]:

<a id="unreal.LowEntryExtendedStandardLibrary.hashcash"></a>

#### hashcash

```python
@classmethod
def hashcash(cls, resource: str, bits: int = 22) -> str
```

X.hashcash(resource, bits=22) -> str
Creates a Hashcash hash, returns a variable amount of characters.

The strength (or value) of the Hashcash hash is determined by the amount of given bits.

20 is an average amount of bits.
22 is a good amount of bits.
24 is a very good amount of bits.

The given 'resource' is basically an ID of the service you are 'buying' with this Hashcash, like an action or an email address or whatever, something that is unique-ish but not necessarily unique.

Hashcash hashes are only valid for a certain amount of time (depending on the receiver of the Hashcash), this blueprint uses the current date and time as the creation date of the Hashcash hash (which is what you normally want).

You can validate Hashcash hashes with the Parse Hashcash blueprints.

Args:
    resource (str): 
    bits (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_string_string"></a>

#### greater\_string\_string

```python
@classmethod
def greater_string_string(cls, a: str, b: str) -> bool
```

X.greater_string_string(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (str): 
    b (str): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_integer_float"></a>

#### greater\_integer\_float

```python
@classmethod
def greater_integer_float(cls, a: int, b: float) -> bool
```

X.greater_integer_float(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_integer_byte"></a>

#### greater\_integer\_byte

```python
@classmethod
def greater_integer_byte(cls, a: int, b: int) -> bool
```

X.greater_integer_byte(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_float_integer"></a>

#### greater\_float\_integer

```python
@classmethod
def greater_float_integer(cls, a: float, b: int) -> bool
```

X.greater_float_integer(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_float_byte"></a>

#### greater\_float\_byte

```python
@classmethod
def greater_float_byte(cls, a: float, b: int) -> bool
```

X.greater_float_byte(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_string_string"></a>

#### greater\_equal\_string\_string

```python
@classmethod
def greater_equal_string_string(cls, a: str, b: str) -> bool
```

X.greater_equal_string_string(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (str): 
    b (str): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_integer_float"></a>

#### greater\_equal\_integer\_float

```python
@classmethod
def greater_equal_integer_float(cls, a: int, b: float) -> bool
```

X.greater_equal_integer_float(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_integer_byte"></a>

#### greater\_equal\_integer\_byte

```python
@classmethod
def greater_equal_integer_byte(cls, a: int, b: int) -> bool
```

X.greater_equal_integer_byte(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (int32): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_float_integer"></a>

#### greater\_equal\_float\_integer

```python
@classmethod
def greater_equal_float_integer(cls, a: float, b: int) -> bool
```

X.greater_equal_float_integer(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_float_byte"></a>

#### greater\_equal\_float\_byte

```python
@classmethod
def greater_equal_float_byte(cls, a: float, b: int) -> bool
```

X.greater_equal_float_byte(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (double): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_byte_integer"></a>

#### greater\_equal\_byte\_integer

```python
@classmethod
def greater_equal_byte_integer(cls, a: int, b: int) -> bool
```

X.greater_equal_byte_integer(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_equal_byte_float"></a>

#### greater\_equal\_byte\_float

```python
@classmethod
def greater_equal_byte_float(cls, a: int, b: float) -> bool
```

X.greater_equal_byte_float(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_byte_integer"></a>

#### greater\_byte\_integer

```python
@classmethod
def greater_byte_integer(cls, a: int, b: int) -> bool
```

X.greater_byte_integer(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.greater_byte_float"></a>

#### greater\_byte\_float

```python
@classmethod
def greater_byte_float(cls, a: int, b: float) -> bool
```

X.greater_byte_float(a, b) -> bool
Returns true if A is greater than B (A > B)
deprecated: Use the new built-in compare blueprint instead.

Args:
    a (uint8): 
    b (double): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.grayscale_pixels"></a>

#### grayscale\_pixels

```python
@classmethod
def grayscale_pixels(cls, pixels: Array[Color]) -> Array[Color]
```

X.grayscale_pixels(pixels) -> Array[Color]
Converts the pixels to accurate-looking gray pixels.

The formula it uses:  brightness  =  21.25% red  +  71.54% green  +  7.21% blue

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.grayscale_pixel"></a>

#### grayscale\_pixel

```python
@classmethod
def grayscale_pixel(cls, pixel: Color) -> Color
```

X.grayscale_pixel(pixel) -> Color
Converts the pixel to an accurate-looking gray pixel.

The formula it uses:  brightness  =  21.25% red  +  71.54% green  +  7.21% blue

Args:
    pixel (Color): 

Returns:
    Color:

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_size"></a>

#### get\_window\_size

```python
@classmethod
def get_window_size(cls) -> Tuple[bool, int, int]
```

X.get_window_size() -> (success=bool, width=int32, height=int32)
Gets the window size in screen pixels.

Returns Success=false, Width=0 and Height=0 if the window bounds could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null

Returns:
    tuple: 

    success (bool): 

    width (int32): 

    height (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_position_in_percentages_centered"></a>

#### get\_window\_position\_in\_percentages\_centered

```python
@classmethod
def get_window_position_in_percentages_centered(
        cls) -> Tuple[bool, float, float]
```

X.get_window_position_in_percentages_centered() -> (success=bool, x=double, y=double)
Gets the window position in screen space in percentages, relative to the primary monitor work area, from 0.0 to 1.0.

This will take the window size in account, meaning that X=0.5 and Y=0.5 will cause the window to be centered in the primary screen work area.

Returns Success=false, X=0.0 and Y=0.0 if the window bounds could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null

Returns:
    tuple: 

    success (bool): 

    x (double): 

    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_position"></a>

#### get\_window\_position

```python
@classmethod
def get_window_position(cls) -> Tuple[bool, int, int]
```

X.get_window_position() -> (success=bool, x=int32, y=int32)
Gets the window position in screen space.

Returns Success=false, X=0 and Y=0 if the window bounds could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null

Returns:
    tuple: 

    success (bool): 

    x (int32): 

    y (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_positiom_in_percentages_centered"></a>

#### get\_window\_positiom\_in\_percentages\_centered

```python
@classmethod
def get_window_positiom_in_percentages_centered(
        cls) -> Tuple[bool, float, float]
```

X.get_window_positiom_in_percentages_centered() -> (success=bool, x=double, y=double)
ReSharper disable once IdentifierTypo
deprecated: Use GetWindowPositionInPercentagesCentered instead

Returns:
    tuple: 

    success (bool): 

    x (double): 

    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_mode"></a>

#### get\_window\_mode

```python
@classmethod
def get_window_mode(cls) -> Tuple[bool, bool, bool]
```

X.get_window_mode() -> (success=bool, fullscreen=bool, is_fullscreen_windowed=bool)
Returns the window mode.

If Fullscreen is false then IsFullscreenWindowed will also be false.

Returns Success=false, Fullscreen=false and Windowed=false if the window mode could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null
 - The mode is pseudo-fullscreen (used for devices like HMDs)

Returns:
    tuple: 

    success (bool): 

    fullscreen (bool): 

    is_fullscreen_windowed (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_bounds"></a>

#### get\_window\_bounds

```python
@classmethod
def get_window_bounds(cls) -> Tuple[bool, int, int, int, int]
```

X.get_window_bounds() -> (success=bool, x=int32, y=int32, width=int32, height=int32)
Returns the windows bounds in screen space.

Returns Success=false, X=0, Y=0, Width=0 and Height=0 if the window bounds could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null

Returns:
    tuple: 

    success (bool): 

    x (int32): 

    y (int32): 

    width (int32): 

    height (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_window_border_size"></a>

#### get\_window\_border\_size

```python
@classmethod
def get_window_border_size(cls) -> Tuple[bool, Margin]
```

X.get_window_border_size() -> (success=bool, margin=Margin)
Gets the window border size.
Useful for when you want to set the window's position while still showing the border as well.

Returns Success=false if the window bounds could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Window is null

Returns:
    tuple: 

    success (bool): 

    margin (Margin):

<a id="unreal.LowEntryExtendedStandardLibrary.get_user_focused_widget_type"></a>

#### get\_user\_focused\_widget\_type

```python
@classmethod
def get_user_focused_widget_type(cls, user_index: int) -> Name
```

X.get_user_focused_widget_type(user_index) -> Name
Clears widget focus.

Args:
    user_index (int32): 

Returns:
    Name:

<a id="unreal.LowEntryExtendedStandardLibrary.get_split_screen_type"></a>

#### get\_split\_screen\_type

```python
@classmethod
def get_split_screen_type(cls) -> LowEntrySplitScreenType
```

X.get_split_screen_type() -> LowEntrySplitScreenType
Get the current split screen type, note that this value also depends on the number of players that are currently in the game.

Returns:
    LowEntrySplitScreenType: 

    type (LowEntrySplitScreenType):

<a id="unreal.LowEntryExtendedStandardLibrary.get_project_version"></a>

#### get\_project\_version

```python
@classmethod
def get_project_version(cls) -> str
```

X.get_project_version() -> str
Returns the project version from the project settings.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_project_name"></a>

#### get\_project\_name

```python
@classmethod
def get_project_name(cls) -> str
```

X.get_project_name() -> str
Returns the project name from the project settings.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_primary_monitor_work_area"></a>

#### get\_primary\_monitor\_work\_area

```python
@classmethod
def get_primary_monitor_work_area(cls) -> Tuple[int, int, int, int]
```

X.get_primary_monitor_work_area() -> (x=int32, y=int32, width=int32, height=int32)
Returns the primary monitor work area, this is the area not covered by task bars or other docked widgets.

Returns:
    tuple: 

    x (int32): 

    y (int32): 

    width (int32): 

    height (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_primary_monitor_resolution"></a>

#### get\_primary\_monitor\_resolution

```python
@classmethod
def get_primary_monitor_resolution(cls) -> Tuple[int, int]
```

X.get_primary_monitor_resolution() -> (width=int32, height=int32)
Returns the primary monitor resolution.

Returns:
    tuple: 

    width (int32): 

    height (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_mouse_position_in_percentages"></a>

#### get\_mouse\_position\_in\_percentages

```python
@classmethod
def get_mouse_position_in_percentages(cls) -> Tuple[bool, float, float]
```

X.get_mouse_position_in_percentages() -> (success=bool, x=double, y=double)
Returns the mouse position (relative to the viewport) in percentages, from 0.0 to 1.0.

X:  0.0 is left, 1.0 is right
Y:  0.0 is top,  1.0 is bottom

Returns Success=false, X=0.0 and Y=0.0 if the mouse position could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Viewport is null
 - the mouse is outside of the viewport

Returns:
    tuple: 

    success (bool): 

    x (double): 

    y (double):

<a id="unreal.LowEntryExtendedStandardLibrary.get_mouse_position"></a>

#### get\_mouse\_position

```python
@classmethod
def get_mouse_position(cls) -> Tuple[bool, int, int]
```

X.get_mouse_position() -> (success=bool, x=int32, y=int32)
Returns the mouse position (relative to the viewport), from 0 to the viewport width or height.

Returns Success=false, X=0 and Y=0 if the mouse position could not be determined, which happens when:
 - GEngine is null
 - GEngine's GameViewportClient is null
 - GameViewportClient's Viewport is null
 - the mouse is outside of the viewport

Returns:
    tuple: 

    success (bool): 

    x (int32): 

    y (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_maximum_volume"></a>

#### get\_maximum\_volume

```python
@classmethod
def get_maximum_volume(cls) -> Tuple[int, bool]
```

X.get_maximum_volume() -> (volume=int32, success=bool)
Returns the maximum system volume.

Doesn't work, use Get Current System Volume (Percentages) instead.

Note: This blueprint is not used to retrieve or change the sound volume in-game, you will have to use Sound Classes for that.
deprecated: This function has been replaced by Get Current System Volume (Percentages).

Returns:
    tuple: 

    volume (int32): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_local_to_absolute_scale"></a>

#### get\_local\_to\_absolute\_scale

```python
@classmethod
def get_local_to_absolute_scale(cls, geometry: Geometry) -> Vector2D
```

X.get_local_to_absolute_scale(geometry) -> Vector2D
Returns the scale of the given Geometry from Local to Absolute (Absolute Size divided by Local Size).

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.LowEntryExtendedStandardLibrary.get_keyboard_focused_widget_type"></a>

#### get\_keyboard\_focused\_widget\_type

```python
@classmethod
def get_keyboard_focused_widget_type(cls) -> Name
```

X.get_keyboard_focused_widget_type() -> Name
Clears widget focus.

Returns:
    Name:

<a id="unreal.LowEntryExtendedStandardLibrary.get_generic_team_id"></a>

#### get\_generic\_team\_id

```python
@classmethod
def get_generic_team_id(cls, target: Actor) -> int
```

X.get_generic_team_id(target) -> uint8
Returns the Team ID of the given Actor.

Args:
    target (Actor): 

Returns:
    uint8: 

    team_id (uint8):

<a id="unreal.LowEntryExtendedStandardLibrary.get_current_volume_percentage"></a>

#### get\_current\_volume\_percentage

```python
@classmethod
def get_current_volume_percentage(cls) -> Tuple[float, bool]
```

X.get_current_volume_percentage() -> (percentage=double, success=bool)
Returns the current system volume in percentages, from 0.0 to 1.0.

Currently only works on Android devices. If you only care about getting the volume on Android, you might as well use the "Get Android Volume" blueprint instead.

Note: This blueprint is not used to retrieve or change the sound volume in-game, you will have to use Sound Classes for that.

Returns:
    tuple: 

    percentage (double): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_current_volume"></a>

#### get\_current\_volume

```python
@classmethod
def get_current_volume(cls) -> Tuple[int, bool]
```

X.get_current_volume() -> (volume=int32, success=bool)
Returns the current system volume.

Doesn't work, use Get Current System Volume (Percentages) instead.

Note: This blueprint is not used to retrieve or change the sound volume in-game, you will have to use Sound Classes for that.
deprecated: This function has been replaced by Get Current System Volume (Percentages).

Returns:
    tuple: 

    volume (int32): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_class_with_name"></a>

#### get\_class\_with\_name

```python
@classmethod
def get_class_with_name(cls, class_name: str) -> Tuple[Class, bool]
```

X.get_class_with_name(class_name) -> (class_=type(Class), success=bool)
Finds a class.

The given ClassName has to be a specific path to your class/object, for example: /Game/Blueprints/GameMode.GameMode_C

Note that you have to append _C to the end of your ClassName, as is done in the example.
Note that is also always has to start with /Game/, no matter what the path to your class is.

The easiest way to get the correct ClassName is by right clicking your class/object in the content browser and by then clicking on 'Copy Reference', then you'll just have to remove the 'Blueprint' and the quotes and add the _C at the end of it.
So this: Blueprint'/Game/Blueprints/PlayerController.PlayerController'
Would turn into this: /Game/Blueprints/PlayerController.PlayerController_C

Args:
    class_name (str): 

Returns:
    tuple: 

    class_ (type(Class)): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_byte_with_bit_set"></a>

#### get\_byte\_with\_bit\_set

```python
@classmethod
def get_byte_with_bit_set(cls, byte: int, bit: int, value: bool) -> int
```

X.get_byte_with_bit_set(byte, bit, value) -> uint8
Sets a bit 1 or 0, depending on the given boolean.

Bytes start with bit 8, ending with bit 1, as such: 87654321

Args:
    byte (uint8): 
    bit (int32): 
    value (bool): 

Returns:
    uint8:

<a id="unreal.LowEntryExtendedStandardLibrary.get_battery_temperature"></a>

#### get\_battery\_temperature

```python
@classmethod
def get_battery_temperature(cls) -> Tuple[float, bool]
```

X.get_battery_temperature() -> (celsius=double, success=bool)
Returns the battery temperature (in degrees of Celsius).

Currently only works on Android devices.

Returns:
    tuple: 

    celsius (double): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_battery_state"></a>

#### get\_battery\_state

```python
@classmethod
def get_battery_state(cls) -> Tuple[LowEntryBatteryState, bool]
```

X.get_battery_state() -> (state=LowEntryBatteryState, success=bool)
Returns the battery state.

Currently only works on Android devices.

Returns:
    tuple: 

    state (LowEntryBatteryState): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_battery_charge"></a>

#### get\_battery\_charge

```python
@classmethod
def get_battery_charge(cls) -> Tuple[int, bool]
```

X.get_battery_charge() -> (percentage=int32, success=bool)
Returns the battery charge (in percentages, from 0% to 100%).

Currently only works on Android devices.

Returns:
    tuple: 

    percentage (int32): 

    success (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_volume"></a>

#### get\_android\_volume

```python
@classmethod
def get_android_volume(cls) -> int
```

X.get_android_volume() -> int32
Returns the current Android volume, from 0 to 15.

This will always only ever work on Android devices, other systems will always return 0. If you want more systems supported later on, use the "Get System Volume (Percentages)" blueprint instead.

Note: This blueprint is not used to retrieve or change the sound volume in-game, you will have to use Sound Classes for that.

Returns:
    int32: 

    volume (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_version"></a>

#### get\_android\_version

```python
@classmethod
def get_android_version(cls) -> str
```

X.get_android_version() -> str
Returns the Android version, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_os_language"></a>

#### get\_android\_os\_language

```python
@classmethod
def get_android_os_language(cls) -> str
```

X.get_android_os_language() -> str
Returns the Android OS language, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_number_of_cores"></a>

#### get\_android\_number\_of\_cores

```python
@classmethod
def get_android_number_of_cores(cls) -> int
```

X.get_android_number_of_cores() -> int32
Returns the number of cores, returns -1 if it failed.

This will always only ever work on Android devices, other systems will always return -1.

Returns:
    int32:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_gpu_family"></a>

#### get\_android\_gpu\_family

```python
@classmethod
def get_android_gpu_family(cls) -> str
```

X.get_android_gpu_family() -> str
Returns the Android GPU family, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_gl_version"></a>

#### get\_android\_gl\_version

```python
@classmethod
def get_android_gl_version(cls) -> str
```

X.get_android_gl_version() -> str
Returns the Android GL version, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_device_model"></a>

#### get\_android\_device\_model

```python
@classmethod
def get_android_device_model(cls) -> str
```

X.get_android_device_model() -> str
Returns the Android device model, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_device_make"></a>

#### get\_android\_device\_make

```python
@classmethod
def get_android_device_make(cls) -> str
```

X.get_android_device_make() -> str
Returns the Android device make, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_default_locale"></a>

#### get\_android\_default\_locale

```python
@classmethod
def get_android_default_locale(cls) -> str
```

X.get_android_default_locale() -> str
Returns the Android default locale, returns an empty string if it failed.

This will always only ever work on Android devices, other systems will always return an empty string.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.get_android_build_version"></a>

#### get\_android\_build\_version

```python
@classmethod
def get_android_build_version(cls) -> int
```

X.get_android_build_version() -> int32
Returns the Android build version, returns -1 if it failed.

This will always only ever work on Android devices, other systems will always return -1.

Returns:
    int32:

<a id="unreal.LowEntryExtendedStandardLibrary.get_absolute_to_local_scale"></a>

#### get\_absolute\_to\_local\_scale

```python
@classmethod
def get_absolute_to_local_scale(cls, geometry: Geometry) -> Vector2D
```

X.get_absolute_to_local_scale(geometry) -> Vector2D
Returns the scale of the given Geometry from Absolute to Local (Local Size divided by Absolute Size).

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.LowEntryExtendedStandardLibrary.get_absolute_size"></a>

#### get\_absolute\_size

```python
@classmethod
def get_absolute_size(cls, geometry: Geometry) -> Vector2D
```

X.get_absolute_size(geometry) -> Vector2D
Returns the absolute size of the given Geometry.

Args:
    geometry (Geometry): 

Returns:
    Vector2D:

<a id="unreal.LowEntryExtendedStandardLibrary.generate_random_bytes_random_length"></a>

#### generate\_random\_bytes\_random\_length

```python
@classmethod
def generate_random_bytes_random_length(cls, min_length: int,
                                        max_length: int) -> Array[int]
```

X.generate_random_bytes_random_length(min_length, max_length) -> Array[uint8]
Returns random bytes.

Args:
    min_length (int32): 
    max_length (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.generate_random_bytes"></a>

#### generate\_random\_bytes

```python
@classmethod
def generate_random_bytes(cls, length: int) -> Array[int]
```

X.generate_random_bytes(length) -> Array[uint8]
Returns random bytes.

Args:
    length (int32): 

Returns:
    Array[uint8]: 

    byte_array (Array[uint8]):

<a id="unreal.LowEntryExtendedStandardLibrary.floor_decimals"></a>

#### floor\_decimals

```python
@classmethod
def floor_decimals(cls, number: float, decimals: int) -> float
```

X.floor_decimals(number, decimals) -> double
Floor to the given Decimals.

Args:
    number (double): 
    decimals (int32): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.float_to_bytes"></a>

#### float\_to\_bytes

```python
@classmethod
def float_to_bytes(cls, value: float) -> Array[int]
```

X.float_to_bytes(value) -> Array[uint8]
Converts a float into a Byte Array (4 bytes).

Args:
    value (float): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_rg"></a>

#### flip\_pixel\_channels\_rg

```python
@classmethod
def flip_pixel_channels_rg(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_rg(pixels) -> Array[Color]
Flips the red and green channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_rb"></a>

#### flip\_pixel\_channels\_rb

```python
@classmethod
def flip_pixel_channels_rb(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_rb(pixels) -> Array[Color]
Flips the red and blue channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_ra"></a>

#### flip\_pixel\_channels\_ra

```python
@classmethod
def flip_pixel_channels_ra(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_ra(pixels) -> Array[Color]
Flips the red and alpha channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_gb"></a>

#### flip\_pixel\_channels\_gb

```python
@classmethod
def flip_pixel_channels_gb(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_gb(pixels) -> Array[Color]
Flips the green and blue channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_ga"></a>

#### flip\_pixel\_channels\_ga

```python
@classmethod
def flip_pixel_channels_ga(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_ga(pixels) -> Array[Color]
Flips the green and alpha channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.flip_pixel_channels_ba"></a>

#### flip\_pixel\_channels\_ba

```python
@classmethod
def flip_pixel_channels_ba(cls, pixels: Array[Color]) -> Array[Color]
```

X.flip_pixel_channels_ba(pixels) -> Array[Color]
Flips the blue and alpha channels of the given pixels.

Args:
    pixels (Array[Color]): 

Returns:
    Array[Color]:

<a id="unreal.LowEntryExtendedStandardLibrary.exec_to_integer"></a>

#### exec\_to\_integer

```python
@classmethod
def exec_to_integer(cls, branch: LowEntryExtendedStandardLibrary0to9) -> int
```

X.exec_to_integer(branch) -> int32
Returns an integer depending on which exec pin has been executed.

Args:
    branch (LowEntryExtendedStandardLibrary0to9): 

Returns:
    int32: 

    value (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.exec_to_byte"></a>

#### exec\_to\_byte

```python
@classmethod
def exec_to_byte(cls, branch: LowEntryExtendedStandardLibrary0to9) -> int
```

X.exec_to_byte(branch) -> uint8
Returns a byte depending on which exec pin has been executed.

Args:
    branch (LowEntryExtendedStandardLibrary0to9): 

Returns:
    uint8: 

    value (uint8):

<a id="unreal.LowEntryExtendedStandardLibrary.exec_to_boolean"></a>

#### exec\_to\_boolean

```python
@classmethod
def exec_to_boolean(
        cls, branch: LowEntryExtendedStandardLibraryTrueOrFalse) -> bool
```

X.exec_to_boolean(branch) -> bool
Returns a boolean depending on which exec pin has been executed.

Args:
    branch (LowEntryExtendedStandardLibraryTrueOrFalse): 

Returns:
    bool: 

    value (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.double_to_bytes"></a>

#### double\_to\_bytes

```python
@classmethod
def double_to_bytes(cls, value: float) -> Array[int]
```

X.double_to_bytes(value) -> Array[uint8]
Converts a double into a Byte Array (8 bytes).

Args:
    value (double): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.double_create_zero"></a>

#### double\_create\_zero

```python
@classmethod
def double_create_zero(cls) -> LowEntryDouble
```

X.double_create_zero() -> LowEntryDouble
Creates a new double (bytes), a double is always 8 bytes.

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryExtendedStandardLibrary.double_create"></a>

#### double\_create

```python
@classmethod
def double_create(cls,
                  byte_array: Array[int],
                  index: int = 0,
                  length: int = 2147483647) -> LowEntryDouble
```

X.double_create(byte_array, index=0, length=2147483647) -> LowEntryDouble
Creates a new double (bytes), a double is always 8 bytes (give less bytes and it will pad with 0, give more bytes and it will only take the first 8).

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryExtendedStandardLibrary.divide_vector2d_vector2d"></a>

#### divide\_vector2d\_vector2d

```python
@classmethod
def divide_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> Vector2D
```

X.divide_vector2d_vector2d(a, b) -> Vector2D
Divides A by B.

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.LowEntryExtendedStandardLibrary.development_build"></a>

#### development\_build

```python
@classmethod
def development_build(cls) -> bool
```

X.development_build() -> bool
Returns true if this is a debug build (UE_BUILD_DEVELOPMENT), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.desktop_platform"></a>

#### desktop\_platform

```python
@classmethod
def desktop_platform(cls) -> bool
```

X.desktop_platform() -> bool
Returns true if this is a desktop (PLATFORM_DESKTOP), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.delay_frames"></a>

#### delay\_frames

```python
@classmethod
def delay_frames(cls, world_context_object: Object, frames: int,
                 latent_info: LatentActionInfo) -> None
```

X.delay_frames(world_context_object, frames, latent_info) -> None
Perform a latent action with a delay (specified in frames).  Calling again while it is counting down will be ignored.

Args:
    world_context_object (Object): World context.
    frames (int32): frames of delay.
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.LowEntryExtendedStandardLibrary.debug_build"></a>

#### debug\_build

```python
@classmethod
def debug_build(cls) -> bool
```

X.debug_build() -> bool
Returns true if this is a debug build (UE_BUILD_DEBUG), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.date_time_to_unix_timestamp"></a>

#### date\_time\_to\_unix\_timestamp

```python
@classmethod
def date_time_to_unix_timestamp(cls, date_time: DateTime) -> LowEntryLong
```

X.date_time_to_unix_timestamp(date_time) -> LowEntryLong
Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT represented by the given FDateTime.

Args:
    date_time (DateTime): 

Returns:
    LowEntryLong: 

    timestamp (LowEntryLong):

<a id="unreal.LowEntryExtendedStandardLibrary.date_time_to_string"></a>

#### date\_time\_to\_string

```python
@classmethod
def date_time_to_string(cls,
                        date_time: DateTime,
                        format: str = "%Y.%m.%d-%H.%M.%S") -> str
```

X.date_time_to_string(date_time, format="%Y.%m.%d-%H.%M.%S") -> str
Returns the string representation of the given FDateTime.

The format works as follows:

case TCHAR('a'): Result += IsMorning() ? TEXT("am") : TEXT("pm"); break;
case TCHAR('A'): Result += IsMorning() ? TEXT("AM") : TEXT("PM"); break;
case TCHAR('d'): Result += FString::Printf(TEXT("%02i"), GetDay()); break;
case TCHAR('D'): Result += FString::Printf(TEXT("%03i"), GetDayOfYear()); break;
case TCHAR('m'): Result += FString::Printf(TEXT("%02i"), GetMonth()); break;
case TCHAR('y'): Result += FString::Printf(TEXT("%02i"), GetYear() % 100); break;
case TCHAR('Y'): Result += FString::Printf(TEXT("%04i"), GetYear()); break;
case TCHAR('h'): Result += FString::Printf(TEXT("%02i"), GetHour12()); break;
case TCHAR('H'): Result += FString::Printf(TEXT("%02i"), GetHour()); break;
case TCHAR('M'): Result += FString::Printf(TEXT("%02i"), GetMinute()); break;
case TCHAR('S'): Result += FString::Printf(TEXT("%02i"), GetSecond()); break;
case TCHAR('s'): Result += FString::Printf(TEXT("%03i"), GetMillisecond()); break;

Args:
    date_time (DateTime): 
    format (str): 

Returns:
    str: 

    string (str):

<a id="unreal.LowEntryExtendedStandardLibrary.date_time_to_iso8601"></a>

#### date\_time\_to\_iso8601

```python
@classmethod
def date_time_to_iso8601(cls, date_time: DateTime) -> str
```

X.date_time_to_iso8601(date_time) -> str
Returns the ISO-8601 string representation of the FDateTime.

The resulting string assumes that the FDateTime is in UTC.

Args:
    date_time (DateTime): 

Returns:
    str: 

    string (str):

<a id="unreal.LowEntryExtendedStandardLibrary.date_time_from_unix_timestamp"></a>

#### date\_time\_from\_unix\_timestamp

```python
@classmethod
def date_time_from_unix_timestamp(cls, timestamp: LowEntryLong) -> DateTime
```

X.date_time_from_unix_timestamp(timestamp) -> DateTime
Creates a FDateTime with the given time in milliseconds after January 1, 1970 00:00:00 GMT.

Args:
    timestamp (LowEntryLong): 

Returns:
    DateTime: 

    date_time (DateTime):

<a id="unreal.LowEntryExtendedStandardLibrary.create_string"></a>

#### create\_string

```python
@classmethod
def create_string(cls, length: int, filler: str = " ") -> str
```

X.create_string(length, filler=" ") -> str
Creates a String of the given length.

Args:
    length (int32): 
    filler (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.create_object"></a>

#### create\_object

```python
@classmethod
def create_object(cls, class_: Class) -> Object
```

X.create_object(class_) -> Object
Returns an instance from the given Class.

Args:
    class_ (type(Class)): 

Returns:
    Object: 

    object (Object):

<a id="unreal.LowEntryExtendedStandardLibrary.crash"></a>

#### crash

```python
@classmethod
def crash(cls) -> None
```

X.crash() -> None
Causes a crash.

<a id="unreal.LowEntryExtendedStandardLibrary.convert_utc_date_to_local_date"></a>

#### convert\_utc\_date\_to\_local\_date

```python
@classmethod
def convert_utc_date_to_local_date(cls, utc: DateTime) -> DateTime
```

X.convert_utc_date_to_local_date(utc) -> DateTime
Converts the given DateTime from the UTC time into the local time.

Args:
    utc (DateTime): 

Returns:
    DateTime: 

    local (DateTime):

<a id="unreal.LowEntryExtendedStandardLibrary.convert_local_date_to_utc_date"></a>

#### convert\_local\_date\_to\_utc\_date

```python
@classmethod
def convert_local_date_to_utc_date(cls, local: DateTime) -> DateTime
```

X.convert_local_date_to_utc_date(local) -> DateTime
Converts the given DateTime from the local time into the UTC time.

Args:
    local (DateTime): 

Returns:
    DateTime: 

    utc (DateTime):

<a id="unreal.LowEntryExtendedStandardLibrary.clipboard_set"></a>

#### clipboard\_set

```python
@classmethod
def clipboard_set(cls, value: str) -> None
```

X.clipboard_set(value) -> None
Sets the given string as the clipboard's content.

Args:
    value (str):

<a id="unreal.LowEntryExtendedStandardLibrary.clipboard_get"></a>

#### clipboard\_get

```python
@classmethod
def clipboard_get(cls) -> str
```

X.clipboard_get() -> str
Retrieves and returns the clipboard's content.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.clear_user_focus"></a>

#### clear\_user\_focus

```python
@classmethod
def clear_user_focus(cls, user_index: int) -> None
```

X.clear_user_focus(user_index) -> None
Clears widget focus.

Args:
    user_index (int32):

<a id="unreal.LowEntryExtendedStandardLibrary.clear_keyboard_focus"></a>

#### clear\_keyboard\_focus

```python
@classmethod
def clear_keyboard_focus(cls) -> None
```

X.clear_keyboard_focus() -> None
Clears widget focus.

<a id="unreal.LowEntryExtendedStandardLibrary.clear_all_user_focus"></a>

#### clear\_all\_user\_focus

```python
@classmethod
def clear_all_user_focus(cls) -> None
```

X.clear_all_user_focus() -> None
Clears widget focus.

<a id="unreal.LowEntryExtendedStandardLibrary.change_map"></a>

#### change\_map

```python
@classmethod
def change_map(cls,
               world_context_object: Object,
               map: str,
               args: str,
               specific_player: PlayerController = None) -> None
```

X.change_map(world_context_object, map, args, specific_player=None) -> None
Changes the map.

Args:
    world_context_object (Object): 
    map (str): 
    args (str): 
    specific_player (PlayerController):

<a id="unreal.LowEntryExtendedStandardLibrary.ceil_decimals"></a>

#### ceil\_decimals

```python
@classmethod
def ceil_decimals(cls, number: float, decimals: int) -> float
```

X.ceil_decimals(number, decimals) -> double
Ceil to the given Decimals.

Args:
    number (double): 
    decimals (int32): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.case_switch_object"></a>

#### case\_switch\_object

```python
@classmethod
def case_switch_object(
        cls, only_check_first_x: int, value: Object, case_1: Object,
        case_2: Object, case_3: Object, case_4: Object, case_5: Object,
        case_6: Object, case_7: Object, case_8: Object, case_9: Object,
        case_10: Object) -> LowEntryExtendedStandardLibrary1to10other
```

X.case_switch_object(only_check_first_x, value, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) -> LowEntryExtendedStandardLibrary1to10other
Executes a the pin of the matching value.

Args:
    only_check_first_x (int32): 
    value (Object): 
    1 (Object): 
    2 (Object): 
    3 (Object): 
    4 (Object): 
    5 (Object): 
    6 (Object): 
    7 (Object): 
    8 (Object): 
    9 (Object): 
    10 (Object): 

Returns:
    LowEntryExtendedStandardLibrary1to10other: 

    branch (LowEntryExtendedStandardLibrary1to10other):

<a id="unreal.LowEntryExtendedStandardLibrary.case_switch_integer"></a>

#### case\_switch\_integer

```python
@classmethod
def case_switch_integer(
        cls, only_check_first_x: int, value: int, case_1: int, case_2: int,
        case_3: int, case_4: int, case_5: int, case_6: int, case_7: int,
        case_8: int, case_9: int,
        case_10: int) -> LowEntryExtendedStandardLibrary1to10other
```

X.case_switch_integer(only_check_first_x, value, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) -> LowEntryExtendedStandardLibrary1to10other
Executes a the pin of the matching value.

Args:
    only_check_first_x (int32): 
    value (int32): 
    1 (int32): 
    2 (int32): 
    3 (int32): 
    4 (int32): 
    5 (int32): 
    6 (int32): 
    7 (int32): 
    8 (int32): 
    9 (int32): 
    10 (int32): 

Returns:
    LowEntryExtendedStandardLibrary1to10other: 

    branch (LowEntryExtendedStandardLibrary1to10other):

<a id="unreal.LowEntryExtendedStandardLibrary.case_switch_byte"></a>

#### case\_switch\_byte

```python
@classmethod
def case_switch_byte(
        cls, only_check_first_x: int, value: int, case_1: int, case_2: int,
        case_3: int, case_4: int, case_5: int, case_6: int, case_7: int,
        case_8: int, case_9: int,
        case_10: int) -> LowEntryExtendedStandardLibrary1to10other
```

X.case_switch_byte(only_check_first_x, value, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) -> LowEntryExtendedStandardLibrary1to10other
Executes a the pin of the matching value.

Args:
    only_check_first_x (int32): 
    value (uint8): 
    1 (uint8): 
    2 (uint8): 
    3 (uint8): 
    4 (uint8): 
    5 (uint8): 
    6 (uint8): 
    7 (uint8): 
    8 (uint8): 
    9 (uint8): 
    10 (uint8): 

Returns:
    LowEntryExtendedStandardLibrary1to10other: 

    branch (LowEntryExtendedStandardLibrary1to10other):

<a id="unreal.LowEntryExtendedStandardLibrary.carriage_return_character"></a>

#### carriage\_return\_character

```python
@classmethod
def carriage_return_character(cls) -> str
```

X.carriage_return_character() -> str
Returns a carriage return (\r).

This blueprint will always return a \r character, no matter what Operating System it is running on.

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_to_bytes"></a>

#### byte\_to\_bytes

```python
@classmethod
def byte_to_bytes(cls, value: int) -> Array[int]
```

X.byte_to_bytes(value) -> Array[uint8]
Converts a byte (uint8) into a Byte Array (1 byte).

Args:
    value (uint8): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_to_boolean"></a>

#### byte\_to\_boolean

```python
@classmethod
def byte_to_boolean(cls, byte: int) -> bool
```

X.byte_to_boolean(byte) -> bool
Converts a Byte into a boolean (00000001 will return true, everything else will return false).

Args:
    byte (uint8): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_to_bits"></a>

#### byte\_to\_bits

```python
@classmethod
def byte_to_bits(
        cls,
        byte: int) -> Tuple[bool, bool, bool, bool, bool, bool, bool, bool]
```

X.byte_to_bits(byte) -> (bit1=bool, bit2=bool, bit3=bool, bit4=bool, bit5=bool, bit6=bool, bit7=bool, bit8=bool)
Converts a byte into bits.

Args:
    byte (uint8): 

Returns:
    tuple: 

    bit1 (bool): 

    bit2 (bool): 

    bit3 (bool): 

    bit4 (bool): 

    bit5 (bool): 

    bit6 (bool): 

    bit7 (bool): 

    bit8 (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_string_utf8"></a>

#### bytes\_to\_string\_utf8

```python
@classmethod
def bytes_to_string_utf8(cls,
                         byte_array: Array[int],
                         index: int = 0,
                         length: int = 2147483647) -> str
```

X.bytes_to_string_utf8(byte_array, index=0, length=2147483647) -> str
Tries to convert a Byte Array into a String (using UTF-8 encoding). Will return an empty String on failure.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_pixels"></a>

#### bytes\_to\_pixels

```python
@classmethod
def bytes_to_pixels(cls,
                    byte_array: Array[int],
                    image_format: LowEntryImageFormat,
                    index: int = 0,
                    length: int = 2147483647) -> Tuple[int, int, Array[Color]]
```

X.bytes_to_pixels(byte_array, image_format, index=0, length=2147483647) -> (width=int32, height=int32, pixels=Array[Color])
Converts a Byte Array into a Pixel Array.

Returns an empty Pixel Array if it fails, the Width and the Height will also be 0 then.

Args:
    byte_array (Array[uint8]): 
    image_format (LowEntryImageFormat): 
    index (int32): 
    length (int32): 

Returns:
    tuple: 

    width (int32): 

    height (int32): 

    pixels (Array[Color]):

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_long_bytes"></a>

#### bytes\_to\_long\_bytes

```python
@classmethod
def bytes_to_long_bytes(cls,
                        byte_array: Array[int],
                        index: int = 0,
                        length: int = 2147483647) -> LowEntryLong
```

X.bytes_to_long_bytes(byte_array, index=0, length=2147483647) -> LowEntryLong
Converts a Byte Array into a signed long (int64) (bytes).

If there are more than 8 bytes given, it will only convert the first 8 bytes to a long.
If there are less than 8 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 00000000 00000000 00000000 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryLong:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_long"></a>

#### bytes\_to\_long

```python
@classmethod
def bytes_to_long(cls,
                  byte_array: Array[int],
                  index: int = 0,
                  length: int = 2147483647) -> int
```

X.bytes_to_long(byte_array, index=0, length=2147483647) -> int64
Converts a Byte Array into a signed long (int64).

If there are more than 8 bytes given, it will only convert the first 8 bytes to an integer.
If there are less than 8 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 00000000 00000000 00000000 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    int64:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_integer"></a>

#### bytes\_to\_integer

```python
@classmethod
def bytes_to_integer(cls,
                     byte_array: Array[int],
                     index: int = 0,
                     length: int = 2147483647) -> int
```

X.bytes_to_integer(byte_array, index=0, length=2147483647) -> int32
Converts a Byte Array into a signed integer (int32).

If there are more than 4 bytes given, it will only convert the first 4 bytes to an integer.
If there are less than 4 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    int32:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_image"></a>

#### bytes\_to\_image

```python
@classmethod
def bytes_to_image(cls,
                   byte_array: Array[int],
                   image_format: LowEntryImageFormat,
                   index: int = 0,
                   length: int = 2147483647) -> Texture2D
```

X.bytes_to_image(byte_array, image_format, index=0, length=2147483647) -> Texture2D
Converts a Byte Array into an image (Texture2D).

Returns nullptr if it fails.

Args:
    byte_array (Array[uint8]): 
    image_format (LowEntryImageFormat): 
    index (int32): 
    length (int32): 

Returns:
    Texture2D:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_hex"></a>

#### bytes\_to\_hex

```python
@classmethod
def bytes_to_hex(cls,
                 byte_array: Array[int],
                 add_spaces: bool = False,
                 index: int = 0,
                 length: int = 2147483647) -> str
```

X.bytes_to_hex(byte_array, add_spaces=False, index=0, length=2147483647) -> str
Converts a Byte Array into a Hexadecimal (Base16) String.

Args:
    byte_array (Array[uint8]): 
    add_spaces (bool): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_float"></a>

#### bytes\_to\_float

```python
@classmethod
def bytes_to_float(cls,
                   byte_array: Array[int],
                   index: int = 0,
                   length: int = 2147483647) -> float
```

X.bytes_to_float(byte_array, index=0, length=2147483647) -> float
Converts a Byte Array into a float.

If there are more than 4 bytes given, it will only convert the first 4 bytes to a float.
If there are less than 4 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    float:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_existing_image"></a>

#### bytes\_to\_existing\_image

```python
@classmethod
def bytes_to_existing_image(
        cls,
        texture2d: Texture2D,
        byte_array: Array[int],
        image_format: LowEntryImageFormat,
        index: int = 0,
        length: int = 2147483647) -> Tuple[Texture2D, bool]
```

X.bytes_to_existing_image(texture2d, byte_array, image_format, index=0, length=2147483647) -> (Texture2D, reused_given_texture2d=bool)
Converts a Byte Array into an image (Texture2D).

Returns nullptr if it fails.

Will re-use the given Texture2D if possible, ReusedGivenTexture2D will be true if it was possible.

Args:
    texture2d (Texture2D): 
    byte_array (Array[uint8]): 
    image_format (LowEntryImageFormat): 
    index (int32): 
    length (int32): 

Returns:
    bool: 

    reused_given_texture2d (bool):

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_double_bytes"></a>

#### bytes\_to\_double\_bytes

```python
@classmethod
def bytes_to_double_bytes(cls,
                          byte_array: Array[int],
                          index: int = 0,
                          length: int = 2147483647) -> LowEntryDouble
```

X.bytes_to_double_bytes(byte_array, index=0, length=2147483647) -> LowEntryDouble
Converts a Byte Array into a double (bytes).

If there are more than 8 bytes given, it will only convert the first 8 bytes to a double.
If there are less than 8 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 00000000 00000000 00000000 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryDouble:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_double"></a>

#### bytes\_to\_double

```python
@classmethod
def bytes_to_double(cls,
                    byte_array: Array[int],
                    index: int = 0,
                    length: int = 2147483647) -> float
```

X.bytes_to_double(byte_array, index=0, length=2147483647) -> double
Converts a Byte Array into a double.

If there are more than 8 bytes given, it will only convert the first 8 bytes to a double.
If there are less than 8 bytes given, it will prefix the bytes with 0 value bytes (so 01010101 01010101 01010101 turns into 00000000 00000000 00000000 00000000 00000000 01010101 01010101 01010101).
If there are no bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    double:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_byte"></a>

#### bytes\_to\_byte

```python
@classmethod
def bytes_to_byte(cls,
                  byte_array: Array[int],
                  index: int = 0,
                  length: int = 2147483647) -> int
```

X.bytes_to_byte(byte_array, index=0, length=2147483647) -> uint8
Converts a Byte Array into a byte (uint8).

If there are more than 1 bytes given, it will return the first byte.
If there are less than 1 bytes given, it will return 0.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    uint8:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_boolean"></a>

#### bytes\_to\_boolean

```python
@classmethod
def bytes_to_boolean(cls,
                     byte_array: Array[int],
                     index: int = 0,
                     length: int = 2147483647) -> bool
```

X.bytes_to_boolean(byte_array, index=0, length=2147483647) -> bool
Converts a Byte Array into a boolean (00000001 will return true, everything else will return false).

If there is more than 1 byte given, it will only convert the first byte to a boolean.
If there are no bytes given, it will return false.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_bit_string"></a>

#### bytes\_to\_bit\_string

```python
@classmethod
def bytes_to_bit_string(cls,
                        byte_array: Array[int],
                        add_spaces: bool = False,
                        index: int = 0,
                        length: int = 2147483647) -> str
```

X.bytes_to_bit_string(byte_array, add_spaces=False, index=0, length=2147483647) -> str
Converts a Byte Array into a Bit (Base2) String, with each byte reversed.

Args:
    byte_array (Array[uint8]): 
    add_spaces (bool): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_binary"></a>

#### bytes\_to\_binary

```python
@classmethod
def bytes_to_binary(cls,
                    byte_array: Array[int],
                    add_spaces: bool = False,
                    index: int = 0,
                    length: int = 2147483647) -> str
```

X.bytes_to_binary(byte_array, add_spaces=False, index=0, length=2147483647) -> str
Converts a Byte Array into a Binary (Base2) String.

Args:
    byte_array (Array[uint8]): 
    add_spaces (bool): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_base64_url"></a>

#### bytes\_to\_base64\_url

```python
@classmethod
def bytes_to_base64_url(cls,
                        byte_array: Array[int],
                        index: int = 0,
                        length: int = 2147483647) -> str
```

X.bytes_to_base64_url(byte_array, index=0, length=2147483647) -> str
Converts a Byte Array into a Base6 Url String.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_to_base64"></a>

#### bytes\_to\_base64

```python
@classmethod
def bytes_to_base64(cls,
                    byte_array: Array[int],
                    index: int = 0,
                    length: int = 2147483647) -> str
```

X.bytes_to_base64(byte_array, index=0, length=2147483647) -> str
Converts a Byte Array into a Base64 String.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.bytes_sub_array"></a>

#### bytes\_sub\_array

```python
@classmethod
def bytes_sub_array(cls,
                    byte_array: Array[int],
                    index: int,
                    length: int = 2147483647) -> Array[int]
```

X.bytes_sub_array(byte_array, index, length=2147483647) -> Array[uint8]
Returns the values of the given bytes of the given index and length.

Args:
    byte_array (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_writer_get_bytes"></a>

#### byte\_data\_writer\_get\_bytes

```python
@classmethod
def byte_data_writer_get_bytes(
        cls, byte_data_writer: LowEntryByteDataWriter) -> Array[int]
```

X.byte_data_writer_get_bytes(byte_data_writer) -> Array[uint8]
Returns the byte data.

Args:
    byte_data_writer (LowEntryByteDataWriter): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_writer_create_from_entry_array_pure"></a>

#### byte\_data\_writer\_create\_from\_entry\_array\_pure

```python
@classmethod
def byte_data_writer_create_from_entry_array_pure(
        cls, array: Array[LowEntryByteDataEntry]) -> LowEntryByteDataWriter
```

X.byte_data_writer_create_from_entry_array_pure(array) -> LowEntryByteDataWriter
Creates a new Byte Data Writer.

Args:
    array (Array[LowEntryByteDataEntry]): 

Returns:
    LowEntryByteDataWriter:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_writer_create_from_entry_array"></a>

#### byte\_data\_writer\_create\_from\_entry\_array

```python
@classmethod
def byte_data_writer_create_from_entry_array(
        cls, array: Array[LowEntryByteDataEntry]) -> LowEntryByteDataWriter
```

X.byte_data_writer_create_from_entry_array(array) -> LowEntryByteDataWriter
Creates a new Byte Data Writer.

Args:
    array (Array[LowEntryByteDataEntry]): 

Returns:
    LowEntryByteDataWriter:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_reader_create"></a>

#### byte\_data\_reader\_create

```python
@classmethod
def byte_data_reader_create(
        cls,
        bytes: Array[int],
        index: int = 0,
        length: int = 2147483647) -> LowEntryByteDataReader
```

X.byte_data_reader_create(bytes, index=0, length=2147483647) -> LowEntryByteDataReader
Creates a new Byte Data Reader.

Args:
    bytes (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryByteDataReader:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_string_utf8_array"></a>

#### byte\_data\_entry\_create\_from\_string\_utf8\_array

```python
@classmethod
def byte_data_entry_create_from_string_utf8_array(
        cls, value: Array[str]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_string_utf8_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a String (UTF-8) array.

Args:
    value (Array[str]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_string_utf8"></a>

#### byte\_data\_entry\_create\_from\_string\_utf8

```python
@classmethod
def byte_data_entry_create_from_string_utf8(
        cls, value: str) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_string_utf8(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a String (UTF-8).

Args:
    value (str): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer3_array"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer3\_array

```python
@classmethod
def byte_data_entry_create_from_positive_integer3_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer3_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer array.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer3"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer3

```python
@classmethod
def byte_data_entry_create_from_positive_integer3(
        cls, value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer3(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer2_array"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer2\_array

```python
@classmethod
def byte_data_entry_create_from_positive_integer2_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer2_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer array.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer2"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer2

```python
@classmethod
def byte_data_entry_create_from_positive_integer2(
        cls, value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer2(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer1_array"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer1\_array

```python
@classmethod
def byte_data_entry_create_from_positive_integer1_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer1_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer array.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_positive_integer1"></a>

#### byte\_data\_entry\_create\_from\_positive\_integer1

```python
@classmethod
def byte_data_entry_create_from_positive_integer1(
        cls, value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_positive_integer1(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a positive integer.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_long_bytes_array"></a>

#### byte\_data\_entry\_create\_from\_long\_bytes\_array

```python
@classmethod
def byte_data_entry_create_from_long_bytes_array(
        cls, value: Array[LowEntryLong]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_long_bytes_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a long (bytes) array.

Args:
    value (Array[LowEntryLong]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_long_bytes"></a>

#### byte\_data\_entry\_create\_from\_long\_bytes

```python
@classmethod
def byte_data_entry_create_from_long_bytes(
        cls, value: LowEntryLong) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_long_bytes(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a long (bytes).

Args:
    value (LowEntryLong): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_long_array"></a>

#### byte\_data\_entry\_create\_from\_long\_array

```python
@classmethod
def byte_data_entry_create_from_long_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_long_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a long (int64) array.

Args:
    value (Array[int64]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_long"></a>

#### byte\_data\_entry\_create\_from\_long

```python
@classmethod
def byte_data_entry_create_from_long(cls, value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_long(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a long (int64).

Args:
    value (int64): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_integer_array"></a>

#### byte\_data\_entry\_create\_from\_integer\_array

```python
@classmethod
def byte_data_entry_create_from_integer_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_integer_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of an integer array.

Args:
    value (Array[int32]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_integer"></a>

#### byte\_data\_entry\_create\_from\_integer

```python
@classmethod
def byte_data_entry_create_from_integer(cls,
                                        value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_integer(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of an integer.

Args:
    value (int32): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_float_array"></a>

#### byte\_data\_entry\_create\_from\_float\_array

```python
@classmethod
def byte_data_entry_create_from_float_array(
        cls, value: Array[float]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_float_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a float array.

Args:
    value (Array[float]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_float"></a>

#### byte\_data\_entry\_create\_from\_float

```python
@classmethod
def byte_data_entry_create_from_float(cls,
                                      value: float) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_float(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a float.

Args:
    value (float): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_double_bytes_array"></a>

#### byte\_data\_entry\_create\_from\_double\_bytes\_array

```python
@classmethod
def byte_data_entry_create_from_double_bytes_array(
        cls, value: Array[LowEntryDouble]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_double_bytes_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a double (bytes) array.

Args:
    value (Array[LowEntryDouble]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_double_bytes"></a>

#### byte\_data\_entry\_create\_from\_double\_bytes

```python
@classmethod
def byte_data_entry_create_from_double_bytes(
        cls, value: LowEntryDouble) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_double_bytes(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a double (bytes).

Args:
    value (LowEntryDouble): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_double_array"></a>

#### byte\_data\_entry\_create\_from\_double\_array

```python
@classmethod
def byte_data_entry_create_from_double_array(
        cls, value: Array[float]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_double_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a double array.

Args:
    value (Array[double]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_double"></a>

#### byte\_data\_entry\_create\_from\_double

```python
@classmethod
def byte_data_entry_create_from_double(cls,
                                       value: float) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_double(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a double.

Args:
    value (double): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_byte_array"></a>

#### byte\_data\_entry\_create\_from\_byte\_array

```python
@classmethod
def byte_data_entry_create_from_byte_array(
        cls, value: Array[int]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_byte_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a byte array.

Args:
    value (Array[uint8]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_byte"></a>

#### byte\_data\_entry\_create\_from\_byte

```python
@classmethod
def byte_data_entry_create_from_byte(cls, value: int) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_byte(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a byte.

Args:
    value (uint8): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_boolean_array"></a>

#### byte\_data\_entry\_create\_from\_boolean\_array

```python
@classmethod
def byte_data_entry_create_from_boolean_array(
        cls, value: Array[bool]) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_boolean_array(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a boolean array.

Args:
    value (Array[bool]): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.byte_data_entry_create_from_boolean"></a>

#### byte\_data\_entry\_create\_from\_boolean

```python
@classmethod
def byte_data_entry_create_from_boolean(cls,
                                        value: bool) -> LowEntryByteDataEntry
```

X.byte_data_entry_create_from_boolean(value) -> LowEntryByteDataEntry
Creates a new Byte Data Entry with the value of a boolean.

Args:
    value (bool): 

Returns:
    LowEntryByteDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.boolean_to_bytes"></a>

#### boolean\_to\_bytes

```python
@classmethod
def boolean_to_bytes(cls, value: bool) -> Array[int]
```

X.boolean_to_bytes(value) -> Array[uint8]
Converts a boolean into a Byte Array (1 byte).

Args:
    value (bool): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.boolean_to_byte"></a>

#### boolean\_to\_byte

```python
@classmethod
def boolean_to_byte(cls, value: bool) -> int
```

X.boolean_to_byte(value) -> uint8
Converts a boolean into a Byte.

Args:
    value (bool): 

Returns:
    uint8:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_string_to_bytes"></a>

#### bit\_string\_to\_bytes

```python
@classmethod
def bit_string_to_bytes(cls, bits: str) -> Array[int]
```

X.bit_string_to_bytes(bits) -> Array[uint8]
Tries to convert a Binary (Base2) String (with each byte reversed) into a Byte Array. Will return an empty Array on failure.

Args:
    bits (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.bits_to_byte"></a>

#### bits\_to\_byte

```python
@classmethod
def bits_to_byte(cls, bit1: bool, bit2: bool, bit3: bool, bit4: bool,
                 bit5: bool, bit6: bool, bit7: bool, bit8: bool) -> int
```

X.bits_to_byte(bit1, bit2, bit3, bit4, bit5, bit6, bit7, bit8) -> uint8
Converts bits into a byte.

Args:
    bit1 (bool): 
    bit2 (bool): 
    bit3 (bool): 
    bit4 (bool): 
    bit5 (bool): 
    bit6 (bool): 
    bit7 (bool): 
    bit8 (bool): 

Returns:
    uint8: 

    byte (uint8):

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_writer_get_bytes"></a>

#### bit\_data\_writer\_get\_bytes

```python
@classmethod
def bit_data_writer_get_bytes(
        cls, bit_data_writer: LowEntryBitDataWriter) -> Array[int]
```

X.bit_data_writer_get_bytes(bit_data_writer) -> Array[uint8]
Returns the byte data.

Args:
    bit_data_writer (LowEntryBitDataWriter): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_writer_create_from_entry_array_pure"></a>

#### bit\_data\_writer\_create\_from\_entry\_array\_pure

```python
@classmethod
def bit_data_writer_create_from_entry_array_pure(
        cls, array: Array[LowEntryBitDataEntry]) -> LowEntryBitDataWriter
```

X.bit_data_writer_create_from_entry_array_pure(array) -> LowEntryBitDataWriter
Creates a new Bit Data Writer.

This is basically a Byte Data Writer, except that it adds certain methods, like methods to add individual bits, and methods to only add a certain number of bits of a given byte or integer.

Booleans are also always stored in 1 bit with a Bit Data Writer, with a Byte Data Writer it will take 1 full byte to store a boolean.

This allows you to create smaller results than you can with the Byte Data Writer, but it costs a little bit more processing power to write data with the Bit Data Writer, and it also costs a little bit more processing power to read data with the Bit Data Reader.

Args:
    array (Array[LowEntryBitDataEntry]): 

Returns:
    LowEntryBitDataWriter:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_writer_create_from_entry_array"></a>

#### bit\_data\_writer\_create\_from\_entry\_array

```python
@classmethod
def bit_data_writer_create_from_entry_array(
        cls, array: Array[LowEntryBitDataEntry]) -> LowEntryBitDataWriter
```

X.bit_data_writer_create_from_entry_array(array) -> LowEntryBitDataWriter
Creates a new Bit Data Writer.

This is basically a Byte Data Writer, except that it adds certain methods, like methods to add individual bits, and methods to only add a certain number of bits of a given byte or integer.

Booleans are also always stored in 1 bit with a Bit Data Writer, with a Byte Data Writer it will take 1 full byte to store a boolean.

This allows you to create smaller results than you can with the Byte Data Writer, but it costs a little bit more processing power to write data with the Bit Data Writer, and it also costs a little bit more processing power to read data with the Bit Data Reader.

Args:
    array (Array[LowEntryBitDataEntry]): 

Returns:
    LowEntryBitDataWriter:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_reader_create"></a>

#### bit\_data\_reader\_create

```python
@classmethod
def bit_data_reader_create(cls,
                           bytes: Array[int],
                           index: int = 0,
                           length: int = 2147483647) -> LowEntryBitDataReader
```

X.bit_data_reader_create(bytes, index=0, length=2147483647) -> LowEntryBitDataReader
Creates a new Bit Data Reader.

Args:
    bytes (Array[uint8]): 
    index (int32): 
    length (int32): 

Returns:
    LowEntryBitDataReader:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_string_utf8_array"></a>

#### bit\_data\_entry\_create\_from\_string\_utf8\_array

```python
@classmethod
def bit_data_entry_create_from_string_utf8_array(
        cls, value: Array[str]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_string_utf8_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a String (UTF-8) array.

Args:
    value (Array[str]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_string_utf8"></a>

#### bit\_data\_entry\_create\_from\_string\_utf8

```python
@classmethod
def bit_data_entry_create_from_string_utf8(cls,
                                           value: str) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_string_utf8(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a String (UTF-8).

Args:
    value (str): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer3_array"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer3\_array

```python
@classmethod
def bit_data_entry_create_from_positive_integer3_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer3_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer array.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer3"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer3

```python
@classmethod
def bit_data_entry_create_from_positive_integer3(
        cls, value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer3(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer.

Will store values below 8.388.608 in 3 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer2_array"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer2\_array

```python
@classmethod
def bit_data_entry_create_from_positive_integer2_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer2_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer array.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer2"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer2

```python
@classmethod
def bit_data_entry_create_from_positive_integer2(
        cls, value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer2(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer.

Will store values below 32.768 in 2 bytes, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer1_array"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer1\_array

```python
@classmethod
def bit_data_entry_create_from_positive_integer1_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer1_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer array.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integers have to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (Array[int32]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_positive_integer1"></a>

#### bit\_data\_entry\_create\_from\_positive\_integer1

```python
@classmethod
def bit_data_entry_create_from_positive_integer1(
        cls, value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_positive_integer1(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a positive integer.

Will store values below 128 in 1 byte, higher values will be stored in 4 bytes.

The given integer has to be 0 or higher, values under 0 will be changed to 0.

Args:
    value (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_long_bytes_array"></a>

#### bit\_data\_entry\_create\_from\_long\_bytes\_array

```python
@classmethod
def bit_data_entry_create_from_long_bytes_array(
        cls, value: Array[LowEntryLong]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_long_bytes_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a long (bytes) array.

Args:
    value (Array[LowEntryLong]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_long_bytes"></a>

#### bit\_data\_entry\_create\_from\_long\_bytes

```python
@classmethod
def bit_data_entry_create_from_long_bytes(
        cls, value: LowEntryLong) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_long_bytes(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a long (bytes).

Args:
    value (LowEntryLong): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_long_array"></a>

#### bit\_data\_entry\_create\_from\_long\_array

```python
@classmethod
def bit_data_entry_create_from_long_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_long_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a long (int64) array.

Args:
    value (Array[int64]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_long"></a>

#### bit\_data\_entry\_create\_from\_long

```python
@classmethod
def bit_data_entry_create_from_long(cls, value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_long(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a long (int64).

Args:
    value (int64): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer_most_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_integer\_most\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_integer_most_significant_bits(
        cls, value: int, bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer_most_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer, will only add a certain amount of bits from the given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value 268435471 and bitcount 4, only the highest 4 bits will be added, meaning only 0001 will be added, which will then have a value of 268435456 when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (int32): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer_least_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_integer\_least\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_integer_least_significant_bits(
        cls, value: int, bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer_least_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer, will only add a certain amount of bits from the given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value 268435471 and bitcount 4, only the lowest 4 bits will be added, meaning only 1111 will be added, which will then have a value of 15 when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (int32): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer_array_most_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_integer\_array\_most\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_integer_array_most_significant_bits(
        cls, value: Array[int], bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer_array_most_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer array, will only add a certain amount of bits from every given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value [268435471, 268435471, 268435471] and bitcount 4, only the highest 4 bits of each integer will be added, meaning only 0001 0001 0001 will be added, which will then have a value of 268435456 for each integer when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (Array[int32]): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer_array_least_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_integer\_array\_least\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_integer_array_least_significant_bits(
        cls, value: Array[int], bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer_array_least_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer array, will only add a certain amount of bits from every given integer.

For example, take 268435471 as the value (bitwise this is: 00010000 00000000 00000000 00001111).
If you use this blueprint with value [268435471, 268435471, 268435471] and bitcount 4, only the lowest 4 bits of each integer will be added, meaning only 1111 1111 1111 will be added, which will then have a value of 15 for each integer when read again.

The bitcount can be anything between 0 and 32, values higher or lower will be clamped to 0 to 32.

Args:
    value (Array[int32]): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer_array"></a>

#### bit\_data\_entry\_create\_from\_integer\_array

```python
@classmethod
def bit_data_entry_create_from_integer_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer array.

Args:
    value (Array[int32]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_integer"></a>

#### bit\_data\_entry\_create\_from\_integer

```python
@classmethod
def bit_data_entry_create_from_integer(cls,
                                       value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_integer(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of an integer.

Args:
    value (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_float_array"></a>

#### bit\_data\_entry\_create\_from\_float\_array

```python
@classmethod
def bit_data_entry_create_from_float_array(
        cls, value: Array[float]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_float_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a float array.

Args:
    value (Array[float]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_float"></a>

#### bit\_data\_entry\_create\_from\_float

```python
@classmethod
def bit_data_entry_create_from_float(cls,
                                     value: float) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_float(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a float.

Args:
    value (float): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_double_bytes_array"></a>

#### bit\_data\_entry\_create\_from\_double\_bytes\_array

```python
@classmethod
def bit_data_entry_create_from_double_bytes_array(
        cls, value: Array[LowEntryDouble]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_double_bytes_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a double (bytes) array.

Args:
    value (Array[LowEntryDouble]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_double_bytes"></a>

#### bit\_data\_entry\_create\_from\_double\_bytes

```python
@classmethod
def bit_data_entry_create_from_double_bytes(
        cls, value: LowEntryDouble) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_double_bytes(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a double (bytes).

Args:
    value (LowEntryDouble): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_double_array"></a>

#### bit\_data\_entry\_create\_from\_double\_array

```python
@classmethod
def bit_data_entry_create_from_double_array(
        cls, value: Array[float]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_double_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a double array.

Args:
    value (Array[double]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_double"></a>

#### bit\_data\_entry\_create\_from\_double

```python
@classmethod
def bit_data_entry_create_from_double(cls,
                                      value: float) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_double(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a double.

Args:
    value (double): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte_most_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_byte\_most\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_byte_most_significant_bits(
        cls, value: int, bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte_most_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte, will only add a certain amount of bits from the given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value 63 and bitcount 4, only the highest 4 bits will be added, meaning only 0011 will be added, which will then have a value of 48 when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (uint8): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte_least_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_byte\_least\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_byte_least_significant_bits(
        cls, value: int, bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte_least_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte, will only add a certain amount of bits from the given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value 63 and bitcount 4, only the lowest 4 bits will be added, meaning only 1111 will be added, which will then have a value of 15 when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (uint8): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte_array_most_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_byte\_array\_most\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_byte_array_most_significant_bits(
        cls, value: Array[int], bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte_array_most_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte array, will only add a certain amount of bits from every given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value [63, 63, 63] and bitcount 4, only the highest 4 bits of each byte will be added, meaning only 0011 0011 0011 will be added, which will then have a value of 48 for each byte when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (Array[uint8]): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte_array_least_significant_bits"></a>

#### bit\_data\_entry\_create\_from\_byte\_array\_least\_significant\_bits

```python
@classmethod
def bit_data_entry_create_from_byte_array_least_significant_bits(
        cls, value: Array[int], bit_count: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte_array_least_significant_bits(value, bit_count) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte array, will only add a certain amount of bits from every given byte.

For example, take 63 as the value (bitwise this is: 0011 1111).
If you use this blueprint with value [63, 63, 63] and bitcount 4, only the lowest 4 bits of each byte will be added, meaning only 1111 1111 1111 will be added, which will then have a value of 15 for each byte when read again.

The bitcount can be anything between 0 and 8, values higher or lower will be clamped to 0 to 8.

Args:
    value (Array[uint8]): 
    bit_count (int32): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte_array"></a>

#### bit\_data\_entry\_create\_from\_byte\_array

```python
@classmethod
def bit_data_entry_create_from_byte_array(
        cls, value: Array[int]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte array.

Args:
    value (Array[uint8]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_byte"></a>

#### bit\_data\_entry\_create\_from\_byte

```python
@classmethod
def bit_data_entry_create_from_byte(cls, value: int) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_byte(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a byte.

Args:
    value (uint8): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_boolean_array"></a>

#### bit\_data\_entry\_create\_from\_boolean\_array

```python
@classmethod
def bit_data_entry_create_from_boolean_array(
        cls, value: Array[bool]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_boolean_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a boolean array, this does the same as a Bit Data Entry with the value of a bit array.

Args:
    value (Array[bool]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_boolean"></a>

#### bit\_data\_entry\_create\_from\_boolean

```python
@classmethod
def bit_data_entry_create_from_boolean(cls,
                                       value: bool) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_boolean(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a boolean, this does the same as a Bit Data Entry with the value of a bit.

Args:
    value (bool): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_bit_array"></a>

#### bit\_data\_entry\_create\_from\_bit\_array

```python
@classmethod
def bit_data_entry_create_from_bit_array(
        cls, value: Array[bool]) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_bit_array(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a bit array.

Args:
    value (Array[bool]): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.bit_data_entry_create_from_bit"></a>

#### bit\_data\_entry\_create\_from\_bit

```python
@classmethod
def bit_data_entry_create_from_bit(cls, value: bool) -> LowEntryBitDataEntry
```

X.bit_data_entry_create_from_bit(value) -> LowEntryBitDataEntry
Creates a new Bit Data Entry with the value of a bit.

Args:
    value (bool): 

Returns:
    LowEntryBitDataEntry:

<a id="unreal.LowEntryExtendedStandardLibrary.binary_to_bytes"></a>

#### binary\_to\_bytes

```python
@classmethod
def binary_to_bytes(cls, binary: str) -> Array[int]
```

X.binary_to_bytes(binary) -> Array[uint8]
Tries to convert a Binary (Base2) String into a Byte Array. Will return an empty Array on failure.

Args:
    binary (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.b_crypt"></a>

#### b\_crypt

```python
@classmethod
def b_crypt(cls,
            byte_array: Array[int],
            salt: Array[int],
            strength: int = 10,
            index: int = 0,
            length: int = 2147483647) -> Array[int]
```

X.b_crypt(byte_array, salt, strength=10, index=0, length=2147483647) -> Array[uint8]
Generates a BCrypt hash, always returns 24 bytes.

If the given ByteArray contain more than 72 bytes, only the first 72 bytes will be used.

The given salt needs to be 16 bytes.
The given strength needs to be between 4 and 30, a strength between 10 and 12 is recommended.

If these conditions aren't met, this blueprint will return an empty byte array.

PS: the Index and Length parameters refer to the Byte Array (see the "Get Bytes Sub Array" blueprint for more information).

Args:
    byte_array (Array[uint8]): 
    salt (Array[uint8]): 
    strength (int32): 
    index (int32): 
    length (int32): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.base64_url_to_bytes"></a>

#### base64\_url\_to\_bytes

```python
@classmethod
def base64_url_to_bytes(cls, base64_url: str) -> Array[int]
```

X.base64_url_to_bytes(base64_url) -> Array[uint8]
Tries to convert a Base64Url String into a Byte Array. Will return an empty Array on failure.

Args:
    base64_url (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.base64_url_to_base64"></a>

#### base64\_url\_to\_base64

```python
@classmethod
def base64_url_to_base64(cls, base64_url: str) -> str
```

X.base64_url_to_base64(base64_url) -> str
Converts a Base64Url string to a Base64 string.

Args:
    base64_url (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.base64_to_bytes"></a>

#### base64\_to\_bytes

```python
@classmethod
def base64_to_bytes(cls, base64: str) -> Array[int]
```

X.base64_to_bytes(base64) -> Array[uint8]
Tries to convert a Base64 String into a Byte Array. Will return an empty Array on failure.

Args:
    base64 (str): 

Returns:
    Array[uint8]:

<a id="unreal.LowEntryExtendedStandardLibrary.base64_to_base64_url"></a>

#### base64\_to\_base64\_url

```python
@classmethod
def base64_to_base64_url(cls, base64: str) -> str
```

X.base64_to_base64_url(base64) -> str
Converts a Base64 string to a Base64Url string.

Args:
    base64 (str): 

Returns:
    str:

<a id="unreal.LowEntryExtendedStandardLibrary.are_bytes_equal"></a>

#### are\_bytes\_equal

```python
@classmethod
def are_bytes_equal(cls,
                    a: Array[int],
                    b: Array[int],
                    index_a: int = 0,
                    length_a: int = 2147483647,
                    index_b: int = 0,
                    length_b: int = 2147483647) -> bool
```

X.are_bytes_equal(a, b, index_a=0, length_a=2147483647, index_b=0, length_b=2147483647) -> bool
Returns true if the two arrays contain the same data.

Args:
    a (Array[uint8]): 
    b (Array[uint8]): 
    index_a (int32): 
    length_a (int32): 
    index_b (int32): 
    length_b (int32): 

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.are_android_headphones_plugged_in"></a>

#### are\_android\_headphones\_plugged\_in

```python
@classmethod
def are_android_headphones_plugged_in(cls) -> bool
```

X.are_android_headphones_plugged_in() -> bool
Returns true if headphones are plugged in, returns false if it failed.

This will always only ever work on Android devices, other systems will always return false.

Returns:
    bool:

<a id="unreal.LowEntryExtendedStandardLibrary.android_platform"></a>

#### android\_platform

```python
@classmethod
def android_platform(cls) -> bool
```

X.android_platform() -> bool
Returns true if this is the Android platform (PLATFORM_ANDROID), returns false otherwise.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionBoolean"></a>