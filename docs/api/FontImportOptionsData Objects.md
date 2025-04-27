## FontImportOptionsData Objects

```python
class FontImportOptionsData(StructBase)
```

Font import options

**C++ Source:**

- **Module**: Engine
- **File**: FontImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_only`` (bool):  [Read-Write] if true then forces PF_G8 and only maintains Alpha value and discards color
- ``character_set`` (FontImportCharacterSet):  [Read-Write] Character set for this font
- ``chars`` (str):  [Read-Write] Explicit list of characters to include in the font
- ``chars_file_path`` (str):  [Read-Write] Path on disk to a folder where files that contain a list of characters to include in the font
- ``chars_file_wildcard`` (str):  [Read-Write] File mask wildcard that specifies which files within the CharsFilePath to scan for characters in include in the font
- ``create_printable_only`` (bool):  [Read-Write] Skips generation of glyphs for any characters that are not considered 'printable'
- ``distance_field_scale_factor`` (int32):  [Read-Write] Scale factor determines how big to scale the font bitmap during import when generating distance field values
  Note that higher values give better quality but importing will take much longer.
- ``distance_field_scan_radius_scale`` (float):  [Read-Write] Shrinks or expands the scan radius used to determine the silhouette of the font edges.
- ``enable_antialiasing`` (bool):  [Read-Write] Whether the font should be antialiased or not.  Usually you should leave this enabled.
- ``enable_bold`` (bool):  [Read-Write] Whether the font should be generated in bold or not
- ``enable_drop_shadow`` (bool):  [Read-Write] Enables a very simple, 1-pixel, black colored drop shadow for the generated font
- ``enable_italic`` (bool):  [Read-Write] Whether the font should be generated in italics or not
- ``enable_legacy_mode`` (bool):  [Read-Write] Enables legacy font import mode.  This results in lower quality antialiasing and larger glyph bounds, but may be useful when debugging problems
- ``enable_underline`` (bool):  [Read-Write] Whether the font should be generated with an underline or not
- ``extend_box_bottom`` (int32):  [Read-Write] How much to extend the bottom of the UV coordinate rectangle for each character in pixels
- ``extend_box_left`` (int32):  [Read-Write] How much to extend the left of the UV coordinate rectangle for each character in pixels
- ``extend_box_right`` (int32):  [Read-Write] How much to extend the right of the UV coordinate rectangle for each character in pixels
- ``extend_box_top`` (int32):  [Read-Write] How much to extend the top of the UV coordinate rectangle for each character in pixels
- ``font_name`` (str):  [Read-Write] Name of the typeface for the font to import
- ``foreground_color`` (LinearColor):  [Read-Write] Color of the foreground font pixels.  Usually you should leave this white and instead use the UI Styles editor to change the color of the font on the fly
- ``height`` (float):  [Read-Write] Height of font (point size)
- ``include_ascii_range`` (bool):  [Read-Write] When specifying a range of characters and this is enabled, forces ASCII characters (0 thru 255) to be included as well
- ``kerning`` (int32):  [Read-Write] The initial horizontal spacing adjustment between rendered characters.  This setting will be copied directly into the generated Font object's properties.
- ``texture_page_max_height`` (int32):  [Read-Write] The maximum vertical size of a texture page for this font in pixels.  The actual height of a texture page may be less than this if the font can fit within a smaller sized texture page.
- ``texture_page_width`` (int32):  [Read-Write] Horizontal size of each texture page for this font in pixels
- ``unicode_range`` (str):  [Read-Write] Range of Unicode character values to include in the font.  You can specify ranges using hyphens and/or commas (e.g. '400-900')
- ``use_distance_field_alpha`` (bool):  [Read-Write] If true then the alpha channel of the font textures will store a distance field instead of a color mask
- ``x_padding`` (int32):  [Read-Write] Horizontal padding between each font character on the texture page in pixels
- ``y_padding`` (int32):  [Read-Write] Vertical padding between each font character on the texture page in pixels

<a id="unreal.FontImportOptionsData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CompositeFont"></a>