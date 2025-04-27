## Font Objects

```python
class Font(Object)
```

A font object, for use by Slate, UMG, and Canvas.

A font can either be:
  * Runtime cached - The font contains a series of TTF files that combine to form a composite font. The glyphs are cached on demand when required at runtime.
  * Offline cached - The font contains a series of textures containing pre-baked cached glyphs and their associated texture coordinates.

**C++ Source:**

- **Module**: Engine
- **File**: Font.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascent`` (float):  [Read-Write]
  todo: document
- ``characters`` (Array[FontCharacter]):  [Read-Write] List of characters in the font.  For a MultiFont, this will include all characters in all sub-fonts!  Thus,
                the number of characters in this array isn't necessary the number of characters available in the font
- ``composite_font`` (CompositeFont):  [Read-Write] Embedded composite font data
- ``descent`` (float):  [Read-Write]
  todo: document
- ``em_scale`` (float):  [Read-Write] Font metrics.
- ``font_cache_type`` (FontCacheType):  [Read-Write] What kind of font caching should we use? This controls which options we see
- ``import_options`` (FontImportOptionsData):  [Read-Write] Options used when importing this font
- ``kerning`` (int32):  [Read-Write] Default horizontal spacing between characters when rendering text with this font
- ``leading`` (float):  [Read-Write]
  todo: document
- ``legacy_font_name`` (Name):  [Read-Write] The default font name to use for legacy Canvas APIs that don't specify a font name
- ``legacy_font_size`` (int32):  [Read-Write] The default size of the font used for legacy Canvas APIs that don't specify a font size
- ``scaling_factor`` (float):  [Read-Write] Scale to apply to the font.

<a id="unreal.FontFace"></a>