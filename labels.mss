#place-labels[zoom<8][population>=50000] name,
#place-labels[zoom=8][population>=15000] name,
#place-labels[zoom=9][population>=5000] name,
#place-labels[zoom=10][population>=1000] name,
#place-labels[zoom>=11][zoom<15][population>0] name,
#place-labels[zoom>=11][zoom<15][place=city] name,
#place-labels[zoom>=11][zoom<15][place=town] name,
#place-labels[zoom>=15][zoom<17] name
{
    text-fill: #586e75;
    text-halo-fill: #fdf6e3;
    text-halo-radius: 2;
    
    text-placement: point;
}

#place-labels[zoom<13] name
{
    text-size: 14;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom<13][population>=35000] name
{
    text-size: 16;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom<13][population>=100000] name
{
    text-size: 19;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom>=13] name
{
    text-size: 14;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#place-labels[zoom>=13][population>=35000] name
{
    text-size: 19;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#place-labels[zoom>=13][population>=100000] name
{
    text-size: 22;
    text-face-name: 'DejaVu Sans Condensed Bold';
}


/*
 * Road labels.
 */

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
