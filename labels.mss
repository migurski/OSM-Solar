#major-road-labels[zoom>=16][highway=motorway] name,
#major-road-labels[zoom>=12][highway=trunk] name,
#major-road-labels[zoom>=12][highway=primary] name,
#major-road-labels[zoom>=13][highway=secondary] name,
#minor-road-labels[zoom>=15][highway=tertiary] name,
#minor-road-labels[zoom>=16] name
{
    text-face-name: 'DejaVu Sans Condensed';
    text-fill: #586e75;
    
    text-placement: line;
    text-spacing: 384;
    text-max-char-angle-delta: 30;
    
    text-halo-fill: #fdf6e3;
    text-halo-radius: 2;
}

/*
 * Increase text size when zoomed in and there's more room for large labels.
 */

#major-road-labels[zoom<14] name,
#minor-road-labels[zoom<16] name
{
    text-size: 12;
}

#major-road-labels[zoom>=14] name,
#minor-road-labels[zoom>=16] name
{
    text-size: 14;
}

/*
 * Switch to an outlined labels when roads are think enough to match them.
 */

#major-road-labels[zoom>=17][highway=motorway] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #d33682;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#major-road-labels[zoom>=17][highway=trunk] name,
#major-road-labels[zoom>=17][highway=primary] name,
#major-road-labels[zoom>=17][highway=secondary] name,
#minor-road-labels[zoom>=17][highway=tertiary] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #657b83;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#minor-road-labels[zoom>=18] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #93a1a1;
    text-face-name: 'DejaVu Sans Condensed Bold';
}
